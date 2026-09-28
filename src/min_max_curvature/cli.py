"""Command-line interface.

    min-max-curvature                           # example (0,0) -> (1,0.5)
    min-max-curvature 0 0 2 0.7 --N 61 --samples 21
    min-max-curvature 0 0 1 0.5 --tol 0.01 --csv curve.csv --plot curve.png
    min-max-curvature --verify                  # numerical checks of the theory
"""
import argparse

from .curve import solve, solve_for_tolerance
from .verification import verify


def main(argv=None):
    p = argparse.ArgumentParser(
        prog="min-max-curvature",
        description="Smooth flat-ended graph of minimal maximal curvature: "
                    "returns gamma(x) and the arc length length(x).")
    p.add_argument("coords", nargs="*", type=float, metavar="a0 b0 a1 b1",
                   help="endpoints (a0, b0) and (a1, b1); default 0 0 1 0.5")
    p.add_argument("--N", type=int, default=41, help="number of cells (default 41)")
    p.add_argument("--tol", type=float,
                   help="target gap J/K* - 1; picks the smallest odd N (overrides --N)")
    p.add_argument("--M", type=int, default=16, help="quadrature sub-intervals per cell")
    p.add_argument("--samples", type=int, default=11, help="rows of the printed table")
    p.add_argument("--csv", metavar="PATH", help="write x, gamma, length, dgamma, curvature")
    p.add_argument("--csv-points", type=int, default=1001)
    p.add_argument("--plot", metavar="PATH", help="save a figure (needs matplotlib)")
    p.add_argument("--verify", action="store_true", help="run the numerical checks")
    args = p.parse_args(argv)

    coords = args.coords or [0.0, 0.0, 1.0, 0.5]
    if len(coords) != 4:
        p.error("give exactly four numbers: a0 b0 a1 b1")
    if args.verify:
        verify(*coords)
        return

    curve = (solve_for_tolerance(*coords, rel_gap=args.tol, M=args.M) if args.tol
             else solve(*coords, N=args.N, M=args.M))
    print(curve.summary())
    d = curve.sample(args.samples)
    print(f"\n{'x':>20} {'gamma(x)':>20} {'length(x)':>20} {'curvature(x)':>20}")
    for row in zip(d["x"], d["gamma"], d["length"], d["curvature"]):
        print("".join(f"{v:>21.12f}" for v in row))
    if args.csv:
        curve.to_csv(args.csv, args.csv_points)
        print(f"\nwrote {args.csv_points} points to {args.csv}")
    if args.plot:
        from .plotting import plot
        plot(curve, args.plot)
        print(f"figure saved to {args.plot}")


if __name__ == "__main__":
    main()
