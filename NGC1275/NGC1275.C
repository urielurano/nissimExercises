{
 gROOT->Reset();

 c1=new TCanvas ("c1", "",20,1,640,480);
 TMultiGraph *mg = new TMultiGraph();
 mg->SetTitle(";E(eV); E^{2}dN/dE (MeV cm^{-2} s^{-1})");
 c1->SetFillColor(10);
 c1->GetFrame()->SetFillColor(25);
 c1->GetFrame()->SetBorderSize(20);
 Int_t n=104;//unkonwn
 Int_t i;
 Float_t w[n]={6.2e8,6.6e8,1.1e9,1.4e9,0.95e9,1.4e9,1.4e9, 5.0e9, 2.0e9, 5.0e9, 5.0e9, 7.2e9, 7.2e9, 7.2e9, 1.5e10, 1.8e10,2.1e10   ,2.1e10, 3.0e10, 3.0e10, 4.0e10,5.0e10,6.0e10,6.0e10, 9.8e10,4.0e11, 3.8e11, 1.8e12, 2.3e12, 2.3e12,3.0e13, 8.8e13,2e14,3e14,4e14, 5.4e12, 5.4e12, 5.4e12,  5.4e12, 4.0e14, 3.8e14, 3.5e14, 3.4e14, 2.1e14, 2.1e14, 2.1e14, 7.0e14,6.5e14,7.5e14,8.1e14, 6.0e14, 6.0e14, 6.2e14, 5.8e14, 6.3e14, 6.2e14, 5.8e14, 6.1e14, 5.7e14, 5.5e14, 3.3e14, 3.5e14,3.7e14,3.9e14,4.0e14,4.3e14,2.5e14,2.6e14,2.8e14,2.9e14,  3.3e14, 3.5e14,3.7e14,3.9e14,4.0e14,4.3e14,2.5e14,2.6e14,2.8e14,2.9e14,  9.5e12,  9.5e12, 2.2e13, 2.2e13, 2.2e13, 2.2e13, 2.2e13, 5e13, 4.5e13,5.5e13,5e13,5.2e13,9.8e12,9.8e12,9.8e12,9.8e12, 9.7e13,1e14,1.6e14,2.1e14, 9.7e13,1e14, 3.2e13, 4.2e13 };//x
 Float_t v[n]={6.6e-14,7.2e-14, 1.4e-13,1.4e-13, 1.7e-13, 1.8e-13, 1.9e-13, 2.7e-13, 3.1e-13,  6.6e-13, 6.8e-13,  9.0e-13, 2.2e-12, 2.6e-12, 4.2e-12,  5.4e-12, 6.8e-12, 7.2e-12, 8.4e-12,  9.0e-12, 1.2e-11, 1.4e-11, 1.6e-11, 1.8e-11, 2.8e-11, 6.1e-11, 5.0e-11, 4.2e-11, 8.0e-11, 9.5e-11, 4.5e-11,4.8e-11, 5.6e-11, 6.0e-11, 6.5e-11, 2.2e-10, 2.5e-10, 2.8e-10, 2.9e-10, 8.4e-10, 7.6e-10, 7.3e-10, 6.1e-10, 5.1e-10, 4.6e-10, 4.0e-10, 7.5e-11,7.0e-11, 6.0e-11, 5.1e-11, 1.1e-10,  1.3e-10,  1.5e-10, 1.8e-10, 1.9e-10, 2.1e-10, 2.3e-10, 2.4e-10, 2.5e-10, 2.6e-10,2.5e-10, 2.6e-10, 2.5e-10, 2.6e-10,      1.105e-10, 1.15e-10, 1.205e-10, 1.25e-10, 1.305e-10, 1.35e-10, 1.25e-10, 1.205e-10,   1.85e-10,  1.87e-10, 1.95e-10, 2.15e-10, 2.205e-10, 2.15e-10, 2.305e-10, 2.45e-10, 2.35e-10, 2.405e-10, 3.505e-10, 3.905e-10,  4.005e-10, 4.505e-10,4.905e-10,   3.5e-10,  3.57e-10, 3.05e-10, 2.85e-10, 2.405e-10, 3.505e-10, 3.905e-10,  4.005e-10, 4.105e-10, 1.105e-10, 1.15e-10, 1.205e-10, 1.25e-10,   2.105e-10, 2.35e-10,9.8e-11, 7.8e-11   };//y,
 Float_t ewl[n]={0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
 Float_t evl[n]={0,0,0,0,0,0,0,   0.35e-13,0,0,0,0,  3.7e-13,4.7e-13,0,0,0,0,0,2.2e-13,0,0,0,0,0,0,2.0e-11,0,      2.0e-11, 3.0e-11, 1.0e-11,1.0e-11,1.0e-11,0,0,0,7.2e-11,7.2e-11,7.2e-11,1.2e-10,1.2e-10,1.2e-10,1.2e-10,1.2e-10,1.2e-10,1.2e-10,1.2e-11,1.2e-11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3.0e-11,3.0e-11,3.0e-11,3.0e-11,3.0e-11,3.0e-11,3.0e-11,3.0e-11,3.0e-11,3.0e-11,3.0e-11,3.0e-11};
 Float_t ewh[n]={0,0,0,0,0,0,0,   0.35e-13,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
 Float_t evh[n]={0,0,0,0,0,0,0,0,0,0,0,0, 3.7e-13 ,4.7e-13,0,0,0,0,0,2.2e-13,0,0,0,0,0,0,2.0e-11,0,     2.0e-11, 3.0e-11, 1.0e-11,1.0e-11,1.0e-11,0,0,0,7.2e-11,7.2e-11,7.2e-11,1.2e-10,0,1.2e-10,1.2e-10,1.2e-10,1.2e-10,1.2e-10,1.2e-10,1.2e-11,1.2e-11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3.0e-11,3.0e-11,3.0e-11,3.0e-11,3.0e-11,3.0e-11,3.0e-11,3.0e-11,3.0e-11,3.0e-11,3.0e-11,3.0e-11};
 gr=new TGraphAsymmErrors(n,w,v,ewl,ewh,evl,evh);
 gr->SetMarkerColor();
 gr->SetMarkerStyle(8);
 gr->SetMarkerSize(0.7);  
 gr->SetLineColor(1); 
 
 gr->SetLineStyle(1);  
 gPad->SetLogy();  
 gPad->SetLogx();
  
 Int_t n1=1;//MOJAVE
 Int_t i;
 Float_t w1[n1]={2.3e10};//x
 Float_t v1[n1]={2.1e-12};//y
 Float_t ewl1[n1]={0};
 Float_t evl1[n1]={0};
 Float_t ewh1[n1]={0};
 Float_t evh1[n1]={0};
 gr1=new TGraphAsymmErrors(n1,w1,v1,ewl1,ewh1,evl1,evh1);
 gr1->SetMarkerColor(kRed+0);
 gr1->SetMarkerStyle(4);
 gr1->SetMarkerSize(1.7);  
 gPad->SetLogy();  
 gPad->SetLogx();
 

 Int_t n6=6;//RATAN-600
 Int_t i;
 Float_t w6[n6]={1.05e9, 4e9, 7e9, 8.7e9, 2.1e10, 3.6e10};//x
 Float_t v6[n6]={1.9e-13, 4.2e-13,7.1e-13, 1.5e-12, 2.0e-12,3.4e-12};//y
 Float_t ewl6[n6]={0,0,0,0,0,0};
 Float_t evl6[n6]={0,0,0,0,0,0};
 Float_t ewh6[n6]={0,0,0,0,0,0};
 Float_t evh6[n6]={0,0,0,0,0,0};
 gr6=new TGraphAsymmErrors(n6,w6,v6,ewl6,ewh6,evl6,evh6);
 gr6->SetMarkerColor(kRed+0);
 gr6->SetMarkerStyle(8);
 gr6->SetMarkerSize(0.9);  
 gr6->SetLineColor(kRed+0); 
 gr6->SetLineStyle(1); 
 gPad->SetLogy();  
 gPad->SetLogx();
 

 Int_t n7=1;//MITsuME
 Int_t i;
 Float_t w7[n7]={6.0e14};//x
 Float_t v7[n7]={8.5e-11};//y
 Float_t ewl7[n7]={0};
 Float_t evl7[n7]={0};
 Float_t ewh7[n7]={0};
 Float_t evh7[n7]={0};
 gr7=new TGraphAsymmErrors(n7,w7,v7,ewl7,ewh7,evl7,evh7);
 gr7->SetMarkerColor(kRed+0);
 gr7->SetMarkerStyle(8);
 gr7->SetMarkerSize(1.4);  
 gPad->SetLogy();  
 gPad->SetLogx();





 Int_t n3=6;//Swift/UVOT
 Int_t i;
 Float_t w3[n3]={7.0e14,8.0e14,8.5e14,1.1e15,1.8e15,2.3e15};
 Float_t v3[n3]={7.0e-11,6.0e-11, 5.0e-11, 4.1e-11, 4.5e-11, 4.3e-11};
 Float_t ewl3[n3]={0,0,0,0,0,0};
 Float_t evl3[n3]={0,0,0,0,0,0};
 Float_t ewh3[n3]={0,0,0,0,0,0};
 Float_t evh3[n3]={0,0,0,0,0,0};
 gr3=new TGraphAsymmErrors(n3,w3,v3,ewl3,ewh3,evl3,evh3);
 gr3->SetMarkerColor(kMagenta-4);
 gr3->SetMarkerStyle(4);
 gr3->SetMarkerSize(1.7);  
  gPad->SetLogy();  
 gPad->SetLogx();
 gr3->SetFillColor(2); 


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





 Int_t n4=6;//VERITAS-data-falling
 Int_t i;
 Float_t w4[n4]={320000,500000,800000,1300000,2000000,3200000};//x
 Float_t v4[n4]={0.0000000018,0.0000000025,0.0000000013,0.00000000064,0.00000000073,0.00000000063};//y
 Float_t ewl4[n4]={0,0,0,0,0,0};
 Float_t evl4[n4]={0,0,0,0,0,0};
 Float_t ewh4[n4]={0,0,0,0,0,0};
 Float_t evh4[n4]={0,0,0,0,0,0};
 gr4=new TGraphAsymmErrors(n4,w4,v4,ewl4,ewh4,evl4,evh4);
 gr4->SetMarkerColor(2);
 gr4->SetMarkerStyle(5);
 gr4->SetMarkerSize(0.7);
 gr4->SetLineColor(2);
 gPad->SetLogy();
 gPad->SetLogx();


 Int_t n9=14;//HST-optical-UV
 Int_t i;
 Float_t w9[n9]={6.2e-12,2.07e-11,6.21e-11,3.73e-10,8.28e-10,1.863e-8,5.382e-8,1.242e-7,2.484e-6,3.519e-6,4.968e-6,8.28e-6,8.28e-6,1.035e-5};//x
 Float_t v9[n9]={0.000000034,0.000000112,0.00000028,0.000001123,0.0000021916,0.00000714,0.000004056,0.000002995,0.000003868,0.000002371,0.000001248,0.000000911,0.000001123,0.000003496};//y
 Float_t ewl9[n9]={0,0,0,0,0,0,0,0,0,0,0,0,0,0};
 Float_t evl9[n9]={0,0,0,0,0,0,0,0,0,0,0,0,0,0};
 Float_t ewh9[n9]={0,0,0,0,0,0,0,0,0,0,0,0,0,0};
 Float_t evh9[n9]={0,0,0,0,0,0,0,0,0,0,0,0,0,0};
 gr9=new TGraphAsymmErrors(n9,w9,v9,ewl9,ewh9,evl9,evh9);
 gr9->SetMarkerColor();
 gr9->SetMarkerStyle(8);
 gr9->SetMarkerSize(0.75);
 gr9->SetLineColor(2);
 gPad->SetLogy();
 gPad->SetLogx();


 Int_t n10=4;//CHANDRA-core-X
 Int_t i;
 Float_t w10[n10]={5.55e-11,8.28e-4,1.242e-3,2.726e-3};
 Float_t v10[n10]={1.06e-7,3.74e-7,4.05e-7,4.36e-7};
 Float_t ewl10[n10]={0,0,0,0};
 Float_t evl10[n10]={0,0,0,0};
 Float_t ewh10[n10]={0,0,0,0};
 Float_t evh10[n10]={0,0,0,0};
 gr10=new TGraphAsymmErrors(n10,w10,v10,ewl10,ewh10,evl10,evh10);
 gr10->SetMarkerColor(kRed+0);
 gr10->SetMarkerStyle(8);
 gr10->SetMarkerSize(0.9);  
 gr10->SetLineColor(3);
 gPad->SetLogy();  
 gPad->SetLogx();
 gr10->SetFillColor(2); 


 Int_t n11=3;//SWIFT-BAT-X
 Int_t i;
 Float_t w11[n11]={3.484e-2,5.796e-2,1.449e-1};
 Float_t v11[n11]={1.435e-6,1.996e-6,1.123e-5};
 Float_t ewl11[n11]={0,0,0};
 Float_t evl11[n11]={0,0,0};
 Float_t ewh11[n11]={0,0,0};
 Float_t evh11[n11]={0,0,0};
 gr11=new TGraphAsymmErrors(n11,w11,v11,ewl11,ewh11,evl11,evh11);
 gr11->SetMarkerColor(kRed-8);
 gr11->SetMarkerStyle(23);
 gr11->SetMarkerSize(0.87);  
 gr11->SetLineColor(3);
 gPad->SetLogy();  
 gPad->SetLogx();
 gr11->SetFillColor(2); 

 Int_t n20=2;//end
 Int_t i;
 Float_t w20[n20]={9.484e27,1.796e28};
 Float_t v20[n20]={1.435e-14,1.996e-14};
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
 Float_t w21[n21]={2.484e7,5.796e7};
 Float_t v21[n21]={1.435e-14,1.996e-14};
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






 mg->Add(gr);
 mg->Add(gr1);
 mg->Add(gr6);
 mg->Add(gr7);
 //mg->Add(gr2);
 mg->Add(gr3);
 //mg->Add(gr4);
 //mg->Add(gr9);
 //mg->Add(gr10);
 //mg->Add(gr11);
 mg->Add(gr20);
 mg->Add(gr21);
 
 mg->Draw("apz");



 TLegend *legend = new TLegend(0.6,0.6,0.92,0.98);
 legend->SetFillColor(0);
 //legend->SetFillAttributes(14);
 legend->SetBorderSize(1.0);
 //legend->SetTextAlign(12);
 legend->AddEntry(gr,"Unkonwn","p");
 legend->AddEntry(gr1,"MOJAVE","p");
 legend->AddEntry(gr6,"RATAN-600","p");
 legend->AddEntry(gr7,"MITsuME","p");
 //legend->AddEntry(gr2,"VERITAS","p");
 legend->AddEntry(gr3,"Swift/UVOT ","p"); 
 //legend->AddEntry(gr4,"VERITAS-data-falling","p");
 //legend->AddEntry(gr9,"HST-optical-UV","p");
 //legend->AddEntry(gr10,"CHANDRA-core-X","p");
 //legend->AddEntry(gr11,"SWIFT-BAT-X-limit","p");
 legend->Draw();


 }


