import dash
import dash_leaflet as dl
import pandas as pd
from dash import Dash, dcc, html
import plotly.graph_objects as go 
import plotly.express as px
import sqlite3

conn = sqlite3.connect('Resources/map.db')

# Read data from the database into a DataFrame
query = 'SELECT * FROM map_data'
df = pd.read_sql(query, conn)

# Close the database connection
conn.close()
fig = px.scatter_mapbox(df,hover_name='Producer', hover_data={'Producer': True,'Worldwide Profit HN': True,'Total Movies': True
                                                              ,'Film Title': True,'Movie Profit': True,'Release Year': True},
                    color_discrete_sequence=["red"],color_continuous_scale='Viridis',                                          
                    color='Worldwide Profit',size='Worldwide Profit',zoom=10.5,
                    center={'lat': 34.07623971367669, 'lon': -118.35312266347428}
                    ,lat="Latitude", lon="Longitude")
fig.update_layout(
    mapbox_style="open-street-map")
fig.update_traces(hovertemplate="<b>%{customdata[0]}</b><br><br>"
                    'Worldwide Profit: %{customdata[1]}<br>'
                    'Total Movies: %{customdata[2]}<br>'
                    'Most Profitable Movie: %{customdata[3]}<br>'
                	'Movie Profit: %{customdata[4]}<br>'
                	'Release Year: %{customdata[5]}<br>')

dash.register_page(__name__)

layout = html.Div([
    dcc.Graph(id='Worldwide',figure=fig,style={'width': 1150, 'height': 600} )

])
