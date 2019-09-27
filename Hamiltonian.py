"""
File: Hamiltonian.py

A two dimensional square Ising Hamiltonian for a ferromagnet:
    energy/J= - neighborSum(Si.Sj) - H/J * sum(Si)
where J is assumed to be positive.

H/J should be given to the Hamiltonian as parameters, along with the initial
condition, which must consist of a sequence of 0's and 1's i.e. "1001"
which represents
     1 -1
    -1  1

*NOTE: Because the lattice is square in shape, the initial condition given
should be a square number - if it isn't, zeroes will be tacked on at the end
until it is a square number

Programmer: Ian Froning (froning.10@osu.edu)
"""

import math
from bitarray import bitarray

class Hamiltonian(object):

    def __init__(self, initialCondition, hfield):
        self.hfield = hfield
        # Store initial condition as a boolean array
        self.spins = bitarray( initialCondition )
        # Fill any leftover space at the end of the lattice with zeroes
        # Method for checking if square only tested for lengths < 10000
        self.sideLength = int( math.sqrt( self.spins.length() ) )
        if self.sideLength ** 2 != self.spins.length():
            self.spins.append(False)

    def getLength(self):
        """ return the number of spins in the Hamiltonian """
        return self.spins.length()

    def getSpin(self, index):
        """ return the spin at a given index """
        if self.spins[index] == True:
            return 1
        else:
            return -1

    def flipSpin(self, index):
        """ flip the spin at a given index """
        self.spins[index] = not self.spins[index]

    def changeH(self, hfield):
        """ change the applied field to a different value """
        self.hfield = hfield

    def getEnergy(self):
        """ calculates and returns the energy of the system """
        energy = 0
        for i in range(0, self.spins.length()):
            # Check external field
            if self.spins[i] == True:
                energy += - self.hfield
            else:
                energy += self.hfield
            # Check to the right
            if int( (i+1) / self.sideLength ) * self.sideLength != i+1:
                if self.spins[i] != self.spins[i+1]:
                    energy += 1
                else:
                    energy += -1
            # Check above
            if i >= self.sideLength:
                if self.spins[i] != self.spins[i-self.sideLength]:
                    energy += 1
                else:
                    energy += -1
        return energy

    def getMagnetization(self):
        magnetization = 0.
        for spin in self.spins:
            if spin == True:
                magnetization += 1
            else:
                magnetization -= 1
        return magnetization
