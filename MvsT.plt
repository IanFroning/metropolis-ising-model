#  file: MvsT.plt 
#
#  Gnuplot plot file for MvsT output
#  

# ensure background is white
set object 1 rectangle from screen 0,0 to screen 1,1 fillcolor rgb"#ffffff" behind

# record the time and date the graph was generated
set timestamp

# titles and labels
set title  '8x8 Ising Ferromagnet Temperature-dependence at H/J = 1'
set xlabel 'kT/J'
set ylabel 'M/spin'

# axes
set yrange [0:1]

# move the legend to a free space
set key off

# set the terminal type to be the screen (which is x11 here)
set term x11

# plot the data as well as the fit, with appropriate titles 
plot "MvsT.dat" using ($1):($2) with lines

# output the plot to the file eigen_basis_plt.ps   
set out "MvsT.ps"
set term postscript enhanced color
replot
