#coding:utf-8
__author__ = 'similarface'

BASEURL='http://www.ncbi.nlm.nih.gov/clinvar/?term='

BASEURLBENGIN='http://clinvitae.invitae.com/#q='
BASEURLEND='&f=&source=ARUP,Carver,ClinVar,EmvClass,Invitae,kConFab&classification=1,2,3,4,5,6'

GENARRAY=['APC','ATM','BRCA1','BRCA2','CDH1','CDKN2A','EPCAM','FANCC','MEN1','MLH1','MSH2','MSH6','MUTYH','PALB2','PMS2','PTEN','STK11','TP53','VHL']
GENARRAYNEW=['AKT1','APC','ATM','AXIN2','BAP1','BARD1','BLM','BMPR1A','BRCA1','BRCA2','BRIP1','BUB1B','CDC73','CDH1','CDK4','CDKN2A','CHEK2','CTNNA1','CTRC','DICER1','EGLN1','ENG','EPCAM','FAM175A','FANCC','FH','FLCN','GALNT12','GREM1','KIF1B','KIT','MAX','MEN1','MET','MLH1','MLH3','MRE11A','MSH2','MSH6','MUTYH','NBN','NF1','PALB2','PALLD','PDGFRA','PIK3CA','PMS2','POLD1','POLE','PTCH1','PTEN','RAD50','RAD51C','RAD51D','RET','RINT1','SDHA','SDHAF2','SDHB','SDHC','SDHD','SMAD4','SMARCA4','SMARCB1','SPINK1','SPRED1','STK11','TMEM127','TP53','TSC1','TSC2','VHL','XRCC2']


#GENARRAY=['RINT1' CTNNA1]
i=0
for gen in list(set(GENARRAYNEW) ^ set(GENARRAY)):
    i=i+1
    print(i)
    print(BASEURLBENGIN+gen+BASEURLEND)
'''
i=0
for gen in GENARRAY:

    i=i+1
    print(i)
    print(BASEURLBENGIN+gen+BASEURLEND)

'''

