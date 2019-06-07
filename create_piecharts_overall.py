import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib import cm
# %matplotlib inline
'''
This file creates two pie charts
One chart shows the market representation of each language 
The other chart shows the amount of listings per language on the market
The purpose is to compare the two metrics and find a correlation
'''

df4 = pd.read_pickle('dataframe4.pkl') #load dataframe4 from the directory

assert(isinstance(df4, pd.Dataframe)) # assert dataframe type 
assert('Market %' in df4.columns)
assert('Language Count' in df4.columns)
assert('Language' in df4.columns)

# assign the datasets of interest to variables
x1 = df4['Market %']
x1_new = x1[0: 10]
x1_new[len(x1)] = np.sum(x1[11:])
x2 = df4['LanguageCount']
x2_new = x2[0: 10]
x2_new[len(x2)] = np.sum(x2[11:])
y = df4['Language']
y_new = y[0: 10]
y_new[len(y)] = 'others'   # Combine the rest of the data into one

explode = [0.40,0.2,0.4] + [0]*(len(x1_new)-3) # this creates the "explode" effect on the top 3 languages 

fig1,ax1 = plt.subplots() #subplot for market %
ax1.pie(x1_new,explode = explode, labels=y_new, colors=plt.cm.Set3(np.linspace(0, 1, 12)), radius=8,shadow=True) #instantiate first pie chart
ax1.title.set_text('Market Percentage of Each Programming Language')
ax1.axis('equal') #Ensures both plots are circular

fig1,ax2 = plt.subplots() #subplot for listing count
ax2.pie(x2_new,explode = explode,labels =y_new, colors=plt.cm.Set3(np.linspace(0, 1, 12)), radius=8,shadow=True) #instantiate second pie chart
ax2.title.set_text('Popularity by Listing Count per Programming Language ')
ax2.axis('equal') #Ensures both plots are circular
