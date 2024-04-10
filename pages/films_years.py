# Import Dependencies
import dash
from dash import dcc, html, callback
from dash.dependencies import Input, Output
import plotly.express as px
import sqlite3
import pandas as pd

# Connect To The SQLite Database
conn=sqlite3.connect('Resources/Blockbusters_2019_1977.db')

# SQL Query To Select All Data From movie_data Table
query = "SELECT * FROM movie_data"

# Load movie_data Table Into Pandas DataFrame
movie_data = pd.read_sql(query, conn)

# Close The Connection
conn.close()

movie_data['genres'] = movie_data[['genre_1', 'genre_2', 'genre_3']].apply(lambda x: ', '.join(x.dropna()), axis=1)

movie_data = movie_data[['film_title',
                         'genre_1',
                         'genre_2',
                         'genre_3',
                         'genres',
                         'release_year',
                         'domestic_distributor',
                         'mpaa_rating',
                         'length_in_min',
                         'imdb_rating',
                         'film_budget',
                         'domestic_gross',
                         'domestic_profit',
                         'worldwide_gross',
                         'worldwide_profit',
                         'rank_year_ww_gross'
                         ]]
year_budget_grouped_data = movie_data.groupby('release_year')['film_budget'].sum().reset_index()
year_budget_grouped_data['film_budget'] /= 1e9
year_budget_grouped_data['worldwide_profit'] = movie_data.groupby('release_year')['worldwide_profit'].sum().values
year_budget_grouped_data['worldwide_profit'] /= 1e9

year_budget_grouped_data = movie_data.groupby('release_year')['film_budget'].sum().reset_index()
year_budget_grouped_data['film_budget'] /= 1e9
year_budget_grouped_data['worldwide_profit'] = movie_data.groupby('release_year')['worldwide_profit'].sum().values
year_budget_grouped_data['worldwide_profit'] /= 1e9

# Define app layout
layout = html.Div([
    html.H4("about-distribution"), html.Br(),
    html.H3("A Look at Profit Distribution by Year", style={'textAlign':'center', 'color':'lightblue'}), html.Br(),
    dcc.Dropdown(
        id='year-dropdown',
        options=[{'label': str(year), 'value': year} for year in year_budget_grouped_data['release_year']],
        value=year_budget_grouped_data['release_year'].iloc[0],  # Default value
        clearable=False,  # Prevents the user from clearing the dropdown
        style={'backgroundColor': 'white', 'color': 'black'},  # Sets The Style Of The Dropdown
    ),
    dcc.Graph(id='pie-chart')
])

# Define callback to update pie chart based on selected year
@callback(
    Output('pie-chart', 'figure'),
    [Input('year-dropdown', 'value')]
)

def update_pie_chart(selected_year):
    year_data = calculate_profit_percentage(selected_year)
    pie_year_profit = px.pie(year_data,
                             values='worldwide_profit_percentage',
                             names='film_title',
                             title=f'Distribution from {selected_year}',
                             color_discrete_map=px.colors.sequential.Viridis,
                             hover_name='film_title',
                             hover_data=['domestic_distributor',
                                         'genres',
                                         'mpaa_rating',
                                         'worldwide_profit',
                                         'rank_year_ww_gross',
                                         'imdb_rating'],
                             width=900,
                             height=650)
    pie_year_profit.update_traces(hovertemplate='<b>%{label}</b><br>' +
                                                    'Domestic Distributor: %{customdata[0][0]}<br>' +
                                                    'Genres: %{customdata[0][1]}<br>' +
                                                    'MPAA Rating: %{customdata[0][2]}<br>' +
                                                    'Worldwide Profit: %{customdata[0][3]:.2f} B<br>' +
                                                    'Worldwide Gross Revenue Rank: %{customdata[0][4]}<br>' +
                                                    'IMDb Rating: %{customdata[0][5]}<br>')
    pie_year_profit.update_layout(
        title_x=0.5,
        title_font_size=22,
        paper_bgcolor='black',
        font=dict(color='white')
        )

    return pie_year_profit

def calculate_profit_percentage(year):
    year_data = movie_data[movie_data['release_year'] == year].copy()
    year_data['worldwide_profit'] /= 1e9
    year_total_profit = year_budget_grouped_data.loc[year_budget_grouped_data['release_year'] == year,
                                                     'worldwide_profit'].values[0]
    year_data['worldwide_profit_percentage'] = year_data['worldwide_profit'] / year_total_profit * 100
    return year_data

# Initialize Dash App
dash.register_page(__name__, path='/films_years')