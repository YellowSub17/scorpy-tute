

import scorpy
import matplotlib.pyplot as plt
import numpy as np

#directory where the tag will be saved
data_dir = './data'
#tag for a set of algorithms
tag = 'lyso-test'


#open the algorithm handler
a = scorpy.AlgoHandler(tag=tag, path=f'{data_dir}/algo')


a.make_data_from_target(verbose=99, save_corr=True, corr_nchunks=32)


blqq = scorpy.BlqqVol(path=a.blqq_data_path())
blqq.plot_q1q2(title='Blqq', ylabel='$q_1=q_2$[\u212b$^{-1}]', xlabel='L')

corr = scorpy.CorrelationVol(path=a.corr_data_path())
corr.plot_q1q2(title='Corr', ylabel='$q_1=q_2$[\u212b$^{-1}]', xlabel='$\\Delta \\Psi$')
plt.show()









