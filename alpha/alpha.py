import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly as pl
import plotly.express as plx
import pandas as pd



# TO-DO:
#   -combine figures into one [may require switching to plotly [not plotly express]]
#   -adjust color scales [different colors + possibly logarithmic scale]
#   -finalize layout [different projection? / multiple views to compare different times (2 of each data - 6 total)]


# Define entire figure to contain/arrange subplots
figure = make_subplots(rows=3, cols=1, specs=[[{'type': 'choropleth'}],[{'type': 'choropleth'}],[{'type': 'choropleth'}]], subplot_titles=('CO2 Total by [YEAR]','CO2 in [YEAR]', 'Disasters in [YEAR]'))

# Read in data from files
all_data = pd.read_csv('co2_cumulative_data.csv')
annual_data = pd.read_csv('co2_annual_data.csv')
disaster_data = pd.read_csv('vis_disaster_total_data.csv')


# Add the desired traces to the figure
figure.add_trace(go.Choropleth(locations=all_data['iso_code'], z=all_data['2022'], colorscale='deep' ), row=1, col=1)
figure.add_trace(go.Choropleth(locations=annual_data['iso_code'], z=annual_data['2022'], colorscale='Greys' ), row=2, col=1)
figure.add_trace(go.Choropleth(locations=disaster_data['ISO3'], z=disaster_data['F2022'], colorscale='Reds'), row=3, col=1)


# Change the layout of the figure to include title
figure.update_layout(title_text='Global CO2 Emissions and Climate-Related Disasters')


figure.show()



