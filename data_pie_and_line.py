import numpy as np
import pandas as pd 
%matplotlib inline

'''
This file will create a database that we will use to compare languageCount vs. the market% that a language represents

Input: Pandas Dataframe
Output: Pandas Dataframe
'''

df2 = pd.read_pickle('dataframe2.pkl') #import pickled dataframe

grp1 = df2.groupby(df2.Language) #group by state
languagelist = grp1.Language.unique() #create a list of the unique languages

totalSalary = df2.Salary.sum() #sum the total salary across all listings

langSalary = [] #stores each language's salary
langCount  = [] #stores each language's count

for lang in languagelist:	#iterate through the list of languages to populate langSalary and langCount
	dfLang = grp1.get_group(lang[0])  #pick sample state

	langCount.append(dfLang.Language.count())
	langProp = (dfLang.Salary.sum() / totalSalary) 
	langSalary.append(langProp)


sumLang = sum(langCount) #sum up the languageCounts in order to normalize the language count 
langProp = langCount/sumLang #normalize the language count

diff = langSalary-langProp


df4 = pd.DataFrame(columns = ['Language', 'Market %','LanguageCount', 'Diff']) #store the lists in a dataframe
df4.Language = languagelist.index #Market% and LanguageCount match up with the index of dataframe4


df4['Market %'] = langSalary 
df4['LanguageCount'] = langProp
df4['Diff'] = diff 

#df4 = df4.sort_values(by=['Market %'],ascending=False) #Sort by highest market % in order to have a more meaningful pie chart
df4.to_pickle('dataframe4.pkl') #pickle the dataframe




