import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly as pl
import plotly.express as plx
import pandas as pd


# TO-DO:
#   -seperate and adjust color scales [adjust colors + set midpoint or min/max for charts]
#   -finish setting up layout

# LAYOUT -------------------------------
#first row:
#co2 this year [done]
#cumulative co2 [done]
#cumulative disasters [need to make cumulative]

#second row:
#co2 per capita this year [not done]
#cumulative co2 per capita [not done]
#temperature anomaly [done]
#---------------------------------------


# Define overall figure, including type and layout of subplots
figure = make_subplots(rows=2, cols=3, specs=[[{'type': 'choropleth'},{'type': 'choropleth'},{'type': 'choropleth'}],[{'type': 'choropleth'},{'type': 'choropleth'},{'type': 'choropleth'}]], 
                       subplot_titles=('CO2 Emitted This Year<br><sup>Measured in millions of tons of CO2.</sup>',
                                       'Cumulative CO2 Emitted<br><sup>Measured in millions of tons of CO2.</sup>',
                                       'Climate Disasters Since 1980',
                                       'CO2 Emitted This Year Per Capita<br><sup>Measured in tons of CO2 per person.</sup>',
                                       'Cumulative CO2 Emitted Per Capita<br><sup>Measured in tons of CO2 emitted per person since 1980.</sup>',
                                       'Temperature Anomaly This Year<br><sup>Measured in degrees celsius above baseline.</sup>'))

# Read in all data from csv files
all_data = pd.read_csv('co2_cumulative_data.csv')
annual_data = pd.read_csv('co2_annual_data.csv')
disaster_data = pd.read_csv('disasters_cumulative.csv')
temp_data = pd.read_csv('temperature_anomaly_annual.csv')
per_capita = pd.read_csv('co2_per_capita_data.csv')
per_capita_cumulative = pd.read_csv('co2_per_capita_cumulative_data.csv')

disaster_data.replace(0, '', inplace=True)
annual_data.replace(0, '', inplace=True)


# add first trace to figure [trace 0]
figure.add_trace(go.Choropleth(locations=annual_data['iso_code'], z=annual_data['1961'], colorscale=['#ADD8E6', '#98FB98', '#FFA500', '#FF4500', '#E2725B'] ), row=1, col=1)

# add trace to figure [trace 1]
figure.add_trace(go.Choropleth(locations=all_data['iso_code'], z=all_data['1961'], colorscale=['#ADD8E6', '#98FB98', '#FFA500', '#FF4500', '#E2725B']), row=1, col=2)

# add ftrace to figure [trace 2]
figure.add_trace(go.Choropleth(locations=disaster_data['ISO3'], z=disaster_data['1961'], colorscale='Reds', zmin=0), row=1, col=3)

#placeholders
# add trace to figure [trace 3]
figure.add_trace(go.Choropleth(locations=per_capita['iso_code'], z=per_capita['1961'], colorscale=['#E6E6FA', '#87CEEB', '#FFDAB9', '#FA8072', '#E2725B'], zmin=0, zmax=25), row=2, col=1)

# add trace to figure [trace 4]
figure.add_trace(go.Choropleth(locations=per_capita_cumulative['iso_code'], z=per_capita_cumulative['1961'], colorscale=['#E6E6FA', '#87CEEB', '#FFDAB9', '#FA8072', '#E2725B'] ), row=2, col=2)

# add trace to figure [trace 5]
figure.add_trace(go.Choropleth(locations=temp_data['ISO3'], z=temp_data['1961'], colorscale=['#B0E0E6', '#008080', '#40E0D0', '#FF6B6B', '#CC5500'], zmin=-2.5, zmax=2.5), row=2, col=3)


# COLOR SCALES:
#--------------------------------------------------------------------------------------------
#ocean breeze
#color_continuous_scale=['#B0E0E6', '#008080', '#40E0D0', '#FF6B6B', '#CC5500']

#sunset glow
#color_continuous_scale=['#E6E6FA', '#87CEEB', '#FFDAB9', '#FA8072', '#E2725B']

#glacier melt
#color_continuous_scale=['#ADD8E6', '#98FB98', '#FFA500', '#FF4500', '#E2725B']
#---------------------------------------------------------------------------------------------



# TODO
# 1- limit per capita this year scale to 40
# 2- limit temperature anomaly scale




# position color scales them below thier respective graph
figure.data[0].colorbar.x=0.15
figure.data[1].colorbar.x=0.5
figure.data[2].colorbar.x=0.85
figure.data[3].colorbar.x=0.15
figure.data[4].colorbar.x=0.5
figure.data[5].colorbar.x=0.85

figure.data[0].colorbar.y=0.59
figure.data[1].colorbar.y=0.59
figure.data[2].colorbar.y=0.59
figure.data[3].colorbar.y=-0.04
figure.data[4].colorbar.y=-0.04
figure.data[5].colorbar.y=-0.04

# flip color scales horizontally 
for i in range(0,6):
    
    figure.data[i].colorbar.orientation='h'
    figure.data[i].colorbar.thicknessmode='pixels'
    figure.data[i].colorbar.lenmode='pixels'
    figure.data[i].colorbar.thickness=10
    figure.data[i].colorbar.len=200

# adjust color scales for data specific parameters







# start year = 1960
# end year = 2022


# iterate over each subplot and create an updated frame for each year
# (currently defines frames 1961-2022 since temp data is from 1961-2022
frames = [go.Frame(
                name=year,
                data=[
                    go.Choropleth(z=annual_data[str(year)], colorscale=['#ADD8E6', '#98FB98', '#FFA500', '#FF4500', '#E2725B']),
                    go.Choropleth(z=all_data[str(year)], colorscale=['#ADD8E6', '#98FB98', '#FFA500', '#FF4500', '#E2725B']),
                    go.Choropleth(z=disaster_data[str(year)], colorscale='Reds', zmin=0),
                    go.Choropleth(z=per_capita[str(year)], colorscale=['#E6E6FA', '#87CEEB', '#FFDAB9', '#FA8072', '#E2725B'], zmin=0, zmax=25),
                    go.Choropleth(z=per_capita_cumulative[str(year)], colorscale=['#E6E6FA', '#87CEEB', '#FFDAB9', '#FA8072', '#E2725B']),
                    go.Choropleth(z=temp_data[str(year)], colorscale=['#B0E0E6', '#008080', '#40E0D0', '#FF6B6B', '#CC5500'], zmin=-2.5, zmax=2.5)
                ],
                traces=[0,1,2,3,4,5]
            ) for year in range(1961, 2022)]

# Parameters to define function of button
updatemenus = [dict(type='buttons',
                    buttons=[dict(label='Play', method='animate', args=[None, dict(frame=dict(duration=2, redraw=True), transition=dict(duration=1), mode='immediate')])],
                    direction= 'left')
            ]

# Parameters to customize slider text, position, and function
sliders = [{'xanchor': 'left', 
            'currentvalue': 
            {
            'font': {'size': 16},
            'prefix': 'Year: ',
            'visible': True,
            'xanchor': 'center'
            },
            'transition': {'duration': 5.0},
            'steps': 
            [
            {'args': [[year], {'frame': {'duration': 2.0,  'redraw': True},'transition': {'duration': 0}}], 
            'label': year, 
            'method': 'animate'} for year in range(1960, 2022)       
            ]
            }]




# Add frames and button/slider to figure
figure.frames = frames

# Alternative way to assign frames to figure
#figure.update(frames=frames)


figure.update_layout(updatemenus=updatemenus,sliders=sliders)







# Render figure
figure.show()






#----------------------------------------------------------------------------------------------------------




