

import scorpy

#directory where the tag will be saved
data_dir = '/home/ec2-user/algo-tute/data'
#tag for a set of algorithms
tag = 'lyso-test'


#open the algorithm handler
a = scorpy.AlgoHandler(tag=tag, path=f'{data_dir}/algo')




a.check_inputs()
a.load_inputs()


recipe_path = f'{data_dir}/recipe.txt'
sphv_init = scorpy.SphericalVol(path=a.sphv_final_path('a'))
a.run_recon(sub_tag='b', recipe=recipe_path, sphv_init=sphv_init, verbose=99)









