set term postscript eps enhanced color 
set key right top
set title 'North Lobe'
set xlabel 'Energy (eV)' 
set ylabel '{/Symbol n} F({/Symbol n}) [erg cm^{-2} s^{-1}]' 

set autoscale
set output '/Users/nifraija/Desktop/2013/recover/FRI/CenA_I/nfit.eps
set logscale x
set logscale y
set format y "10^{%L}"
#set style line 1 lt 1 lw 6

set bars 1
set points 0.8 

plot [1e-7:1e10][3e-13:0.4e-10] 'nlob_syn.dat' title "Synchrotron radiation"  with xyerrorbars linestyle 1  lt 1 pt 7, "nsyn.dat" u 1:2 smooth sbezier title "" w lines linestyle  1 lt 1 lc 3, 'nlob_pp.dat' title "pp interactions" with xyerrorbars lt -1 pt 7, "npp.dat" u 1:2 title "" w line linestyle  1 lt 1 lc 3
#lw 1  pt 7 ps 0.7

set autoscale
set output '/Users/nifraija/Desktop/2013/recover/FRI/CenA_I/nfit_ic.eps
set logscale x
set logscale y
set format y "10^{%L}"
#set style line 1 lt 1 lw 6

set bars 1
set points 0.8 

plot [1e-7:1e11][3e-13:1e-9] 'nlob_syn.dat' title "Synchrotron radiation"  with xyerrorbars linestyle 1  lt 1 pt 7, "nsyn.dat" u 1:2 smooth sbezier title "" w lines linestyle  1 lt 1 lc 3, 'nlob_pp.dat' title "pp interactions" with xyerrorbars lt -1 pt 7, "npp.dat" u 1:2 title "" w line linestyle  1 lt 1 lc 3, "nic_cmb.dat" u 1:2 smooth sbezier title "IC/CMB" w lines lc 3 , "nic_ebl.dat" u 1:2 smooth sbezier title "IC/EBL" w lines lc 4, "nic_tot.dat" u 1:2 smooth sbezier title "Total" w lines linestyle 1 lw 3 lc 7

#linestyle  2 lt 1 lc 3
#linestyle  3 lt 1 lc 3