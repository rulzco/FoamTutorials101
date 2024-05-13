# Gnuplot script file for plotting data from file "k_0"

# set logscale y
set term wxt 1 size 640,480 
plot 'postProcessing/forces/0/force.dat' using ($1):($2) title 'Fx' with lines,\
 'postProcessing/forces/0/force.dat' using ($1):($3) title 'Fy' with lines,

set term wxt 2 size 640,480 
plot 'postProcessing/forceCoeffs/0/coefficient.dat' using ($1):($2) title 'Cd' with lines,\
 'postProcessing/forceCoeffs/0/coefficient.dat' using ($1):($3) title 'Cl' with lines,


pause mouse
~                            