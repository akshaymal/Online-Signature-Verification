def HelperFunction(i):
	data = ""
	count = 0
	f = open("Constants.txt", "r")
	for line in f:
		data = line.split(" ")
		if( count == i ):
			break
		count += 1
	f.close()
	return data[0]

def getFilterInput():
	return HelperFunction(0)

def getFilterOutput():
	return HelperFunction(1)

def getInterpolateInput():
	return HelperFunction(1)

def getInterpolateOutput():
	return HelperFunction(2)

def getClassifyInput():
	return HelperFunction(2)

def getClassifyOutput():
	return HelperFunction(3)

def getFeatureVectorInput():
	return HelperFunction(3)

def getFeatureVectorOutput():
	return HelperFunction(4)

def getGenuineFeatureVector():
	return HelperFunction(6)

def getForgeryFeatureVector():
	return HelperFunction(5)

def getMaximumNoOfUsers():
	return HelperFunction(7)

def getBase():
	return HelperFunction(8)

def getLastbit():
	return HelperFunction(9)

	
def Message(left, string):
	if( left > 1):
		#print (left)
		print( str(left) + " Files are left for " + string)
	else:
		#print (left)
		print( str(left) + " File is left for " + string)

'''
print getFilterGenuineDataset()
print getFilterForgeryDataset()
print saveFilterGenuine()
print saveFilterForgery()
print saveInterpolateGenuine()
print saveInterpolateForgery()
print saveClassifyGenuine()
print saveClassifyForgery()
print saveFeatureVectorGenuine()
print saveFeatureVectorForgery()
'''