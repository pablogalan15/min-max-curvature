# Min-Max Curvature: Smooth Transition Curves

A rigorous implementation of smooth transition curves with **minimal maximal curvature**, based on solid mathematical theory with exact convergence guarantees.

## What This Does

Finds the optimal smooth curve `y = γ(x)` joining two points with:
- **Flat endpoints** (all derivatives ≥1 vanish at boundaries)
- **Minimal maximum curvature** (quantifiably close to the theoretical infimum)
- **Exact computation** (no numerical optimization over functions — the global minimiser is characterised in closed form)

**Key result**: The mathematical infimum K* is never attained by smooth curves, but the discrete minimizers γ_N returned by this package converge to it with an explicit O(1/N) bound.

## Installation

### Requirements
- Python 3.8+
- NumPy ≥ 1.19
- SciPy ≥ 1.5
- Matplotlib (optional, only for `--plot` / `plot()`)

### Install
```bash
git clone <this-repo>
cd min_max_curvature
pip install -e .              # core package
pip install -e ".[plot,dev]"  # + matplotlib + pytest
```

## Usage

### Python API

```python
import numpy as np
from min_max_curvature import solve, DoubleArc

# Solve for a curve from (0, 0) to (1, 0.5)
curve = solve(a0=0, b0=0, a1=1, b1=0.5, N=41)

# Access curve properties
x = np.linspace(0, 1, 100)
y = curve.gamma(x)                    # y-values
curvature = curve.curvature(x)        # curvature κ(x)
arc_length = curve.length(x)          # arc length from start
slope = curve.dgamma(x)               # dy/dx

# Quality metrics
print(f"Max curvature J: {curve.J:.10f}")
print(f"Infimum K*: {curve.K_star:.10f}")
print(f"Relative gap: {curve.gap:.3e}")  # (J/K* - 1)

# Arc-length parametrization
s = np.linspace(0, curve.total_length, 50)
x_arc, y_arc = curve.point_at_length(s)

# Export to CSV
curve.to_csv("curve_data.csv", n=1001)

# Plot (requires: pip install -e ".[plot]")
from min_max_curvature import plot
plot(curve, "curve.png")
```

See [`examples/quickstart.py`](examples/quickstart.py) for a runnable version of these snippets.

### Command Line

```bash
# Default example: (0,0) → (1, 0.5)
min-max-curvature

# Custom endpoints with N cells
min-max-curvature 0 0 2 0.7 --N 61 --samples 21

# Auto-select N to achieve tolerance on J/K* - 1
min-max-curvature 0 0 1 0.5 --tol 0.01

# CSV export and plot
min-max-curvature 0 0 1 0.5 --csv curve.csv --plot curve.png

# Numerical verification against theory
min-max-curvature --verify
```

Equivalently, without installing the console script: `python -m min_max_curvature.cli ...`.

## Theory at a Glance

### The Problem

Minimize the **maximum curvature** κ_max of a smooth curve y = γ(x) on [a₀, a₁]:

$$J(\gamma) = \max_{x \in [a_0, a_1]} \frac{|\gamma''(x)|}{(1 + \gamma'(x)^2)^{3/2}}$$

Subject to:
- γ(a₀) = b₀, γ(a₁) = b₁  (endpoint values)
- γ^(n)(a₀) = γ^(n)(a₁) = 0 for all n ≥ 1  (flat endpoints)

### Exact Results

| Case | Infimum K* | Attained? | Notes |
|------|-----------|-----------|-------|
| 0 < \|H\| < L | 4\|H\|/(L²+H²) | ❌ No | Relaxed solution: double circular arc |
| \|H\| ≥ L | 2/L | ❌ No | Degenerate; slope → ∞ in minimizing sequences |
| H = 0 | 0 | ✓ Yes | Constant function |

Where L = a₁ - a₀ (span) and H = b₁ - b₀ (rise).

### The Solution Method

1. **Smooth hat basis**: C^∞ compactly-supported functions with flat edges (Section 4.2)
2. **Bang-bang profile**: Optimal curvature coefficients are ±1 (sign of L/2 - x) (Section 4.4)
3. **Single scalar equation**: Find t_N such that ∫F(t_N Ψ_N) = |H| (Lemma 4.8)
4. **Convergence**: J(γ_N) - K* = O(1/N) with explicit first-order coefficient (Corollary 5.2)

## API Reference

### Main Solver

#### `solve(a0, b0, a1, b1, N=41, M=16) → TransitionCurve`

Computes the unique minimizer γ_N of max curvature over the N-cell smooth class.

**Parameters:**
- `a0, b0, a1, b1` (float): Endpoints (a₀, b₀) and (a₁, b₁)
- `N` (int): Number of cells (≥ 3; odd recommended). Default 41.
- `M` (int): Gauss-Legendre quadrature sub-intervals per cell. Default 16.

**Returns:** `TransitionCurve` object

#### `solve_for_tolerance(a0, b0, a1, b1, rel_gap=1e-2, M=16) → TransitionCurve`

Auto-selects smallest odd N to guarantee J/K* - 1 ≤ rel_gap.

**Parameters:**
- `rel_gap` (float): Target relative gap. Default 0.01 (1%).

### TransitionCurve Class

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| `J` | float | Maximum curvature of curve |
| `K_star` | float | Theoretical infimum (exact) |
| `gap` | float | Relative gap J/K* - 1 |
| `min_radius` | float | Minimum radius of curvature (1/J) |
| `total_length` | float | Arc length of entire curve |

#### Methods

| Method | Returns | Description |
|--------|---------|-------------|
| `gamma(x)` | ndarray/float | y-values (vectorized) |
| `dgamma(x)` | ndarray/float | dy/dx (first derivative) |
| `d2gamma(x)` | ndarray/float | d²y/dx² (second derivative) |
| `curvature(x)` | ndarray/float | κ(x) (unsigned curvature) |
| `signed_curvature(x)` | ndarray/float | u'(x) (signed curvature) |
| `curvature_rate(x)` | ndarray/float | dκ/dx (curvature derivative) |
| `length(x)` | ndarray/float | Arc length from (a₀, b₀) |
| `x_at_length(s)` | ndarray/float | Inverse of length(x) |
| `point_at_length(s)` | tuple(x, y) | (x, y) at arc length s |
| `sample(n=201)` | dict | Sample curve on n points |
| `to_csv(path, n=1001)` | None | Export to CSV |
| `summary()` | str | Summary statistics |

### Comparison: DoubleArc

#### `DoubleArc(a0, b0, a1, b1) → DoubleArc`

The unique C¹·¹ minimizer when 0 < |H| < L (not C^∞, for comparison).

```python
arc = DoubleArc(0, 0, 1, 0.5)
print(f"Radius: {arc.R:.6f}")
print(f"Curvature: {arc.K_star:.6f}")
```

## Output Interpretation

### Sample Output
```
Transition curve from (0, 0) to (1, 0.5)
  cells N                       : 41
  max curvature J = t_N         : 0.513890631227   (min radius 1.945880632908)
  infimum K* (not attainable)   : 0.480000000000
  gap J/K* - 1                  : 0.070e+00   (a priori bound 0.074e-01)
  total length                  : 1.142368125481
  length of the double arc      : 1.065235203325
```

**Interpretation:**
- **J**: Maximum curvature reached anywhere on the curve
- **K***: Theoretical lower bound (infimum) — never attained in C^∞ class
- **gap**: How far above K* we are; smaller N means larger gap
- **min radius**: Smallest radius of curvature (1/J)
- **a priori bound**: Guaranteed gap from theory (always ≥ actual gap)

## Numerical Precision

Default configuration achieves **machine precision** (~1e-15 relative error):
- 10-point Gauss-Legendre quadrature per sub-interval
- 16 sub-intervals per cell (M=16)
- Brent's method for root-finding (xtol=1e-15)
- Newton's method for arc-length inversion

Use `--verify` to see comprehensive numerical checks.

## Project Structure

```
min_max_curvature/
├── README.md                        ← You are here
├── LICENSE                          ← MIT
├── pyproject.toml                   ← package metadata, dependencies, CLI entry point
├── .gitignore
├── docs/
│   └── theory.md                    ← full mathematical theory (theorems + proofs)
├── src/
│   └── min_max_curvature/
│       ├── __init__.py              ← public API
│       ├── _quadrature.py           ← shared Gauss-Legendre helpers
│       ├── basis.py                 ← smooth step + hat-function basis (§§4.1-4.4)
│       ├── exact.py                 ← closed-form results + DoubleArc (§3)
│       ├── curve.py                 ← TransitionCurve, solve, solve_for_tolerance (§4)
│       ├── blackbox.py              ← independent SLSQP sanity check (§6, Algorithm 3)
│       ├── verification.py          ← the --verify diagnostics
│       ├── plotting.py              ← plot() (lazy matplotlib import)
│       └── cli.py                   ← command-line interface
├── tests/                           ← pytest suite
└── examples/
    └── quickstart.py                ← runnable version of the README examples
```

## Theory Document

[`docs/theory.md`](docs/theory.md) contains the full paper this package implements:
- **Sections 0–3**: Problem formulation, exact results, non-attainment
- **Sections 4–5**: Discrete minimizer and convergence theory
- **Section 6**: Numerical implementation details
- **Section 7**: Numerical experiments (the reference tables used by the test suite)
- **Section 8**: Relation to the literature
- **Appendix A**: Reproducibility and implementation checks

Theorems are numbered (Thm 3.2, Cor. 5.2, etc.) and cross-referenced directly in the code's docstrings.

## Examples

### Example 1: Quick Solve
```python
from min_max_curvature import solve

curve = solve(0, 0, 1, 0.5)
print(curve)
# TransitionCurve((0,0)->(1,0.5), N=41, J=0.5139, length=1.1424)
```

### Example 2: Convergence Study
```python
from min_max_curvature import solve

for N in [5, 17, 65, 257]:
    c = solve(0, 0, 1, 0.5, N=N)
    print(f"N={N:>3}  J={c.J:.8f}  gap={c.gap:.3e}")
# N=  5  J=2.27846804  gap=4.240e-01
# N= 17  J=1.76222014  gap=1.014e-01
# N= 65  J=1.64013647  gap=2.509e-02
# N=257  J=1.61000850  gap=6.256e-03
```

### Example 3: Arc-Length Parametrization
```python
curve = solve(0, 0, 1, 0.5, N=41)

# Sample by arc length instead of x
s_values = np.linspace(0, curve.total_length, 100)
x_arc, y_arc = curve.point_at_length(s_values)

# Check: slope should increase monotonically
slopes = curve.dgamma(x_arc)
```

## Testing

```bash
pip install -e ".[dev]"
pytest
```

The suite covers endpoint/flatness conditions, curvature-vs-finite-difference agreement, arc-length inversion, and the O(1/N) convergence rate against the reference values published in `docs/theory.md`, Section 7.

You can also run the built-in diagnostic mode directly:
```bash
min-max-curvature --verify
```
This checks endpoint conditions, curvature formulas (vs. finite differences), arc-length consistency, convergence rates against theory, and agreement with a black-box NLP solver (SLSQP).

## Mathematical References

The implementation is based on the full theory in [`docs/theory.md`](docs/theory.md).

**Key results:**
- **Lemma 2.2**: Tangent-sine transformation u = γ'/√(1+γ'²)
- **Theorem 3.2**: Lower bound J ≥ K*
- **Theorem 3.5**: Uniqueness of the double-arc relaxed minimiser
- **Theorem 4.11**: Exact characterization of γ_N via the bang-bang profile
- **Corollary 5.2**: O(1/N) convergence rate with explicit first-order coefficient

## Citation

If you use this code, please cite:
```bibtex
@misc{minmaxcurvature,
  title={Smooth transition curves with minimal maximal curvature},
  author={Gal\'an J\'ativa, Pablo},
  year={2026},
  howpublished={\url{https://github.com/yourname/min-max-curvature}}
}
```

## License

MIT — see [`LICENSE`](LICENSE).

## Contributing

Contributions welcome! Please:
1. Fork the repo
2. Create a feature branch
3. Add tests for new functionality
4. Ensure `pytest` and `min-max-curvature --verify` both pass
5. Submit a pull request

## Contact

Questions or issues? Open an issue on GitHub.

---

**Last updated**: 2026-09-28
**Tested with**: Python 3.8–3.11, NumPy 1.19+, SciPy 1.5+
