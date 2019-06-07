import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib import cm
'''
This file creates the pie chart showing the amount of internship listings per language on the market

'''

intern_data = np.load('internshipPopularity.npy', allow_pickle=True)
intern_data = intern_data[()]   # Convert to a dictionary
languages = intern_data.keys()
count = intern_data.values()

# Store values into a Dataframe
df = pd.DataFrame()
df['languages'] = languages
df['count'] = count
df = df.sort_values('count', ascending = False)

lan = df['languages']
x1_new = lan[0: 10]
x1_new[len(lan)] = 'others'
c = df['count']
x2_new = c[0: 10]
x2_new[len(c)] = np.sum(c[11:])   # Combine the rest of the data into one

explode = [0.40,0.2,0.4] + [0]*(len(x1_new)-3) # this creates the "explode" effect on the top 3 languages 
colors = plt.cm.Set3(np.linspace(0, 1, 12))
# Reorder color map so each languague has the same color as in the other pie charts
elements = [1, 0, 2, 3, 6, 5, 9, 8, 7, 4, 10, 11]   
colors_new = [colors[i] for i in elements]

plt.pie(x2_new,explode = explode, labels=x1_new, colors=colors_new, radius=8,shadow=True) # instantiate first pie chart
plt.title('Internship Popularity')
plt.axis('equal') # Ensures both plots are circular