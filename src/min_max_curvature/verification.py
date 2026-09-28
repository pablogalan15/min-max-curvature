"""Numerical checks of the results in docs/theory.md (the --verify CLI flag).

These are printed diagnostics for interactive use; see tests/ for the
equivalent automated pytest assertions.
"""
import numpy as np

from .blackbox import solve_P_N_blackbox
from .curve import solve
from .exact import DoubleArc, certified_gap_bound, exact_infimum


def verify(a0=0.0, b0=0.0, a1=1.0, b1=0.5):
    """Numerical checks of the results in docs/theory.md."""
    L, H = a1 - a0, abs(b1 - b0)
    Ks = exact_infimum(a0, b0, a1, b1)
    arc = DoubleArc(a0, b0, a1, b1) if 0 < H < L else None
    print(f"Data: L = {L:g}, H = {b1 - b0:g};  K* = {Ks:.12f}")

    print("\nConvergence (Thm 5.1, Cor. 5.2)")
    print(f"{'N':>6} {'t_N':>15} {'t_N/K*-1':>11} {'N*gap':>8} {'a priori':>10}"
          f" {'N^2|t_N-K*(L-h)|':>18} {'total length':>15}")
    for N in [5, 17, 65, 257, 1025]:
        c = solve(a0, b0, a1, b1, N)
        second = (N**2 * abs(c.t - 4 * H / ((L - L / N) ** 2 + H**2))
                  if H < L - L / N else np.nan)
        print(f"{N:>6} {c.t:>15.10f} {c.gap:>11.3e} {N * c.gap:>8.4f}"
              f" {certified_gap_bound(a0, b0, a1, b1, N):>10.3e} {second:>18.4f}"
              f" {c.total_length:>15.10f}")
    if arc is not None:
        print(f"{'limit':>6} {Ks:>15.10f} {'':>11} {2 * L**2 / (L**2 + H**2):>8.4f}"
              f" {'':>10} {'':>18} {arc.total_length:>15.10f}  (double arc)")

    N = 41
    c = solve(a0, b0, a1, b1, N)
    x = np.linspace(a0, a1, 200001)
    y, ell = c.gamma(x), c.length(x)
    dx = x[1] - x[0]
    yp = np.gradient(y, dx)
    print(f"\nChecks for N = {N}")
    print(f"  gamma(a0) - b0, gamma(a1) - b1           : "
          f"{c.gamma(a0) - b0:.1e}, {c.gamma(a1) - b1:.1e}")
    print(f"  max curvature on 2e5 points - t_N         : {c.curvature(x).max() - c.t:.1e}")
    kfd = np.abs(np.gradient(yp, dx)) / (1 + yp**2) ** 1.5
    print(f"  max curvature from finite differences     : {kfd.max():.8f}  (t_N = {c.t:.8f})")
    print(f"  max |d gamma/dx (FD) - dgamma|             : "
          f"{np.abs(yp - c.dgamma(x))[1:-1].max():.1e}")
    print(f"  max |d length/dx (FD) - sqrt(1+gamma'^2)|  : "
          f"{np.abs(np.gradient(ell, dx) - np.sqrt(1 + c.dgamma(x) ** 2))[1:-1].max():.1e}")
    poly = np.sum(np.hypot(np.diff(x), np.diff(y)))
    print(f"  polyline length (2e5 segments) - length   : {poly - c.total_length:.1e}")
    xs = np.linspace(a0, a1, 1001)
    print(f"  max |x_at_length(length(x)) - x|          : "
          f"{np.abs(c.x_at_length(c.length(xs)) - xs).max():.1e}")
    edge = np.linspace(a0, a0 + 0.02 * L / N, 50)
    print(f"  max |gamma'|, |gamma''| near a0           : "
          f"{np.abs(c.dgamma(edge)).max():.1e}, {np.abs(c.d2gamma(edge)).max():.1e}")
    c2 = solve(a0, b0, a1, b1, N, M=32)
    print(f"  M=16 vs M=32: |change in t_N|, |in length|: "
          f"{abs(c2.t - c.t):.1e}, {abs(c2.total_length - c.total_length):.1e}")
    print(f"  max |curvature rate| (grows like N)       : {np.abs(c.curvature_rate(x)).max():.4f}")

    if 0 < H < L:
        res, z0 = solve_P_N_blackbox(a0, b0, a1, b1, N=15, M=4)
        ref = solve(a0, b0, a1, b1, 15, M=4)
        print(f"\nBlack-box SLSQP on (P_15) from a cosine start (t = {z0[-1]:.6f}):")
        print(f"  SLSQP t = {res.x[-1]:.10f},  exact t_15 = {ref.t:.10f}")
        print(f"  SLSQP coefficients / t = {np.round(res.x[:-1] / res.x[-1], 4)}")
