from CommonPyTools.python.CommonTools import *
import os, sys

SKFlat_WD = os.getenv('SKFlat_WD')
sys.path.insert(0,SKFlat_WD+'/CommonTools/include')
from Definitions import * # to use enumerate for unfolding histogram type

#columns=['ALL'] # To read all
#columns=['diLep_Ch','diLep_m','diLep_pt','diLep_passSelectiveQ','IdSF_Q_Up','IdSF_Q_Do','IdSF_Q','baseW','PUweight','trgSF_Q','recoSF','IsoSF','ZPtCor','trgSF_Q_Up','trgSF_Q_Do','PDFWeights_AlphaS']

# xaxis, yaxis to set title

variables['mll'] = {
    'name': 'dilep_mass_rec',
    'range':(120,60,120),
    'xaxis': 'm_{ll} [GeV]',
    'fold' : 0
    }

variables['ptll'] = {
    'name': 'dilep_pt_rec',
    'range':(100,0,1000),
    'xaxis': 'm_{ll} [GeV]',
    'fold' : 0
    }
