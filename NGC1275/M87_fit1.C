{
 gROOT->Reset();

 c1=new TCanvas ("c1", "",20,1,640,480);
 TMultiGraph *mg = new TMultiGraph();
 mg->SetTitle(";E(eV); E^{2}dN/dE (MeV cm^{-2} s^{-1})");
 c1->SetFillColor(10);
 c1->GetFrame()->SetFillColor(25);
 c1->GetFrame()->SetBorderSize(20);

 // ################################# Unities #################################

 Double_t eV,KeV,MeV,GeV,TeV,PeV,EeV,ZeV,Jule,erg;   //Energy scales
 Double_t Hz,Kelvin;  //others
 Double_t me,mp,md,mu,mpion,mdelta,mkaon,Mw,Mz,gram,Kg,Msun,Mearth;   //Mass
 Double_t alph, e ; //Unity of electric charge
 Double_t Gauss,Tesla;  //Unity of magnetic field
 Double_t fm,cm,meter,inc,Km,pc,Ly,kpc,Mpc,Gpc,barn,Rsun,Rearth, mbarn, barn; //Distances Scales  
 Double_t sec,msec,minute,hour,day,year;   //Time Scales
 Double_t sigmaT,sigmaTp,sigmapp,sigmapg;   //Cross Section
 Double_t c,hbar, pi; //fundamentals

 // ################################# VARIABLES     #################################

 Double_t Lpg,Lpp;
 Double_t theta_jet,Eknot,taupssc;
 Double_t xie,xiB,Gama,dtob,dtob1,Lob,Lob1,z,fes,alpha,dz,xf,theta_inc,E0; //Variables
 Double_t beta,mu,deltad,reg_obs,Bgauss;//Variables as a function of other variables 
 Double_t Esyn_obsm,Esyn_obsb,Esyn_obsmax;//synchroton
 Double_t gama_em,gama_eb,gama_emax,Eic_obsm,Eic_obsb,Eic_obsmax;//IC
 Double_t Epgama_obsb,Dpg,Dpp,xipgpeak,sigmapeak,deltaEpeak,Epeak,theta_pg; //pgama interaction 
 Double_t np,kpp,xipppeak,R; // PP interaction
 Double_t Epm,taup,E04,an,Ad,w,nevents;//Number of events
 Double_t Ap,Ap1,Ap2,Ae,Aic,Egob1,Egob2,Egob1c,Egob2c,Egobm,fopp;
 Double_t alphar,alpha1,alpha2,Eic_obsb,Apg,App,Apg2,App2,n_events_pg,n_events_pp;

 // ################################ CONSTANTES FUNDAMENTALES ################################################
 // ################################ NUNCA TOCAR #############################################################
 // ##########################################################################################################
 // ##########################################################################################################

 // #########################   SCALES     ####################################

 //Energy Scales
 eV=1;
 KeV=1E3*eV;
 MeV=1E6*eV;
 GeV=1E9*eV;
 TeV=1E12*eV;
 PeV=1E15*eV;
 EeV=1E18*eV;
 ZeV=1E21*eV;
 Hz=(1/(2.418*1E14))*eV;
 Kelvin=(1/(300*38.681686))*eV;
 Jule=(1/(1.602176462))*1E19*eV;
 erg=1E-7*Jule;

 //Mass
 me=0.510998902*MeV;
 mp=938.271998*MeV;
 md=1875.612762*MeV;
 mu=931.494013*MeV;
 mpion=139.57*MeV;
 mdelta=1232*MeV;
 mkaon=493.67*MeV;
 Mw=80.419*GeV;
 Mz=91.1882*GeV;
 gram=(1/1.782661731)*1E33*eV;
 Kg=1E3*gram;
 Msun=1.98844*1E30*Kg;
 Mearth=5.9723*1E24*Kg;

 //Unity of electric charge
 alph=7.297352533*1E-3; 
 e=0.3028;  // Lorentz - Heaviside

 //Unity of magnetic field
 Gauss=(5.788381749*1E-15)*MeV*2*(me/e);
 Tesla=1E4*Gauss;

 //Distance Scales  
 fm=1/(197.3269602*MeV); 
 cm=1E13*fm;
 meter=1E2*cm;
 inc=0.0254*meter;
 Km=1E3*meter;
 pc=3.0856775807*1E16*meter;
 Ly=0.9462*1E16*meter;
 kpc=1E3*pc;
 Mpc=1E6*pc;
 Gpc=1E9*pc;
 barn=1E-28*meter**2; 
 mbarn=1E-3*barn;
 Rsun=6.961*1E8*meter;
 Rearth=6.378140*1E6*meter;

 //Time Scales
 sec=299792458*meter;
 msec=1E-3*sec;
 minute=60*sec;
 hour=60*minute;
 day=24*hour;
 year=31556925.2*sec;

 //Cross Section
 sigmaT=6.65*1E-25*cm**2;
 sigmaTp=((me/mp)**2)*sigmaT;
 sigmapp=3.0*1E-26*cm**2;
 sigmapg=5.0*1E-28*cm**2;
 pi = 3.1415926; 
 c = 1;
 hbar=1;

 //##########################################################################################################################################################
 //###########################################   DATES  #####################################################################################################
 //##########################################################################################################################################################


 Int_t n2=6;//VERITAS
 Int_t i;
 Float_t w2[n2]={0.24e+12,0.42e+12,0.75e+12,1.33e+12,2.37e+12,4.22e+12};//x
 Float_t v2[n2]={0.0576*1.99e-5, 0.17* 3.56e-6, 0.5625*1.51e-6, 1.7689*1.7e-7,5.6169*6.02e-8,17.8084*1.72e-8};
 Float_t ewl2[n2]={0,0,0,0,0,0};
 Float_t evl2[n2]={0.0576*0.54e-5,0.17* 1.16e-6,  0.5625* 0.34e-6, 1.7689* 0.95e-7, 5.6169* 3.4e-8, 17.8084* 1.13e-8};
 Float_t ewh2[n2]={0,0,0,0,0,0};
 Float_t evh2[n2]={0.0576*0.54e-5,0.17* 1.16e-6,  0.5625* 0.34e-6, 1.7689* 0.95e-7, 5.6169* 3.4e-8, 17.8084* 1.13e-8};
 gr2=new TGraphAsymmErrors(n2,w2,v2,ewl2,ewh2,evl2,evh2);
 gr2->SetMarkerColor();
 gr2->SetMarkerStyle(22);
 gr2->SetMarkerSize(0.8);  
 gPad->SetLogy();  
 gPad->SetLogx();





 Int_t n3=6;//Magic
 Int_t i;
 Float_t w3[n3]={0.12e+12,0.205e+12,0.320e+12,0.5e+12,0.79e+12,1.3e+12};//x
 Float_t v3[n3]={1.096e-6, 6.3037e-7, 5.2224e-7, 0.75e-6,4.0935e-7,6.39e-7};
 Float_t ewl3[n3]={0.03e+12,0.05e+12,0.07e+12,0.1e+12,0,0};//0.03e+12,0.05e+12,0.07e+12,0.1e+12,0.05e+12,0.01e+12
 Float_t evl3[n3]={2.46e-7,2.0e-7,1.8e-7,2.1e-7,1.1e-7,1.38e-7};//0.4*4.46e-7,0.4*3.78e-7,0.4*3.07e-7,0.4*7.5e-7,0.4*2.496e-7,0.4*3.38e-7
 Float_t ewh3[n3]={0.04e+12,0.05e+12,0.06e+12,0.14e+12,0,0};//0.04e+12,0.05e+12,0.06e+12,0.14e+12,0.1e+12,0.03e+12
 Float_t evh3[n3]={0.316e-6,0.81e-7,1.16e-7,0.2e-6,0.4e-7,0.22e-7};//0.18*2.016e-6,0.18*8.41e-7,0.18*7.16e-7,0.13*1.25e-6,0.13*6.24e-7,0.13*6.76e-7
 gr3=new TGraphAsymmErrors(n3,w3,v3,ewl3,ewh3,evl3,evh3);
 gr3->SetMarkerColor();
 gr3->SetMarkerStyle(22);
 gr3->SetMarkerSize(0.8);  
 gPad->SetLogy();  
 gPad->SetLogx();



 Int_t n4=6;//Flare
 Int_t i;
 Float_t w4[n4]={0.165e+12,0.332e+12,0.74e+12,1.51e+12,3.35e+12,7.15e+12};//x
 Float_t v4[n4]={6.878e-6, 4.60896e-6, 6.2878e-6, 4.78821e-6,3.52286e-6,2.6265e-6};
 Float_t ewl4[n4]={0.03e+12,0.1e+12,0.24e+12,0.3e+12,1.0e+12,0};//0.01e+12,0.1e+12,0.24e+12,0.3e+12,1.0e+12,2.0e+12
 Float_t evl4[n4]={0.15*4.81e-6,0.3*2.31e-6,0.3*3.83e-6,0.3*3.422e-6,0.3*2.24e-6,0.7*5.11e-7};
 Float_t ewh4[n4]={0.075e+12,0.14e+12,0.45e+12,0.7e+12,1.0e+12,0};//0.01e+12,0.14e+12,0.45e+12,0.7e+12,1.5e+12,0.4e+13
 Float_t evh4[n4]={0.13*9.85e-6,0.3*5.62e-6,0.3*7.119e-6,0.3*7.069e-6,0.3*5.05e-6,0.3*3.579e-6};
 gr4=new TGraphAsymmErrors(n4,w4,v4,ewl4,ewh4,evl4,evh4);
 gr4->SetMarkerColor();
 gr4->SetMarkerStyle(22);
 gr4->SetMarkerSize(0.8);  
 gPad->SetLogy();  
 gPad->SetLogx();






 Int_t n5=9;//HESS
 Int_t i;
 Float_t w5[n5]={0.445e+12,0.68e+12,1.05e+12,1.65e+12,2.41e+12,3.8e+12,5.86e+12,8.9e+12,1.05e+13 };//x
 Float_t v5[n5]={1.46834e-6, 1.4011e-6, 1.4435e-6, 7.23e-7,1.15e-6,1.0985e-6,6.292e-7, 0.877e-6, 8.517e-7};
 Float_t ewl5[n5]={0,0,0,0,0,0,0,0,0};
 Float_t evl5[n5]={0.3*5.94e-7,0.2*1.16e-6,0.24*1.10e-6,0.24*4.62e-7,0.24*7.55e-7,0.2*8.66e-7,0.24*8.59e-8,0.24*6.33e-7,0.24*4.41e-7};
 Float_t ewh5[n5]={0,0,0,0,0,0,0,0,0};
 Float_t evh5[n5]={0.17*1.78e-6,0.15*1.80e-6,0.17*1.87e-6,0.17*1.03e-6,0.17*1.33e-6,0.17*1.598e-6,0.12*7.55e-7,0.12*1.58e-6,0.12*1.54e-6};
 gr5=new TGraphAsymmErrors(n5,w5,v5,ewl5,ewh5,evl5,evh5);
 gr5->SetMarkerColor();
 gr5->SetMarkerStyle(8);
 gr5->SetMarkerSize(0.8);  
 gPad->SetLogy();  
 gPad->SetLogx();

 Int_t n9=2;//
 Int_t i;
 Float_t w9[n9]={1e+10,0.68e+14};//x
 Float_t v9[n9]={1e-4, 1.4011e-8};
 Float_t ewl9[n9]={0,0};
 Float_t evl9[n9]={0,0};
 Float_t ewh9[n9]={0,0};
 Float_t evh9[n9]={0,0};
 gr9=new TGraphAsymmErrors(n9,w9,v9,ewl9,ewh9,evl9,evh9);
 gr9->SetMarkerColor();
 gr9->SetMarkerStyle();
 gr9->SetMarkerSize(0.001);  
 gPad->SetLogy();  
 gPad->SetLogx();




 //mg->Add(gr2);
 mg->Add(gr3);
 //mg->Add(gr4);
 //mg->Add(gr5);
 mg->Add(gr9);
 mg->Draw("apz");

 //############################################################################################################################################
 //############################################################################################################################################
 //############################################################################################################################################

 //############################################################################################################################################
 //############################################################################################################################################
 //############################################################################################################################################


 //############################################################################################################################################
 //###########################################     ESPECTRUM   ################################################################################
 //############################################################################################################################################ 

 fun2 = new TF1("fun2"," [0]*((0.5e12/0.3e12)^(-1)*(x/0.3e12)**(3-[1])*(x>=0.7e11)*(x<0.5e12)+((x/0.3e12)**(2-[1])*(x>=0.5e12)*(x<5e13)))",1E11,7E14); //pgamma interaction

 //fun3 = new TF1("fun3","[0]*(x/1e12)^(2-[1])",1e+11,1e+13); //pp interaction
 
 //fun2->GetParameter(0,a);
//   cout<<a <<endl;
 //############################################################################################################################################
 //################################################# SET PARAMETERS ###########################################################################
 //############################################################################################################################################
 

 

 fun2->SetLineWidth(2);
 gr3->Fit("fun2","APL+"); 
 //gr3->Fit("fun3","APL+"); 



 }


// Float_t a=fun2.GetParameter(0);
// Float_t b=fun2.GetParameter(1);
// Float_t aer=fun2.GetParError(0);
// Float_t ber=fun2.GetParError(1);


//fun3 = new TF1("fun3"," [0]*((674.98e9/1e12)^(-1)*(x/1e12)**(3-[1])*(x>=1e11)*(x<674.98e9)+((x/1e12)**(2-[1])*(x>=674.98e9)*(x<1e13)))",1E11,3E13);


//fun3->SetParameter(0,a);   
//fun3->SetParameter(1,b);   

// fun3->Draw("C","same");

// cout<<a<<"\n"<<b<<endl;
// cout<<aer<<"\n"<<ber<<endl;

