import scorpy
import matplotlib.pyplot as plt


#directory where the tag will be saved
data_dir = '/home/ec2-user/algo-tute/data'
#tag for a set of algorithms
tag = 'lyso-test'


#open the algorithm handler
a = scorpy.AlgoHandler(tag=tag, path=f'{data_dir}/algo')


a.make_support_from_target(verbose=99)


sphv = scorpy.SphericalVol(path=a.sphv_supp_loose_path())


fig, axes = plt.subplots(1,1, figsize=(8/2.54, 8/2.54), dpi=150)
sphv.plot_slice(0, 290, fig=fig, axes=axes,
                title='Loose Support',ylabel='$\\theta$ [rad]', xlabel='$\\phi$ [rad]')
plt.show()












