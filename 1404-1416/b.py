##############################################################################################
##########################Class of some equations of the article:#############################
############An Up-scattered Cocoon Emission Model of Gamma-Ray Burst High-Energy Lags#########
##############################################################################################
##############################################################################################
######Note: We denote r instead of r*#########################################################
##############################################################################################

import math

#Module of rs
#Here gammaC is the Terminal Lorentz Factor
def rs(r, gammaC):
    return r*gammaC


#Module of rph
#Here sigmaT is the Thomson Cross Section
def rph(Ec, sigmaT, thetaC, gammaC, mp, c):
    return math.sqrt((Ec*sigmaT)/(math.pi*2)*(1-math.cos(thetaC))*gammaC*mp*math.pow(c,2))


#Module of deltaTi
#Here gammaJ is the bulk Lorentz factor of the jet and z is the source redshift
def deltaTi(ri, c, gammaJ, z):
    return (ri/(2*c*math.pow(gammaJ,2)))*(1+z)


#Module of deltaTc
def deltaTc(rph, c, gammaC, z):
    return (rph/(2*c*math.pow(gammaC,2)))*(1+z)


#Module of rd
#Were alfa <= 1
def rd(alfar, gammaC):
    return (2*alfar)*math.pow(gammaC,2)

#Module of TprimeInit
def tPrimeInit(Ec, thetaC, r, a):
    return math.pow((Ec/2*math.pi*(1-math.cos(thetaC))*math.pow(r,3))*a,(1/4))

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
