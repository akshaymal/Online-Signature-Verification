from RDP import rdp
import pandas as pd
import math
import os
import glob
import ntpath
import numpy as np
import Helper

SOURCE_PATH       = Helper.getFilterInput()        #Returns path for input file
DESTINATION_PATH  = Helper.getFilterOutput()       #Returns path for output file

#os.makedirs to make directories recursively
if not os.path.exists(DESTINATION_PATH): 
	os.makedirs(DESTINATION_PATH)    

#Filter the dataset using RDP algorithm
def FilterData():
	#Recurse through all the files in the SOURCE_PATH
	for root, dirs, files in os.walk(SOURCE_PATH):
		left = len(files)
		for filename in files:
			#Function to display the message in terminal
			Helper.Message(left, "Filtering")
			
			temp = str( SOURCE_PATH + "/" + filename)		        #Making the path for file
			df = pd.read_table(temp, sep=' ',skiprows=[1] ) #First 2 rows is skip; First two rows are header
			
			l = []
			for i in range(0, df.shape[0]):
				l.append((df.ix[i, 'X,'], df.ix[i, 'Y,'],  df.ix[i, 'TStamp,'], df.ix[i, 'Pres.,'], df.ix[i, 'EndPts'] ))

			#rdp function will reduce points in the signature
			finalpoints = rdp(l, 1.0)
			df = pd.DataFrame(finalpoints)
			temp2 = str( DESTINATION_PATH + "/" + filename )	#Path for the destination file
			df.to_csv(temp2, ' ', index=False, header=None) 
			left = left - 1
			
FilterData()
