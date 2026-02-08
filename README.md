[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18513310.svg)](https://doi.org/10.5281/zenodo.18513310)

Title: Collatz-6 Python Implementation
Author: Hiroshi Harada
Year: 2026
License: CC BY 4.0

Description:
This archive provides a minimal and clean Python implementation of the Collatz-6
dynamical system. The Collatz-6 map is defined by modular rules based on n mod 6,
including divisions by 6, 3, and 2, and jump operations of the form 7n±1 with
6-adic valuation reduction.

The system is strongly convergent, but some numbers exhibit temporary
"glider-like" behavior, remaining in the Chaos Rim (numbers congruent to 1 or 5
mod 6) for many steps before eventually falling to the fixed point 1. This code
supports numerical exploration of such behavior.

Included Functions:
- v6(n): 6-adic valuation
- collatz6_step(n): one iteration of the map
- collatz6_orbit(n): orbit generation until 1
- analyze_orbit_rim(n): steps, maximum value, growth ratio, Chaos Rim count
- scan_rim(start, end): search for glider-like numbers in a range

Files in this archive:
- collatz6.py      (main implementation)
- README.md        (GitHub-style documentation)
- LICENSE          (CC BY 4.0)

Purpose:
This archive is intended for reproducible research, numerical experiments, and
exploration of escape-like behavior in the Collatz-6 system.

Citation:
If you use this code, please cite the Zenodo DOI associated with this archive.

Contact:
Hiroshi Harada
