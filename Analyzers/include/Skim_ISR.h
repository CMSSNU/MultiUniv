#ifndef Skim_ISR_h
#define Skim_ISR_h

#include "AnalyzerCore.h"
#include "RootHelper.h"

class Skim_ISR : public AnalyzerCore {

public:

    void initializeAnalyzer();
    void executeEventFromParameter(AnalyzerParameter param);
    void executeEvent();
    
    int findInitialMoterIndex(int mother_index, int current_index, bool same_flavor=true);
    void saveIndexToMap(int current_index, int mother_index, std::map<int,int> &partindex_map);

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

    bool save_detector_info;
    bool save_generator_info;

    std::vector<Gen>      gen_particles;
    std::vector<Gen>      gen_photons;
    std::vector<Muon>     muons;
    std::vector<Electron> electrons;
    std::vector<Photon>   photons;
    std::vector<Lepton*>  leps;

    Gen gen_particle_ME, gen_antiparticle_ME;
    Gen gen_particle_status1, gen_antiparticle_status1;
    int gen_particle_index_ME, gen_antiparticle_index_ME;
    int gen_particle_index_status1, gen_antiparticle_index_status1;

    double (MCCorrection::*PileUpWeight)(int,int);

    double Lep0PtCut;
    double Lep1PtCut;
    double LepEtaCut;

    int mother_id_of_prefsr_dilep;

    double dilep_pt_gen_prefsr   ;
    double dilep_mass_gen_prefsr ;
    double particle_pt_gen_prefsr ;
    double antiparticle_pt_gen_prefsr;
    double particle_eta_gen_prefsr   ;
    double antiparticle_eta_gen_prefsr;

    double dilep_pt_gen_postfsr   ;
    double dilep_mass_gen_postfsr ;
    double particle_pt_gen_postfsr  ;
    double antiparticle_pt_gen_postfsr ;
    double particle_eta_gen_postfsr   ;
    double antiparticle_eta_gen_postfsr;

    std::vector<Double_t> dilep_pt_gen_dressed_drX;
    std::vector<Double_t> dilep_mass_gen_dressed_drX;
    std::vector<Double_t> drX_gen_dressed;

    std::vector<Double_t> dilep_pt_gen_lepton_matched_dressed_drX;
    std::vector<Double_t> dilep_mass_gen_lepton_matched_dressed_drX;
    std::vector<Double_t> drX_gen_lepton_matched_dressed;

    std::vector<Double_t> photons_et_gen;
    std::vector<Int_t> photons_mother_id_gen;
    std::vector<Double_t> photons_closest_dr_to_leptons_gen;
    std::vector<Double_t> lepton_matched_photons_closest_dr_to_leptons_gen;

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

    double evt_weight_pureweight, evt_weight_pureweight_up, evt_weight_pureweight_down;
    double evt_weight_l1prefire, evt_weight_l1prefire_up, evt_weight_l1prefire_down;
    double evt_weight_bveto, evt_weight_bveto_up, evt_weight_bveto_down;

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

