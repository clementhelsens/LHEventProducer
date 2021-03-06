#eos tests
eostest='/eos/experiment/fcc/hh/tests/testfile.lhe.gz'
eostest_size=1312594

#stat
lhe_stat="/afs/cern.ch/user/h/helsens/www/data/statlhe_FCC.html"
delphes_stat="/afs/cern.ch/user/h/helsens/www/data/statdelphesVERSION_FCC.html"

#web
lhe_web="/afs/cern.ch/user/h/helsens/www/data/LHEevents.txt"
delphes_web="/afs/cern.ch/user/h/helsens/www/data/Delphesevents_VERSION.txt"

#yaml directory
yamldir='/afs/cern.ch/work/h/helsens/public/FCCDicts/yaml/FCC/'
yamlcheck_lhe='/afs/cern.ch/work/h/helsens/public/FCCDicts/yaml/FCC/lhe/check.yaml'
yamlcheck_reco='/afs/cern.ch/work/h/helsens/public/FCCDicts/yaml/FCC/VERSION/check.yaml'

##eos directory for MG5@MCatNLO gridpacks
gp_dir      = '/eos/experiment/fcc/hh/generation/gridpacks/'
##eos directory for lhe files
lhe_dir     = '/eos/experiment/fcc/hh/generation/lhe/'
##extension
lhe_ext     ='.lhe.gz'

##FCC versions
fcc_versions=['fcc_v01', 'fcc_v02', 'cms']

##eos directory for FCCSW pythia delphes files
delphes_dir = '/eos/experiment/fcc/hh/generation/DelphesEvents/'
##extension
delphes_ext='.root'
##name of the ttree
treename='events'

##where the delphes cards are stored
delphescards_dir = '/eos/experiment/fcc/hh/utils/delphescards/'
##where the pythia cards are stored
pythiacards_dir  = '/eos/experiment/fcc/hh/utils/pythiacards/'
##where the FCC config script is stored
fccconfig_dir    = '/eos/experiment/fcc/hh/utils/config/'

##muom momentum delphes resolution card
delphescard_mmr='muonMomentumResolutionVsP.tcl'
##momentum resolution delphes card
delphescard_mr='momentumResolutionVsP.tcl'
##delphes base card
delphescard_base='card.tcl'
##FCC config script name
fccconfig='PythiaDelphes_config_v02.py'

##base dir of FCCSW
fccsw_dir='/cvmfs/fcc.cern.ch/sw/0.8.2/'
##init script for FCCSW
stack=fccsw_dir+'init_fcc_stack.sh'
##FCCSW dir
fccsw=fccsw_dir+'fccsw/0.8.2/x86_64-slc6-gcc62-opt/'

#list of processes only with Pythia, meaning no LHE
pythialist={
'p8_pp_Zprime_5TeV_ll':['5TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','1.043e-1','1.0','1.0'],
'p8_pp_Zprime_10TeV_ll':['10TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','5.914e-3','1.0','1.0'],
'p8_pp_Zprime_15TeV_ll':['15TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','7.989e-4','1.0','1.0'],
'p8_pp_Zprime_20TeV_ll':['20TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','1.639e-4','1.0','1.0'],
'p8_pp_Zprime_25TeV_ll':['25TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','4.437e-5','1.0','1.0'],
'p8_pp_Zprime_30TeV_ll':['30TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','1.375e-5','1.0','1.0'],
'p8_pp_Zprime_35TeV_ll':['35TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','4.821e-6','1.0','1.0'],
'p8_pp_Zprime_40TeV_ll':['40TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','2.171e-6','1.0','1.0'],
'p8_pp_Zprime_45TeV_ll':['45TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','1.165e-6','1.0','1.0'],
'p8_pp_Zprime_50TeV_ll':['50TeV Z\'(SSM) -> ll (l=e,mu,tau)','','','6.863e-7','1.0','1.0'],
'p8_pp_Zprime_2TeV_ttbar':['2TeV Z\' -> ttbar','','','7.6378','1.0','1.0'],
'p8_pp_Zprime_5TeV_ttbar':['5TeV Z\' -> ttbar','','','0.305493','1.0','1.0'],
'p8_pp_Zprime_10TeV_ttbar':['10TeV Z\' -> ttbar','','','0.0175724','1.0','1.0'],
'p8_pp_Zprime_15TeV_ttbar':['15TeV Z\' -> ttbar','','','0.002439429','1.0','1.0'],
'p8_pp_Zprime_20TeV_ttbar':['20TeV Z\' -> ttbar','','','0.0004845249','1.0','1.0'],
'p8_pp_Zprime_20TeV_ttbar_qcdBDTtrain':['20TeV Z\' -> ttbar','','','0.0004845249','1.0','1.0'],
'p8_pp_Zprime_25TeV_ttbar':['25TeV Z\' -> ttbar','','','0.0001164359','1.0','1.0'],
'p8_pp_Zprime_30TeV_ttbar':['30TeV Z\' -> ttbar','','','3.16759213029e-05','1.0','1.0'],
'p8_pp_Zprime_35TeV_ttbar':['35TeV Z\' -> ttbar','','','9.65649631373e-06','1.0','1.0'],
'p8_pp_Zprime_40TeV_ttbar':['40TeV Z\' -> ttbar','','','3.4131033281e-06','1.0','1.0'],
'p8_pp_RSGraviton_2TeV_ww':['2TeV Z\' -> WW','','','1.811e1','1.0','1.0'],
'p8_pp_RSGraviton_5TeV_ww':['5TeV Z\' -> WW','','','2.892e-1','1.0','1.0'],
'p8_pp_RSGraviton_10TeV_ww':['10TeV Z\' -> WW','','','7.686e-3','1.0','1.0'],
'p8_pp_RSGraviton_15TeV_ww':['15TeV Z\' -> WW','','','7.386e-4','1.0','1.0'],
'p8_pp_RSGraviton_20TeV_ww':['20TeV Z\' -> WW','','','1.182e-4','1.0','1.0'],
'p8_pp_RSGraviton_20TeV_ww_qcdBDTtrain':['20TeV Z\' -> WW','','','1.182e-4','1.0','1.0'],

'p8_pp_RSGraviton_25TeV_ww':['25TeV Z\' -> WW','','','2.284e-5','1.0','1.0'],
'p8_pp_RSGraviton_30TeV_ww':['30TeV Z\' -> WW','','','5.253e-6','1.0','1.0'],
'p8_pp_RSGraviton_35TeV_ww':['35TeV Z\' -> WW','','','1.215e-6','1.0','1.0'],
'p8_pp_RSGraviton_40TeV_ww':['40TeV Z\' -> WW','','','2.984e-7','1.0','1.0'],
'p8_pp_jj_PT_500_1000':['di-jet','500 < PT < 1000','','7.166e+04','1.0','1.0'],
'p8_pp_jj_PT_1000_2000':['di-jet','1000 < PT < 2000','','3.472e+03','1.0','1.0'],
'p8_pp_jj_PT_2000_4000':['di-jet','2000 < PT < 4000','','1.475e+02','1.0','1.0'],
'p8_pp_jj_PT_4000_6000':['di-jet','4000 < PT < 6000','','3.891e+00','1.0','1.0'],
'p8_pp_jj_PT_6000_8000':['di-jet','6000 < PT < 8000','','3.252e-01','1.0','1.0'],
'p8_pp_jj_PT_8000_10000':['di-jet','8000 < PT < 10000','','5.247e-02','1.0','1.0'],
'p8_pp_jj_PT_10000_12000':['di-jet','10000 < PT < 12000','','9.919e-03','1.0','1.0'],
'p8_pp_jj_PT_12000_14000':['di-jet','12000 < PT < 14000','','2.348e-03','1.0','1.0'],
'p8_pp_jj_PT_14000_16000':['di-jet','14000 < PT < 16000','','6.380e-04','1.0','1.0'],
'p8_pp_jj_PT_16000_20000':['di-jet','16000 < PT < 20000','','2.268e-04','1.0','1.0'],
'p8_pp_jj_PT_20000_100000':['di-jet','20000 < PT < 100000','','2.541e-05','1.0','1.0'],
'p8_pp_tt_PT_0_1000':['ttbar','0 < PT < 1000','','2.592e+04','3.0','1.0'],
'p8_pp_tt_PT_1000_2000':['ttbar','1000 < PT < 2000','','1.258e+01','3.0','1.0'],
'p8_pp_tt_PT_2000_4000':['ttbar','2000 < PT < 4000','','4.762e-01','3.0','1.0'],
'p8_pp_tt_PT_4000_6000':['ttbar','4000 < PT < 6000','','1.066e-02','3.0','1.0'],
'p8_pp_tt_PT_6000_8000':['ttbar','6000 < PT < 8000','','8.795e-04','3.0','1.0'],
'p8_pp_tt_PT_8000_10000':['ttbar','8000 < PT < 10000','','1.199e-04','3.0','1.0'],
'p8_pp_tt_PT_10000_12000':['ttbar','10000 < PT < 12000','','2.210e-05','3.0','1.0'],
'p8_pp_tt_PT_12000_14000':['ttbar','12000 < PT < 14000','','4.833e-06','3.0','1.0'],
'p8_pp_tt_PT_14000_16000':['ttbar','14000 < PT < 16000','','1.165e-06','3.0','1.0'],
'p8_pp_tt_PT_16000_20000':['ttbar','16000 < PT < 20000','','4.046e-07','3.0','1.0'],
'p8_pp_tt_PT_20000_100000':['ttbar','20000 < PT < 100000','','3.364e-08','3.0','1.0'],
'p8_pp_vv_PT_0_1000':['di-boson (gamma/W/Z)','0 < PT < 1000','','9.750e+02','1.7','1.0'],
'p8_pp_vv_PT_1000_2000':['di-boson (gamma/W/Z)','1000 < PT < 2000','','1.579e-01','1.7','1.0'],
'p8_pp_vv_PT_2000_4000':['di-boson (gamma/W/Z)','2000 < PT < 4000','','2.174e-02','1.7','1.0'],
'p8_pp_vv_PT_4000_6000':['di-boson (gamma/W/Z)','4000 < PT < 6000','','2.556e-03','1.7','1.0'],
'p8_pp_vv_PT_6000_8000':['di-boson (gamma/W/Z)','6000 < PT < 8000','','7.138e-04','1.7','1.0'],
'p8_pp_vv_PT_8000_10000':['di-boson (gamma/W/Z)','8000 < PT < 10000','','2.673e-04','1.7','1.0'],
'p8_pp_vv_PT_10000_12000':['di-boson (gamma/W/Z)','10000 < PT < 12000','','1.140e-04','1.7','1.0'],
'p8_pp_vv_PT_12000_14000':['di-boson (gamma/W/Z)','12000 < PT < 14000','','5.252e-05','1.7','1.0'],
'p8_pp_vv_PT_14000_16000':['di-boson (gamma/W/Z)','14000 < PT < 16000','','2.471e-05','1.7','1.0'],
'p8_pp_vv_PT_16000_20000':['di-boson (gamma/W/Z)','16000 < PT < 20000','','1.717e-05','1.7','1.0'],
'p8_pp_vv_PT_20000_100000':['di-boson (gamma/W/Z)','20000 < PT < 100000','','4.080e-06','1.7','1.0'],

'p8_pp_tt_M_5000_10000':['ttbar','5000 < M < 10000 and pT > 2500.','','1.425e-01','3.0','1.0'],
'p8_pp_tt_M_10000_15000':['ttbar','10000 < M < 15000 and pT > 2500.','','1.170e-02','3.0','1.0'],
'p8_pp_tt_M_15000_100000':['ttbar','15000 < M < 100000 and pT > 2500.','','1.392e-03','3.0','1.0'],

'p8_pp_jj_M_5000_10000':['dijet','5000 < M < 10000 and pT > 2500.','','39.84','3.0','1.0'],
'p8_pp_jj_M_10000_15000':['dijet','10000 < M < 15000 and pT > 2500.','','7.818','3.0','1.0'],
'p8_pp_jj_M_15000_100000':['dijet','15000 < M < 100000 and pT > 2500.','','2.570','3.0','1.0'],

'p8_pp_jj_ws_M_5000_10000':['dijet weak shower','5000 < M < 10000 and pT > 2500.','','39.84','3.0','1.0'],
'p8_pp_jj_ws_M_10000_15000':['dijet weak shower','10000 < M < 15000 and pT > 2500.','','7.818','3.0','1.0'],
'p8_pp_jj_ws_M_15000_100000':['dijet weak shower','15000 < M < 100000 and pT > 2500.','','2.570','3.0','1.0'],

'p8_pp_vv_M_5000_10000':['di-boson','5000 < M < 10000 and pT > 2500.','','8.453e-03','3.0','1.0'],
'p8_pp_vv_M_10000_15000':['di-boson','10000 < M < 15000 and pT > 2500.','','3.647e-03','3.0','1.0'],
'p8_pp_vv_M_15000_100000':['di-boson','15000 < M < 100000 and pT > 2500.','','1.841e-03','3.0','1.0'],

'p8_pp_tt_Pt2500toInf':['ttbar','pT > 2500.','','1.531e-1','3.0','1.0'],
'p8_pp_jj_Pt2500toInf':['dijet','pT > 2500.','','49.99','3.0','1.0'],
'p8_pp_vv_Pt2500toInf':['di-boson','pT > 2500.','','1.377e-2','3.0','1.0'],
'p8_pp_ll_Pt5000toInf':['di-lepton','pT > 5000.','','2.775e-5','3.0','1.0'],

}


##list of possible decays of LHE files

decaylist = {
'mg_pp_h012j_5f':['hmumu', 'haa', 'hlla', 'hllll', 'hlvlv', 'hbb', 'htautau'],
'mg_pp_hh01j_5f':['hhaabb'],
'mg_pp_vbf_h01j_5f':['hmumu', 'haa', 'hlla', 'hllll', 'hlvlv', 'hbb', 'htautau', 'hnunununu'],
'mg_pp_tth01j_5f':['hmumu', 'haa', 'hlla', 'hllll', 'hlvlv', 'hbb', 'htautau'],
'mg_pp_vh012j_5f':['hmumu', 'haa', 'hlla', 'hllll', 'hlvlv', 'hbb', 'htautau'],
'mg_pp_v0123j_5f':['znunu'],
'mg_pp_z0123j_4f':['zll'],
'mg_pp_w0123j_4f':['wlv'],
'mg_pp_ttz_5f':['znunu'],
'mg_pp_hh_lambda050_5f':['haa'],
'mg_pp_hh_lambda090_5f':['haa'],
'mg_pp_hh_lambda095_5f':['haa'],
'mg_pp_hh_lambda100_5f':['haa'],
'mg_pp_hh_lambda105_5f':['haa'],
'mg_pp_hh_lambda110_5f':['haa'],
'mg_pp_hh_lambda150_5f':['haa'],
'mg_pp_hhj_lambda090_5f':['hhbbbb'],
'mg_pp_hhj_lambda095_5f':['hhbbbb'],
'mg_pp_hhj_lambda100_5f':['hhbbbb'],
'mg_pp_hhj_lambda105_5f':['hhbbbb'],
'mg_pp_hhj_lambda110_5f':['hhbbbb'],
'mg_pp_hhj_lambda150_5f':['hhbbbb'],
'mg_pp_hhj_lambda050_5f':['hhbbbb'],

}



##list of decays branching ratios 
# from https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBR 
# and Particle data Group

branching_ratios = {
'hmumu':2.176E-04,
'haa':2.270E-03,
'hlla':1.533E-03*(3.363E-02 + 3.366E-02),
'hllll':1.240E-04,
'hlvlv':1.055E-02,
'hbb':5.824E-01,
'htautau':6.272E-02,
'zll':0.307,
'wlv':3*0.108,
'hhaabb':2*2.270E-03*5.824E-01,
'hhbbbb':5.824E-01*5.824E-01,
'znunu':0.205,
}


##Gridpack list
##     0          1            2                 3           4           5
## description/comment/matching parameters/cross section/kfactor/matching efficiency

gridpacklist = {
'mg_pp_w012j_5f':['w + 0,1,2 jets 5 flavor scheme','inclusive','xqcut = 30, qCut = 45','1.4995e06','1.0','0.724'],
'mg_pp_z012j_5f':['z + 0,1,2 jets 5 flavor scheme','inclusive','xqcut = 30, qCut = 45','5.1839e05','1.0','0.691'],
'mg_pp_jjaa01j_5f':['dijet diphoton + 0,1 jets 5 flavor scheme','','xqcut = 20, qCut = 30','55.72','1.0','0.236'],
'mg_pp_jjaa_5f':['dijet diphoton','','','17.97','1.0','1.0'],
'mg_pp_jjja01j_5f':['photon +jets + 0,1 jets 5 flavor scheme','','xqcut = 20, qCut = 25','4.133e+05','1.0','0.143'],
'mg_pp_jjja_5f':['photon +jets','','','1.023e05','1.0','1.0'],
'mg_pp_jjaa_4f':['dijet diphoton 4 flavor scheme','','','431.2','1.0','1.0'],
'mg_pp_bbja_4f':['bbja 4 flavor scheme','','','4679','1.0','1.0'],
'mg_pp_bbaa01j_4f':['bbaa + 0,1 jets 4 flavor scheme','','xqcut = 25, qCut = 35','5.899','1.0','0.312'],
'mg_pp_bjaa01j_4f':['bjaa + 0,1 jets 4 flavor scheme','','xqcut = 25, qCut = 35','16.9','1.0','0.335'],
'mg_pp_bbj_4f_PT_0_500':['bbbar + jet','0 < PT < 500','','201.4','2.0','1.0'],
'mg_pp_bbj_4f_PT_500_1000':['bbbar + jet','500 < PT < 1000','','0.5511','2.0','1.0'],
'mg_pp_bbj_4f_PT_1000_2000':['bbbar + jet','1000 < PT < 2000','','0.004057','2.0','1.0'],
'mg_pp_bbj_4f_PT_2000_4000':['bbbar + jet','2000 < PT < 4000','','6.688e-06','2.0','1.0'],
'mg_pp_bbbbj_4f_PT_0_250':['4b + jet','0 < PT < 250','','2516','2.0','1.0'],
'mg_pp_bbbbj_4f_PT_250_500':['4b + jet','250 < PT < 500','','224.3','2.0','1.0'],
'mg_pp_bbbbj_4f_PT_500_1000':['4b + jet','500 < PT < 1000','','20.99','2.0','1.0'],
'mg_pp_bbbbj_4f_PT_500_inf':['4b + jet','500 < PT','','57.71','2.0','1.0'],
'mg_pp_bbbbj_4f_PT_200_500':['4b + jet','200 < PT < 500','','756.4','2.0','1.0'],
'mg_pp_bbbbj_4f_PT_1000_100000':['4b + jet','1000 < PT < 100000','','0.2959','2.0','1.0'],
'mg_pp_bbbbj_QCD':['4b + jet (QCD only)','250 < PT ','','443.1','1.0','1.0'],
'mg_pp_bbbbj_QCDQED':['4b + jet (QCD+QED)','250 < PT ','','6.204','1.0','1.0'],
'mg_pp_bbbbj_QED':['4b + jet (QED)','250 < PT ','','0.07206','1.0','1.0'],
'mg_pp_z012j_5f':['z + 0,1,2 jets 5 flavor scheme','inclusive','xqcut = 30, qCut = 45','5.1839e05','1.0','0.691'],
'mg_pp_tth':['ttbar plus higgs','inclusive','','23.37','1.0','1.0'],
'mg_pp_bbh':['bbar plus higgs','50 < mbb < 300','','0.916','1.0','1.0'],
'mg_pp_zh':['z plus higgs production','inclusive','','7.42','1.0','1.0'],
'mg_pp_hh':['gluon gluon fusion di-higgs','inclusive','','0.65','1.0','1.0'],
'mg_pp_vbf_hh':['vector boson fusion di-higgs','inclusive','','0.06612','1.0','1.0'],
'mg_pp_llll_5f':['Z/gamma* Z/gamma* to 4l','inclusive','xqcut = 40, qCut = 60','0.6045','1.0'],
'mg_pp_llll01j_5f_HT_0_800':['Z/gamma* Z/gamma* to 4l + 0/1 jets','0 < HT < 800','xqcut = 40, qCut = 60','0.8786','1.60','0.684'],
'mg_pp_llll01j_5f_HT_800_2000':['Z/gamma* Z/gamma* to 4l + 0/1 jets','800 < HT < 2000','xqcut = 40, qCut = 60','0.01657','1.60','0.766'],
'mg_pp_llll01j_5f_HT_2000_4000':['Z/gamma* Z/gamma* to 4l + 0/1 jets','2000 < HT < 4000','xqcut = 40, qCut = 60','0.001004','1.60','0.785'],
'mg_pp_llll01j_5f_HT_4000_100000':['Z/gamma* Z/gamma* to 4l + 0/1 jets','4000 < HT < 100000','xqcut = 40, qCut = 60','9.656e-05','1.60','0.781'],
'mg_pp_llll01j_5f':['Z/gamma* Z/gamma* to 4l + 0/1 jets','inclusive','xqcut = 40, qCut = 60','0.899','1.60','0.685'],
'mg_pp_vbf_v01j_5f_HT_0_2000':['vbf vector boson + 0/1 jets','0 < HT < 2000','xqcut = 40, qCut = 60','1.151e+07','1.20','1.0'],
'mg_pp_vbf_v01j_5f_HT_2000_4000':['vbf vector boson + 0/1 jets','2000 < HT < 4000','xqcut = 40, qCut = 60','1.912e+04','1.20','1.0'],
'mg_pp_vbf_v01j_5f_HT_4000_7200':['vbf vector boson + 0/1 jets','4000 < HT < 7200','xqcut = 40, qCut = 60','400.9','1.20','1.0'],
'mg_pp_vbf_v01j_5f_HT_7200_100000':['vbf vector boson + 0/1 jets','7200 < HT < 100000','xqcut = 40, qCut = 60','72.31','1.20','1.0'],
'mg_pp_vbf_v01j_5f':['vbf vector boson + 0/1 jets','inclusive','xqcut = 40, qCut = 60','7.081e+06','1.20','1.0'],
'mg_pp_t123j_5f_HT_0_1900':['single top (s,t channels)+ 1/2/3 jets','0 < HT < 1900','xqcut = 40, qCut = 60','7490','2.16','0.287'],
'mg_pp_t123j_5f_HT_1900_3500':['single top (s,t channels)+ 1/2/3 jets','1900 < HT < 3500','xqcut = 40, qCut = 60','13.65','2.16','0.194'],
'mg_pp_t123j_5f_HT_3500_5900':['single top (s,t channels)+ 1/2/3 jets','3500 < HT < 5900','xqcut = 40, qCut = 60','1.371','2.16','0.171'],
'mg_pp_t123j_5f_HT_5900_100000':['single top (s,t channels)+ 1/2/3 jets','5900 < HT < 100000','xqcut = 40, qCut = 60','0.175','2.16','0.158'],
'mg_pp_t123j_5f':['single top (s,t channels)+ 1/2/3 jets','inclusive','xqcut = 40, qCut = 60','7524','2.16','0.288'],
'mg_pp_llv01j_5f_HT_0_800':[' di-vector with V -> ll (l=e,mu,ve,vm,vt) + 0/1 jets','0 < HT < 800','xqcut = 40, qCut = 60','108.7','1.70','0.78'],
'mg_pp_llv01j_5f_HT_800_2000':[' di-vector with V -> ll (l=e,mu,ve,vm,vt) + 0/1 jets','800 < HT < 2000','xqcut = 40, qCut = 60','0.9956','1.70','0.743'],
'mg_pp_llv01j_5f_HT_2000_4000':[' di-vector with V -> ll (l=e,mu,ve,vm,vt) + 0/1 jets','2000 < HT < 4000','xqcut = 40, qCut = 60','0.07411','1.70','0.805'],
'mg_pp_llv01j_5f_HT_4000_100000':[' di-vector with V -> ll (l=e,mu,ve,vm,vt) + 0/1 jets','4000 < HT < 100000','xqcut = 40, qCut = 60','0.008311','1.70','0.823'],
'mg_pp_llv01j_5f':[' di-vector with V -> ll (l=e,mu,ve,vm,vt) + 0/1 jets','inclusive','xqcut = 40, qCut = 60','110.3','1.70','0.779'],
'mg_pp_vh012j_5f_HT_0_300':['higgsstrahlung + 0/1/2 jets','0 < HT < 300','xqcut = 40, qCut = 60','25.24','1.32','0.604'],
'mg_pp_vh012j_5f_HT_300_1400':['higgsstrahlung + 0/1/2 jets','300 < HT < 1400','xqcut = 40, qCut = 60','11.7','1.32','0.416'],
'mg_pp_vh012j_5f_HT_1400_2900':['higgsstrahlung + 0/1/2 jets','1400 < HT < 2900','xqcut = 40, qCut = 60','0.3437','1.32','0.378'],
'mg_pp_vh012j_5f_HT_2900_5300':['higgsstrahlung + 0/1/2 jets','2900 < HT < 5300','xqcut = 40, qCut = 60','0.03349','1.32','0.371'],
'mg_pp_vh012j_5f_HT_5300_8800':['higgsstrahlung + 0/1/2 jets','5300 < HT < 8800','xqcut = 40, qCut = 60','0.003608','1.32','0.364'],
'mg_pp_vh012j_5f_HT_8800_100000':['higgsstrahlung + 0/1/2 jets','8800 < HT < 100000','xqcut = 40, qCut = 60','0.0004647','1.32','0.357'],
'mg_pp_vh012j_5f':['higgsstrahlung + 0/1/2 jets','inclusive','xqcut = 40, qCut = 60','37.43','1.32','0.544'],
'mg_pp_tt012j_5f_HT_0_600':['top pair + 0/1/2 jets','0 < HT < 600','xqcut = 60, qCut = 90','3.207e+04','1.74','0.507'],
'mg_pp_tt012j_5f_HT_600_1200':['top pair + 0/1/2 jets','600 < HT < 1200','xqcut = 60, qCut = 90','8883','1.74','0.352'],
'mg_pp_tt012j_5f_HT_1200_2100':['top pair + 0/1/2 jets','1200 < HT < 2100','xqcut = 60, qCut = 90','1737','1.74','0.328'],
'mg_pp_tt012j_5f_HT_2100_3400':['top pair + 0/1/2 jets','2100 < HT < 3400','xqcut = 60, qCut = 90','284.3','1.74','0.315'],
'mg_pp_tt012j_5f_HT_3400_5300':['top pair + 0/1/2 jets','3400 < HT < 5300','xqcut = 60, qCut = 90','44.91','1.74','0.306'],
'mg_pp_tt012j_5f_HT_5300_8100':['top pair + 0/1/2 jets','5300 < HT < 8100','xqcut = 60, qCut = 90','6.484','1.74','0.298'],
'mg_pp_tt012j_5f_HT_8100_15000':['top pair + 0/1/2 jets','8100 < HT < 15000','xqcut = 60, qCut = 90','0.8583','1.74','0.294'],
'mg_pp_tt012j_5f_HT_15000_25000':['top pair + 0/1/2 jets','15000 < HT < 25000','xqcut = 60, qCut = 90','0.0219','1.74','0.296'],
'mg_pp_tt012j_5f_HT_25000_35000':['top pair + 0/1/2 jets','25000 < HT < 35000','xqcut = 60, qCut = 90','0.0004247','1.74','0.307'],
'mg_pp_tt012j_5f_HT_35000_100000':['top pair + 0/1/2 jets','35000 < HT < 100000','xqcut = 60, qCut = 90','1.459e-05','1.74','0.323'],
'mg_pp_tt012j_5f':['top pair + 0/1/2 jets','inclusive','xqcut = 60, qCut = 90','4.311e+04','1.74','0.466'],
'mg_pp_vbf_h01j_5f_HT_0_2000':['vbf higgs + 0/1 jets','0 < HT < 2000','xqcut = 40, qCut = 60','83.91','4.3','0.187'],
'mg_pp_vbf_h01j_5f_HT_2000_4000':['vbf higgs + 0/1 jets','2000 < HT < 4000','xqcut = 40, qCut = 60','0.07215','4.3','0.168'],
'mg_pp_vbf_h01j_5f_HT_4000_7200':['vbf higgs + 0/1 jets','4000 < HT < 7200','xqcut = 40, qCut = 60','0.003946','4.3','0.128'],
'mg_pp_vbf_h01j_5f_HT_7200_100000':['vbf higgs + 0/1 jets','7200 < HT < 100000','xqcut = 40, qCut = 60','0.000268','4.3','0.102'],
'mg_pp_vbf_h01j_5f':['vbf higgs + 0/1 jets','inclusive','xqcut = 40, qCut = 60','84.17','4.3','0.187'],
'mg_pp_vbf_hh01j_5f_HT_0_2000':['vbf di-higgs + 0/1 jets','0 < HT < 2000','xqcut = 60, qCut = 90','0.08974','1.0','1.0'],
'mg_pp_vbf_hh01j_5f_HT_2000_4000':['vbf di-higgs + 0/1 jets','2000 < HT < 4000','xqcut = 60, qCut = 90','0.0007247','1.0','1.0'],
'mg_pp_vbf_hh01j_5f_HT_4000_7200':['vbf di-higgs + 0/1 jets','4000 < HT < 7200','xqcut = 60, qCut = 90','7.489e-05','1.0','1.0'],
'mg_pp_vbf_hh01j_5f_HT_7200_100000':['vbf di-higgs + 0/1 jets','7200 < HT < 100000','xqcut = 60, qCut = 90','8.888e-06','1.0','1.0'],
'mg_pp_vbf_hh01j_5f':['vbf di-higgs + 0/1 jets','inclusive','xqcut = 60, qCut = 90','0.06453','1.0','1.0'],
'mg_pp_tthh01j_5f':['top pair di-higgs + 0/1 jets','inclusive','xqcut = 100, qCut = 150','0.1164','1.0','1.0'],
'mg_pp_v0123j_5f_HT_0_1500':['vector boson + 0/1/2/3 jets','0 < HT < 1500','xqcut = 30, qCut = 45','8.889e+06','1.20','0.231'],
'mg_pp_v0123j_5f_HT_1500_2900':['vector boson + 0/1/2/3 jets','1500 < HT < 2900','xqcut = 30, qCut = 45','2868','1.20','0.257'],
'mg_pp_v0123j_5f_HT_2900_5100':['vector boson + 0/1/2/3 jets','2900 < HT < 5100','xqcut = 30, qCut = 45','300.8','1.20','0.244'],
'mg_pp_v0123j_5f_HT_5100_8500':['vector boson + 0/1/2/3 jets','5100 < HT < 8500','xqcut = 30, qCut = 45','30.94','1.20','0.227'],
'mg_pp_v0123j_5f_HT_8500_100000':['vector boson + 0/1/2/3 jets','8500 < HT < 100000','xqcut = 30, qCut = 45','2.95','1.20','0.204'],
'mg_pp_v0123j_5f':['vector boson + 0/1/2/3 jets','inclusive','xqcut = 30, qCut = 45','8.886e+06','1.20','0.232'],
'mg_gg_aa01j_5f_HT_0_500':['gluon fusion di-photon + 0/1 jets','0 < HT < 500','xqcut = 20, qCut = 30','850.4','2.0','0.578'],
'mg_gg_aa01j_5f_HT_500_1000':['gluon fusion di-photon + 0/1 jets','500 < HT < 1000','xqcut = 20, qCut = 30','0.5129','2.0','0.383'],
'mg_gg_aa01j_5f_HT_1000_2000':['gluon fusion di-photon + 0/1 jets','1000 < HT < 2000','xqcut = 20, qCut = 30','0.04712','2.0','0.344'],
'mg_gg_aa01j_5f_HT_2000_4000':['gluon fusion di-photon + 0/1 jets','2000 < HT < 4000','xqcut = 20, qCut = 30','0.002895','2.0','0.319'],
'mg_gg_aa01j_5f_HT_4000_7200':['gluon fusion di-photon + 0/1 jets','4000 < HT < 7200','xqcut = 20, qCut = 30','8.602e-05','2.0','0.319'],
'mg_gg_aa01j_5f_HT_7200_100000':['gluon fusion di-photon + 0/1 jets','7200 < HT < 100000','xqcut = 20, qCut = 30','4.357e-06','2.0','0.322'],
'mg_gg_aa01j_5f':['gluon fusion di-photon + 0/1 jets','inclusive','xqcut = 20, qCut = 30','851.5','2.0','0.576'],
'mg_pp_vv012j_4f_HT_0_300':['di-vector boson + 0/1/2 jets (4f)','0 < HT < 300','xqcut = 40, qCut = 60','3.093e+04','1.70','0.453'],
'mg_pp_vv012j_4f_HT_300_1400':['di-vector boson + 0/1/2 jets (4f)','300 < HT < 1400','xqcut = 40, qCut = 60','2133','1.70','0.542'],
'mg_pp_vv012j_4f_HT_1400_2900':['di-vector boson + 0/1/2 jets (4f)','1400 < HT < 2900','xqcut = 40, qCut = 60','69.23','1.70','0.534'],
'mg_pp_vv012j_4f_HT_2900_5300':['di-vector boson + 0/1/2 jets (4f)','2900 < HT < 5300','xqcut = 40, qCut = 60','8.001','1.70','0.541'],
'mg_pp_vv012j_4f_HT_5300_8800':['di-vector boson + 0/1/2 jets (4f)','5300 < HT < 8800','xqcut = 40, qCut = 60','0.9684','1.70','0.55'],
'mg_pp_vv012j_4f_HT_8800_15000':['di-vector boson + 0/1/2 jets (4f)','8800 < HT < 15000','xqcut = 40, qCut = 60','0.1286','1.70','0.571'],
'mg_pp_vv012j_4f_HT_15000_25000':['di-vector boson + 0/1/2 jets (4f)','15000 < HT < 25000','xqcut = 40, qCut = 60','0.009475','1.70','0.617'],
'mg_pp_vv012j_4f_HT_25000_35000':['di-vector boson + 0/1/2 jets (4f)','25000 < HT < 35000','xqcut = 40, qCut = 60','0.0003517','1.70','0.69'],
'mg_pp_vv012j_4f_HT_35000_100000':['di-vector boson + 0/1/2 jets (4f)','35000 < HT < 100000','xqcut = 40, qCut = 60','2.07e-05','1.70','0.758'],
'mg_pp_vv012j_5f':['di-vector boson + 0/1/2 jets','inclusive','xqcut = 40, qCut = 60','3.39e+04','1.70','0.457'],
'mg_pp_jj012j_5f_HT_0_500':['di-jet + 0/1/2 jets','0 < HT < 500','xqcut = 20, qCut = 30','6.517e+09','1.0','0.141'],
'mg_pp_jj012j_5f_HT_500_1000':['di-jet + 0/1/2 jets','500 < HT < 1000','xqcut = 20, qCut = 30','1.642e+07','1.0','0.092'],
'mg_pp_jj012j_5f_HT_1000_2000':['di-jet + 0/1/2 jets','1000 < HT < 2000','xqcut = 20, qCut = 30','1.673e+06','1.0','0.071'],
'mg_pp_jj012j_5f_HT_2000_4000':['di-jet + 0/1/2 jets','2000 < HT < 4000','xqcut = 20, qCut = 30','1.32e+05','1.0','0.057'],
'mg_pp_jj012j_5f_HT_4000_7200':['di-jet + 0/1/2 jets','4000 < HT < 7200','xqcut = 20, qCut = 30','7316','1.0','0.048'],
'mg_pp_jj012j_5f_HT_7200_15000':['di-jet + 0/1/2 jets','7200 < HT < 15000','xqcut = 20, qCut = 30','474.9','1.0','0.043'],
'mg_pp_jj012j_5f_HT_15000_25000':['di-jet + 0/1/2 jets','15000 < HT < 25000','xqcut = 20, qCut = 30','7.349','1.0','0.041'],
'mg_pp_jj012j_5f_HT_25000_35000':['di-jet + 0/1/2 jets','25000 < HT < 35000','xqcut = 20, qCut = 30','0.1759','1.0','0.041'],
'mg_pp_jj012j_5f_HT_35000_100000':['di-jet + 0/1/2 jets','35000 < HT < 100000','xqcut = 20, qCut = 30','0.007654','1.0','0.043'],
'mg_pp_jj012j_5f':['di-jet + 0/1/2 jets','inclusive','xqcut = 20, qCut = 30','6.563e+09','1.0','0.118'],
'mg_pp_tv012j_5f_HT_0_500':['top pair off-shell t* -> Wj + 0/1/2 jets','0 < HT < 500','xqcut = 60, qCut = 90','3000','1.34','0.488'],
'mg_pp_tv012j_5f_HT_500_1500':['top pair off-shell t* -> Wj + 0/1/2 jets','500 < HT < 1500','xqcut = 60, qCut = 90','1124','1.34','0.396'],
'mg_pp_tv012j_5f_HT_1500_2800':['top pair off-shell t* -> Wj + 0/1/2 jets','1500 < HT < 2800','xqcut = 60, qCut = 90','72.13','1.34','0.376'],
'mg_pp_tv012j_5f_HT_2800_4700':['top pair off-shell t* -> Wj + 0/1/2 jets','2800 < HT < 4700','xqcut = 60, qCut = 90','7.738','1.34','0.358'],
'mg_pp_tv012j_5f_HT_4700_7400':['top pair off-shell t* -> Wj + 0/1/2 jets','4700 < HT < 7400','xqcut = 60, qCut = 90','0.7973','1.34','0.334'],
'mg_pp_tv012j_5f_HT_7400_100000':['top pair off-shell t* -> Wj + 0/1/2 jets','7400 < HT < 100000','xqcut = 60, qCut = 90','0.09901','1.34','0.329'],
'mg_pp_tv012j_5f':['top pair off-shell t* -> Wj + 0/1/2 jets','inclusive','xqcut = 60, qCut = 90','4210','1.34','0.461'],
'mg_pp_tth01j_5f_HT_0_1100':['higgs associated with top pair + 0/1 jets','0 < HT < 1100','xqcut = 80, qCut = 120','36.94','1.22','0.612'],
'mg_pp_tth01j_5f_HT_1100_2700':['higgs associated with top pair + 0/1 jets','1100 < HT < 2700','xqcut = 80, qCut = 120','7.466','1.22','0.613'],
'mg_pp_tth01j_5f_HT_2700_4900':['higgs associated with top pair + 0/1 jets','2700 < HT < 4900','xqcut = 80, qCut = 120','0.4224','1.22','0.636'],
'mg_pp_tth01j_5f_HT_4900_8100':['higgs associated with top pair + 0/1 jets','4900 < HT < 8100','xqcut = 80, qCut = 120','0.0336','1.22','0.642'],
'mg_pp_tth01j_5f_HT_8100_100000':['higgs associated with top pair + 0/1 jets','8100 < HT < 100000','xqcut = 80, qCut = 120','0.002924','1.22','0.644'],
'mg_pp_tth01j_5f':['higgs associated with top pair + 0/1 jets','inclusive','xqcut = 80, qCut = 120','44.84','1.22','0.612'],
'mg_pp_hh01j_5f_HT_0_300':['gluon fusion di-higgs + 0/1 jets','0 < HT < 300','xqcut = 60, qCut = 90','0.3501','3.87','0.418'],
'mg_pp_hh01j_5f_HT_300_1400':['gluon fusion di-higgs + 0/1 jets','300 < HT < 1400','xqcut = 60, qCut = 90','0.7453','3.87','0.412'],
'mg_pp_hh01j_5f_HT_1400_2900':['gluon fusion di-higgs + 0/1 jets','1400 < HT < 2900','xqcut = 60, qCut = 90','0.01265','3.87','0.451'],
'mg_pp_hh01j_5f_HT_2900_5300':['gluon fusion di-higgs + 0/1 jets','2900 < HT < 5300','xqcut = 60, qCut = 90','0.0007173','3.87','0.433'],
'mg_pp_hh01j_5f_HT_5300_8800':['gluon fusion di-higgs + 0/1 jets','5300 < HT < 8800','xqcut = 60, qCut = 90','4.124e-05','3.87','0.426'],
'mg_pp_hh01j_5f_HT_8800_100000':['gluon fusion di-higgs + 0/1 jets','8800 < HT < 100000','xqcut = 60, qCut = 90','2.703e-06','3.87','0.413'],
'mg_pp_hh01j_5f':['gluon fusion di-higgs + 0/1 jets','inclusive','xqcut = 60, qCut = 90','1.113','3.87','0.414'],
'mg_pp_ttv01j_5f_HT_0_1100':['top pair + boson + 0/1 jets','0 < HT < 1100','xqcut = 80, qCut = 120','222','1.14','0.537'],
'mg_pp_ttv01j_5f_HT_1100_2700':['top pair + boson + 0/1 jets','1100 < HT < 2700','xqcut = 80, qCut = 120','32.88','1.14','0.657'],
'mg_pp_ttv01j_5f_HT_2700_4900':['top pair + boson + 0/1 jets','2700 < HT < 4900','xqcut = 80, qCut = 120','2.163','1.14','0.706'],
'mg_pp_ttv01j_5f_HT_4900_8100':['top pair + boson + 0/1 jets','4900 < HT < 8100','xqcut = 80, qCut = 120','0.2143','1.14','0.73'],
'mg_pp_ttv01j_5f_HT_8100_100000':['top pair + boson + 0/1 jets','8100 < HT < 100000','xqcut = 80, qCut = 120','0.02413','1.14','0.744'],
'mg_pp_ttv01j_5f':['top pair + boson + 0/1 jets','inclusive','xqcut = 80, qCut = 120','258.3','1.14','0.552'],
'mg_pp_ll012j_5f_HT_0_200':['V -> ll (l=e,mu,ve,vm,vt) + ','0 < HT < 200','xqcut = 30, qCut = 45','1.158e+04','1.20','0.85'],
'mg_pp_ll012j_5f_HT_200_700':['V -> ll (l=e,mu,ve,vm,vt) + ','200 < HT < 700','xqcut = 30, qCut = 45','717.3','1.20','0.464'],
'mg_pp_ll012j_5f_HT_700_1500':['V -> ll (l=e,mu,ve,vm,vt) + ','700 < HT < 1500','xqcut = 30, qCut = 45','37.04','1.20','0.448'],
'mg_pp_ll012j_5f_HT_1500_2700':['V -> ll (l=e,mu,ve,vm,vt) + ','1500 < HT < 2700','xqcut = 30, qCut = 45','3.723','1.20','0.448'],
'mg_pp_ll012j_5f_HT_2700_4200':['V -> ll (l=e,mu,ve,vm,vt) + ','2700 < HT < 4200','xqcut = 30, qCut = 45','0.4862','1.20','0.452'],
'mg_pp_ll012j_5f_HT_4200_8000':['V -> ll (l=e,mu,ve,vm,vt) + ','4200 < HT < 8000','xqcut = 30, qCut = 45','0.1125','1.20','0.44'],
'mg_pp_ll012j_5f_HT_8000_15000':['V -> ll (l=e,mu,ve,vm,vt) + ','8000 < HT < 15000','xqcut = 30, qCut = 45','0.008175','1.20','0.424'],
'mg_pp_ll012j_5f_HT_15000_25000':['V -> ll (l=e,mu,ve,vm,vt) + ','15000 < HT < 25000','xqcut = 30, qCut = 45','0.000314','1.20','0.429'],
'mg_pp_ll012j_5f_HT_25000_35000':['V -> ll (l=e,mu,ve,vm,vt) + ','25000 < HT < 35000','xqcut = 30, qCut = 45','8.832e-06','1.20','0.474'],
'mg_pp_ll012j_5f_HT_35000_100000':['V -> ll (l=e,mu,ve,vm,vt) + ','35000 < HT < 100000','xqcut = 30, qCut = 45','4.069e-07','1.20','0.509'],
'mg_pp_ll012j_5f':['V -> ll (l=e,mu,ve,vm,vt) + ','inclusive','xqcut = 30, qCut = 45','1.235e+04','1.20','0.83'],
'mg_pp_aa012j_5f_HT_0_500':['di-photon + 0/1/2 jets','0 < HT < 500','xqcut = 20, qCut = 30','6919','2.0','0.302'],
'mg_pp_aa012j_5f_HT_500_1000':['di-photon + 0/1/2 jets','500 < HT < 1000','xqcut = 20, qCut = 30','88.64','2.0','0.612'],
'mg_pp_aa012j_5f_HT_1000_2000':['di-photon + 0/1/2 jets','1000 < HT < 2000','xqcut = 20, qCut = 30','13.72','2.0','0.659'],
'mg_pp_aa012j_5f_HT_2000_4000':['di-photon + 0/1/2 jets','2000 < HT < 4000','xqcut = 20, qCut = 30','1.424','2.0','0.679'],
'mg_pp_aa012j_5f_HT_4000_7200':['di-photon + 0/1/2 jets','4000 < HT < 7200','xqcut = 20, qCut = 30','0.01786','2.0','0.446'],
'mg_pp_aa012j_5f_HT_7200_100000':['di-photon + 0/1/2 jets','7200 < HT < 100000','xqcut = 20, qCut = 30','4.859e-05','2.0','0.151'],
'mg_pp_aa012j_5f':['di-photon + 0/1/2 jets','inclusive','xqcut = 20, qCut = 30','7030','2.0','0.307'],
'mg_pp_aj012j_5f_HT_0_500':['photon + jet + 0/1/2 jets','0 < HT < 500','xqcut = 20, qCut = 30','6.722e+06','1.0','0.132'],
'mg_pp_aj012j_5f_HT_500_1000':['photon + jet + 0/1/2 jets','500 < HT < 1000','xqcut = 20, qCut = 30','3.222e+04','1.0','0.266'],
'mg_pp_aj012j_5f_HT_1000_2000':['photon + jet + 0/1/2 jets','1000 < HT < 2000','xqcut = 20, qCut = 30','4045','1.0','0.26'],
'mg_pp_aj012j_5f_HT_2000_4000':['photon + jet + 0/1/2 jets','2000 < HT < 4000','xqcut = 20, qCut = 30','399','1.0','0.257'],
'mg_pp_aj012j_5f_HT_4000_7200':['photon + jet + 0/1/2 jets','4000 < HT < 7200','xqcut = 20, qCut = 30','14.68','1.0','0.253'],
'mg_pp_aj012j_5f_HT_7200_100000':['photon + jet + 0/1/2 jets','7200 < HT < 100000','xqcut = 20, qCut = 30','0.467','1.0','0.231'],
'mg_pp_aj012j_5f':['photon + jet + 0/1/2 jets','inclusive','xqcut = 20, qCut = 30','6.759e+06','1.0','0.132'],
'mg_pp_h012j_5f_HT_0_100':['gluon fusion higgs (finite mt) + 0/1/2 jets','0 < HT < 100','xqcut = 30, qCut = 45','312.9','3.76','0.404'],
'mg_pp_h012j_5f_HT_100_400':['gluon fusion higgs (finite mt) + 0/1/2 jets','100 < HT < 400','xqcut = 30, qCut = 45','220.4','3.76','0.317'],
'mg_pp_h012j_5f_HT_400_1000':['gluon fusion higgs (finite mt) + 0/1/2 jets','400 < HT < 1000','xqcut = 30, qCut = 45','47.28','3.76','0.312'],
'mg_pp_h012j_5f_HT_400_100000':['gluon fusion higgs (finite mt) + 0/1/2 jets','400 < HT < 100000','xqcut = 30, qCut = 45','51.44','3.76','0.312'],
'mg_pp_h012j_5f_HT_1000_1900':['gluon fusion higgs (finite mt) + 0/1/2 jets','1000 < HT < 1900','xqcut = 30, qCut = 45','3.587','3.76','0.31'],
'mg_pp_h012j_5f_HT_1900_4400':['gluon fusion higgs (finite mt) + 0/1/2 jets','1900 < HT < 4400','xqcut = 30, qCut = 45','0.277','3.76','0.296'],
'mg_pp_h012j_5f_HT_4400_8500':['gluon fusion higgs (finite mt) + 0/1/2 jets','4400 < HT < 8500','xqcut = 30, qCut = 45','0.003902','3.76','0.27'],
'mg_pp_h012j_5f_HT_8500_100000':['gluon fusion higgs (finite mt) + 0/1/2 jets','8500 < HT < 100000','xqcut = 30, qCut = 45','6.368e-05','3.76','0.28'],
'mg_pp_h012j_5f':['gluon fusion higgs (finite mt) + 0/1/2 jets','inclusive','xqcut = 30, qCut = 45','587.5','3.76','0.364'],
'mg_pp_vvv01j_5f_HT_0_1200':['tri-vector boson + 0/1 jets','0 < HT < 1200','xqcut = 60, qCut = 90','73.04','1.05','0.515'],
'mg_pp_vvv01j_5f_HT_1200_3000':['tri-vector boson + 0/1 jets','1200 < HT < 3000','xqcut = 60, qCut = 90','2.093','1.05','0.838'],
'mg_pp_vvv01j_5f_HT_3000_6000':['tri-vector boson + 0/1 jets','3000 < HT < 6000','xqcut = 60, qCut = 90','0.2028','1.05','0.872'],
'mg_pp_vvv01j_5f_HT_6000_100000':['tri-vector boson + 0/1 jets','6000 < HT < 100000','xqcut = 60, qCut = 90','0.02111','1.05','0.893'],
'mg_pp_vvv01j_5f':['tri-vector boson + 0/1 jets','inclusive','xqcut = 60, qCut = 90','75.87','1.05','0.525'],
'mg_pp_z0123j_4f_HT_0_150':['z + 0/1/2/3 jets','0 < HT < 150','xqcut = 30, qCut = 45','4.658e+05','1.20','1.0'],
'mg_pp_z0123j_4f_HT_150_300':['z + 0/1/2/3 jets','150 < HT < 300','xqcut = 30, qCut = 45','2.944e+04','1.20','1.0'],
'mg_pp_z0123j_4f_HT_300_500':['z + 0/1/2/3 jets','300 < HT < 500','xqcut = 30, qCut = 45','8958','1.20','1.0'],
'mg_pp_z0123j_4f_HT_500_1000':['z + 0/1/2/3 jets','500 < HT < 1000','xqcut = 30, qCut = 45','3756','1.20','1.0'],
'mg_pp_z0123j_4f_HT_1000_2000':['z + 0/1/2/3 jets','1000 < HT < 2000','xqcut = 30, qCut = 45','703.8','1.20','1.0'],
'mg_pp_z0123j_4f_HT_2000_5000':['z + 0/1/2/3 jets','2000 < HT < 5000','xqcut = 30, qCut = 45','102.3','1.20','1.0'],
'mg_pp_z0123j_4f_HT_5000_100000':['z + 0/1/2/3 jets','5000 < HT < 100000','xqcut = 30, qCut = 45','4.196','1.20','1.0'],
'mg_pp_z0123j_4f':['z + 0/1/2/3 jets','inclusive','xqcut = 30, qCut = 45','5.091e+05','1.20','1.0'],
'mg_pp_w0123j_4f_HT_0_150':['w + 0/1/2/3 jets','0 < HT < 150','xqcut = 30, qCut = 45','1.478e+06','1.20','1.0'],
'mg_pp_w0123j_4f_HT_150_300':['w + 0/1/2/3 jets','150 < HT < 300','xqcut = 30, qCut = 45','8.377e+04','1.20','1.0'],
'mg_pp_w0123j_4f_HT_300_500':['w + 0/1/2/3 jets','300 < HT < 500','xqcut = 30, qCut = 45','2.493e+04','1.20','1.0'],
'mg_pp_w0123j_4f_HT_500_1000':['w + 0/1/2/3 jets','500 < HT < 1000','xqcut = 30, qCut = 45','1.037e+04','1.20','1.0'],
'mg_pp_w0123j_4f_HT_1000_2000':['w + 0/1/2/3 jets','1000 < HT < 2000','xqcut = 30, qCut = 45','1917','1.20','1.0'],
'mg_pp_w0123j_4f_HT_2000_5000':['w + 0/1/2/3 jets','2000 < HT < 5000','xqcut = 30, qCut = 45','273.7','1.20','1.0'],
'mg_pp_w0123j_4f_HT_5000_100000':['w + 0/1/2/3 jets','5000 < HT < 100000','xqcut = 30, qCut = 45','11.11','1.20','1.0'],
'mg_pp_w0123j_4f':['w + 0/1/2/3 jets','inclusive','xqcut = 30, qCut = 45','1.599e+06','1.20','1.0'],
'mg_pp_jjj_5f_PT_500_inf':['tri-jet','pT(leading) > 500 GeV','','3.236e+04','2.0','0.999'],
'mg_pp_tt_nlo':['ttbar @NLO','pT(top) > 2.5 TeV','','2.008e-02','1.0','1.0'],
'mg_pp_vv_nlo':['VV (W/Z) @NLO','pT(V) > 2.5 TeV','','2.926e-04','1.0','1.0'],
'mg_pp_ee_nlo':['e+e- @NLO','m(ee) > 5 TeV','','1.553e-04','1.0','1.0'],
'mg_pp_mumu_nlo':['m+m- @NLO','m(mumu) > 5 TeV','','1.553e-04','1.0','1.0'],
'mg_pp_wj_4f_M_5000_inf':['w+ 1j','m(wj) > 5 TeV','','0.3314','2.0','1.0'],
'mg_pp_vj_4f_M_5000_inf':['w/z+ 1j','m(vj) > 5 TeV','','0.4679','2.0','1.0'],
'mg_pp_ee_lo':['','m > 10 TeV','','9.428e-06','2.0','1.0'],
'mg_pp_mumu_lo':['','m > 10 TeV','','9.428e-06','2.0','1.0'],
'mg_pp_mumu_lo_2TeV':['','m > 2 TeV','','0.00717','2.0','1.0'],
'mg_pp_tt_lo':['','m > 5 TeV','','0.1373','2.0','1.0'],
'mg_pp_jj_lo':['','m > 5 TeV','','43.05','2.0','1.0'],
'mg_pp_jj_lo_filter_pTjet7.5TeV':['','m > 15 TeV','','0.07777','2.0','1.0'],
'mg_pp_vv_lo':['','m > 5 TeV','','0.00316','2.0','1.0'],
'mg_pp_www_4f':['WWW (4FS)','inclusive','','1.686','2.5','1.0'],
'mg_pp_wwz_4f':['WWZ (4FS)','inclusive','','1.437','2.8','1.0'],
'mg_pp_wzz_5f':['WZZ','inclusive','','0.4479','3.0','1.0'],
'mg_pp_zzz_5f':['ZZZ','inclusive','','0.151','1.7','1.0'],
'mg_pp_wwwz_4f':['WWWZ (4FS)','inclusive','','0.01792','3.3','1.0'],
'mg_pp_wwww_4f':['WWWW (4FS)','inclusive','','0.01361','3.0','1.0'],
'mg_pp_wwzz_4f':['WWZZ (4FS)','inclusive','','0.01247','2.7','1.0'],
'mg_pp_wzzz_5f':['WZZZ','inclusive','','0.001633','1.5','1.0'],
'mg_pp_zzzz_5f':['ZZZZ','inclusive','','0.000461','1.7','1.0'],
'mg_pp_zzzzz_5f':['ZZZZZ','inclusive','','2.267e-06','2.0','1.0'],
'mg_pp_tttt_5f':['tttt','inclusive','','2.316','2.1','1.0'],
'mg_pp_ttz_5f':['ttZ','inclusive','','38.05','1.5','0.0'],
'mg_pp_ttw_5f':['ttW','inclusive','','6.545','2.5','1.0'],
'mg_pp_ttww_4f':['ttWW (4FS)','inclusive','','0.7827','1.4','1.0'],
'mg_pp_ttwz_5f':['ttWZ','inclusive','','0.07427','2.3','1.0'],
'mg_pp_ttzz_5f':['ttZZ','inclusive','','0.1206','1.3','0.0'],
'mg_pp_tt4l_4f':['tt4l non resonant','inclusive','','4.122e-05','1.3','1.0'],
'mg_pp_tt2l_4f':['tt2l non resonant','inclusive','','4.389','1.5','1.0'],
'mg_pp_mumu012j_mhcut_5f':['mu+ mu- + 0/1/2 jets','50 < m(mumu) < 200','','1.4e+04','1.0','0.753'],
'mg_pp_lla01j_mhcut_5f':['l+ l- gamma + 0/1 jets','50 < m(lla) < 200','','639.1','1.0','0.78'],
'mg_gg_aa01j_mhcut_5f':['gluon fusion di-photon + 0/1 jets','50 < m(aa) < 200','','484.2','1.0','0.592'],
'mg_pp_aa012j_mhcut_5f':['di-photon + 0/1/2 jets','50 < m(aa) < 200','','1530','1.0','0.403'],
'mg_pp_llll01j_mhcut_5f':['4l + 0/1 jets','50 < m(4l) < 200','','0.1517','1.0','0.813'],
'mg_pp_aa012j_mhcut_5f_HT_0_100':['di-photon + 0/1/2 jets','0 < HT < 100','xqcut = 30, qCut = 40','116.8','2.0','0.656'],
'mg_pp_aa012j_mhcut_5f_HT_100_300':['di-photon + 0/1/2 jets','100 < HT < 300','xqcut = 30, qCut = 40','61.58','2.0','0.591'],
'mg_pp_aa012j_mhcut_5f_HT_300_500':['di-photon + 0/1/2 jets','300 < HT < 500','xqcut = 30, qCut = 40','7.016','2.0','0.75'],
'mg_pp_aa012j_mhcut_5f_HT_500_700':['di-photon + 0/1/2 jets','500 < HT < 700','xqcut = 30, qCut = 40','1.203','2.0','0.837'],
'mg_pp_aa012j_mhcut_5f_HT_700_900':['di-photon + 0/1/2 jets','700 < HT < 900','xqcut = 30, qCut = 40','0.4198','2.0','0.872'],
'mg_pp_aa012j_mhcut_5f_HT_900_1100':['di-photon + 0/1/2 jets','900 < HT < 1100','xqcut = 30, qCut = 40','0.1834','2.0','0.896'],
'mg_pp_aa012j_mhcut_5f_HT_1100_100000':['di-photon + 0/1/2 jets','1100 < HT < 100000','xqcut = 30, qCut = 40','0.3637','2.0','0.931'],
'mg_pp_mumu012j_mhcut_5f_HT_0_100':['mu+ mu- + 0/1/2 jets','0 < HT < 100','xqcut = 30, qCut = 40','382.9','1.20','0.694'],
'mg_pp_mumu012j_mhcut_5f_HT_100_300':['mu+ mu- + 0/1/2 jets','100 < HT < 300','xqcut = 30, qCut = 40','44.08','1.20','0.339'],
'mg_pp_mumu012j_mhcut_5f_HT_300_500':['mu+ mu- + 0/1/2 jets','300 < HT < 500','xqcut = 30, qCut = 40','4.723','1.20','0.221'],
'mg_pp_mumu012j_mhcut_5f_HT_500_700':['mu+ mu- + 0/1/2 jets','500 < HT < 700','xqcut = 30, qCut = 40','1.14','1.20','0.148'],
'mg_pp_mumu012j_mhcut_5f_HT_700_900':['mu+ mu- + 0/1/2 jets','700 < HT < 900','xqcut = 30, qCut = 40','0.3945','1.20','0.115'],
'mg_pp_mumu012j_mhcut_5f_HT_900_1100':['mu+ mu- + 0/1/2 jets','900 < HT < 1100','xqcut = 30, qCut = 40','0.1691','1.20','0.09'],
'mg_pp_mumu012j_mhcut_5f_HT_1100_100000':['mu+ mu- + 0/1/2 jets','1100 < HT < 100000','xqcut = 30, qCut = 40','0.2093','1.20','0.058'],
'mg_pp_lla01j_mhcut_5f_HT_0_100':['l+ l- gamma + 0/1 jets','0 < HT < 100','xqcut = 30, qCut = 40','39.52','1.50','0.743'],
'mg_pp_lla01j_mhcut_5f_HT_100_300':['l+ l- gamma + 0/1 jets','100 < HT < 300','xqcut = 30, qCut = 40','1.326','1.50','0.486'],
'mg_pp_lla01j_mhcut_5f_HT_300_500':['l+ l- gamma + 0/1 jets','300 < HT < 500','xqcut = 30, qCut = 40','0.004548','1.50','0.245'],
'mg_pp_lla01j_mhcut_5f_HT_300_100000':['l+ l- gamma + 0/1 jets','300 < HT < 100000','xqcut = 30, qCut = 40','0.08149','1.50','0.234'],
'mg_pp_lla01j_mhcut_5f_HT_500_100000':['l+ l- gamma + 0/1 jets','500 < HT < 100000','xqcut = 30, qCut = 40','0.002727','1.50','0.162'],
'mg_pp_llll01j_mhcut_5f_HT_0_200':['Z/gamma* Z/gamma* to 4l + 0/1 jets','0 < HT < 200','xqcut = 40, qCut = 60','0.04957','1.60','0.808'],
'mg_pp_llll01j_mhcut_5f_HT_200_500':['Z/gamma* Z/gamma* to 4l + 0/1 jets','200 < HT < 500','xqcut = 40, qCut = 60','0.0002159','1.60','0.937'],
'mg_pp_llll01j_mhcut_5f_HT_500_1100':['Z/gamma* Z/gamma* to 4l + 0/1 jets','500 < HT < 1100','xqcut = 40, qCut = 60','5.573e-06','1.60','0.949'],
'mg_pp_llll01j_mhcut_5f_HT_1100_100000':['Z/gamma* Z/gamma* to 4l + 0/1 jets','1100 < HT < 100000','xqcut = 40, qCut = 60','1.361e-07','1.60','0.972'],
'mg_gg_aa01j_mhcut_5f_HT_0_200':['gluon fusion di-photon + 0/1 jets','0 < HT < 200','xqcut = 20, qCut = 30','60.21','2.0','0.408'],
'mg_gg_aa01j_mhcut_5f_HT_200_500':['gluon fusion di-photon + 0/1 jets','200 < HT < 500','xqcut = 20, qCut = 30','0.026','2.0','0.915'],
'mg_gg_aa01j_mhcut_5f_HT_200_100000':['gluon fusion di-photon + 0/1 jets','200 < HT < 100000','xqcut = 20, qCut = 30','0.02618','2.0','0.917'],
'mg_gg_aa01j_mhcut_5f_HT_500_100000':['gluon fusion di-photon + 0/1 jets','500 < HT < 100000','xqcut = 20, qCut = 30','0.0002481','2.0','0.956'],
'mg_pp_llaj_mhcut_5f_HT_0_150':['l+ l- gamma + 1 jet','0 < HT < 150','','5.504','','1.0'],
'mg_pp_llaj_mhcut_5f_HT_150_100000':['l+ l- gamma + 1 jet','150 < HT < 100000','','0.2045','','1.0'],
'mg_gg_aaj_mhcut_5f_HT_0_150':['gluon fusion di-photon + 1 jet','0 < HT < 150','','53.86','','1.0'],
'mg_gg_aaj_mhcut_5f_HT_150_100000':['gluon fusion di-photon + 1 jet','150 < HT < 100000','','0.08556','','1.0'],
'mg_pp_mumuj_mhcut_5f_HT_0_100':['mu+ mu- + 1 jet','0 < HT < 100','','103.8','','1.0'],
'mg_pp_mumuj_mhcut_5f_HT_100_500':['mu+ mu- + 1 jet','100 < HT < 500','','11.74','','1.0'],
'mg_pp_mumuj_mhcut_5f_HT_500_100000':['mu+ mu- + 1 jet','500 < HT < 100000','','0.1245','','1.0'],
#Zprime signals to fit flavor anomalie Ben Allanach https://arxiv.org/abs/1710.06363
'mg_pp_Zprime_mumu_5f_Mzp_2TeV':['','Zp->mu+mu-','','0.002573','1.0','1.0'],
'mg_pp_Zprime_mumu_5f_Mzp_4TeV':['','Zp->mu+mu-','','0.0005878','1.0','1.0'],
'mg_pp_Zprime_mumu_5f_Mzp_5TeV':['','Zp->mu+mu-','','0.000332','1.0','1.0'],
'mg_pp_Zprime_mumu_5f_Mzp_6TeV':['','Zp->mu+mu-','','0.000202','1.0','1.0'],
'mg_pp_Zprime_mumu_5f_Mzp_8TeV':['','Zp->mu+mu-','','8.857e-05','1.0','1.0'],
'mg_pp_Zprime_mumu_5f_Mzp_10TeV':['','Zp->mu+mu-','','4.497e-05','1.0','1.0'],
'mg_pp_Zprime_mumu_5f_Mzp_12TeV':['','Zp->mu+mu-','','2.803e-05','1.0','1.0'],
'mg_pp_Zprime_mumu_5f_Mzp_15TeV':['','Zp->mu+mu-','','1.717e-05','1.0','1.0'],
'mg_pp_Zprime_mumu_5f_Mzp_14TeV':['','Zp->mu+mu-','','1.968e-05','1.0','1.0'],
'mg_pp_Zprime_mumu_5f_Mzp_16TeV':['','Zp->mu+mu-','','1.548e-05','1.0','1.0'],
'mg_pp_Zprime_mumu_5f_Mzp_18TeV':['','Zp->mu+mu-','','1.321e-05','1.0','1.0'],
'mg_pp_Zprime_mumu_5f_Mzp_20TeV':['','Zp->mu+mu-','','1.136e-05','1.0','1.0'],
'mg_pp_Zprime_mumu_5f_Mzp_25TeV':['','Zp->mu+mu-','','9.823e-06','1.0','1.0'],
'mg_pp_Zprime_mumu_5f_Mzp_30TeV':['','Zp->mu+mu-','','8.493e-06','1.0','1.0'],
'mg_pp_Zprime_mumu_5f_Mzp_35TeV':['','Zp->mu+mu-','','7.108e-06','1.0','1.0'],
'mg_pp_Zprime_mumu_5f_Mzp_40TeV':['','Zp->mu+mu-','','5.819e-06','1.0','1.0'],
'mg_pp_Zprime_mumu_5f_Mzp_45TeV':['','Zp->mu+mu-','','4.64e-06','1.0','1.0'],

# xsec is given by 2*xsec(NLO)*BR(H->bb), then NNLL/NLO kfactor = 1.33/1.15 is app_mglied according to prescription I.7.8 in Higgs XSECWG YR4 (1610.07922) with delta_t=-0.315
# lambda dep xsec(NLO) from 100TeV version of Fig.12 left plot in 1608.04798 (from private conversation with Gudrun Heinrich)
# for now keep kfactor 1.75/1.15 obtained directly from NNLL (for sake of comparison with YR)
'mg_pp_hh_lambda050_5f':['HH, H->bb, H undec., kl = 0.50','','','1.92258','1.52','1.0'],
'mg_pp_hh_lambda090_5f':['HH, H->bb, H undec., kl = 0.90','','','1.41752','1.52','1.0'],
'mg_pp_hh_lambda095_5f':['HH, H->bb, H undec., kl = 0.95','','','1.36266','1.52','1.0'],
'mg_pp_hh_lambda096_5f':['HH, H->bb, H undec., kl = 0.96','','','1.35191','1.52','1.0'],
'mg_pp_hh_lambda097_5f':['HH, H->bb, H undec., kl = 0.97','','','1.34124','1.52','1.0'],
'mg_pp_hh_lambda098_5f':['HH, H->bb, H undec., kl = 0.98','','','1.33063','1.52','1.0'],
'mg_pp_hh_lambda099_5f':['HH, H->bb, H undec., kl = 0.99','','','1.32011','1.52','1.0'],
'mg_pp_hh_lambda100_5f':['HH, H->bb, H undec., kl = 1.00','','','1.30965','1.52','1.0'],
'mg_pp_hh_lambda101_5f':['HH, H->bb, H undec., kl = 1.01','','','1.29927','1.52','1.0'],
'mg_pp_hh_lambda102_5f':['HH, H->bb, H undec., kl = 1.02','','','1.28896','1.52','1.0'],
'mg_pp_hh_lambda103_5f':['HH, H->bb, H undec., kl = 1.03','','','1.27872','1.52','1.0'],
'mg_pp_hh_lambda104_5f':['HH, H->bb, H undec., kl = 1.04','','','1.26856','1.52','1.0'],
'mg_pp_hh_lambda105_5f':['HH, H->bb, H undec., kl = 1.05','','','1.25848','1.52','1.0'],
'mg_pp_hh_lambda110_5f':['HH, H->bb, H undec., kl = 1.10','','','1.20914','1.52','1.0'],
'mg_pp_hh_lambda150_5f':['HH, H->bb, H undec., kl = 1.50','','','0.88070','1.52','1.0'],
'mg_pp_hhj_lambda050_5f':['HH + 1 jet, pT(HH) > 200, kl = 0.50','inclusive','','0.08285','1.95','1.0'],
'mg_pp_hhj_lambda090_5f':['HH + 1 jet, pT(HH) > 200, kl = 0.90','inclusive','','0.06107','1.95','1.0'],
'mg_pp_hhj_lambda095_5f':['HH + 1 jet, pT(HH) > 200, kl = 0.95','inclusive','','0.05870','1.95','1.0'],
'mg_pp_hhj_lambda100_5f':['HH + 1 jet, pT(HH) > 200, kl = 1.00','inclusive','','0.05644','1.95','1.0'],
'mg_pp_hhj_lambda105_5f':['HH + 1 jet, pT(HH) > 200, kl = 1.05','inclusive','','0.05424','1.95','1.0'],
'mg_pp_hhj_lambda110_5f':['HH + 1 jet, pT(HH) > 200, kl = 1.10','inclusive','','0.05209','1.95','1.0'],
'mg_pp_hhj_lambda150_5f':['HH + 1 jet, pT(HH) > 200, kl = 1.50','inclusive','','0.03793','1.95','1.0'],


#DM signals Caterina Doglioni
'mg_pp_DMSimp_V_jj_gq0p25_gdm1p00_mDM0p01_mMed30p00':['30TeV DM mediator','di-jet','','1','1','1.0'],

#ADDED BY CLEMENT TO FIX PRINTER
'mg_gg_aa01j_mhcut_5f_HT_100_300':['gluon fusion di-photon + 0/1 jets','0 < HT < 500','xqcut = 20, qCut = 30','850.4','2.0','0.578'],
'mg_gg_aa01j_mhcut_5f_HT_200_10000':['gluon fusion di-photon + 0/1 jets','200 < HT < 100000','xqcut = 20, qCut = 30','0.02618','2.0','0.917'],
'mg_pp_hhj_lambda200_5f':['HH + 1 jet, pT(HH) > 200, kl = 2.00','inclusive','','0.03793','1.95','1.0'],


}


##Gridpack list for MG5@MC@NLO
##     0          1            2                 3           4           5
## description/comment/matching parameters/cross section/kfactor/matching efficiency

