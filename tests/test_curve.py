"""Tests for TransitionCurve / solve (docs/theory.md, Section 4, Theorem 4.11)."""
import numpy as np
import pytest

from min_max_curvature import solve

CASES = [
    (0.0, 0.0, 1.0, 0.5),     # 0 < H < L
    (0.0, 0.0, 2.0, 0.7),     # different span/rise
    (-1.0, 2.0, 3.0, 2.0),    # H == 0 (constant graph)
]


@pytest.mark.parametrize("a0,b0,a1,b1", CASES)
def test_endpoint_values(a0, b0, a1, b1):
    curve = solve(a0, b0, a1, b1, N=41)
    assert curve.gamma(a0) == pytest.approx(b0, abs=1e-9)
    assert curve.gamma(a1) == pytest.approx(b1, abs=1e-9)


@pytest.mark.parametrize("a0,b0,a1,b1", CASES)
def test_endpoint_slopes_vanish(a0, b0, a1, b1):
    curve = solve(a0, b0, a1, b1, N=41)
    assert curve.dgamma(a0) == pytest.approx(0.0, abs=1e-9)
    assert curve.dgamma(a1) == pytest.approx(0.0, abs=1e-9)


@pytest.mark.parametrize("a0,b0,a1,b1", CASES)
def test_max_curvature_equals_J(a0, b0, a1, b1):
    curve = solve(a0, b0, a1, b1, N=41)
    x = np.linspace(a0, a1, 20001)
    assert curve.curvature(x).max() == pytest.approx(curve.J, abs=1e-8)


@pytest.mark.parametrize("a0,b0,a1,b1", CASES)
def test_arc_length_inverse(a0, b0, a1, b1):
    curve = solve(a0, b0, a1, b1, N=41)
    x = np.linspace(a0, a1, 101)
    x_back = curve.x_at_length(curve.length(x))
    np.testing.assert_allclose(x_back, x, atol=1e-9)


def test_signed_curvature_matches_finite_differences():
    curve = solve(0.0, 0.0, 1.0, 0.5, N=41)
    x = np.linspace(0.0, 1.0, 200001)
    dx = x[1] - x[0]
    y = curve.gamma(x)
    yp = np.gradient(y, dx)
    ypp = np.gradient(yp, dx)
    curvature_fd = np.abs(ypp) / (1 + yp**2) ** 1.5
    # skip the boundary points, where one-sided finite differences are least accurate
    np.testing.assert_allclose(curvature_fd[5:-5], curve.curvature(x)[5:-5], atol=1e-4)


def test_gap_is_positive_and_bounded():
    curve = solve(0.0, 0.0, 1.0, 0.5, N=41)
    assert curve.gap > 0    # infimum is never attained, Cor. 3.6
    assert curve.gap < certified_gap_bound_for(curve)


def certified_gap_bound_for(curve):
    from min_max_curvature import certified_gap_bound
    return certified_gap_bound(curve.a0, curve.b0, curve.a1, curve.b1, curve.N)


def test_solve_rejects_degenerate_span():
    with pytest.raises(ValueError):
        solve(1.0, 0.0, 1.0, 0.5)   # a0 == a1


def test_solve_warns_in_degenerate_H_ge_L_regime():
    with pytest.warns(UserWarning):
        solve(0.0, 0.0, 1.0, 1.5, N=21)   # |H| >= L
