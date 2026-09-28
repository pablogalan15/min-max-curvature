"""Tests for the closed-form relaxed results (docs/theory.md, Sections 3 and 5)."""
import numpy as np
import pytest

from min_max_curvature import DoubleArc, certified_N, certified_gap_bound, exact_infimum


@pytest.mark.parametrize("a0,b0,a1,b1,expected", [
    (0, 0, 1, 0.5, 4 * 0.5 / (1**2 + 0.5**2)),   # 0 < H < L
    (0, 0, 1, 1.0, 2.0 / 1.0),                    # H == L (boundary, uses 2/L branch)
    (0, 0, 1, 2.0, 2.0 / 1.0),                    # H > L
    (0, 0, 1, 0.0, 0.0),                          # H == 0
    (0, 3, 2, 3.0, 0.0),                          # H == 0, shifted
])
def test_exact_infimum_formula(a0, b0, a1, b1, expected):
    assert exact_infimum(a0, b0, a1, b1) == pytest.approx(expected)


def test_exact_infimum_translation_invariant():
    # Shifting (a0, b0, a1, b1) rigidly must not change K*.
    base = exact_infimum(0, 0, 1, 0.5)
    shifted = exact_infimum(3, -7, 4, -6.5)
    assert shifted == pytest.approx(base)


class TestDoubleArc:
    def test_requires_0_lt_H_lt_L(self):
        with pytest.raises(ValueError):
            DoubleArc(0, 0, 1, 0.0)     # H == 0
        with pytest.raises(ValueError):
            DoubleArc(0, 0, 1, 2.0)     # H >= L

    def test_endpoint_values(self):
        arc = DoubleArc(0, 0, 1, 0.5)
        assert arc.gamma(0.0) == pytest.approx(0.0, abs=1e-12)
        assert arc.gamma(1.0) == pytest.approx(0.5, abs=1e-12)

    def test_curvature_magnitude_is_K_star(self):
        arc = DoubleArc(0, 0, 1, 0.5)
        x = np.linspace(0.05, 0.95, 37)   # avoid the endpoints/midpoint (curvature is 0/undefined there)
        np.testing.assert_allclose(np.abs(arc.signed_curvature(x)), arc.K_star, rtol=1e-12)

    def test_curvature_sign_flips_at_midpoint(self):
        arc = DoubleArc(0, 0, 1, 0.5)
        left = arc.signed_curvature(0.25)
        right = arc.signed_curvature(0.75)
        assert left * right < 0


@pytest.mark.parametrize("H", [0.5, 0.9])
def test_certified_gap_bound_decreases_with_N(H):
    Ns = [11, 21, 41, 81, 161]
    bounds = [certified_gap_bound(0, 0, 1, H, N) for N in Ns]
    assert all(np.isinf(b) or np.isfinite(b) for b in bounds)
    finite = [b for b in bounds if np.isfinite(b)]
    assert all(a > b for a, b in zip(finite, finite[1:]))


def test_certified_N_meets_its_own_bound():
    rel_gap = 0.02
    N = certified_N(0, 0, 1, 0.5, rel_gap)
    assert certified_gap_bound(0, 0, 1, 0.5, N) <= rel_gap
    assert certified_gap_bound(0, 0, 1, 0.5, N - 1) > rel_gap
