#!/usr/bin/env python
# coding: utf-8

# In[86]:


"""
Collatz-6 Dynamics
------------------
This module implements the Collatz-6 map:

    n mod 6 = 0 → n/6
    n mod 6 = 2,4 → n/2
    n mod 6 = 3 → n/3
    n mod 6 = 1 → (7n - 1) / 6^v6(7n - 1)
    n mod 6 = 5 → (7n + 1) / 6^v6(7n + 1)

Where v6(x) is the 6-adic valuation (the largest k such that 6^k divides x).

This file contains:
- v6: 6-adic valuation
- collatz6_step: one iteration
- collatz6_orbit: orbit until 1
- analyze_orbit_rim: steps, max, growth, rim count
- scan_rim: search for “glider-like” numbers
"""

from typing import List, Tuple


# ------------------------------------------------------------
# 6-adic valuation
# ------------------------------------------------------------
def v6(n: int) -> int:
    """Return the largest k such that 6**k divides n."""
    if n == 0:
        return 0
    k = 0
    while n % 6 == 0:
        n //= 6
        k += 1
    return k


# ------------------------------------------------------------
# One step of the Collatz-6 map
# ------------------------------------------------------------
def collatz6_step(n: int) -> int:
    """One step of the Collatz-6 map."""
    r = n % 6

    if r == 0:
        return n // 6
    elif r in (2, 4):
        return n // 2
    elif r == 3:
        return n // 3
    elif r == 1:
        x = 7 * n - 1
        return x // (6 ** v6(x))
    else:  # r == 5
        x = 7 * n + 1
        return x // (6 ** v6(x))


# ------------------------------------------------------------
# Orbit until fixed point 1
# ------------------------------------------------------------
def collatz6_orbit(n: int, max_steps: int = 2000) -> List[int]:
    """Generate orbit of n under Collatz-6, stopping at 1."""
    seq = [n]
    for _ in range(max_steps):
        if n == 1:
            break
        n = collatz6_step(n)
        seq.append(n)
    return seq


# ------------------------------------------------------------
# Analyze orbit: steps, max value, growth, Chaos Rim count
# ------------------------------------------------------------
def analyze_orbit_rim(n: int, max_steps: int = 2000) -> Tuple[int, int, float, int]:
    """
    Return:
        steps: number of steps until 1
        max_val: maximum value reached
        growth: max_val / n
        rim_count: number of times n mod 6 ∈ {1,5}
    """
    x = n
    steps = 0
    max_val = n
    rim_count = 0

    for _ in range(max_steps):
        if x == 1:
            break

        if x % 6 in (1, 5):
            rim_count += 1

        x = collatz6_step(x)
        steps += 1
        max_val = max(max_val, x)

    growth = max_val / n
    return steps, max_val, growth, rim_count


# ------------------------------------------------------------
# Scan a range for “glider-like” numbers
# ------------------------------------------------------------
def scan_rim(start: int, end: int, min_rim: int = 10, min_steps: int = 30) -> None:
    """
    Print numbers whose orbits show:
        - rim_count ≥ min_rim
        - steps ≥ min_steps
    """
    for n in range(start, end + 1):
        steps, max_val, growth, rim = analyze_orbit_rim(n)
        if rim >= min_rim and steps >= min_steps:
            print(f"n={n}, steps={steps}, rim={rim}, max={max_val}, growth={growth:.2f}")


# ------------------------------------------------------------
# Example usage
# ------------------------------------------------------------
if __name__ == "__main__":
    # Example: analyze a known “escape-like” number
    n = 20737
    seq = collatz6_orbit(n)
    print("Orbit:", seq)

    steps, max_val, growth, rim = analyze_orbit_rim(n)
    print(f"steps={steps}, max={max_val}, growth={growth:.2f}, rim={rim}")

