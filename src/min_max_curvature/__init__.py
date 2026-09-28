"""min_max_curvature: smooth transition curves with minimal maximal curvature.

Among C^inf graphs on [a0, a1] with gamma(a0) = b0, gamma(a1) = b1 and
gamma^(n)(a0) = gamma^(n)(a1) = 0 for all n >= 1, minimise

    J(gamma) = max_x |gamma''(x)| / (1 + gamma'(x)^2)^(3/2).

The infimum K* (= 4|H|/(L^2+H^2) if |H| < L, 2/L otherwise) is NOT attained by
any smooth curve. This package returns the unique minimiser gamma_N of J over
the N-cell smooth class A_N; its maximal curvature t_N converges to K*.

See docs/theory.md for the full statements and proofs.

    >>> from min_max_curvature import solve
    >>> curve = solve(0, 0, 1, 0.5, N=41)
    >>> curve.J, curve.K_star, curve.gap
"""
from .blackbox import solve_P_N_blackbox
from .curve import TransitionCurve, solve, solve_for_tolerance
from .exact import DoubleArc, certified_gap_bound, certified_N, exact_infimum
from .plotting import plot
from .verification import verify

__version__ = "0.1.0"

__all__ = [
    "solve",
    "solve_for_tolerance",
    "solve_P_N_blackbox",
    "TransitionCurve",
    "DoubleArc",
    "exact_infimum",
    "certified_gap_bound",
    "certified_N",
    "verify",
    "plot",
]
