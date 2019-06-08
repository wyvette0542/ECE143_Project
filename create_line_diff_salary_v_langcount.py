import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib
import sys
from matplotlib.pylab import gca
'''
This file creates two pie charts
One chart shows the market representation of each language 
The other chart shows the amount of listings per language on the market
The purpose is to compare the two metrics and find a correlation
'''

df4 = pd.read_pickle('dataframe4.pkl') #load dataframe4 from the directory

#assign the datasets of interest to variables
df4 = df4.sort_values(by=['Diff'],ascending=False)

maxvalue = abs(df4.Diff).max()
y = 100*(df4.Diff / maxvalue)
x = df4.Language



#y[11:] = '' #Only show the labels for y[0:11]

#explode = [0.40,0.2,0.4] + [0]*(len(x1)-3) #this creates the "explode" effect on the top 3 languages 

fig,ax = plt.subplots() #subplot for market %
line,= plt.plot(x,y, 'r-o',linewidth=4) #instantiate first pie chart

ax.set_title(r'Difference Between Market% and Listing%')
ax.set_xlabel('Languages')
ax.set_ylabel(r'Difference Percentage')

plt.setp(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
# plt.xticks(rotation=60)
plt.tick_params(axis='x',which='major',labelsize=6)
plt.tick_params(axis='y',which='major',labelsize=6)

plt.subplots_adjust(bottom=0.15)

annot = ax.annotate("", xy=(0,0), xytext=(-20,20),textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

def update_annot(ind):
    x,y = line.get_data()
    annot.xy = (x[ind["ind"][0]], y[ind["ind"][0]])
    text = "{}, {}".format(" ".join(list(map(str,ind["ind"]))), 
                           " ".join([x[n] for n in ind["ind"]]))
    annot.set_text(text)
    annot.get_bbox_patch().set_alpha(0.4)


def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        cont, ind = line.contains(event)
        if cont:
            update_annot(ind)
            annot.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annot.set_visible(False)
                fig.canvas.draw_idle()

fig.canvas.mpl_connect("motion_notify_event", hover)

plt.show()