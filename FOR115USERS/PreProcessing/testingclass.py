import pandas as pd
import math
import os
import glob
import ntpath
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier

"""
random forest
bit tickling 
"""

genuine_path = '5FeatureVector/GENUINE/SESSION1/' #FROM FILE PATH
forgery_path = '5FeatureVector/FORGERY/'	#TO FILE PATH

genuinefiles = []
forgeryfiles = []
for root, dirs, files in os.walk(genuine_path):
	for f in files:
		genuinefiles = np.append(genuinefiles,f)

for root, dirs, files in os.walk(forgery_path):
	for f in files:
		forgeryfiles = np.append(forgeryfiles,f)

counter = 1
finalscore = 0

value = [0.1, 0.2, 0.5, 1.0, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5]

for v in value:
	counter=1
	finalscore=0
	while (counter<116):
		if (counter<10):
			base1 = "00"
		elif (counter <100):
			base1 = "0"
		else:
			base1 = ""

		temp1 = str(base1) + str(counter) + "_1_11.sig"
		temp2 = str(base1) + str(counter) + "_f_11.sig"
		finalgenuinepath = genuine_path + temp1
		finalforgerypath = forgery_path + temp2

		if (temp1 in genuinefiles and temp2 in forgeryfiles):
			dfgenuine = pd.read_table(finalgenuinepath, sep=',',header=None)
			dfforgery = pd.read_table(finalforgerypath, sep=',',header=None)
			df_X = dfgenuine.append(dfforgery)
			df_Y = df_X[[515]]
			del df_X[515] 
			df_Y = np.asarray(df_Y).squeeze()

			X_train, X_test, Y_train, Y_test = train_test_split(df_X, df_Y, test_size=0.3, random_state=1)
			#clf = MLPClassifier(solver='lbfgs', alpha=0.01, random_state=1, verbose=1, hidden_layer_sizes=(256, 128, 64)).fit(X_train, Y_train)
			clf = svm.SVC(kernel='poly', C=v).fit(X_train, Y_train)
			score = clf.score(X_test, Y_test)
			finalscore = finalscore + score	

			df_X = ""
			df_Y = ""
		counter = counter + 1

	length = len(genuinefiles)
	print (v)
	print (finalscore/length)