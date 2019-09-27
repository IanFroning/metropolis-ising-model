#  file: MvsT_example.plt 
#
#  Gnuplot plot file for MvsT_example output
#  

# ensure background is white
set object 1 rectangle from screen 0,0 to screen 1,1 fillcolor rgb"#ffffff" behind

# record the time and date the graph was generated
set timestamp

# titles and labels
set title  'Ising Ferromagnet Temperature-dependence at H/J = 1 for viarious lattice dimensions'
set xlabel 'kT/J'
set ylabel 'M/spin'

# axes
set yrange [0:1]

# move the legend to a free space
set key top right

# set the terminal type to be the screen (which is x11 here)
set term x11

# plot the data as well as the fit, with appropriate titles 
plot "MvsT8x8.dat" using ($1):($2) with lines title "8x8 lattice", \
     "MvsT4x4.dat" using ($1):($2) with lines title "4x4 lattice", \
     "MvsT2x2.dat" using ($1):($2) with lines title "2x2 lattice"

# output the plot to the file eigen_basis_plt.ps   
set out "MvsT_example.ps"
set term postscript enhanced color
replot
