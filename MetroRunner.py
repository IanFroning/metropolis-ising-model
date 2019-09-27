"""
File: MetroRunner.py

Runs the Metropolis algorithm on a randomized Hamiltonian with
user-specified temperature, field, and lattice size

Programmer: Ian Froning (froning.10@osu.edu)
"""

from optparse import OptionParser
import random
from Hamiltonian import Hamiltonian
from Metropolis import metropolis

# Read in parameters from command line
parser = OptionParser()
parser.add_option('-T',
                  type='float', dest='kt', default=1,
                  help='set the ratio kT/J')
parser.add_option('-H',
                  type='float', dest='h', default=0,
                  help='set the ratio H/J')
parser.add_option('-s',
                  type='int', dest='size', default=16,
                  help='set the length of one side of the lattice')
parser.add_option('-c',
                  type='int', dest='cycles', default=100,
                  help='set the number of cycles to run the algorithm' )
(options, args) = parser.parse_args()
kt = options.kt
h = options.h
size = options.size
cycles = options.cycles

# Create randomized initial Hamiltonian
initialState = ""
for i in range(0, size):
    initialState += str( random.randint(0, 1) )
metroHam = Hamiltonian( initialState, h )

# Run Metropolis algorithm
magnetization = metropolis( metroHam, kt, cycles )
print('ratio magnetized: ' % magnetization)
