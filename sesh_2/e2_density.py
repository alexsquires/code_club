#!/usr/bin/env python3

"""
Mass Density vs Energy Scatter Plot (Using loadfn to load JSON)
----------------------------------------------------------------

This script:
    1. Loads a JSON file containing ComputedStructureEntry objects
       using monty.serialization.loadfn
    2. Extracts:
         - structures (entry.structure)
         - energies   (entry.energy)
    3. Computes mass densities (g/cm^3)
    4. Plots density vs energy

Written linearly (no functions) for clarity.
"""

import numpy as np
import matplotlib.pyplot as plt
from monty.serialization import loadfn

# ------------------------------------------------------------
# LOAD JSON FILE CONTAINING ComputedStructureEntry OBJECTS
# ------------------------------------------------------------

# Replace this with your filename:
entries = loadfn("entries_raw.json")

# Extract structures and energies from the entries
structures = []
energies = []

for entry in entries:
    structures.append(entry.structure)
    energies.append(entry.energy)


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