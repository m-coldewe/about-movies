import dash
from dash import html, dcc, callback, Input, Output
import plotly.express as px
import pandas as pd
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('Resources/Blockbusters_2019_1977.db')

# Read data from the database into a DataFrame
query = "SELECT domestic_distributor, SUM(worldwide_profit) AS worldwide_profit FROM movie_data GROUP BY domestic_distributor"
df = pd.read_sql(query, conn)

# Close the database connection
conn.close()

# Create the Plotly figure
fig = px.bar(df, x='domestic_distributor', y='worldwide_profit', title='Worldwide Profit by Movie Distributor')
fig.update_xaxes(title_text='Movie Distributor')
fig.update_yaxes(title_text='Worldwide Profit')
# Create the Dash app
dash.register_page(__name__)

# Define the layout
layout = html.Div(children=[
    html.H1(children='Worldwide Profit Visualization'),

    dcc.Graph(
        id='Worldwide Profit-bar-chart',
        figure=fig
    )
])
