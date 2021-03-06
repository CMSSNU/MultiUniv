from CommonPyTools.python.CommonTools import *

###########################
# Number of Leptons and WP
###########################

FakeRate = 'evt_weight_TL_rec_Fake' 
McWeight = 'evt_weight_total_gen * evt_weight_total_rec * evt_weight_TL_rec_Fake' 
McWeightZptReweight = 'evt_weight_total_gen * evt_weight_total_rec * evt_weight_TL_rec_Fake * evt_weight_zptcorr' 

#--------------------    
# MC
#--------------------    

samples['DYJets@DYJetsToMuMu'] = {
    'skim'   :'ISR_v1', # use default skim defined in configuration.py
    'combine_cuts' : True,
    'cut'    :'evt_tag_dimuon_hardprocess == 1',
    'weight' :McWeightZptReweight,
    }

samples['DYJets10to50_MG@DYJets10to50ToMuMu'] = {
    'skim'   :'ISR_v1', # use default skim defined in configuration.py
    'combine_cuts' : True,
    'cut'    :'evt_tag_dimuon_hardprocess == 1',
    'weight' :McWeightZptReweight,
    }

samples['DYJets@DYJetsToTauTau'] = {
    'skim'   :'ISR_v1', # use default skim defined in configuration.py
    'combine_cuts' : True,
    'cut'    :'evt_tag_ditau_hardprocess == 1',
    'weight' :McWeight,
    }

samples['DYJets10to50_MG@DYJets10to50ToTauTau'] = {
    'skim'   :'ISR_v1', # use default skim defined in configuration.py
    'combine_cuts' : True,
    'cut'    :'evt_tag_ditau_hardprocess == 1',
    'weight' :McWeight,
    }

samples['TTLL_powheg'] = {
    'skim'   :'', # use default skim defined in configuration.py
    'combine_cuts' : True,
    'cut'    :'',
    'weight' :McWeight,
    }

samples['WJets_MG'] = {
    'skim'   :'',
    'combine_cuts' : True,
    'cut'    :'',
    'weight' :McWeight,
    }

samples['WW_pythia'] = {
    'skim'   :'',
    'combine_cuts' : True,
    'cut'    :'',
    'weight' :McWeight,
    }

samples['WZ_pythia'] = {
    'skim'   :'',
    'combine_cuts' : True,
    'cut'    :'',
    'weight' :McWeight,
    }

samples['ZZ_pythia'] = {
    'skim'   :'',
    'combine_cuts' : True,
    'cut'    :'',
    'weight' :McWeight,
    }

samples['DoubleMuon'] = {
    'skim'   :'',
    'combine_cuts' : True,
    'cut'    :'',
    'weight' :FakeRate,
    }

