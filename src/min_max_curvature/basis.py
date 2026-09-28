"""Smooth step function and the smooth hat-function basis it generates.

See docs/theory.md, Sections 4.1-4.4:
    - smooth_step / smooth_step_prime / step_integral  implement S, S', I  (4.1)
    - HatProfile                                       implements B_j, k, u  (4.2-4.3)
    - bang_bang                                        implements the saturated
                                                        sign profile c_hat  (4.4)
    - F / dF                                           implement the tangent-sine
                                                        map F = G^{-1} and its
                                                        derivative  (Lemma 2.1)
"""
import numpy as np
from scipy.special import expit

from ._quadrature import gauss_legendre


# ---------------------------------------------------------------------------
# 1. Smooth step S, its derivative and its integral  (Section 4.1)
# ---------------------------------------------------------------------------
def smooth_step(tau):
    """S(tau) = 1/(1 + exp(1/tau - 1/(1-tau))) on (0,1), 0 for tau <= 0, 1 for
    tau >= 1.  C^inf on R, flat at 0 and 1, S(tau) + S(1 - tau) = 1."""
    tau = np.asarray(tau, dtype=float)
    out = np.array(tau >= 1.0, dtype=float)
    inside = (tau > 0.0) & (tau < 1.0)
    ti = tau[inside]
    out[inside] = expit(1.0 / (1.0 - ti) - 1.0 / ti)
    return out


def smooth_step_prime(tau):
    """S'(tau); it is below 1e-300 outside (1e-3, 1 - 1e-3)."""
    tau = np.asarray(tau, dtype=float)
    out = np.zeros(tau.shape)
    inside = (tau > 1e-3) & (tau < 1.0 - 1e-3)
    ti = tau[inside]
    s = expit(1.0 / (1.0 - ti) - 1.0 / ti)
    out[inside] = s * (1.0 - s) * (1.0 / ti**2 + 1.0 / (1.0 - ti) ** 2)
    return out


class _StepIntegral:
    """I(tau) = int_0^tau S for any tau in [0, 1], to machine precision:
    a table on tau_m = m/n plus a Gauss-Legendre rule on [tau_m, tau]."""

    def __init__(self, n=256):
        self.n = n
        edges = np.linspace(0.0, 1.0, n + 1)
        pieces = gauss_legendre(smooth_step, edges[:-1], edges[1:])
        self.table = np.concatenate(([0.0], np.cumsum(pieces)))

    def __call__(self, tau):
        tau = np.clip(np.asarray(tau, dtype=float), 0.0, 1.0)
        m = np.minimum((tau * self.n).astype(int), self.n - 1)
        return self.table[m] + gauss_legendre(smooth_step, m / self.n, tau)


step_integral = _StepIntegral()


# ---------------------------------------------------------------------------
# 2. Curvature profiles spanned by smooth hats  (Sections 4.2-4.3)
# ---------------------------------------------------------------------------
class HatProfile:
    """k(s) = sum_{j=1}^{N-1} c_j B_j(s) on [0, L] and u(s) = int_0^s k,
    evaluated exactly at arbitrary s.  On the cell [s_i, s_i + h], with
    s = s_i + tau h:  k = c_i (1 - S(tau)) + c_{i+1} S(tau)  (c_0 = c_N = 0)."""

    def __init__(self, L, c):
        self.C = np.concatenate(([0.0], np.asarray(c, dtype=float), [0.0]))
        self.N = self.C.size - 1
        if self.N < 3:
            raise ValueError("N must be >= 3 (N = 2 forces k = 0).")
        self.L = float(L)
        self.h = self.L / self.N
        self.u_knots = self.h * np.concatenate(
            ([0.0], np.cumsum(0.5 * (self.C[:-1] + self.C[1:]))))

    def _locate(self, s):
        s = np.clip(np.asarray(s, dtype=float), 0.0, self.L)
        i = np.minimum((s / self.h).astype(int), self.N - 1)
        return i, np.clip(s / self.h - i, 0.0, 1.0)

    def k(self, s):
        i, tau = self._locate(s)
        S = smooth_step(tau)
        return self.C[i] * (1.0 - S) + self.C[i + 1] * S

    def dk(self, s):
        i, tau = self._locate(s)
        return (self.C[i + 1] - self.C[i]) * smooth_step_prime(tau) / self.h

    def u(self, s):
        i, tau = self._locate(s)
        I = step_integral(tau)
        return self.u_knots[i] + self.h * (self.C[i] * (tau - I) + self.C[i + 1] * I)


def bang_bang(N):
    """c_hat_j = sgn(N - 2j), j = 1..N-1  (Section 4.4)."""
    return np.sign(N - 2.0 * np.arange(1, N))


def F(u):
    """gamma' as a function of u = sin(theta)."""
    return u / np.sqrt(1.0 - u * u)


def dF(u):
    return (1.0 - u * u) ** -1.5
