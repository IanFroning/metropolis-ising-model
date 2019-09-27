Programmer: Ian Froning (froning.10@osu.edu)

# Analysis of Example Plot

The included plot was run at a field of *H*/*J* = 1, with *kT*/*J* ranging from
0.1 to 10 in 100 steps, for 3 different lattice sizes. Each data point
is the result of 250 Metropolis cycles.

The plot shows three different lattice sizes, where the maximum size
is limited by the processing power available on my laptop. There isn't
much to remark on about the effect of lattice size, except to say that
smaller lattices are noisier. We can explain this feature by noting
that a single spin flip on a smaller lattice has a proportionally
larger effect on the overall magnetization, and so we expect more
variation for smaller lattices.

We can see that, not surprisingly, the magnetization drops as the
temperature increases; as T increases, the Boltzman factor *e*^-*E*/*kT*
increases, and it becomes more and more likely that the spins will
flip to higher energy, antiparallel states. This is consistent with
our physical intuition for a real ferromagnet, in which magnetic
order is counteracted by entropy, the effect of which increases with
temperature. The system does not, however, appear to have a
well-defined Curie Temperature; the magnetization does not drop sharply
to 0. Based on Figure 13.6 in the 2013 Hjorth-Jensen Lectures, which
shows the same plot for much larger simulations, I expect that this
discrepancy is an artifact of the small scale of my simulation.

It is interesting that at *kT* = *H* = 1, the lattice is almost fully
magnetized; it seems that *kT* must be several times larger than *H*
before the lattice starts to demagnetize. Although I understand why
the lattice demagnetizes at higher temperatures, I'm not sure I
understand what determines the actual value at which demagnetization
happens.
