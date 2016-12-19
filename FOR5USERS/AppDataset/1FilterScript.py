from RDP import rdp
import pandas as pd
import math
import os
import glob
import ntpath
import numpy as np

base_path = 'Dataset/VisualSubCorpus/FORGERY' #FROM FILE PATH
new_path = 'FilteredDataset/FORGERY'	#TO FILE PATH
i = 0
for root, dirs, files in os.walk(base_path):
	for f in files:
		temp = str(base_path+"/"+f)
		df = pd.read_table(temp, sep=' ',skiprows=[1] )
		l = []
		for i in range(0, df.shape[0]):
			l.append((df.ix[i, 'X,'], df.ix[i, 'Y,'],  df.ix[i, 'TStamp,'], df.ix[i, 'Pres.,'], df.ix[i, 'EndPts'] ))

		final = rdp(l, 1.0)
		print (f)
		df = pd.DataFrame(final)
		temp2 = str(new_path+"/"+f)
		print (temp2)
		df.to_csv(temp2, ' ', index=False, header=None) 


