"""
File: MvsT.py

Runs the Metropolis algorithm on a randomized Hamiltonian with
user-specified temperature, field, and lattice size

Programmer: Ian Froning (froning.10@osu.edu)
"""

from optparse import OptionParser   # command-line options
from subprocess import call         # shell commands
import random
from Hamiltonian import Hamiltonian
from Metropolis import metropolis

# Read in parameters from command-line
parser = OptionParser()
parser.add_option('-H',
                  type='float', dest='h', default=0,
                  help='set the ratio H/J')
parser.add_option('-m',
                  type='float', dest='minimum', default=0,
                  help='set the min for kt/J')
parser.add_option('-M',
                  type='float', dest='maximum', default=1,
                  help='set the max for kt/J')
parser.add_option('-s',
                  type='int', dest='steps', default=10,
                  help='set the number of steps between min and max for \
                        kt/J')
parser.add_option('-l',
                  type='int', dest='length', default=16,
                  help='set the length of one side of the lattice')
parser.add_option('-c',
                  type='int', dest='cycles', default=100,
                  help='set the number of cycles to run the algorithm' )
(options, args) = parser.parse_args()
h = options.h
minimum = options.minimum
maximum = options.maximum
steps = options.steps
length = options.length
cycles = options.cycles
kt = minimum

# Create randomized initial Hamiltonian
initialState = ""
for j in range(0, length):
    initialState += str( random.randint(0, 1) )
hamiltonian = Hamiltonian( initialState, h )

# Run Metropolis algorithm for all T and write to file
out = open('MvsT.dat', 'w')
out.write('kT    M\n')
for i in range( 0, steps ):
    magnetization = metropolis( hamiltonian, kt, cycles )
    out.write( '%s   %s\n' % (kt, magnetization) )
    kt += ( maximum - minimum ) / steps
out.close()

# Plot it
call(['gnuplot', '-p', 'MvsT.plt'])
