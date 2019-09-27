# metropolis-ising-model

This set of files runs the Metropolis algorithm on a 2D Ising model,
and returns the percent magnetization for a given set of parameters.
`Hamiltonian.py` contains the Hamiltonian for a square lattice of
nearest-neighbor interacting spins, and `Metropolis.py` contains
the Metropolis algorithm that acts on a given Hamiltonian and returns
the magnetization. All energies are assumed to be divided by the
interaction term *J*, and the units of both *J* and the applied field *H* are
such that they both have units of energy.

There are two programs that can be run from the command-line via
`python2 <program name> <options>`, where `-h` can be passed as an
argument to receive more specific instructions.

`MetroRunner.py` will run the Metropolis algorithm on a randomized
initial Hamiltonian with a given size, at a given temperature and
applied field, for a given number of cycles, and print out the
resulting magnetization. This is a good toy model for how changing
the values of *H* and *T* can affect the magnetization: for *H* >> *T*,
near 100% magnetization is calculated; whereas for *H* << *T*,
magnetizations are close to 0.

`MetroPlotter.py` plots magnetization vs temperature, and is run in a
similar way, but also asks for a range of T to loop over and spits out
a data file (`MvsT.dat`) which is plotted with gnuplot (using `MvsT.plt`).
One example plot is included (`MvsT_example.ps`).
