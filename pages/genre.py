import dash
from dash import html, dcc, callback, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import pandas as pd
import sqlite3

# get gitbash to recognize @app
app = dash.Dash(__name__)

# connect to the SQLite database
conn=sqlite3.connect(r"C:\Users\macol\OneDrive\Desktop\Classwork\about-movies\Resources\Blockbusters_2019_1977.db")

# read data for genre and year
query = "SELECT release_year, genre_1, genre_2, genre_3, domestic_distributor FROM movie_data"
df = pd.read_sql(query, conn)

# close the database connection
conn.close()

genre_first = df[['release_year', 'genre_1', 'domestic_distributor']]
genre_second = df[['release_year', 'genre_2', 'domestic_distributor']]
genre_third = df[['release_year', 'genre_3', 'domestic_distributor']]

genre_first_rn = genre_first.rename(columns={'genre_1':'genre'})
genre_second_rn = genre_second.rename(columns={'genre_2':'genre'})
genre_third_rn = genre_third.rename(columns={'genre_3':'genre'})

genre_combined = pd.concat([genre_first_rn, genre_second_rn, genre_third_rn], axis=0)



fig = px.line(genre_combined, x='release_year')
fig.show()
# get the list of unique genres for the checkboxes

#print(genres)
# register the page in the app
dash.register_page(__name__, path='/genre')

# set initial value for load view of the graph
initial_value = list(genres.unique())

template = load_figure_template('cyborg')

# define the layout
layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H2("about-genre"))
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Checklist(
                id = 'genre-checklist',
                options = [{'label': genre, 'value': genre} for genre in genres],
                value = initial_value,
                inline=True
            )
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='genre-graph', figure={})
        ])
    ])
])


# # define the callback to update the graph based on the selected genres
# @app.callback(
#     Output('genre-graph', 'figure'),
#     [Input('genre-radio', 'value')],
# )



# def update_genre_graph(selected_genres):

#     # if no genres, return empty figure
#     if not selected_genres:
#         return px.line(), {'display': 'none'}
    
#     filtered_df = df[df[['genre_1', 'genre_2', 'genre_3']].apply(lambda row: any(genre in selected_genres for genre in row),axis=1)]

#     if filtered_df.empty:
#         return px.line(), {'display': 'none'}
    
#     # plot the graph based on the filtered dataframe
#     fig = px.line(filtered_df.groupby('release_year').size().reset_index(name='count'),
#                  x='release_year', y='count', title='Genres Through the Years', template=template )
#     return fig, {}