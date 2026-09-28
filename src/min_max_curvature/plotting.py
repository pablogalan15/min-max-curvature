"""Figure generation for a solved TransitionCurve (requires matplotlib)."""
from .exact import DoubleArc


def plot(curve, path):
    """Save a three-panel figure (curve, signed curvature, arc length) to path."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    d = curve.sample(2001)
    fig, ax = plt.subplots(1, 3, figsize=(16, 4.6))
    if 0 < abs(curve.H) < curve.L:
        arc = DoubleArc(curve.a0, curve.b0, curve.a1, curve.b1)
        ax[0].plot(d["x"], arc.gamma(d["x"]), "k--", lw=1.2, label="double arc (not $C^\\infty$)")
        ax[1].plot(d["x"], arc.signed_curvature(d["x"]), "k--", lw=1.2, label="double arc")
        ax[2].plot(d["x"], arc.length(d["x"]), "k--", lw=1.2,
                   label=f"double arc, total {arc.total_length:.5f}")
    ax[0].plot(d["x"], d["gamma"], "C0", label=f"$\\gamma_N$, N={curve.N}")
    ax[1].plot(d["x"], curve.signed_curvature(d["x"]), "C0", label=f"J = {curve.J:.5f}")
    ax[2].plot(d["x"], d["length"], "C0", label=f"length(x), total {curve.total_length:.5f}")
    ax[0].set_aspect("equal")
    ax[0].set_title("curve y = $\\gamma$(x)")
    ax[1].set_title(f"signed curvature  (K* = {curve.K_star:.5f})")
    ax[2].set_title("arc length from the start")
    for a in ax:
        a.set_xlabel("x")
        a.grid(alpha=0.3)
        a.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)
