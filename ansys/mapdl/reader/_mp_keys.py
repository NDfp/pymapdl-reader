"""Contains material property indices

Obtained from:
/usr/ansys_inc/v212/ansys/customize/include/mpcom.inc

c        ---- MP command labels --------
c        EX  = 1, EY  = 2, EZ  = 3, NUXY= 4, NUYZ= 5, NUXZ= 6, GXY = 7, GYZ = 8,
c        GXZ = 9, ALPX=10, ALPY=11, ALPZ=12, DENS=13, MU  =14, DAMP=15, KXX =16,
c        KYY =17, KZZ =18, RSVX=19, RSVY=20, RSVZ=21, C   =22, HF  =23, VISC=24,
c        EMIS=25, ENTH=26, LSST=27, PRXY=28, PRYZ=29, PRXZ=30, MURX=31, MURY=32,
c        MURZ=33, PERX=34, PERY=35, PERZ=36, MGXX=37, MGYY=38, MGZZ=39, EGXX=40,
c        EGYY=41, EGZZ=42, SBKX=43, SBKY=44, SBKZ=45, SONC=46, DMPS=47, ELIM=48,
c        USR1=49, USR2=50, USR3=51, USR4=52, FLUI=53, ORTH=54, CABL=55, RIGI=56,
c        HGLS=57, BVIS=58, QRAT=59, REFT=60, CTEX=61, CTEY=62, CTEZ=63, THSX=64,
c        THSY=65, THSZ=66, DMPR=67, LSSM=68, BETD=69, ALPD=70, RH  =71, DXX =72,
c        DYY =73, DZZ =74, BETX=75, BETY=76, BETZ=77, CSAT=78, CREF=79, CVH =80

These indices are used when reading in results using ptrMAT from a
binary result file.
"""

# order is critical here
mp_keys = ['EX', 'EY', 'EZ', 'NUXY', 'NUYZ', 'NUXZ', 'GXY', 'GYZ',
           'GXZ', 'ALPX', 'ALPY', 'ALPZ', 'DENS', 'MU', 'DAMP', 'KXX',
           'KYY', 'KZZ', 'RSVX', 'RSVY', 'RSVZ', 'C', 'HF', 'VISC',
           'EMIS', 'ENTH', 'LSST', 'PRXY', 'PRYZ', 'PRXZ', 'MURX',
           'MURY', 'MURZ', 'PERX', 'PERY', 'PERZ', 'MGXX', 'MGYY',
           'MGZZ', 'EGXX', 'EGYY', 'EGZZ', 'SBKX', 'SBKY', 'SBKZ',
           'SONC', 'SLIM', 'ELIM', 'USR1', 'USR2', 'USR3', 'USR4',
           'FLUI', 'ORTH', 'CABL', 'RIGI', 'HGLS', 'BVIS', 'QRAT',
           'REFT', 'CTEX', 'CTEY', 'CTEZ', 'THSX', 'THSY', 'THSZ',
           'DMPR', 'LSSM', 'BETD', 'ALPD', 'RH', 'DXX', 'DYY', 'DZZ',
           'BETX', 'BETY', 'BETZ', 'CSAT', 'CREF', 'CVH']
