from CommonPyTools.python.CommonTools import *

###########################
# Number of Leptons and WP
###########################

#Nlep='2'
#eleWP='mediumSelectiveQ'

McWeight = 'evt_weight_total_gen * evt_weight_total_rec * evt_weight_isoSF_rec * evt_weight_idSF_rec * evt_weight_trigSF_rec'
McWeight_forDY10to50 = 'evt_weight_total_gen * evt_weight_total_rec * evt_weight_isoSF_rec * evt_weight_idSF_rec * evt_weight_trigSF_rec * 1.0687524'

#--------------------    
# MC
#--------------------    

samples['DYJets@DYJetsToMuMu'] = {
    'skim'   :'ISR_v1', # use default skim defined in configuration.py
    'cut'    :'evt_tag_dimuon_gen == 1',
    'weight' :McWeight,
    }

samples['DYJets10to50@DYJets10to50ToMuMu'] = {
    'skim'   :'ISR_v1', # use default skim defined in configuration.py
    'cut'    :'evt_tag_dimuon_gen == 1',
    'weight' :McWeight_forDY10to50,
    }

samples['DYJets@DYJetsToTauTau'] = {
    'skim'   :'ISR_v1', # use default skim defined in configuration.py
    'cut'    :'evt_tag_ditau_gen == 1',
    'weight' :McWeight,
    }

samples['DYJets10to50@DYJets10to50ToTauTau'] = {
    'skim'   :'ISR_v1', # use default skim defined in configuration.py
    'cut'    :'evt_tag_ditau_gen == 1',
    'weight' :McWeight_forDY10to50,
    }

samples['TTLL_powheg'] = {
    'skim'   :'', # use default skim defined in configuration.py
    'cut'    :'',
    'weight' :McWeight,
    }

samples['WJets_MG'] = {
    'skim'   :'',
    'cut'    :'',
    'weight' :McWeight,
    }

samples['WW_pythia'] = {
    'skim'   :'',
    'cut'    :'',
    'weight' :McWeight,
    }

samples['WZ_pythia'] = {
    'skim'   :'',
    'cut'    :'',
    'weight' :McWeight,
    }

samples['ZZ_pythia'] = {
    'skim'   :'',
    'cut'    :'',
    'weight' :McWeight,
    }

samples['DoubleMuon'] = {
    'skim'   :'',
    'cut'    :'',
    'weight' :'1',
    }
#--------------------    
# DATA driven QCD
#--------------------
'''
samples['DoubleEG_FakeElEl'] = {
    'skim'   :'MetFt_L_v0_LL_v0_EEOrElElFake_v1', #TODO: this skim is not exist currently
    'weight' :'1',
    }

samples['DobuleMuon_FakeEE'] = {
    'skim'   :'MetFt_L_v0_LL_v0_EEOrElElFake_v1', #TODO: this skim is not exist currently
    'weight' :'1',
    }
'''
