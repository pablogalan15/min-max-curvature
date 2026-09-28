"""Convergence checks (docs/theory.md, Theorem 5.1, Corollary 5.2, Section 7).

The reference values below are Table 1 of docs/theory.md (L=1, H=0.5, K*=1.6),
computed with the original implementation; they pin down the numerics exactly.
"""
import numpy as np
import pytest

from min_max_curvature import solve

L, H = 1.0, 0.5
K_STAR = 4 * H / (L**2 + H**2)   # 1.6
FIRST_ORDER_COEFF = 2 * L**2 / (L**2 + H**2)   # 1.6, Corollary 5.2(3)

TABLE_1 = {
    5: 2.2784680449,
    17: 1.7622201421,
    65: 1.6401364655,
    257: 1.6100084967,
    1025: 1.6025005305,
}


@pytest.mark.parametrize("N,expected_t", TABLE_1.items())
def test_matches_published_table(N, expected_t):
    curve = solve(0.0, 0.0, L, H, N=N)
    assert curve.t == pytest.approx(expected_t, abs=5e-8)


def test_t_N_decreases_monotonically_towards_K_star():
    values = [solve(0.0, 0.0, L, H, N=N).t for N in TABLE_1]
    assert all(v > K_STAR for v in values)                       # Thm 5.1(1): never attained
    assert all(a > b for a, b in zip(values, values[1:]))        # decreasing towards K*


def test_relative_gap_first_order_rate():
    # N * (t_N / K* - 1) -> 2L^2/(L^2+H^2), Corollary 5.2(3); the O(N^-2)
    # remainder should have shrunk to well under 1% by N = 1025.
    curve = solve(0.0, 0.0, L, H, N=1025)
    rate = 1025 * curve.gap
    assert rate == pytest.approx(FIRST_ORDER_COEFF, rel=5e-3)


def test_quadrature_refinement_is_stable():
    c16 = solve(0.0, 0.0, L, H, N=41, M=16)
    c32 = solve(0.0, 0.0, L, H, N=41, M=32)
    assert c16.t == pytest.approx(c32.t, abs=1e-12)
    assert c16.total_length == pytest.approx(c32.total_length, abs=1e-10)


def test_length_converges_to_double_arc():
    from min_max_curvature import DoubleArc
    arc_length = DoubleArc(0.0, 0.0, L, H).total_length
    lengths = [solve(0.0, 0.0, L, H, N=N).total_length for N in TABLE_1]
    errors = [abs(ell - arc_length) for ell in lengths]
    assert all(a > b for a, b in zip(errors, errors[1:]))   # monotonically closer
    assert errors[-1] < 1e-3
