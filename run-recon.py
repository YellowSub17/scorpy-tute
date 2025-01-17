

import scorpy





#directory where the tag will be saved
data_dir = '/home/ec2-user/algo-tute/data'
#tag for a set of algorithms
tag = 'lyso-test'


#open the algorithm handler
a = scorpy.AlgoHandler(tag=tag, path=f'{data_dir}/algo')

#check and load inputs for launch
a.check_inputs(verbose=99)
a.load_inputs(verbose=99)


#run the algoithm
recipe_path = f'{data_dir}/recipe.txt'
a.run_recon(sub_tag='a', recipe=recipe_path, verbose=99)






