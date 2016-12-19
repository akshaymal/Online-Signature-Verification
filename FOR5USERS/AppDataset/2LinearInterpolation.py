import math
import os
import glob
import ntpath
import numpy as np
from RDP import rdp
import pandas as pd
import scipy.interpolate
from sklearn.preprocessing import MinMaxScaler

base_path = 'FilteredDataset/FORGERY' #FROM FILE PATH
new_path = 'InterpolatedDataset/FORGERY'	#TO FILE PATH

for root, dirs, files in os.walk(base_path):
	for f in files:
		temp = str(base_path+"/"+f)
		df = pd.read_table(temp, sep=' ',skiprows=[1],header=None )
		maxx = int (df[[0]].max())
		maxy = int (df[[1]].max())
		minx = int (df[[0]].min())
		miny = int (df[[1]].min())

		check = 0
		penx = 0
		peny = 0
		for i in range(0, df.shape[0]):
			if ((df.iloc[i][4]) == 1):
				check = 1
				penx = np.asarray(df.iloc[i][0])
				peny = np.asarray(df.iloc[i][1])
				break

		x = np.asarray(df[[0]]).squeeze() 									#COLUMNS TO ARRAYS
		y = np.asarray(df[[1]]).squeeze()

		y_interp = scipy.interpolate.interp1d(x, y)
		equalxvalues = np.linspace(minx+1, maxx, num=256) 					#INTERPOLATING DATA AND FIND 256 POINTS
		equalyvalues = np.asarray([y_interp(equalxvalues)]).squeeze()

		finalxvalues = np.floor(equalxvalues) 								#FLOORING ALL THE FLOAT VALUES
		finalxvalues = finalxvalues.astype(int)
		finalyvalues = np.floor(equalyvalues)
		finalyvalues = finalyvalues.astype(int)

		newmaxxvalue = np.amax(finalxvalues)								#FINDING NEW MAX AND MIN OF X & Y AFTER GETTING 256 POINTS
		newminxvalue = np.amin(finalxvalues)								
		newmaxyvalue = np.amax(finalyvalues)
		newminyvalue = np.amin(finalyvalues)

		differ_x = (newmaxxvalue + newminxvalue)/2							#COORDINATE NORMALIZATION
		differ_y = (newmaxyvalue + newminyvalue)/2
		finalxvalues = np.subtract(finalxvalues, differ_x)
		finalyvalues = np.subtract(finalxvalues, differ_y) 

		if (check == 1):
			penx = np.subtract(penx, differ_x) 
			peny = np.subtract(peny, differ_y) 

			finalxvalues = np.append(finalxvalues,penx)
			finalyvalues = np.append(finalyvalues,peny)

			mms = MinMaxScaler()
			scaledX = mms.fit_transform(finalxvalues.reshape(257,1))			#SIZE NORMALIZATION - SCALING
			scaledY = mms.fit_transform(finalyvalues.reshape(257,1))
		else:
			mms = MinMaxScaler()
			scaledX = mms.fit_transform(finalxvalues.reshape(256,1))			#SIZE NORMALIZATION - SCALING
			scaledY = mms.fit_transform(finalyvalues.reshape(256,1))
			scaledX = np.append(scaledX,0)
			scaledY = np.append(scaledY,0)


		features1 = np.append (scaledX,scaledY)

		df = pd.DataFrame(features1)
		temp2 = str(new_path+"/"+f)
		df.to_csv(temp2, ' ', index=False, header=None) 
