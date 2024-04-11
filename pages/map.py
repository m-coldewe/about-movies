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

def create_marker(studio):
    # Calculate marker size based on profit
    size_factor = studio['Worldwide Profit'] / df['Worldwide Profit'].max()  # Adjust for relative sizes
    icon_size = [300* size_factor, 150 * size_factor]

    icon = {
        "iconUrl": studio['url_image'],
        "iconSize":   icon_size,
        "iconAnchor": [22, 94],
        "popupAnchor": [-3, -76],
        "className": "icon"
    }
    tooltip_content = ([html.P(f"Worldwide Profit: {studio['Worldwide Profit']}"),
                       html.P(f"Total Movies: {studio['Total Movies']}"),
                       html.P(f"Most Profitable Movie: {studio['Film Title']}"),
                       html.P(f"Movie Profit: {studio['Movie Profit']} "),
                       html.P(f"Release Year: {studio['Release Year']} ")])
    
                      
    return dl.Marker(
        position=[studio['Latitude'], studio['Longitude']],
        icon=icon,
        children=[
            dl.Tooltip(tooltip_content, direction='top')
                    
        ]
    )
markers = [create_marker(row) for index, row in df.iterrows()]

layout = html.Div([
    dl.Map(center=[34.07623971367669, -118.35312266347428], zoom=11, children=[
        dl.TileLayer(),
        *markers
    ], style={'width': '100%', 'height': '500px'}
    )
])



dash.register_page(__name__)