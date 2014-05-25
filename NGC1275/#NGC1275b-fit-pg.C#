{
 gROOT->Reset();

 c1=new TCanvas ("c1", "",20,1,640,480);
 TMultiGraph *mg = new TMultiGraph();
 mg->SetTitle(";E(eV); E^{2}dN/dE (MeV cm^{-2} s^{-1})");
 c1->SetFillColor(10);
 c1->GetFrame()->SetFillColor(25);
 c1->GetFrame()->SetBorderSize(20);
 




 Int_t n4=3;//Magic
 Int_t i;
 Float_t w4[n4]={1e11, 1.9e11, 3.8e11};//x
 Float_t v4[n4]={3.8e-6,6.8e-7,3.7e-7};//y
 Float_t ewl4[n4]={0,0,0};
 Float_t evl4[n4]={1.0e-6,4.8e-7,3.1e-7};
 Float_t ewh4[n4]={0,0,0};
 Float_t evh4[n4]={1.8e-6,4.8e-7,3.1e-7};
 gr4=new TGraphAsymmErrors(n4,w4,v4,ewl4,ewh4,evl4,evh4);
 gr4->SetMarkerColor();
 gr4->SetMarkerStyle(8);
 gr4->SetMarkerSize(0.7);
 gr4->SetLineColor(1);
 gPad->SetLogy();
 gPad->SetLogx();


 
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






  mg->Add(gr4);
 
 mg->Add(gr20);
 mg->Add(gr21);
 
 mg->Draw("apz");



 TLegend *legend = new TLegend(0.6,0.6,0.92,0.98);
 legend->SetFillColor(0);
 //legend->SetFillAttributes(14);
 legend->SetBorderSize(1.0);
 //legend->SetTextAlign(12);
  legend->AddEntry(gr4,"Magic","p");
 //legend->AddEntry(gr9,"HST-optical-UV","p");
 //legend->AddEntry(gr10,"CHANDRA-core-X","p");
 //legend->AddEntry(gr11,"SWIFT-BAT-X-limit","p");
 legend->Draw();

//############################Fit formulas###############
//################
//##############################################################
 fun2 = new TF1("fun2"," [0]*((0.1e12/0.1e12)^(-1)*(x/0.1e12)**(3-[1])*(x>=0.06e12)*(x<0.1e12)+((x/0.1e12)**(2-[1])*(x>=0.1e12)*(x<5e13)))",1E11,7E14); //pgamma interaction

// fun3 = new TF1("fun3","[0]*(x/0.1e12)^(2-[1])",1e+11,1e+13); //pp interaction
 
//#################fit commands############
//####################################
//###############
//
//
//

 fun2->SetLineWidth(2);
  gr4->Fit("fun2","APL+"); 
 // gr4->Fit("fun3","APL+"); 
 }


