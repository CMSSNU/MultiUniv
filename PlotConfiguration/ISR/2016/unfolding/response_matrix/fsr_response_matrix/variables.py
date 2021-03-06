from CommonPyTools.python.CommonTools import *
import os, sys

SKFlat_WD = os.getenv('SKFlat_WD')
sys.path.insert(0,SKFlat_WD+'/CommonTools/include')
from Definitions import * # to use enumerate for unfolding histogram type

#columns=['ALL'] # To read all
#columns=['diLep_Ch','diLep_m','diLep_pt','diLep_passSelectiveQ','IdSF_Q_Up','IdSF_Q_Do','IdSF_Q','baseW','PUweight','trgSF_Q','recoSF','IsoSF','ZPtCor','trgSF_Q_Up','trgSF_Q_Do','PDFWeights_AlphaS']

# xaxis, yaxis to set title

# for FSR unfold closure test input 
variables['hist_ptll'] = {

    'unfoldBinType': ISRUnfold.PtGen2DHist,
    'linesToAdd': (".L " + SKFlat_WD + "/ShapeAnalysis/scripts/userfunc/TUnfold_Bin_Definition.C",),
    'fold':   0,
    'range':  None,
    'name':  'Get2DPtGenBinIndex(dilep_pt_FSRgammaDRp1_gen_ispromptfinal, dilep_mass_FSRgammaDRp1_gen_ispromptfinal)',
    'xaxis': 'Mass p_{T} [GeV]',
    'yaxis': 'Events',
    'useTUnfoldBin': True,
    'unfoldBinDefinition': "electron",
    'go1D': True
}

variables['hist_mll'] = {

    'unfoldBinType': ISRUnfold.MassGen2DHist,
    'fold':   0,
    'range':  None,
    'name':  'Get2DMassGenBinIndex(dilep_mass_FSRgammaDRp1_gen_ispromptfinal, dilep_pt_FSRgammaDRp1_gen_ispromptfinal)',
    'xaxis': 'Mass [GeV]',
    'yaxis': 'Events',
    'useTUnfoldBin': True,
    'unfoldBinDefinition': "electron",
    'go1D': False
}

variables['ptll_gen_post_fsr_dRp1_pre_fsr_response_matrix'] = {

    'unfoldBinType': ISRUnfold.PtFSRMigrationM,
    'linesToAdd': (".L " + SKFlat_WD + "/ShapeAnalysis/scripts/userfunc/TUnfold_Bin_Definition.C",),
    'fold': 0,
    'range': None,
    'name': 'Get2DPtGenBinIndex(dilep_pt_FSRgammaDRp1_gen_ispromptfinal, dilep_mass_FSRgammaDRp1_gen_ispromptfinal):Get2DPtGenBinIndex(dilep_pt_FSRgamma_gen_ispromptfinal, dilep_mass_FSRgamma_gen_ispromptfinal)',
    'xaxis': 'Post FSR',
    'useTUnfoldBin': True,
    'unfoldBinDefinition': "electron",
    'go1D': False,
    'isResMatrix':True
}

variables['mll_gen_post_fsr_dRp1_pre_fsr_response_matrix'] = {

    'unfoldBinType': ISRUnfold.MassFSRMigrationM,
    'fold': 0,
    'range': None,
    'name': 'Get2DMassGenBinIndex(dilep_mass_FSRgammaDRp1_gen_ispromptfinal, dilep_pt_FSRgammaDRp1_gen_ispromptfinal):Get2DMassGenBinIndex(dilep_mass_FSRgamma_gen_ispromptfinal, dilep_pt_FSRgamma_gen_ispromptfinal)',
    'xaxis': 'Post FSR',
    'useTUnfoldBin': True,
    'unfoldBinDefinition': "electron",
    'go1D': False,
    'isResMatrix':True
}

variables['ptll'] = {
    'name': 'dilep_pt_FSRgamma_gen_ispromptfinal',
    'range':([0., 4., 8., 12., 18., 28., 40., 55., 75., 100.],),
    'xaxis': ' p_{T}^{ee} [GeV]',
    'yaxis': 'Events/ bin',
    'go1D': False,
    'fold' : 0
    }

variables['mll'] = {
    'name': 'dilep_mass_FSRgamma_gen_ispromptfinal',
    'range':([50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,126,133,141,150,160,171,185,200,218,240,268,300,350],),
    'xaxis': ' m^{ee} [GeV]',
    'yaxis': 'Events/ bin',
    'go1D': False,
    'fold' : 0
    }
