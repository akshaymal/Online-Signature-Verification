import pandas as pd
import math
import os
import glob
import ntpath
import numpy as np

base_path = '3InterpolatedDataset/FORGERY' #FROM FILE PATH
new_path = '4ClassifyDataset/FORGERY'	#TO FILE PATH

for root, dirs, files in os.walk(base_path):
	for f in files:
		temp = str(base_path+"/"+f)
		df = pd.read_table(temp, sep=' ',header=None )
		x = np.asarray(df[[0]]).squeeze() 
		finalx = np.append(x,0)
		df_x = pd.DataFrame(finalx)
		temp = str(new_path+"/"+f)
		df_x.transpose().to_csv(temp, index=False, header=False)