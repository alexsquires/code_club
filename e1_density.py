#!/usr/bin/env python3

"""
Mass Density vs Energy Scatter Plot (Single List Version)
---------------------------------------------------------

This script takes:
    - structures : a list of pymatgen Structure objects
    - energies   : a matching list of energies (eV)

For each structure it:
    1. Computes the total mass of all atoms in the unit cell
    2. Converts that mass from amu → grams
    3. Converts the cell volume from Å^3 → cm^3
    4. Computes the mass density (g/cm^3)
    5. Plots density vs energy

Written linearly (no functions) for clarity.
"""

import numpy as np
import matplotlib.pyplot as plt
from pymatgen.core import Structure

# ------------------------------------------------------------
# USER INPUT: YOU provide these lists
# ------------------------------------------------------------

# Example placeholders — replace with your real data:
# structures = [struct1, struct2, struct3, ...]
# energies   = [E1,      E2,      E3,      ...]

# Make sure they have the same length:
# len(structures) == len(energies)


# ------------------------------------------------------------
# Constants for unit conversion
# ------------------------------------------------------------

AMU_TO_GRAMS = 1.66053906660e-24   # grams per atomic mass unit
ANGSTROM3_TO_CM3 = 1e-24           # 1 Å^3 = 1e-24 cm^3


# ------------------------------------------------------------
# Compute mass densities
# ------------------------------------------------------------

densities = []

for struct in structures:

    # -------------------------------
    # 1. Atomic mass in the structure
    # -------------------------------
    total_mass_amu = 0.0
    for site in struct.sites:
        total_mass_amu += site.specie.atomic_mass

    total_mass_g = total_mass_amu * AMU_TO_GRAMS

    # -------------------------------
    # 2. Convert volume Å^3 → cm^3
    # -------------------------------
    volume_A3 = struct.volume
    volume_cm3 = volume_A3 * ANGSTROM3_TO_CM3

    # -------------------------------
    # 3. Compute mass density (g/cm^3)
    # -------------------------------
    rho = total_mass_g / volume_cm3

    densities.append(rho)

densities = np.array(densities)
energies = np.array(energies)


# ------------------------------------------------------------
# Plot density vs energy
# ------------------------------------------------------------

plt.figure(figsize=(7,5))
plt.scatter(energies, densities, s=60)
plt.xlabel("Energy (eV)")
plt.ylabel("Mass Density (g/cm³)")
plt.title("Mass Density vs Energy")
plt.tight_layout()
plt.show()

# questions arising:
# why do I need to use a numpy array for densities and energies?
# I don't understand how we get the volume from the structure object