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

assert(isinstance(df2,pd.Dataframe))
assert('States' in df2)
assert('Language' in df2)
assert('Salary' in df2)

grp1 = df2.groupby(df2.States) #group by state
statelist = grp1.States.unique() #create a list of unique states in our dataset

for state in statelist: #iterate through our unique states to find meaningful data within each state dataset 
	#print(state[0])
	dfState = grp1.get_group(state[0])  #the state variable is extracted as a list so choose the variable within the list 
	grp2 = dfState.groupby('Language') #group the initial grouping,grp1, by a new grouping by Language #This allows us to divide unique languages in each state


	langmean = grp2.Salary.mean() #take the mean of each language per state
	langmean = langmean[(np.abs(stats.zscore(langmean)) < 3)] #filter out outliers that have zscore higher than 3 #removes outliers from dataset
	

	#the try except loop accounts for states that are underrepresented and have too low of a listing count to provide good data
	try: #if there is enough data in a state's dataset
		#this data is per state
		langMax  = langmean.idxmax() #find max average language
		langMin  = langmean.idxmin() #find min average language
		langMaxInfo= grp2.get_group(langMax) #pull the group of the max language
		langMinInfo= grp2.get_group(langMin) #pull the group of the min language
		langMaxMean  = int(langMaxInfo.Salary.mean())	#mean of the highest paying language
		langMaxMin   =    int(langMaxInfo.Salary.min()) #Minimum of the highest paying language
		langMaxMax   =    int(langMaxInfo.Salary.max()) #maximum of the highest paying language
		langMinMean  =	int(langMinInfo.Salary.mean()) # mean of the lowest paying language
		langMinMin   =int(langMinInfo.Salary.min()) #low of the lowest paying language
		langMinMax   =int(langMinInfo.Salary.max()) #max of the lowest paying language
		langMean     = int((langMaxMean+langMinMean) / 2) #mean between the highest and lowest paying languages
	except: #this except statement accounts for states that are underrepresented

		print('Insufficient Data for {0}'.format(state[0])) 
		langMax = grp1.get_group(state[0]).Language.get_values()
		langMin  = 'NA'
		langMaxInfo= grp1.get_group(state[0]) #pull the group of the max language
		langMaxMean  = int(langMaxInfo.Salary.mean())
		langMaxMin   = langMaxMean
		langMaxMax   = langMaxMean
		langMinMean  =	'NA'
		langMinMin   =	'NA'
		langMinMax   =	'NA'
		langMean = langMaxMean
	langStats = np.array([state[0], langMax, langMaxMean, langMaxMin , langMaxMax,langMin,langMinMean ,langMinMin ,langMinMax,langMean]) #put statistics into an array
	totalStats = np.vstack((totalStats,langStats)) #stack the langStats array that is generated from each individual state

df3 = pd.DataFrame( data = totalStats[1:,:],columns = ['State', 'MaxName','MaxMean','MaxMin','MaxMax','MinName','MinMean','MinMin','MinMax','Mean']) #create dataframe
df3.to_pickle('dataframe3.pkl') #pickledataframe
