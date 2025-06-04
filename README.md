# Quadrotor State Estimation and Control

This repository contains a complete design and analysis of a linearized quadrotor model, including attitude and vertical motion. It covers state-space modeling, controllability, observability, state feedback control, and observer design.

## ✈️ Overview

The project is structured around a simplified LTI (Linear Time-Invariant) model of a quadrotor near hover conditions. It assumes:
- Small angle approximation around hover
- Euler angles: roll (ϕ), pitch (θ), yaw (ψ)
- Vertical position and velocity (z, ẋ)

## 🧩 Features

- ✅ Controllability and observability analysis
- ✅ State feedback controller design (`τ = -Kx`)
- ✅ State observer / estimator design (`x̂' = A x̂ + Bτ + L(y - C x̂)`)
- ✅ Full system integration including altitude control
- ✅ Mathematical derivations in LaTeX

## 📁 Repository Contents

- `/latex/`: LaTeX source code of the report
- `/figures/`: Diagrams and block structures (if any)
- `/matlab/` or `/python/`: Scripts for pole placement and simulations (optional)
- `README.md`: You are here!
- `main.pdf`: Compiled final report (if present)

## 🚀 Running the Project

If control design is simulated:
- In MATLAB:
  - Run `main.m` or `controller_design.m` for control
  - Use `place()` for pole placement
- In Python:
  - Use `scipy.signal.place_poles` for controller and observer gain calculation

If only LaTeX is used:
- Compile with `pdflatex main.tex` or your preferred LaTeX editor.

## 📚 Dependencies

- LaTeX (with `amsmath`, `amsthm`, `graphicx`)
- MATLAB or Python (optional, for gain computation)

## 📄 License

MIT License — free to use with attribution.
