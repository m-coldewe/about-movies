# Import Dependencies
import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import pandas as pd
import sqlite3

# Connect To SQLite Database
conn=sqlite3.connect('Resources/Blockbusters_2019_1977.db')

# Query Data For Genre And Year, Create DataFrame
query = "SELECT release_year, genre_1, genre_2, genre_3, domestic_distributor FROM movie_data"
df = pd.read_sql(query, conn)

# Close SQLite Database Connection
conn.close()

# Load Figure Template Named 'cyborg' Using Plotly
template = load_figure_template('cyborg')

# Create Fataframe With Only One Genre Column By Creating New column For
# Each Genre Column, Changing The Column Name To Match, And Contatenating
genre_first = df[['release_year', 'genre_1', 'domestic_distributor']]
genre_second = df[['release_year', 'genre_2', 'domestic_distributor']]
genre_third = df[['release_year', 'genre_3', 'domestic_distributor']]

genre_first_rn = genre_first.rename(columns={'genre_1':'genre'})
genre_second_rn = genre_second.rename(columns={'genre_2':'genre'})
genre_third_rn = genre_third.rename(columns={'genre_3':'genre'})

genre_combined = pd.concat([genre_first_rn, genre_second_rn, genre_third_rn], axis=0)
genre_per_year = genre_combined.groupby(['release_year', 'genre']).size().reset_index(name='count')

# Create The Figure
fig = px.line(genre_per_year, x="release_year", y="count", color="genre", template=template, height=700)

# Update Scatter Plot With Labels
fig.update_layout(
        xaxis_title='Release Year',
        yaxis_title='Genre Count')

# Define Layout
layout = html.Div([
    html.H4("about-genres"), html.Br(),
    html.H3("A Look at Genre from 1977 - 2019", style={'color': 'lightblue', 'textAlign':'center'}),
    dcc.Graph(
        id="line-graph",
        figure=fig
    )
]),

# Register Current Python Module As Page In The Dash Application
dash.register_page(__name__, path='/genre')

