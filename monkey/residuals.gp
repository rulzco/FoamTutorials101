# Gnuplot script file for plotting data from file "k_0"

set logscale y
plot 'logs/Ux_0' title 'Ux_0' with lines,\
'logs/Uy_0' title 'Uy_0' with lines,\
'logs/Uz_0' title 'Uz_0' with lines,\
'logs/p_0' title 'p_0' with lines

pause mouse