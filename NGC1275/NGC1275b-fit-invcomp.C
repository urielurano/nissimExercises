{
 gROOT->Reset();

 c1=new TCanvas ("c1", "",20,1,640,480);
 TMultiGraph *mg = new TMultiGraph();
 mg->SetTitle(";E(eV); E^{2}dN/dE (MeV cm^{-2} s^{-1})");
 c1->SetFillColor(10);
 c1->GetFrame()->SetFillColor(25);
 c1->GetFrame()->SetBorderSize(20);



 Int_t n2=11;//FERMI
 Int_t i;
 //The last four data points were taken from the "butterfly boxes".
 Float_t w2[n2]={3.39070000e+08,   4.96200000e+08,   1.24050000e+09,
         2.68775000e+09,   4.13500000e+09,   1.24050000e+10,
         2.48100000e+10, 2.51e+4, 6.31e+4, 2.818e+5, 4.5e+3};//x
 Float_t v2[n2]={1.87500000e-05,   2.00000000e-05,   1.75000000e-05,
         1.56250000e-05,   1.15625000e-05,   1.00000000e-05,
         8.12500000e-06, 1e-5,1.5e-5, 5e-5, 2e-6};
 Float_t ewl2[n2]={0,0,0,0,0,0,0,0,0,0,0};
 Float_t evl2[n2]={1.87500000e-07,   2.00000000e-07,   1.75000000e-07,
         5.56250000e-06,   4.15625000e-06,   5.00000000e-06,
         5.82500000e-06, 8e-6,8.5e-6, 4.5e-5,0};
 Float_t ewh2[n2]={0,0,0,0,0,0,0,0,0,0,0};
 Float_t evh2[n2]={1.87500000e-07,   2.00000000e-07,   1.75000000e-07,
         5.56250000e-06,   4.15625000e-06,   5.00000000e-06,
         5.82500000e-06,0,0,0,0}; 
gr2=new TGraphAsymmErrors(n2,w2,v2,ewl2,ewh2,evl2,evh2);
 gr2->SetMarkerColor(1);
 gr2->SetMarkerStyle(4);
 gr2->SetMarkerSize(0.7);  
 gr2->SetLineColor(kRed+0); 
 gr2->SetLineStyle(1); 
 gPad->SetLogy();  
 gPad->SetLogx();





  //Int_t n4=3;//Magic
  //Int_t i;
  //Float_t w4[n4]={1e11, 1.9e11, 3.8e11};//x
  //Float_t v4[n4]={3.8e-6,6.8e-7,3.7e-7};//y
  //Float_t ewl4[n4]={0,0,0};
  //Float_t evl4[n4]={1.0e-6,4.8e-7,3.1e-7};
  //Float_t ewh4[n4]={0,0,0};
  //Float_t evh4[n4]={1.8e-6,4.8e-7,3.1e-7};
  //gr4=new TGraphAsymmErrors(n4,w4,v4,ewl4,ewh4,evl4,evh4);
  //gr4->SetMarkerColor();
  //gr4->SetMarkerStyle(8);
  //gr4->SetMarkerSize(0.7);
  //gr4->SetLineColor(1);
  //gPad->SetLogy();
  //gPad->SetLogx();



 Int_t n20=2;//end
 Int_t i;
 Float_t w20[n20]={9.484e13,1.796e13};
 Float_t v20[n20]={1.435e-9,1.996e-9};
 Float_t ewl20[n20]={0,0};
 Float_t evl20[n20]={0,0};
 Float_t ewh20[n20]={0,0};
 Float_t evh20[n20]={0,0};
 gr20=new TGraphAsymmErrors(n20,w20,v20,ewl20,ewh20,evl20,evh20);
 gr20->SetMarkerColor();
 gr20->SetMarkerStyle(8);
 gr20->SetMarkerSize(0.0001);  
 gr20->SetLineColor(3);
 gPad->SetLogy();  
 gPad->SetLogx();
 gr20->SetFillColor(2); 

 Int_t n21=2;//beginning
 Int_t i;
 Float_t w21[n21]={2.484e-9,5.796e-9};
 Float_t v21[n21]={1.435e-9,1.996e-9};
 Float_t ewl21[n21]={0,0};
 Float_t evl21[n21]={0,0};
 Float_t ewh21[n21]={0,0};
 Float_t evh21[n21]={0,0};
 gr21=new TGraphAsymmErrors(n21,w21,v21,ewl21,ewh21,evl21,evh21);
 gr21->SetMarkerColor();
 gr21->SetMarkerStyle(8);
 gr21->SetMarkerSize(0.0001);  
 gr21->SetLineColor(3);
 gPad->SetLogy();  
 gPad->SetLogx();
 gr21->SetFillColor(2); 






 mg->Add(gr2);
 mg->Add(gr20);
 mg->Add(gr21);
 
 mg->Draw("apz");



 TLegend *legend = new TLegend(0.6,0.6,0.92,0.98);
 legend->SetFillColor(0);
 //legend->SetFillAttributes(14);
 legend->SetBorderSize(1.0);
 //legend->SetTextAlign(12);
 legend->AddEntry(gr2,"Fermi","p");
 //legend->AddEntry(gr9,"HST-optical-UV","p");
 //legend->AddEntry(gr10,"CHANDRA-core-X","p");
 //legend->AddEntry(gr11,"SWIFT-BAT-X-limit","p");
 //legend->Draw();

//############################Fit formulas###############
//################
//##############################################################
//

 fun4 = new TF1("fun4"," [0]*((x/[1])^(4/3)*(x>1e-6)*(x<[1])+((x/[1])**((3-2.8267)/2)*(x>=[1])*(x<[2])) + (([2]/[1])**((3-2.8267)/2))*((x/[2])**((2-2.8267)/2))*(x>=[2]))",  1e+4,1e+12); //pgamma interaction
 // Se fija el valor inicial de las energías de normalización:
  fun4->SetParameter(0,6.32041e-07);
  //fun4->SetParLimits(0,1e+5,1e+7);
  fun4->SetParameter(1,1e+6);
  fun4->SetParLimits(1,1e+5,1e+7);
  fun4->SetParameter(2,5e+7);
  fun4->SetParLimits(2,1e+7,1e+9);
 
//#################fit commands############
//####################################
//###############
//
//
//

 fun4->SetLineWidth(2);
 gr2->Fit("fun4","APL+"); 
 //gr4->Fit("fun3","APL+"); 
 }


