from CommonPyTools.python.CommonTools import *
SKFlat_WD = os.getenv('SKFlat_WD')
sys.path.insert(0,SKFlat_WD+'/CommonTools/include') 
from Definitions import *

supercut = 'passIso==1 && passTightID==1 && pfMET_Type1_pt>20 && selected_lepton_pt>0'

cuts['El2b'] = 'n_bjet_deepcsv_m_noSF==2 && IsEl==1'
cuts['El3b'] = 'n_bjet_deepcsv_m_noSF>=2 && IsEl==1'
cuts['El2b_KF'] = 'n_bjet_deepcsv_m_noSF==2 && IsEl==1 && fitter_status==0'
cuts['El3b_KF'] = 'n_bjet_deepcsv_m_noSF>=2 && IsEl==1 && fitter_status==0'
