from CommonPyTools.python.CommonTools import *
SKFlat_WD = os.getenv('SKFlat_WD')
sys.path.insert(0,SKFlat_WD+'/CommonTools/include')
from Definitions import *

# supercut will be applied last in the cuts
supercut = 'is_dimuon_gen == 1'

# dressed level distribution
cuts['fiducial_phase_dRp1'] = 'pass_kinematic_cut_mu_FSRgammaDRp1_gen == 1 '

# matrix
cuts['full_phase_dRp1'] = 'is_dimuon_gen == 1 && pass_kinematic_cut_mu_FSRgammaDRp1_gen == 1 '

massCut_low  = ["40.", "60.", "80.", "100.", "200."]
massCut_high = ["60.", "80.", "100.", "200.", "350."]

# full phase distribution
for i in range(len(massCut_low)):
    cuts['full_phase_m' + massCut_low[i] + 'to' + massCut_high[i]] = 'is_dimuon_gen == 1 && dilep_mass_FSRgamma_gen_ispromptfinal > ' + massCut_low[i] + ' && dilep_mass_FSRgamma_gen_ispromptfinal < ' + massCut_high[i] + ' && dilep_pt_FSRgamma_gen_ispromptfinal < 100.'

