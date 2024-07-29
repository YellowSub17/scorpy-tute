
import scorpy
import numpy as np
import matplotlib.pyplot as plt


#directory where the tag will be saved
data_dir = '/home/ec2-user/algo-tute/data'
#tag for a set of algorithms
tag = 'lyso-test'
# cif file to generate target intensity
cif_path = f'{data_dir}/lysozyme-sf.cif'


#open the algorithm handler
a = scorpy.AlgoHandler(tag=tag, path=f'{data_dir}/algo')
#Make the target intensity files.
a.make_targets(cif_path)

#Plot the target intensites
sphv = scorpy.SphericalVol(path=a.sphv_targ_path())
sphv.vol *= 1e-5
fig, ax = plt.subplots(1,2, figsize = (16/2.54, 8/2.54), dpi=150, sharex=True, sharey=True)
sphv.plot_slice(0, 150,fig=fig, axes=ax[0],
                title='Target intensity',ylabel='$\\theta$ [rad]', xlabel='$\\phi$ [rad]')
sphv.vol[np.isnan(sphv.vol)] = 0
sphv.convolve(kern_L=2, kern_n=9, std_x=1, std_y=1, std_z=1)
sphv.plot_slice(0, 150, fig=fig, axes=ax[1],
                title='Target intensity (convolved)',ylabel='$\\theta$ [rad]', xlabel='$\\phi$ [rad]')
plt.show()
















