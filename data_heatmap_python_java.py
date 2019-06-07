import numpy as np
import pandas as pd 
from scipy import stats 
'''
This file creates dataframe3
Dataframe 3 is used to create the heatmap comparing states vs. language vs. salary
The file extracts maximum, minimum, and mean salary values per state for the highest and lowest paying languages

'''

np.seterr(divide='ignore',invalid='ignore')
totalStats = np.empty([1,10])

df2 = pd.read_pickle('dataframe2.pkl')

grp1 = df2.groupby(df2.States) #group by state
statelist = grp1.States.unique() #create a list of unique states in our dataset

for state in statelist: #iterate through our unique states to find meaningful data within each state dataset 
	#print(state[0])
	dfState = grp1.get_group(state[0])  #the state variable is extracted as a list so choose the variable within the list 
	grp2 = dfState.groupby('Language') #group the initial grouping,grp1, by a new grouping by Language #This allows us to divide unique languages in each state


	# langmean = grp2.Salary.mean() #take the mean of each language per state
	# langmean = langmean[(np.abs(stats.zscore(langmean)) < 3)] #filter out outliers that have zscore higher than 3 #removes outliers from dataset
	

	#the try except loop accounts for states that are underrepresented and have too low of a listing count to provide good data
	try: #if there is enough data in a state's dataset
		#this data is per state
		langPython  = 'python' #find max average language
		langPythonInfo= grp2.get_group(langPython) #pull the group of the max language
		langPythonMean  = int(langPythonInfo.Salary.mean())	#mean of the highest paying language
		langPythonMin   =    int(langPythonInfo.Salary.min()) #Minimum of the highest paying language
		langPythonMax   =    int(langPythonInfo.Salary.max()) #maximum of the highest paying language
		langMean     = int((langPythonMean+langJavaMean) / 2) #mean between the highest and lowest paying languages
	except:
		print('Insufficient Data for {0} for {1}'.format(state[0],langPython)) 
		langPython = 'python'
		langPythonMean  = 'NA'
		langPythonMin   = 'NA'
		langPythonMax   = 'NA'

	try:
		langJava  = 'java' #find min average language
		langJavaInfo= grp2.get_group(langJava) #pull the group of the min language
		langJavaMean  =	int(langJavaInfo.Salary.mean()) # mean of the lowest paying language
		langJavaMin   =int(langJavaInfo.Salary.min()) #low of the lowest paying language
		langJavaMax   =int(langJavaInfo.Salary.max()) #max of the lowest paying language

	except: #this except statement accounts for states that are underrepresented

		print('Insufficient Data for {0} for {1}'.format(state[0],langJava))
		langJava  = 'java'
		langJavaMean  =	'NA'
		langJavaMin   =	'NA'
		langJavaMax   =	'NA'

	try:
		langMean = int((langPythonMean + langJavaMean)/2)
	except:
		if(isinstance(langJavaMean,int)):
			langMean = langJavaMean
		elif(isinstance(langPythonMean,int)):
			langMean = langPythonMean
		else:
			langMean = 0

	langStats = np.array([state[0], langPython, langPythonMean, langPythonMin , langPythonMax,langJava,langJavaMean ,langJavaMin ,langJavaMax,langMean]) #put statistics into an array
	totalStats = np.vstack((totalStats,langStats)) #stack the langStats array that is generated from each individual state

df5 = pd.DataFrame( data = totalStats[1:,:],columns = ['State', 'PythonName','PythonMean','PythonMin','PythonMax','JavaName','JavaMean','JavaMin','JavaMax','Mean']) #create dataframe
df5.to_pickle('dataframe5.pkl') #pickledataframe
