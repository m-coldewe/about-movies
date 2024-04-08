import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import pandas as pd
import sqlite3

# get gitbash to recognize @app
app = dash.Dash(__name__)

# connect to the SQLite database
conn=sqlite3.connect('Resources\Blockbusters_2019_1977.db')

# read data for genre and year
query = "SELECT release_year, genre_1, genre_2, genre_3, domestic_distributor FROM movie_data"
df = pd.read_sql(query, conn)

# close the database connection
conn.close()

template = load_figure_template('cyborg')

# create dataframe with only one genre column by creating a new column for
# each genre column, changing the column name to match, and contatenating
genre_first = df[['release_year', 'genre_1', 'domestic_distributor']]
genre_second = df[['release_year', 'genre_2', 'domestic_distributor']]
genre_third = df[['release_year', 'genre_3', 'domestic_distributor']]

genre_first_rn = genre_first.rename(columns={'genre_1':'genre'})
genre_second_rn = genre_second.rename(columns={'genre_2':'genre'})
genre_third_rn = genre_third.rename(columns={'genre_3':'genre'})

genre_combined = pd.concat([genre_first_rn, genre_second_rn, genre_third_rn], axis=0)
genre_per_year = genre_combined.groupby(['release_year', 'genre']).size().reset_index(name='count')

# create the figure
fig = px.line(genre_per_year, x="release_year", y="count", color="genre", template=template)

# # define layout
layout = html.Div([
    html.H4("about-genre"), html.Br(),
    html.H3("A Look at Genre from 1977 - 2019", style={'color': 'lightblue', 'textAlign':'center'}),
    dcc.Graph(
        id="line-graph",
        figure=fig
    )
]),

# register the page in the app
dash.register_page(__name__, path='/genre')

