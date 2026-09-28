"""Composite Gauss-Legendre quadrature helpers shared across the package.

See docs/theory.md, Section 6, for the accuracy guarantees of the composite
10-point Gauss-Legendre rule used throughout (Proposition 6.1).
"""
import numpy as np

GAUSS_POINTS = 10
_GX, _GW = np.polynomial.legendre.leggauss(GAUSS_POINTS)  # rule on [-1, 1]
EPS = np.finfo(float).eps


def gauss_legendre(f, a, b):
    """Gauss-Legendre approximation of int_a^b f, vectorised over arrays a, b."""
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    mid, half = 0.5 * (a + b), 0.5 * (b - a)
    return half * (f(mid[..., None] + half[..., None] * _GX) @ _GW)


def to_scalar(v):
    """Return a Python float for 0-d results, the array otherwise."""
    v = np.asarray(v)
    return float(v) if v.ndim == 0 else v
