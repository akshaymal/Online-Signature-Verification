import pandas as pd
import math
import os
import glob
import ntpath
import numpy as np

base_path = '4ClassifyDataset/GENUINE/SESSION2/' #FROM FILE PATH
new_path = '5FeatureVector/GENUINE/SESSION2/'	#TO FILE PATH

l = []
for root, dirs, files in os.walk(base_path):
	for f in files:
		l = np.append(l,f)

#axis is important

base = "_2_"
base1 = ""
person = 1
stringperson = str(person)
instance = 1
stringinstance = str(instance)
footer = ".sig"
underscore = "_"

while (person<116):

	outstring = []
	stringperson = str(person)
	stringinstance = str(instance)
	if (person<10):
		base1 = "00"
	elif (person <100):
		base1 = "0"
	else:
		base1 = ""
	final = base1 + stringperson + base + stringinstance + footer
	finalfilestring = base_path + final

	if (final in l):
		if (instance == 1):
			finalfile = np.array([])
			df = pd.read_csv(finalfilestring,sep=',', header = None, nrows = 1)
			tempfile = np.asarray(df).squeeze() 
			finalfile = np.hstack((finalfile,tempfile))
			df = ""
			tempfile = ""
			instance = instance + 1
			stringinstance = str(instance)
			final = base1 + stringperson + base + stringinstance + footer
			finalfilestring = base_path + final
		if (instance<11 and instance!=1):
			df = pd.read_csv(finalfilestring,sep=',', header = None, nrows = 1)
			tempfile = np.asarray(df).squeeze() 
			finalfile = np.vstack((finalfile,tempfile))
			df = ""
			tempfile = ""
			print (person,instance)
			instance = instance + 1

	else:
		if (instance == 11):
			#print (finalfile)
			df_1 = pd.DataFrame(finalfile)
			temp2 = str(new_path+final)
			df_1.to_csv(temp2, index=False, header=None) 
		person = person + 1
		instance = 1