# Import Dependencies
import dash
import dash_leaflet as dl
import pandas as pd
from dash import html
import sqlite3

# Connect To The SQLite Database
conn = sqlite3.connect('Resources/map.db')

# Read Data From The Database Into A DataFrame
query = 'SELECT * FROM map_data'
df = pd.read_sql(query, conn)

# Close The Database Connection
conn.close()

# Define Function To Create Markers
def create_marker(studio):
    
    size_factor = studio['Worldwide Profit'] / df['Worldwide Profit'].max()  # Adjust for relative sizes
    icon_size = [300* size_factor, 150 * size_factor]
    icon = {
        "iconUrl": studio['url_image'],
        "iconSize":   icon_size,
        "iconAnchor": [22, 94],
        "popupAnchor": [-3, -76],
        "className": "icon"
    }
    tooltip_content = ([html.P(f"Producer: {studio['Producer']}"),
                        html.P(f"Worldwide Profit: {studio['Worldwide Profit']}"),
                       html.P(f"Total Movies: {studio['Total Movies']}"),
                       html.P(f"Most Profitable Movie: {studio['Film Title']}"),
                       html.P(f"Movie Profit: {studio['Movie Profit']} "),
                       html.P(f"Release Year: {studio['Release Year']} ")])       
    return dl.Marker(
        position=[studio['Latitude'], studio['Longitude']],
        icon=icon,
        children=[
            dl.Tooltip(tooltip_content, direction='top',)                    
        ]
    )

markers = [create_marker(row) for index, row in df.iterrows()]

# Define Layout
layout = html.Div([
    html.H4("about-distributors"),
    html.H3("Domestic Distributors by Worldwide Profit", style={'textAlign':'center', 'color':'lightblue'}), html.Br(),
    dl.Map(center=[34.07623971367669, -118.35312266347428], zoom=11, children=[
        dl.TileLayer(),
        *markers
    ], style={'width': '100%', 'height': '650px'}
    )
])

# Register Current Python Module As Page In The Dash Application
dash.register_page(__name__)

