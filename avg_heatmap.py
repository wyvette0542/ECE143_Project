import plotly.plotly as py
import plotly.graph_objs as go
import plotly

import pandas as pd
import numpy as np

'''
This file is used to create a heatmap that compares the highest paying jobs vs. the lowest paying jobs per state
'''

plotly.tools.set_credentials_file(username='wyvette0542', api_key='9IqIPiGXjRvppiBBZSER')   # Credentials to use plotly

df = pd.read_pickle('dataframe3.pkl')

# df['text'] creates the text that is displayed when you hover over a state
df['text'] = 'State: '+ df['State'] + '<br>'+'Highest: '+ df['MaxName'] + '<br>' + \
    'Mean: ' + df['MaxMean'].map(str)+ ' Max: ' +df['MaxMax'].map(str) + \
    ' Min: ' + df['MaxMin'].map(str) + '<br>' +'Lowest: ' + df['MinName'] + '<br>'+\
    ' Mean: ' + df['MinMean'].map(str) + ' Max: ' + df['MinMax'].map(str) + ' Min: '+ df['MinMin'].map(str)

# This instantiates the Chloropleth heat Map
data = [go.Choropleth(
    colorscale = 'Reds',   # This is a template colorscale 
    autocolorscale = False, 
    locations = df['State'].str.upper(),   # This provides the key for which we can assign to the heatmap
    z=df['Mean'],   # Our main metric is the average salary per state
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
        text = 'Salaries Per Languages Per State'
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