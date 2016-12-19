import pandas as pd
import math
import os
import glob
import ntpath
import numpy as np
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
import Helper

"""
random forest
bit tickling 
"""

GENUINE_PATH = Helper.getGenuineFeatureVector()        #Returns path for input file
FORGERY_PATH = Helper.getForgeryFeatureVector()	       #Returns path for output file

genuinefiles = []
forgeryfiles = []
for root, dirs, files in os.walk(GENUINE_PATH):
	for f in files:
		genuinefiles = np.append(genuinefiles,f)

for root, dirs, files in os.walk(FORGERY_PATH):
	for f in files:
		forgeryfiles = np.append(forgeryfiles,f)


def Classifier(k, g, c):
	finalscore = 0
	counter = 1
	max_no_of_users = int(Helper.getMaximumNoOfUsers())

	while ( counter <= max_no_of_users ):
		#Function to display the message in terminal
		#Helper.Message(counter, "ClassifyingDataset")

		if (counter<10):
			base1 = "00"
		elif (counter <100):
			base1 = "0"
		else:
			base1 = ""

		temp1 = str(base1) + str(counter) + "_1_11.sig"
		temp2 = str(base1) + str(counter) + "_f_11.sig"

		finalgenuinepath = GENUINE_PATH + "/" + temp1
		finalforgerypath = FORGERY_PATH + "/" + temp2
		#print (finalforgerypath)
		#print (finalgenuinepath)
		
		#print finalgenuinepath, finalforgerypath

		if (temp1 in genuinefiles and temp2 in forgeryfiles):
			dfgenuine = pd.read_table(finalgenuinepath, sep=',',header=None)
			dfforgery = pd.read_table(finalforgerypath, sep=',',header=None)
			df_X = dfgenuine.append(dfforgery)
			df_Y = df_X[[516]]
			del df_X[516] 
			
			df_Y = np.asarray(df_Y).squeeze()
			#print df_Y.shape
			#break
			X_train, X_test, Y_train, Y_test = train_test_split(df_X, df_Y, test_size=0.3, random_state=1)
			svr = SVC()
			#tuned_parameters = [{'kernel': ['poly'], 'gamma': [1e-3, 1e-4], 'C': [1, 10, 100, 1000]}]
			#clf = GridSearchCV(svr, tuned_parameters)
			clf = svm.SVC(kernel=k, gamma=g, C=c)
			clf.fit(X_train, Y_train)
			#print (clf.get_params)
			#print (clf.best_params_)
			score = clf.score(X_test, Y_test)
			#preds = clf.predict(X_test)
			#print ("Correct Results")
			#print (Y_test)
			#print ("Predicted Results")
			#print (preds)
			finalscore = finalscore + score	

			df_X = ""
			df_Y = ""
		
		counter = counter + 1

	length = len(genuinefiles)
	#print (finalscore/length)
	return (finalscore/length)

#Classifier()

def GRID_SEARCH():
	
	ker = ['rbf', 'poly']

	gamma = 0.001
	Ingamma = 0.001
	MAXGAMMA = 1.5

	C = 0.1
	InC = 0.01
	MAXC = 500

	ChoosenGamma = 0.0001
	ChoosenC = 0.1
	ChoosenKernal = 'rbf'

	Accuracy = 0.0

	outputfile = open("GRID_TEST1.txt", "w")

	for k in ker:
		while ( gamma <= MAXGAMMA ):
			C = 0.1
			while ( C <= MAXC ):
				A = Classifier(k, gamma, C)
				print ("For kernel: " + k + " gamma:" + str(gamma) + " C:" + str(C) + " Accuracy:" + str(A) + " MaxAccuracytillnow:" + str(Accuracy))
				outputfile.write("For kernel: " + k + " gamma:" + str(gamma) + " C:" + str(C) + " Accuracy:" + str(A) + " MaxAccuracytillnow:" + str(Accuracy) + "\n")

				if( A > Accuracy ):
					Accuracy = A
					ChoosenC = C
					ChoosenGamma = gamma
					ChoosenKernal = k
				C = C + InC
			gamma = gamma + Ingamma

	outputfile.write("Selected kernel:" + ChoosenKernal + "  ChoosenGamma" + str(ChoosenGamma) + "  ChoosenC:" + str(ChoosenC) + " MaxAccuracy:" + str(Accuracy))
	outputfile.close()

GRID_SEARCH()
"""
dfgenuine = pd.read_table(GENUINE_PATH, sep=',',header=None)
dfforgery = pd.read_table(FORGERY_PATH, sep=',',header=None)

df_X = dfgenuine.append(dfforgery)

df_Y = df_X[[515]]

del df_X[515] 

df_Y = np.asarray(df_Y).squeeze()
print (df_Y.shape)



X_train, X_test, Y_train, Y_test = train_test_split(df_X, df_Y, test_size=0.6, random_state=1)
"""
#NEURAL NET
"""clf = MLPClassifier(solver='lbfgs', alpha=0.001, random_state=1, hidden_layer_sizes=(256, 128, 64)).fit(X_train, Y_train)
score = clf.score(X_test, Y_test)"""

#RANDOM FOREST
"""clf = RandomForestClassifier(n_estimators=500 ,verbose = 1).fit(X_train, Y_train)
score = clf.score(X_test, Y_test)"""

#SUPPORT VECTOR MACHINE
#clf = svm.SVC(kernel='rbf', C=1).fit(X_train, Y_train)
#score = clf.score(X_test, Y_test)




#print (score)
