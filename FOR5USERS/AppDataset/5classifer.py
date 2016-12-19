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
from sklearn import svm, datasets
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt


"""
random forest
bit tickling 
"""

genuine_path = 'FeatureVector/GENUINE/SESSION1/' #FROM FILE PATH
forgery_path = 'FeatureVector/FORGERY/'	#TO FILE PATH

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
finalfirst1 = 0
finalfirst2 = 0
finalsecond1 = 0
finalsecond2 = 0
finalcm = np.matrix('0 0; 0 0')

while (counter<116):
	if (counter<10):
		base1 = "00"
	elif (counter <100):
		base1 = "0"
	else:
		base1 = ""

	temp1 = str(base1) + str(counter) + "_1_11.sig"
	temp2 = str(base1) + str(counter) + "_f_1.sig"
	finalgenuinepath = genuine_path + temp1
	finalforgerypath = forgery_path + temp2

	if (temp1 in genuinefiles and temp2 in forgeryfiles):
		dfgenuine = pd.read_table(finalgenuinepath, sep=',',header=None)
		dfforgery = pd.read_table(finalforgerypath, sep=',',header=None)
		df_X = dfgenuine.append(dfforgery)
		df_Y = df_X[[514]]
		del df_X[514] 
		df_Y = np.asarray(df_Y).squeeze()

		X_train, X_test, Y_train, Y_test = train_test_split(df_X, df_Y, test_size=0.3, random_state=1)
		svr = SVC()
		tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4], 'C': [1, 10, 100, 1000]},{'kernel': ['poly'], 'gamma': [1e-3, 1e-4], 'C': [1,10, 100, 1000]}]
		clf = GridSearchCV(svr, tuned_parameters)
		clf.fit(X_train, Y_train)
		#print (clf.get_params)
		#print (clf.best_params_)
		score = clf.score(X_test, Y_test)
		preds = clf.predict(X_test)
		print ("Correct Results")
		print (Y_test)
		print ("Predicted Results")
		print (preds)
		finalscore = finalscore + score	
		print("for " + temp1 + " " +str(score) )

		df_X = ""
		df_Y = ""

		# Show confusion matrix in a separate window
		cm = confusion_matrix(Y_test, preds)
		finalcm = finalcm + cm

		first1 = cm.item(0)
		first2 = cm.item(1)
		second1 = cm.item(2)
		second2 = cm.item(3)

		finalfirst1 = finalfirst1 + first1
		finalfirst2 = finalfirst2 + first2
		finalsecond1 = finalsecond1 + second1
		finalsecond2 = finalsecond2 + second2
		
		'''
		plt.matshow(cm)
		plt.title('Confusion matrix')
		plt.colorbar()
		plt.ylabel('True label')
		plt.xlabel('Predicted label')
		plt.show()
		'''
	counter = counter + 1

length = len(genuinefiles)
print ((finalscore/length) *100 )
print (finalfirst1)
print (finalfirst2)
print (finalsecond1)
print (finalsecond2)
print (finalcm)
#finalcm = np.matrix('276 48; 69 297')
plt.matshow(finalcm)
plt.title('Confusion matrix')
plt.colorbar()
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.show()
"""
dfgenuine = pd.read_table(genuine_path, sep=',',header=None)
dfforgery = pd.read_table(forgery_path, sep=',',header=None)

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
