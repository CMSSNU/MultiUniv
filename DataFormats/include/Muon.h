#ifndef Muon_h
#define Muon_h

#include "Lepton.h"
#include "TString.h"

class Muon: public Lepton{

public:

  Muon();
  ~Muon();

  void SetTypeBit(unsigned int typebit);
  void SetIDBit(unsigned int idbit);

  enum Selector {
    CutBasedIdLoose        = 1UL<< 0,  
    CutBasedIdMedium       = 1UL<< 1,  
    CutBasedIdMediumPrompt = 1UL<< 2,  // medium with IP cuts
    CutBasedIdTight        = 1UL<< 3,  
    CutBasedIdGlobalHighPt = 1UL<< 4,  // high pt muon for Z',W' (better momentum resolution)
    CutBasedIdTrkHighPt    = 1UL<< 5,  // high pt muon for boosted Z (better efficiency)
    PFIsoVeryLoose         = 1UL<< 6,  // reliso<0.40
    PFIsoLoose             = 1UL<< 7,  // reliso<0.25
    PFIsoMedium            = 1UL<< 8,  // reliso<0.20
    PFIsoTight             = 1UL<< 9,  // reliso<0.15
    PFIsoVeryTight         = 1UL<<10,  // reliso<0.10
    TkIsoLoose             = 1UL<<11,  // reliso<0.10
    TkIsoTight             = 1UL<<12,  // reliso<0.05
    SoftCutBasedId         = 1UL<<13,  
    SoftMvaId              = 1UL<<14,  
    MvaLoose               = 1UL<<15,  
    MvaMedium              = 1UL<<16,  
    MvaTight               = 1UL<<17,
    MiniIsoLoose           = 1UL<<18,  // reliso<0.40
    MiniIsoMedium          = 1UL<<19,  // reliso<0.20
    MiniIsoTight           = 1UL<<20,  // reliso<0.10
    MiniIsoVeryTight       = 1UL<<21,  // reliso<0.05
    TriggerIdLoose         = 1UL<<22,  // robust selector for HLT
    InTimeMuon             = 1UL<<23,   
    PFIsoVeryVeryTight     = 1UL<<24,  // reliso<0.05
    MultiIsoLoose          = 1UL<<25,  // miniIso with ptRatio and ptRel 
    MultiIsoMedium         = 1UL<<26   // miniIso with ptRatio and ptRel 
  };

  enum Type {
    GlobalMuon     =  1<<1,
    TrackerMuon    =  1<<2,
    StandAloneMuon =  1<<3,
    CaloMuon =  1<<4,
    PFMuon =  1<<5,
    RPCMuon =  1<<6,
    GEMMuon =  1<<7,
    ME0Muon = 1<<8
  };

  inline bool PassSelector( unsigned int s ) const { return (j_IDBit & s)==s; }
  inline bool IsType( unsigned int t ) const { return (j_TypeBit & t); }


  inline bool isPOGTight() const {return PassSelector(CutBasedIdTight);}
  inline bool isPOGHighPt() const {return PassSelector(CutBasedIdGlobalHighPt);}
  inline bool isPOGMedium() const {return PassSelector(CutBasedIdMedium);}
  inline bool isPOGLoose() const {return PassSelector(CutBasedIdLoose);}

  inline double getRelIsoNoPH() { return j_relIsoNoPH;}
  inline double getRelIsoNoPHCH() { return j_relIsoNoPHNoCH;}
  void SetRelIsoFSRStudy();

  bool isPOGTightIso(); // for ABCD method
  bool isAntiIso(int syst=0); // for ABCD method

  void SetIso(double ch04, double nh04, double ph04, double pu04, double trkiso);
  void CalcPFRelIso();
  inline double TrkIso() const {return j_trkiso;}
  double EA();

  void SetChi2(double chi2);
  inline double Chi2() const { return j_chi2; }

  void SetMiniAODPt(double d);
  void SetMiniAODTunePPt(double d);
  inline double MiniAODPt() const {return j_MiniAODPt;}
  inline double MiniAODTunePPt() const {return j_MiniAODTunePPt;}


  void SetTrackerLayersWithMeasurement(int trackerLayers);
  inline int GetTrackerLayersWithMeasurement(){ return j_trackerLayers; }
  void SetMomentumScaleAndError(double rc, double rc_err);
  inline double MomentumScale() const {return j_rc;}
  inline double MomentumScaleError() const {return j_rc_err;}
  inline double MomentumShift(int s) const {
    if(s==0) return 1.;
    else if(s>0) return Pt() * (j_rc + j_rc_err) / j_rc;
    else         return Pt() * (j_rc - j_rc_err) / j_rc;
  }

  void SetTuneP4(double pt, double pt_err, double eta, double phi, double q);
  inline Particle TuneP4() const {return j_TuneP4;}
  inline double TunePPtError() const {return j_TunePPtError;}

  //==== ID
  bool PassID(TString ID);
  bool Pass_POGTight();
  bool Pass_POGTightWithTightIso();
  bool Pass_POGLooseWithLooseIso();
  bool Pass_POGTightWithLooseIso();
  bool Pass_isPOGTightWithRelIsoNoPH();
  bool Pass_isPOGTightWithRelIsoNoPHCH();
  bool Pass_POGHighPtWithLooseTrkIso();
  bool Pass_POGMediumWithLooseTrkIso();
  bool Pass_TESTID();

  bool Pass_HNLoose() const;
  bool Pass_HNTight() const;

private:

  int j_trackerLayers;
  unsigned int j_TypeBit, j_IDBit;
  double j_chi2;
  double j_PFCH04, j_PFNH04, j_PFPH04, j_PU04, j_trkiso;
  double j_MiniAODPt, j_MiniAODTunePPt, j_rc, j_rc_err, j_MomentumUp, j_MomentumDown;
  Particle j_TuneP4;
  double j_TunePPtError;
    
  double j_relIsoNoPH, j_relIsoNoPHNoCH;

  ClassDef(Muon,1);
};

#endif
