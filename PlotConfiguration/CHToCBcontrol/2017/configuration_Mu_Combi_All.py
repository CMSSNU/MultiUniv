
Analyzer    = 'mkShape'
Outputdir   = 'Output'
Category    = 'SMP'
Year        = '2017'
lumi        = 41.527540
InSkim      = 'MetFt_L_TTSemiLep_v1_K2_v1'
#InSkim      = 'MetFt_L_v2_TTSemiLep_v1_K2_Mistag_v1'
##InSkim      = 'MetFt_L_v2_TTSemiLep_v1_K2_v1_ABCD_v1'
# Userflags: separate by ','
Userflags   = 'CHToCB_Mu_CombiAll' # flag appends to ouput directory name
#Userflags   = 'AlPhaS'
#Userflags   = 'DY'
treeName    = 'recoTree/SKFlat'


samplesFile   = 'samples_Mu_Combi_All.py'
# sample in plot check structure.py to be used in plotting
plotFile      = 'plot_Mu_Combi_All.py'
variablesFile = 'variables_Combi_All.py'
cutsFile      = 'cuts_Mu_Combi.py'
nuisancesFile = 'nuisances_Mu_Combi.py'
structureFile = 'structure.py'
