##############################################################################################
##########################Class of some equations of the article:#############################
############An Up-scattered Cocoon Emission Model of Gamma-Ray Burst High-Energy Lags#########
##############################################################################################

import c
from c import *




###########################################################################################
####################### Dynamics of Cocoon   ##############################################
###########################################################################################




def rs(r_star, gammac): #Here gammaC is the Terminal Lorentz Factor
    return r_star*gammac*1/cm

def rph(Ec, thetac, gammac):#Module of rph
    return sqrt(Ec*sigmaT/(2*pi*(1-cos(thetac))*gammac*mp))*1/cm

def delta_tc(gammac, z):#Module of delta_tc
    rp=sqrt(Ec*sigmaT/(2*pi*(1-cos(thetac))*gammac*mp))
    return rp/(2*pow(gammac,2))*(1+z)*1/sec

def rd(r_star, gammac,alphar):#modulo of internal shocks radius
    return 2*alphar*r_star*pow(gammac,2)*1/cm

def Tin(Ec, thetac, r_star):
    return pow(Ec/(2*pi*(1-cos(thetac))*pow(r_star,3.0)*asigmaB),1.0/4.0)*1/Kelvin

def Tad(Ec, r_star, gammac,alphar, thetac):
    Tin=pow(Ec/(2*pi*(1-cos(thetac))*pow(r_star,3.0)*asigmaB),1.0/4.0)
    rs=r_star*gammac
    rd=2*alphar*r_star*pow(gammac,2)
    return Tin*pow(rs/r_star,-1.0)*pow(rd/rs,-2.0/3.0)*1/Kelvin

def Td(Ec, r_star, gammac,alphar, thetac):
    Tin=pow(Ec/(2*pi*(1-cos(thetac))*pow(r_star,3.0)*asigmaB),1.0/4.0)
    rs=r_star*gammac
    rd=2*alphar*r_star*pow(gammac,2)
    Tad=Tin*pow(rs/r_star,-1.0)*pow(rd/rs,-2.0/3.0)
    return Tad*pow(rd/rs,1.0/6.0)*pow(xiD,1.0/4.0)*1/Kelvin


def Tph(Ec, r_star, gammac,alphar, thetac):
    Tin=pow(Ec/(2*pi*(1-cos(thetac))*pow(r_star,3.0)*asigmaB),1.0/4.0)
    rs=r_star*gammac
    rd=2*alphar*r_star*pow(gammac,2)
    Tad=Tin*pow(rs/r_star,-1.0)*pow(rd/rs,-2.0/3.0)
    rph=sqrt(Ec*sigmaT/(2*pi*(1-cos(thetac))*gammac*mp))
    return Tad*pow(rph/rd,-2.0/3.0)*1/Kelvin
    

def En(Ec, r_star, gammac,alphar, thetac):
    Tin=pow(Ec/(2*pi*(1-cos(thetac))*pow(r_star,3.0)*asigmaB),1.0/4.0)
    rs=r_star*gammac
    rd=2*alphar*r_star*pow(gammac,2)
    Tad=Tin*pow(rs/r_star,-1.0)*pow(rd/rs,-2.0/3.0)
    rph=sqrt(Ec*sigmaT/(2*pi*(1-cos(thetac))*gammac*mp))
    Tph=Tad*pow(rph/rd,-2.0/3.0)
    return 2.82*2*gammac*1/(1+z)*Tph*1/KeV

########   Verificar   #######

def fcon(Ec, r_star, gammac,alphar, thetac):
    Tin=pow(Ec/(2*pi*(1-cos(thetac))*pow(r_star,3.0)*asigmaB),1.0/4.0)
    rs=r_star*gammac
    rd=2*alphar*r_star*pow(gammac,2)
    Tad=Tin*pow(rs/r_star,-1.0)*pow(rd/rs,-2.0/3.0)
    rph=sqrt(Ec*sigmaT/(2*pi*(1-cos(thetac))*gammac*mp))
    Tph=Tad*pow(rph/rd,-2.0/3.0)
    Enu=2.82*2*gammac*1/(1+z)*Tph
    return pow(1+z,3)/pow(dz, 2)*2*pi*pow(Enu/(2*pi),2)*Tph*gammac*pow(rph/gammac,2.0)*pow(cm,2.0)*sec







###########################################################################################
####################### Dynamics of jet   ##############################################
###########################################################################################





def ris(gammaj,dt,z):#modulo of internal shocks radius
    return 2*pow(gammaj,2)*dt/(1+z)*1/cm



def denp(Lj, z,gammaj, dt):
    return Lj*pow(1+z,2.0)/(32*pi*mp*pow(gammaj,6.0)*pow(dt,2.0))*pow(cm,3)

def opt(Lj, z,gammaj, dt):
    nden= Lj*pow(1+z,2.0)/(32*pi*mp*pow(gammaj,6.0)*pow(dt,2.0))
    rj=2*pow(gammaj,2)*dt/(1+z)
    return sigmaT*nden*rj/gammaj


def B(xiB,Lj, gammaj,dt):
    denp=Lj*pow(1+z,2.0)/(32*pi*mp*pow(gammaj,6.0)*pow(dt,2.0))   
    return sqrt(8*pi*xiB*denp*mp)*1/Gauss


def gamma_mi(xiB,Lj, gammaj,dt):
    return (p-2.0)/(p-1.0)*mp/me*xie


def gamma_c(xiB,Lj, gammaj,dt,xuc):
    denp=Lj*pow(1+z,2.0)/(32*pi*mp*pow(gammaj,6.0)*pow(dt,2.0))   
    B=sqrt(8*pi*xiB*denp*mp)
    cons=6*pi*me/sigmaT
    rsi=2*pow(gammaj,2)*dt/(1+z)
    nden= Lj*pow(1+z,2.0)/(32*pi*mp*pow(gammaj,6.0)*pow(dt,2.0))
    rj=2*pow(gammaj,2)*dt/(1+z)
    tau=sigmaT*nden*rj/gammaj
    gamc=1.0*pow(10,2.8)
    x1=4.0/3.0*tau*pow(gamc,2.0)*p/(p-2.0)
    return cons*pow(B,-2.0)*pow(rsi,-1.0)*gammaj*pow(1+x1+x1*xuc,-1.0)
    


def E_m(xiB,Lj, gammaj,dt):
    denp=Lj*pow(1+z,2.0)/(32*pi*mp*pow(gammaj,6.0)*pow(dt,2.0))   
    B=sqrt(8*pi*xiB*denp*mp)
    gamma_mi=(p-2.0)/(p-1.0)*mp/me*xie
    return 3*e*B*1/me*pow(gamma_mi,2.0)*2*gammaj/(1+z)


def Fco(xiB,Lj, gammaj,dt,dz):
    denp=Lj*pow(1+z,2.0)/(32*pi*mp*pow(gammaj,6.0)*pow(dt,2.0))   
    B=sqrt(8*pi*xiB*denp*mp)
    N=Lj*dt/(1+z)*1/(gammaj*mp)
    return sqrt(3)*pow(e,3.0)*B/me*N*2*gammaj*(1+z)/(4*pi*pow(dz,2.0))*pow(cm,2.0)*sec 
   
def E_mssc(xiB,Lj, gammaj,dt):
    denp=Lj*pow(1+z,2.0)/(32*pi*mp*pow(gammaj,6.0)*pow(dt,2.0))   
    B=sqrt(8*pi*xiB*denp*mp)
    gamma_mi=(p-2.0)/(p-1.0)*mp/me*xie
    E_m=3*e*B*1/me*pow(gamma_mi,2.0)*2*gammaj/(1+z)
    return 4*pow(gamma_mi,2.0)*E_m


def Fcossc(xiB,Lj, gammaj,dt,dz):
    denp=Lj*pow(1+z,2.0)/(32*pi*mp*pow(gammaj,6.0)*pow(dt,2.0))   
    B=sqrt(8*pi*xiB*denp*mp)
    N=Lj*dt/(1+z)*1/(gammaj*mp)
    Fco=sqrt(3)*pow(e,3.0)*B/me*N*2*gammaj*(1+z)/(4*pi*pow(dz,2.0))
    nden= Lj*pow(1+z,2.0)/(32*pi*mp*pow(gammaj,6.0)*pow(dt,2.0))
    rj=2*pow(gammaj,2)*dt/(1+z)
    tau= sigmaT*nden*rj/gammaj
    return tau*Fco*pow(cm,2.0)*sec 






#Module of deltaTi
#Here gammaJ is the bulk Lorentz factor of the jet and z is the source redshift
def deltaTi(ri, c, gammaJ, z):
    return (ri/(2*c*math.pow(gammaJ,2)))*(1+z)




#Module of rd
#Were alfa <= 1


#Module of TprimeInit


#Module TprimeD
def tPrimeD(Ec, xid, gammaC, thetaC, rd, r, a):
    return  ((Ec*xid)/gammaC)/(2*math.pi*(1-math.cos(thetaC))*math.pow(rd,2)*r*gammaC*a)


#Module epsilonPhCo
def epsilonPhCo(k, tPrimePh, gammaC, z):
    return 2.82*k*tPrimePh*((2*gammaC)/(1+z))

#Module fEpsilonPhCo
def fEpsilonPhCo(z, dl, vPhCo, c, k, tPrimePh, gammaC, rPh):
 a = math.pow((1+z),3)/math.pow(dl, 2),
 b = ((2*math.pi*math.pow(vPhCo,2))/math.pow(c,2)),
 c = k*tPrimePh*gammaC*math.pow(rPh/gammaC,2),
 return a[0]*b[0]*c[0]
 
#Module ri
def ri(c, gammaJ, deltaTi, z):
    return (2*c*math.pow(gammaJ,2))*(deltaTi/(1+z))

#Module nPrime
def nPrime(L, z, mp, c, gammaJ, deltaTi):
    return (L*math.pow((1+z),2))/(32*math.pi*mp*math.pow(c,5)*math.pow(gammaJ,6)*math.pow(deltaTi,2))

#Module bPrime
def bPrime(xiB, uPrime):
    return math.sqrt(8*math.pi*xiB*uPrime)

#Module epsilonM
def epsilonM(h,bPrime, me, c, gammaM, gammaJ, z):
    a = (3*h*math.exp(1)*bPrime)/(4*math.pi*me*c),
    b = math.pow(gammaM,2),
    c = (2*gammaJ)/(1+z),
    return a[0]*b[0]*c[0]

#Module fEpsilonC
def fEpsilonC(bPrime, N, me, c, gammaJ, z, dl):
    a = (math.sqrt(3)*math.exp(3)*bPrime*N)/(me*math.pow(c,2)),
    b = (2*gammaJ*(1+z))/(4*math.pi*math.pow(dl,2)),
    return a[0]*b[0]

#Module epsilonSCa
def epsilonSCa(gammaC, epsilonA):
    return 4*math.pow(gammaC, 2)*epsilonA

#Module epsilonSCc
def epsilonSCa(gammaC, epsilonC):
    return 4*math.pow(gammaC, 2)*epsilonC

#Module epsilonKN
#Where KN is the Klein-Nishina effect
def epsilonKN(gammaJ, gammaC, me, c, z):
    return gammaJ*gammaC*me*math.pow(c,2)*(1/(1+z))

#Module jEpsilonS
def jEpsilonS(ri, dl, z, fCoEpsilonS):
    return ((1)/(4*math.pi*math.pow(ri,2)))*((math.pow(dl,2))/(1+z))*fCoEpsilonS

#Module xiTheta
def _xi(thetaPrime, xPrime):
    return (1-cos(thetaPrime + xPrime), 1-cos(thetaPrime - xPrime))


#Module epsilonUCprimeC
#Remember make the value of theta and x before use _xi
def epsilonUCprimeC(gammaC, epsilonCOprimePH, theta, x):
    xi = _xi(thetaPrime, xPrime),
    return (2*math.pow(gammaC,2)*epsilonCOprimePH*xi*theta)


#Module epsilonUCprimeM                                                                                                                              #Remember make the value of theta and x before use _xi                                                                                               
def epsilonUCprimeM(gammaM, epsilonCOprimePH, theta, x):
    xi = _xi(thetaPrime, xPrime),
    return (2*math.pow(gammaM,2)*epsilonCOprimePH*xi*theta)

#Module epsilonUCprimeCut
#Remember make the value of theta and x before use _xi                                                                                               
def epsilonUCprimeCut(gammaM, epsilonCOprimeCut, theta, x):
    xi = _xi(thetaPrime, xPrime),
    return (2*math.pow(gammaM,2)*epsilonCOprimeCut*xi*theta)

#Module rPhj
def rPhj(sigmaT, L, mp, c, gammaJ):
    return(sigmaT*L)/(4*math.pi*mp*math.pow(c,3)*math.pow(gammaJ,3))
