import b
from b import *

rsc=rs(r_star, gammac)
rphc=rph(Ec, thetac, gammac)
delta_tcc=delta_tc(gammac, z)
rdc=rd(r_star, gammac,alphar)
Tinc=Tin(Ec, thetac, r_star)
Tphc=Tph(Ec, r_star, gammac,alphar, thetac)
Enc=En(Ec, r_star, gammac,alphar, thetac)
fconc=fcon(Ec, r_star, gammac,alphar, thetac)
risj=ris(gammaj,dt,z)
denpj=denp(Lj, z,gammaj, dt)
optj=opt(Lj, z,gammaj, dt)
Bj=B(xiB,Lj, gammaj,dt)
gamma_mij=gamma_mi(xiB,Lj, gammaj,dt)
gamma_cj=gamma_c(xiB,Lj, gammaj,dt,xuc)
E_mj=E_m(xiB,Lj, gammaj,dt)
Fcoj=Fco(xiB,Lj, gammaj,dt,dz)
E_msscj=E_mssc(xiB,Lj, gammaj,dt)
Fcosscj=Fcossc(xiB,Lj, gammaj,dt,dz)


print 'Saturation radius %2.2e ' %rsc
print 'Photospheric radius %2.2e ' %rphc
print 'Photospheric emission time %2.2e '%delta_tcc
print 'internal shocks radius %2.2e '%rdc
print 'initial temperature %2.2e '%Tinc
print 'photospheric temperature %2.2e '%Tphc
print 'observed energy %2.2e '%Enc
print 'const flux %2.2e '%fconc
print 'internal shock radius %2.2e '%risj
print 'proton density %2.2e '%denpj
print 'optical depth %2.2e '%optj
print 'Magnetic field %2.2e '%Bj
print 'minimum Lorentz factor %2.2e '%gamma_mij
print 'cut off Lorentz factor %2.2e '%gamma_cj
print 'minimum energy %2.2e '%E_mj
print 'const flux %2.2e '%Fcoj
print 'ssc energy m %2.2e '%E_msscj
print 'ssc flux m %2.2e '%Fcosscj
