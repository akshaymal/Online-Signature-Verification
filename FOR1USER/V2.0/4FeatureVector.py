import pandas as pd
import math
import os
import glob
import ntpath
import numpy as np
import Helper

SOURCE_PATH      = Helper.getFeatureVectorInput()          #Returns path for input file
DESTINATION_PATH = Helper.getFeatureVectorOutput()	       #Returns path for output file

#os.makedirs to make directories recursively
if not os.path.exists( DESTINATION_PATH ): 
	os.makedirs( DESTINATION_PATH )

def CalculateFileList():
	l = []
	for root, dirs, files in os.walk( SOURCE_PATH ):
		for f in files:
			l = np.append(l,f)
	return l

base = Helper.getBase()
base1 = ""
person = 1
stringperson = str(person)
instance = 1
stringinstance = str(instance)
footer = ".sig"
max_no_users = int(Helper.getMaximumNoOfUsers())



def CalculateFeatureVector():
	person = 1
	instance = 1
	l = CalculateFileList();

	while ( person <= max_no_users ):
		
		outstring = []
		stringperson = str(person)
		stringinstance = str(instance)

		#Generating initial base for file ( eg. 001 )
		if ( person < 10 ):
			base1 = "00"
		elif ( person < 100 ):
			base1 = "0"
		else:
			base1 = ""
			
		final = base1 + stringperson + base + stringinstance + footer
		finalfilestring = SOURCE_PATH + "/" + final

		#print(final)

		#If file is present in filelist
		if (final in l):
			if (instance == 1):
				finalfile = np.array([])
				df = pd.read_csv(finalfilestring,sep=',', header = None, nrows = 1)
				tempfile = np.asarray(df).squeeze() 
				finalfile = np.hstack((finalfile,tempfile))
				df = ""
				tempfile = ""
				
				#print (person,instance)
				stringinstance = str(instance)
				final = base1 + stringperson + base + stringinstance + footer
				finalfilestring = SOURCE_PATH + "/" + final
				instance = instance + 1
				#print(instance + "sfsd")
			if (instance < 6 and instance!=1):
				df = pd.read_csv(finalfilestring,sep=',', header = None, nrows = 1)
				tempfile = np.asarray(df).squeeze() 
				finalfile = np.vstack((finalfile,tempfile))
				df = ""
				tempfile = ""
				#print (person,instance)
				instance = instance + 1

		else:
			if (instance == 6):	#If all the instantace of the user is done
				#print (finalfile)
				Helper.Message(person, " Creating Feature Vector")
				df_1 = pd.DataFrame(finalfile)
				temp2 = str( DESTINATION_PATH + "/" + final)
				df_1.to_csv(temp2, index=False, header=None) 
			person = person + 1
			instance = 1

CalculateFeatureVector()