"""The best smooth candidate gamma_N and its arc length.

See docs/theory.md, Section 4.5 and Theorem 4.11:

    gamma_N(x) = b0 + sgn(H) int_{a0}^x F(u),
    length(x)  = int_{a0}^x (1 - u^2)^(-1/2),
    u(x)       = t_N Psi_N(x - a0),
    t_N        = unique root of  int_0^L F(t Psi_N) = |H|   (Lemma 4.8).
"""
import warnings

import numpy as np
from scipy.optimize import brentq

from ._quadrature import _GX, _GW, EPS, gauss_legendre, to_scalar
from .basis import F, HatProfile, bang_bang, dF
from .exact import DoubleArc, certified_N, certified_gap_bound, exact_infimum


class TransitionCurve:
    """Unique minimiser gamma_N of J over A_N, with its arc length.

    N >= 3 cells (odd N recommended); M >= 1 quadrature sub-intervals per cell,
    each with a 10-point Gauss-Legendre rule."""

    def __init__(self, a0, b0, a1, b1, N=41, M=16):
        self.a0, self.b0, self.a1, self.b1 = map(float, (a0, b0, a1, b1))
        self.L, self.H = self.a1 - self.a0, self.b1 - self.b0
        if not self.L > 0:
            raise ValueError("need a0 < a1")
        self.N, self.M = int(N), int(M)
        if self.M < 1:
            raise ValueError("M must be >= 1")
        self.sign = float(np.sign(self.H))
        self.K_star = exact_infimum(self.a0, self.b0, self.a1, self.b1)
        self.profile = HatProfile(self.L, bang_bang(self.N))      # psi_N, Psi_N
        H_abs = abs(self.H)
        if H_abs >= self.L:
            warnings.warn("|b1-b0| >= a1-a0: inf J = 2/L is not attained and "
                          "near-optimal graphs are almost vertical in the middle "
                          "(Prop. 3.7); the graph formulation is degenerate here.")

        # composite Gauss-Legendre on the uniform grid z_k = k*dz of [0, L]
        n_sub = self.N * self.M
        self._dz = self.L / n_sub
        self._z = np.linspace(0.0, self.L, n_sub + 1)
        half = 0.5 * self._dz
        nodes = 0.5 * (self._z[:-1] + self._z[1:])[:, None] + half * _GX
        psi_nodes = self.profile.u(nodes)                          # Psi_N at the nodes

        if H_abs == 0:                                             # straight line
            self.t = 0.0
        else:
            M_N = float(self.profile.u(0.5 * self.L))              # max Psi_N (Lemma 4.7)
            g = lambda t: half * np.sum(F(t * psi_nodes) @ _GW) - H_abs
            t_hi = (1.0 - 1e-14) / M_N
            if not g(t_hi) > 0:
                raise RuntimeError(
                    "cannot bracket t_N: the quadrature does not resolve the nearly "
                    "vertical middle of the curve; increase M or decrease N"
                    + (" (|b1-b0| >= a1-a0 is the degenerate case, Prop. 3.7)"
                       if H_abs >= self.L else ""))
            self.t = brentq(g, 0.0, t_hi, xtol=1e-15, rtol=4 * EPS, maxiter=500)

        u = self.t * psi_nodes
        self._gam_table = np.concatenate(([0.0], np.cumsum(half * (F(u) @ _GW))))
        self._len_table = np.concatenate(
            ([0.0], np.cumsum(half * ((1.0 - u * u) ** -0.5 @ _GW))))
        self.total_length = float(self._len_table[-1])

    # -- basic quantities ---------------------------------------------------
    @property
    def J(self):
        """Maximal curvature of the curve (= t_N, Thm 4.11)."""
        return self.t

    @property
    def gap(self):
        """J / K* - 1 (exact, since K* is known in closed form)."""
        return self.t / self.K_star - 1.0 if self.K_star > 0 else 0.0

    @property
    def min_radius(self):
        return 1.0 / self.t if self.t > 0 else np.inf

    def _u(self, s):
        return self.t * self.profile.u(s)

    def _local(self, x):
        s = np.asarray(x, dtype=float) - self.a0
        return s, np.clip(s, 0.0, self.L)

    def _cumulative(self, table, integrand, sc):
        k = np.minimum((sc / self._dz).astype(int), self._z.size - 2)
        return table[k] + gauss_legendre(integrand, k * self._dz, sc)

    # -- the parametrisation x -> (x, gamma(x)) ------------------------------
    def gamma(self, x):
        """y = gamma(x)."""
        _, sc = self._local(x)
        val = self._cumulative(self._gam_table, lambda z: F(self._u(z)), sc)
        return to_scalar(self.b0 + self.sign * val)

    __call__ = gamma

    def dgamma(self, x):
        _, sc = self._local(x)
        return to_scalar(self.sign * F(self._u(sc)))

    def d2gamma(self, x):
        _, sc = self._local(x)
        return to_scalar(self.sign * self.t * self.profile.k(sc) * dF(self._u(sc)))

    def signed_curvature(self, x):
        """Signed curvature as a function of x (= u'(x), Lemma 2.2)."""
        _, sc = self._local(x)
        return to_scalar(self.sign * self.t * self.profile.k(sc))

    def curvature(self, x):
        return to_scalar(np.abs(self.signed_curvature(x)))

    def curvature_rate(self, x):
        """d(signed curvature)/dx; its maximum grows like N (Remark 6.2)."""
        _, sc = self._local(x)
        return to_scalar(self.sign * self.t * self.profile.dk(sc))

    # -- arc length -----------------------------------------------------------
    def _length_local(self, sc):
        return self._cumulative(self._len_table,
                                lambda z: (1.0 - self._u(z) ** 2) ** -0.5, sc)

    def length(self, x):
        """Arc length of the curve from (a0, b0) to (x, gamma(x))."""
        s, sc = self._local(x)
        return to_scalar(self._length_local(sc) + (s - sc))

    def x_at_length(self, ell):
        """Inverse of length(x): the abscissa reached after arc length ell.
        Newton's method; d length/dx = 1/sqrt(1 - u^2) >= 1."""
        ell = np.asarray(ell, dtype=float)
        ec = np.clip(ell, 0.0, self.total_length)
        s = np.interp(ec, self._len_table, self._z)
        tol = 4 * EPS * max(1.0, self.total_length)
        for _ in range(8):
            r = self._length_local(s) - ec
            s = np.clip(s - r * np.sqrt(1.0 - self._u(s) ** 2), 0.0, self.L)
            if np.max(np.abs(r), initial=0.0) < tol:
                break
        return to_scalar(self.a0 + s + (ell - ec))

    def point_at_length(self, ell):
        """(x, y) of the point at arc length ell from (a0, b0)."""
        x = self.x_at_length(ell)
        return x, self.gamma(x)

    # -- output helpers -------------------------------------------------------
    def sample(self, n=201):
        """Dictionary of arrays x, gamma, length, dgamma, curvature on n points."""
        x = np.linspace(self.a0, self.a1, n)
        return {"x": x, "gamma": self.gamma(x) + 0.0, "length": self.length(x),
                "dgamma": self.dgamma(x) + 0.0, "curvature": self.curvature(x)}

    def to_csv(self, path, n=1001):
        d = self.sample(n)
        np.savetxt(path, np.column_stack(list(d.values())), delimiter=",",
                   header=",".join(d), comments="", fmt="%.16e")

    def summary(self):
        lines = [f"Transition curve from ({self.a0:g}, {self.b0:g}) to ({self.a1:g}, {self.b1:g})",
                 f"  cells N                       : {self.N}",
                 f"  max curvature J = t_N         : {self.t:.12f}"
                 f"   (min radius {self.min_radius:.12f})",
                 f"  infimum K* (not attainable)   : {self.K_star:.12f}"]
        if self.K_star > 0:
            bound = certified_gap_bound(self.a0, self.b0, self.a1, self.b1, self.N)
            lines.append(f"  gap J/K* - 1                  : {self.gap:.3e}"
                         f"   (a priori bound {bound:.3e})")
        lines.append(f"  total length                  : {self.total_length:.12f}")
        if 0 < abs(self.H) < self.L:
            arc_len = DoubleArc(self.a0, self.b0, self.a1, self.b1).total_length
            lines.append(f"  length of the double arc      : {arc_len:.12f}")
        return "\n".join(lines)

    def __repr__(self):
        return (f"TransitionCurve(({self.a0:g},{self.b0:g})->({self.a1:g},{self.b1:g}), "
                f"N={self.N}, J={self.t:.10g}, length={self.total_length:.10g})")


def solve(a0, b0, a1, b1, N=41, M=16):
    """Best smooth candidate on N cells (Algorithm 1).  Returns a TransitionCurve
    exposing gamma(x), length(x) and the other quantities listed above.
    In the degenerate case |b1-b0| >= a1-a0 the middle of the curve is nearly
    vertical; M is then refined automatically (up to 1024) if needed, and the
    accuracy is lower (the problem is ill-conditioned there)."""
    while True:
        try:
            return TransitionCurve(a0, b0, a1, b1, N, M)
        except RuntimeError:
            if abs(b1 - b0) < a1 - a0 or M >= 1024:
                raise
            M = min(4 * M, 1024)


def solve_for_tolerance(a0, b0, a1, b1, rel_gap=1e-2, M=16):
    """Smallest odd N with J(gamma_N) <= (1 + rel_gap) K*.  The a priori bound
    (Algorithm 2) gives an N that is guaranteed to work; bisection over odd N
    below it finds the smallest one (the gap is monotone over odd N in all
    tests; the returned curve satisfies the tolerance in any case)."""
    if b1 == b0:
        return solve(a0, b0, a1, b1, 3, M)
    hi = (certified_N(a0, b0, a1, b1, rel_gap) - 1) // 2 + 1    # N = 2*hi + 1 works
    lo = 0                                                      # N = 1: not admissible
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if solve(a0, b0, a1, b1, 2 * mid + 1, M).gap > rel_gap:
            lo = mid
        else:
            hi = mid
    return solve(a0, b0, a1, b1, 2 * hi + 1, M)
