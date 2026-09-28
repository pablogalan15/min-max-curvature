#!/usr/bin/env python3
"""Quickstart examples for the min_max_curvature package.

Run with:
    python examples/quickstart.py
"""
import numpy as np

from min_max_curvature import DoubleArc, solve


def example_quick_solve():
    print("=== Example 1: quick solve ===")
    curve = solve(0, 0, 1, 0.5)
    print(curve)
    print()


def example_convergence_study():
    print("=== Example 2: convergence study ===")
    for N in [5, 17, 65, 257]:
        c = solve(0, 0, 1, 0.5, N=N)
        print(f"N={N:>3}  J={c.J:.8f}  gap={c.gap:.3e}")
    print()


def example_arc_length_parametrisation():
    print("=== Example 3: arc-length parametrisation ===")
    curve = solve(0, 0, 1, 0.5, N=41)
    s_values = np.linspace(0, curve.total_length, 10)
    x_arc, y_arc = curve.point_at_length(s_values)
    for s, x, y in zip(s_values, x_arc, y_arc):
        print(f"s={s:6.4f}  ->  (x, y) = ({x:7.4f}, {y:7.4f})")
    print()


def example_compare_to_double_arc():
    print("=== Example 4: comparison with the relaxed (non-smooth) double arc ===")
    curve = solve(0, 0, 1, 0.5, N=81)
    arc = DoubleArc(0, 0, 1, 0.5)
    print(f"J (smooth, N=81)      : {curve.J:.10f}")
    print(f"K* (double arc, exact): {arc.K_star:.10f}")
    print(f"length (smooth)       : {curve.total_length:.10f}")
    print(f"length (double arc)   : {arc.total_length:.10f}")


if __name__ == "__main__":
    example_quick_solve()
    example_convergence_study()
    example_arc_length_parametrisation()
    example_compare_to_double_arc()
