

import scorpy





#directory where the tag will be saved
data_dir = './data'
#tag for a set of algorithms
tag = 'lyso-test'


#open the algorithm handler
a = scorpy.AlgoHandler(tag=tag, path=f'{data_dir}/algo')

#check and load inputs for launch
a.check_inputs(verbose=99)
a.load_inputs(verbose=99)


#run the algoithm
recipe_path = f'{data_dir}/rec.txt'
a.run_recon(sub_tag='b', recipe=recipe_path, verbose=99)






