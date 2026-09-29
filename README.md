# Numerical methods in Python

KPI numerical-analysis coursework covering nonlinear equations, numerical linear algebra, interpolation, cubic splines, quadrature and initial-value ODE solvers.

## Topics

- comparison of bisection, chord, Newton and fixed-point root-finding methods
- LU factorisation and determinant calculations, documented in the main coursework report
- tridiagonal systems solved with the Thomas algorithm
- Lagrange and Newton interpolation
- natural cubic-spline construction
- trapezoidal and Simpson quadrature with refinement/error analysis
- Euler and classical fourth-order Runge–Kutta methods

## Structure

```text
src/root_finding_and_linear_systems/
src/interpolation/
src/splines/
src/quadrature/
src/ode_solvers/
figures/
report/
```

The main coursework PDF contains the complete root-finding comparison and numerical-linear-algebra methodology. The standalone source files reproduce the laboratory implementations.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run an individual example, for example:

```bash
python src/ode_solvers/euler_rk4.py
python src/quadrature/simpson.py
```

## Technology

Python, NumPy, SciPy and Matplotlib.

## Academic context

Individual KPI Numerical Methods coursework, 2025. Reports in `report/` are retained as evidence of methodology, error analysis and convergence discussion.

