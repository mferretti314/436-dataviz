import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly as pl
import plotly.express as plx
import pandas as pd


# TO-DO:
#   -seperate and adjust color scales [different colors + possibly logarithmic scale]
#   -finalize layout [small multiples/ 6 total views]


# Define overall figure, including type and layout of subplots
figure = make_subplots(rows=3, cols=1, specs=[[{'type': 'choropleth'}],[{'type': 'choropleth'}],[{'type': 'choropleth'}]], subplot_titles=('Cumulative CO2 Emitted','CO2 Emitted This Year', 'Climate Disasters This Year'))

# Read in all data from csv files
all_data = pd.read_csv('co2_cumulative_data.csv')
annual_data = pd.read_csv('co2_annual_data.csv')
disaster_data = pd.read_csv('vis_disaster_total_data.csv')

# add first trace to figure [trace 0]
figure.add_trace(go.Choropleth(locations=all_data['iso_code'], z=all_data['1960'], colorscale='deep'), row=1, col=1)

# add first trace to figure [trace 1]
figure.add_trace(go.Choropleth(locations=annual_data['iso_code'], z=annual_data['1960'], colorscale='Greys' ), row=2, col=1)

# add first trace to figure [trace 2]
figure.add_trace(go.Choropleth(locations=disaster_data['ISO3'], z=disaster_data['F1960'], colorscale='Reds' ), row=3, col=1)

figure.data[0].colorbar.x=0.9
figure.data[1].colorbar.x=1.0
figure.data[2].colorbar.x=1.1
# start year = 1750 [currently using 1980, will need to fix charts/adjust data later]
# end year = 2022


# iterate over each subplot and create an updated frame for each year
# (currently defines frames 1980-2022 since disaster data does not go back as far as the other data)
frames = [go.Frame(
                name=year,
                data=[
                    go.Choropleth(z=all_data[str(year)], colorscale='deep'),
                    go.Choropleth(z=annual_data[str(year)], colorscale='Greys'),
                    go.Choropleth(z=disaster_data["".join(['F',str(year)])], colorscale='Reds')
                ],
                traces=[0,1,2]
            ) for year in range(1960, 2022)]

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




