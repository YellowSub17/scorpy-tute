import scorpy
import numpy as np
import matplotlib.pyplot as plt


#directory where the tag will be saved
data_dir = '/home/ec2-user/algo-tute/data'

#tag for a set of algorithms
tag = 'lyso-test'

#number of qbins in correlation fn.
nq = 300
#max and minimum q values for correlation and reciprocal space intensity fn.
qmax = 3.5
qmin = 0.0725
#number of angular sampling bins in correlation fn.
npsi = 360*32
#determines sampling of reciprocal space intensity fn.
nl = 250
#blqq harmonics are cropped to this value.
lcrop=45
#number of pixels around each bragg peak (radius of support).
dxsupp=2
#condition number of pseudo inverse for correlation fn to blqq.
pinv_rcond=0.1
#condition number of eigen vectors
eig_rcond=1e-15

#sets overwrite algo tag permissions.
#0: make new folder if it doesn't exist, otherwise dont overwrite, just load parameters
#1: prompt asking if you want to overwrite
#2: overwrite without prompt
overwrite = 1

a = scorpy.AlgoHandler(tag=tag, path=f'{data_dir}/algo',
                       nq=nq, qmax=qmax, qmin=qmin, npsi=npsi, nl=nl,
                       lcrop=lcrop, dxsupp=dxsupp, pinv_rcond=pinv_rcond, eig_rcond=eig_rcond,
                       overwrite=overwrite)








