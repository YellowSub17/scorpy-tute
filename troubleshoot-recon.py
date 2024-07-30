

import scorpy
import numpy as np
import matplotlib.pyplot as plt



#directory where the tag will be saved
data_dir = '/home/ec2-user/algo-tute/data'
#tag for a set of algorithms
tag = 'lyso-test'

a = scorpy.AlgoHandler(tag=tag, path=f'{data_dir}/algo')


a.check_inputs()
a.load_inputs()




sphv_f =  scorpy.SphericalVol(nq = a.nq, ntheta=a.nl*2, nphi=a.nl*4, qmax=a.qmax, qmin=a.qmin)
sphv_f.vol = np.random.random(sphv_f.vol.shape)





for i in range(4):
    for j in range(5):

        sphv_i, sphv_f, _ = a.HIO(sphv_i = sphv_f)
        print(f'Running HIO: {j}')


    fig, axes = plt.subplots(1,1, sharex=True, sharey=True)
    sphv_f.plot_slice(0, -100, fig=fig, axes=axes, title=f'iter: {(i+1)*5}')



sphv_i, sphv_f, _ = a.Ps(sphv_i = sphv_f)

sphv_f.plot_slice(0, -100, fig=fig, axes=axes, title=f'Support Masked')



sphv_t =  scorpy.SphericalVol(path=a.sphv_targ_path())
sphv_t.vol[np.isnan(sphv_t.vol)] = 0
sphv_t.convolve(kern_L=2, kern_n=5, std_x=2, std_y=0.0001, std_z=2)

fig, axes = plt.subplots(1,1, sharex=True, sharey=True)
sphv_t.plot_slice(0, -100, fig=fig, axes=axes, title=f'target (convolved)')

plt.show()












