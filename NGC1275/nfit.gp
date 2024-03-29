set term postscript eps enhanced color 
set key right top
set title 'North Lobe'
set xlabel 'Energy (eV)' 
set ylabel '{/Symbol n} F({/Symbol n}) [erg cm^{-2} s^{-1}]' 

set autoscale
set output '/home/antonio/nissimExercises/NGC1275/figure.eps'
set logscale x
set logscale y
set format y "10^{%L}"
#set style line 1 lt 1 lw 6

set bars 1
set points 0.8 

plot  'syn.dat' u 1:2 smooth sbezier title "" w lines linestyle  1 lt 1 lc 3, "comp.dat" u 1:2 smooth sbezier title "" w lines linestyle  1 lt 1 lc 3, 'butterfly-final.dat' title "" with xyerrorbars  , 'FERMI.dat' title "" with xyerrorbars  , 'magic.dat' title "" with xyerrorbars  , 'MisuMe.dat' title "" with xyerrorbars  , 'Swift_uvot.dat' title "" with xyerrorbars  , 'unkown.dat' title "" with xyerrorbars  , 'ratan.dat' title "" with xyerrorbars  , 'mojave.dat' title "" with xyerrorbars  ,
         
   






