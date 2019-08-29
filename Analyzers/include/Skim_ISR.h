#ifndef Skim_ISR_h
#define Skim_ISR_h

#include "AnalyzerCore.h"
#include "RootHelper.h"

class Skim_ISR : public AnalyzerCore {

public:

    void initializeAnalyzer();
    void executeEventFromParameter(AnalyzerParameter param);
    void executeEvent();

    Skim_ISR();
    ~Skim_ISR();

    TTree *newtree;

    void WriteHist();

private:

    bool debug_;

    int IsMuMu;
    int IsElEl;

    vector<TString> DiMuTrgs;
    vector<TString> DiElTrgs;

    Event* evt;

    std::vector<Muon> muons;
    std::vector<Electron> electrons;
    std::vector<Photon> photons;
    std::vector<Lepton*> leps;

    double (MCCorrection::*PileUpWeight)(int,int);
    double PUweight, PUweight_Up, PUweight_Dn;
    double L1Prefire, L1Prefire_Up, L1Prefire_Dn;

    double Lep0PtCut;
    double Lep1PtCut;
    double LepEtaCut;

    double dilep_pt_rec;
    double dilep_mass_rec;
    double dilep_photon_mass_rec;
    double leadinglep_pt_rec;
    double subleadinglep_pt_rec;
    double leadinglep_eta_rec;
    double subleadinglep_eta_rec;
    double leadingphoton_pt_rec;
    double leadingphoton_eta_rec;
    double leadingphoton_lepton_dr_rec;
    int photon_n_rec;

    double evt_weight_total_gen;
    double evt_weight_total_rec;
    double evt_weight_btag_rec;

    bool evt_tag_leptonpt_sel_rec;
    bool evt_tag_leptoneta_sel_rec;
    bool evt_tag_oppositecharge_sel_rec;
    bool evt_tag_analysisevnt_sel_rec;

    bool evt_tag_ditau_gen;
    bool evt_tag_dielectron_gen;
    bool evt_tag_dimuon_gen;
    bool evt_tag_dielectron_rec;
    bool evt_tag_dimuon_rec;
    bool evt_tag_bvetoed_rec;

};



#endif

