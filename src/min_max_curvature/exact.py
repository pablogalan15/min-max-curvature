"""Exact closed-form results for the relaxed problem.

See docs/theory.md, Sections 3 and 5:
    - exact_infimum          K* = inf J over the smooth class          (Cor. 5.2)
    - certified_gap_bound    a priori bound on J(gamma_N)/K* - 1        (Cor. 5.2(1))
    - certified_N            smallest N guaranteeing a given tolerance (Algorithm 2)
    - DoubleArc              the unique C^{1,1} relaxed minimiser       (Prop. 3.4)
"""
import numpy as np

from ._quadrature import to_scalar


def exact_infimum(a0, b0, a1, b1):
    """K* = inf of J over the smooth class (Cor. 5.2)."""
    L, H = a1 - a0, abs(b1 - b0)
    if H == 0:
        return 0.0
    return 4.0 * H / (L**2 + H**2) if H < L else 2.0 / L


def certified_gap_bound(a0, b0, a1, b1, N):
    """A priori bound on J(gamma_N)/K* - 1 (Cor. 5.2(1)); inf if not applicable."""
    L, H = a1 - a0, abs(b1 - b0)
    h = L / N
    if H >= L:
        return 2.0 / (N - 2)
    if N <= 2 * L / (L - H):
        return np.inf
    return 4 * h * (L - h) / ((L - 2 * h) ** 2 + H**2)


def certified_N(a0, b0, a1, b1, rel_gap):
    """Smallest N for which the a priori bound guarantees J <= (1 + rel_gap) K*
    (Algorithm 2).  The bound is decreasing in N, so bisection applies."""
    lo, hi = 2, 3
    while certified_gap_bound(a0, b0, a1, b1, hi) > rel_gap:
        lo, hi = hi, 2 * hi
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if certified_gap_bound(a0, b0, a1, b1, mid) > rel_gap:
            lo = mid
        else:
            hi = mid
    return hi


class DoubleArc:
    """Relaxed optimum for 0 < |H| < L (Prop. 3.4): two tangent circular arcs of
    radius R* = (L^2 + H^2)/(4|H|).  Only C^{1,1}; provided for comparison."""

    def __init__(self, a0, b0, a1, b1):
        self.a0, self.b0, self.a1, self.b1 = map(float, (a0, b0, a1, b1))
        L, H = self.a1 - self.a0, self.b1 - self.b0
        if not 0 < abs(H) < L:
            raise ValueError("the double arc exists only for 0 < |b1 - b0| < a1 - a0")
        self.sign = np.sign(H)
        self.R = (L**2 + H**2) / (4 * abs(H))
        self.m = 0.5 * (self.a0 + self.a1)
        self.K_star = 1.0 / self.R
        self.total_length = 2 * self.R * np.arcsin(L / (2 * self.R))

    def gamma(self, x):
        xc = np.clip(np.asarray(x, dtype=float), self.a0, self.a1)
        R, s = self.R, self.sign
        left = self.b0 + s * (R - np.sqrt(np.maximum(R**2 - (xc - self.a0) ** 2, 0.0)))
        right = self.b1 - s * (R - np.sqrt(np.maximum(R**2 - (self.a1 - xc) ** 2, 0.0)))
        return to_scalar(np.where(xc <= self.m, left, right))

    def signed_curvature(self, x):
        x = np.asarray(x, dtype=float)
        inside = (x > self.a0) & (x < self.a1)
        return to_scalar(np.where(inside, self.sign * self.K_star * np.sign(self.m - x), 0.0))

    def length(self, x):
        x = np.asarray(x, dtype=float)
        xc = np.clip(x, self.a0, self.a1)
        R = self.R
        left = R * np.arcsin(np.minimum((xc - self.a0) / R, 1.0))
        right = self.total_length - R * np.arcsin(np.minimum((self.a1 - xc) / R, 1.0))
        return to_scalar(np.where(xc <= self.m, left, right) + (x - xc))
