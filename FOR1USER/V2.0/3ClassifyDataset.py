import pandas as pd
import math
import os
import glob
import ntpath
import numpy as np
import Helper

SOURCE_PATH      = Helper.getClassifyInput()           #Returns path for input file
DESTINATION_PATH = Helper.getClassifyOutput()          #Returns path for output file

#print SOURCE_PATH
#print DESTINATION_PATH

#os.makedirs to make directories recursively
if not os.path.exists( DESTINATION_PATH ): 
	os.makedirs( DESTINATION_PATH )

for root, dirs, files in os.walk( SOURCE_PATH ):
	left = len(files)
	print(left)
	for filename in files:
		#Function to display the message in terminal
		Helper.Message(left, "ClassifyingDataset")

		temp = str( SOURCE_PATH + "/" + filename)
		df = pd.read_table( temp, sep=' ', header=None )

		x = np.asarray( df[[0]] ).squeeze() 
		finalx = np.append(x, Helper.getLastbit())  #CHANGE ZERO TO ONE FOR GENUINE
		df_x = pd.DataFrame(finalx)
		
		temp = str( DESTINATION_PATH + "/" + filename )
		df_x.transpose().to_csv(temp, index=False, header=False)

		left = left - 1