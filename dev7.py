import pandas as pd 
import plotly.express as px 
data = pd.DataFrame({ 
'Country': ['India', 'United States', 'Brazil', 'China', 'Australia'], 
'Code': ['IND', 'USA', 'BRA', 'CHN', 'AUS'], 
'Population': [1393409038, 332915073, 213993437, 1444216107, 25687041], 
'GDP': [3.5, 21.4, 2.1, 14.7, 1.4] # Trillion USD 
}) 
fig = px.choropleth( data_frame=data, locations='Code', # ISO-3 country codes color='GDP', 
# Data to color by 
hover_name='Country', 
# Hover label 
hover_data={'Population': True, 'Code': False}, 
color_continuous_scale='Viridis', 
projection='natural earth', 
title='World GDP Map (Interactive)' 
) 
# Update layout for interactivity 
fig.update_layout( geo=dict(showframe=False, showcoastlines=True), 
margin={"r":0,"t":40,"l":0,"b":0} 
) 
fig.show()
