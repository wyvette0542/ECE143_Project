import plotly.plotly as py
import plotly.graph_objs as go
import plotly

import pandas as pd
import numpy as np

'''
This file is used to create a heatmap that shows Java salary per state
'''

plotly.tools.set_credentials_file(username='wyvette0542', api_key='9IqIPiGXjRvppiBBZSER')   # Credentials to use plotly

df = pd.read_pickle('dataframe5.pkl')
assert(isinstance(df,pd.Dataframe))
assert('State' in df.columns)
assert('JavaMean' in df.columns)
assert('JavaMax' in df.columns)
assert('JavaMin' in df.columns)

scl = [
    [0.0, 'rgb(242,240,247)'],
    [0.2, 'rgb(218,218,235)'],
    [0.4, 'rgb(188,189,220)'],
    [0.6, 'rgb(158,154,200)'],
    [0.8, 'rgb(117,107,177)'],
    [1.0, 'rgb(84,39,143)']
]

# df['text'] creates the text that is displayed when you hover over a state
df['text'] = 'State: '+ df['State'] + '<br>'+\
    ' Mean: ' + df['JavaMean'].map(str) + ' Max: ' + df['JavaMax'].map(str) + ' Min: '+ df['JavaMin'].map(str)

# This instantiates the Chloropleth heat Map
data = [go.Choropleth(
    colorscale = scl,   # This is a template colorscale 
    autocolorscale = False, 
    locations = df['State'].str.upper(),   # This provides the key for which we can assign to the heatmap
    z=df['JavaMean'],   # Our main metric is the average salary per state
    locationmode = 'USA-states',   # This is mapping for our key
    text = df['text'],   # This displays the box text per state
    marker = go.choropleth.Marker(
        line = go.choropleth.marker.Line(
            color = 'rgb(255,255,255)',
            width = 2
        )),
    colorbar = go.choropleth.ColorBar(   # This will determine the characteristics of the colorbar
        title = "Average Salary",
       )
)]

layout = go.Layout(
    title = go.layout.Title(
        text = 'Java Mean Salary Per State'
    ),
    geo = go.layout.Geo(
        scope = 'usa',
        projection = go.layout.geo.Projection(type = 'albers usa'),
        showlakes = True,
        lakecolor = 'rgb(255, 255, 255)'),
)

fig = go.Figure(data = data, layout = layout)
print(py.iplot(fig, filename = 'd3-cloropleth-map'))
print(py.plot(fig))
