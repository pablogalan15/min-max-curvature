"""Independent check: (P_N) solved with a generic NLP solver.

See docs/theory.md, Section 6, Algorithm 3.  This is a sanity check, not part
of the proof: Theorem 4.11 already gives the exact global minimiser via
curve.solve(); SLSQP is a local method with no global-optimality guarantee,
so agreement with the exact t_N only validates the implementation.
"""
import numpy as np
from scipy.optimize import brentq, minimize

from ._quadrature import _GX, _GW
from .basis import F, HatProfile, dF


def solve_P_N_blackbox(a0, b0, a1, b1, N=15, M=4, maxiter=2000):
    """Epigraph form of (P_N): min t s.t. -t <= c_j <= t, sum c_j = 0,
    int F(u_c) = |H|, |u_c| < 1, solved by SLSQP from a cosine curvature
    profile.  Uses the same quadrature as TransitionCurve(..., N, M)."""
    L, H = a1 - a0, abs(b1 - b0)
    n = N - 1
    z = np.linspace(0.0, L, N * M + 1)
    half = 0.5 * (L / (N * M))
    nodes = (0.5 * (z[:-1] + z[1:])[:, None] + half * _GX).ravel()
    wts = np.tile(half * _GW, N * M)
    A = np.column_stack([HatProfile(L, e).u(nodes) for e in np.eye(n)])
    As = A[:: max(1, nodes.size // (8 * N))]
    ucap = 1.0 - 1e-6

    def G(c):
        return (wts @ F(np.clip(A @ c, -ucap, ucap)) - H) / L

    def dG(c):
        return (A.T @ (wts * dF(np.clip(A @ c, -ucap, ucap)))) / L

    shape = np.cos(np.pi * np.arange(1, N) / N)
    shape -= shape.mean()
    a = brentq(lambda a: G(a * shape), 0.0, (1 - 1e-9) / np.abs(A @ shape).max())
    z0 = np.append(a * shape, np.abs(a * shape).max())
    eye, one = np.eye(n), np.ones((n, 1))
    cons = [
        {"type": "ineq", "fun": lambda z: np.concatenate([z[-1] - z[:-1], z[-1] + z[:-1]]),
         "jac": lambda z: np.block([[-eye, one], [eye, one]])},
        {"type": "eq", "fun": lambda z: np.array([z[:-1].sum()]),
         "jac": lambda z: np.append(np.ones(n), 0.0)[None, :]},
        {"type": "eq", "fun": lambda z: np.array([G(z[:-1])]),
         "jac": lambda z: np.append(dG(z[:-1]), 0.0)[None, :]},
        {"type": "ineq", "fun": lambda z: np.concatenate([ucap - As @ z[:-1], ucap + As @ z[:-1]]),
         "jac": lambda z: np.hstack([np.vstack([-As, As]), np.zeros((2 * len(As), 1))])},
    ]
    res = minimize(lambda z: z[-1], z0, jac=lambda z: np.append(np.zeros(n), 1.0),
                   method="SLSQP", constraints=cons,
                   options={"maxiter": maxiter, "ftol": 1e-15})
    return res, z0
