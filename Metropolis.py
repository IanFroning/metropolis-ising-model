"""
File: Metropolis.py

Metropolis algorithm outlined by Hjorth-Jensen in "Computational Physics"
    1. Compute energy of initial state
    2. Flip a spin at random
    3. Compute energy of new state
    4. Accept change if energy is lowered
    5. If energy is increased, calculate Boltzman factor
    6. Compare BF with ranndom number; if the random number is lower,
       accept the change
    7. Repeat for all latice sites
    8. Update expectation value of magnetization
    9. Divide by number of cycles and number of spins

All energies are expressed in units of J

Programmer: Ian Froning (froning.10@osu.edu)
"""

import random
import math
from Hamiltonian import Hamiltonian

def metropolis( hamiltonian, kt, cycles ):
    """ runs the Metropolis algorithm on a given hamiltonian at a given
        temperature, for a given number of cycles """
    magnetizationSum = hamiltonian.getMagnetization()

    for i in range(1, cycles):

        for j in range(1, hamiltonian.getLength()):

            # 1. Compute energy of initial state
            oldEnergy = hamiltonian.getEnergy()

            # 2. Flip a spin at random
            spinToFlip = random.randint(0, hamiltonian.getLength()-1)
            hamiltonian.flipSpin( spinToFlip )

            # 3. Compute energy of new state
            newEnergy = hamiltonian.getEnergy()

            # 4. Accept change if energy is lowered
            # 5. If energy is increased, calculate Boltzman factor
            # 6. Compare BF with ranndom number; if the random number is
            #    lower, accept the change
            if newEnergy > oldEnergy:
                boltzmanFactor = math.exp( -(newEnergy - oldEnergy) / kt )
                if boltzmanFactor < random.uniform(0, 1):
                    hamiltonian.flipSpin( spinToFlip )

            # 7. Repeat for all latice sites

        # 8. Update expectation value of magnetization
        magnetizationSum += hamiltonian.getMagnetization()

    # 9. Divide by number of cycles
    magnetization = float( magnetizationSum ) / cycles / hamiltonian.getLength()
    return magnetization
