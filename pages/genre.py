import dash
from dash import html, dcc, callback, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import sqlite3

# get gitbash to recognize @app
app = dash.Dash(__name__)

# connect to the SQLite database
conn=sqlite3.connect(r"C:\Users\macol\OneDrive\Desktop\Classwork\about-movies\Resources\Blockbusters_2019_1977.db")

# read data for genre and year
query = "SELECT release_year, genre_1, genre_2, genre_3 FROM movie_data"
df = pd.read_sql(query, conn)

# close the database connection
conn.close()

genres = df[['genre_1', 'genre_2', 'genre_3']].stack().reset_index(drop=True)

dash.register_page(__name__, path='/genre')

# define the layout
layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H2("about-genre"))
    ]),
    dbc.Row([
        dbc.Col([
            dcc.RadioItems(
                id = 'genre-radio',
                options = [{'label': genre, 'value': genre} for genre in genres.unique()],
                value='action', 
                inline=True,
            )
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id = 'genre-graph')
        ])
    ]),
])


# define the callback to update the graph based on the selected genres
@app.callback(
    Output('genre-graph', 'figure'),
    [Input('genre-radio', 'value')],
)

def update_genre_graph(selected_genres):
    filtered_df = df[df[['genre_1', 'genre_2', 'genre_3']].isin(selected_genres).any(axis=1)]
    fig = px.line(filtered_df.groupby('release_year').size().reset_index(name='count'), 
                  x = 'release_year', y = 'count', title = 'Genre Through the Years')
    return fig
