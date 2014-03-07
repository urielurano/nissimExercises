import a, math
from a import *
from math import *

xi=0.2
theta=90.0


num=pow(mdelta,2)-pow(mp,2)
den=1-cos(theta)


##################################################
# parameter of the Cen A 
Epeak_c=0.150*MeV
deltaD_c=1.47
z_c=0.0


Eres_c=pow(deltaD_c,2)/pow((1+z_c),2)*xi/4.0*num/den*1/Epeak_c
ggg_c=Eres_c/GeV
print 'el valor de cen A es %s ' %ggg_c +'GeV' 



##################################################
# parameter of the M87 
Epeak_m=0.496*MeV
deltaD_m=3.9
z_m=0.0

Eres_m=pow(deltaD_m,2)/pow((1+z_m),2)*xi/4.0*num/den*1/Epeak_m
ggg_m=Eres_m/GeV
print 'el valor de M87 es %s ' %ggg_m +'GeV' 



##################################################
# parameter of the NGC1275 
Epeak_n=4.4*MeV
deltaD_n=2.9
z_n=0.0179

Eres_n=pow(deltaD_n,2)/pow((1+z_n),2)*xi/4.0*num/den*1/Epeak_n
ggg_n=Eres_n/GeV
print 'el valor de NGC1275 es %s ' %ggg_n +'GeV' 


##################################################
#to Obtain delta from gamma
gama=3.0
th=20.0
a= cos(th*pi/180.0)
beta=sqrt((gama**2-1)/gama**2)

delta=1/(gama*(1-beta*a))
print 'el valor de delta para  NGC1275 es %s ' %delta

