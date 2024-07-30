

import scorpy
import matplotlib.pyplot as plt




#directory where the tag will be saved
data_dir = '/home/ec2-user/algo-tute/data'
#tag for a set of algorithms
tag = 'lyso-test'


#open the algorithm handler
a = scorpy.AlgoHandler(tag=tag, path=f'{data_dir}/algo')

sphv_targ = scorpy.SphericalVol(path=a.sphv_targ_path())
sphv_init = scorpy.SphericalVol(path=a.sphv_init_path('a'))
sphv_a_final = scorpy.SphericalVol(path = a.sphv_final_path('a'))
sphv_b_final = scorpy.SphericalVol(path = a.sphv_final_path('b'))

fig, axes = plt.subplots(2,2, sharex=True, sharey=True)
sphv_init.plot_slice(0, -10, fig=fig, axes=axes[0,0])
sphv_a_final.plot_slice(0, -10, fig=fig, axes=axes[0,1])
sphv_b_final.plot_slice(0, -10, fig=fig, axes=axes[1,0])
sphv_targ.plot_slice(0, -10, fig=fig, axes=axes[1,1])


plt.show()









