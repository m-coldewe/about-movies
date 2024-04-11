# Import Dependencies
import dash
from dash import dcc, html, callback
from dash.dependencies import Input, Output
import plotly.express as px
import sqlite3
import pandas as pd

# Connect To The SQLite Database
conn=sqlite3.connect('Resources/scatter_bar_pie.db')

# SQL Query To Select All Data From movie_data Table
query = "SELECT * FROM graph_movie_data"

# Load movie_data Table Into Pandas DataFrame
movie_data = pd.read_sql(query, conn)

# Close The Connection
conn.close()

# Group Movie Data By Release Year, Calculate Total Film Budget For Each Year, Convert To Billions
year_budget_grouped_data = movie_data.groupby('release_year')['film_budget'].sum().reset_index()
year_budget_grouped_data['film_budget'] /= 1e9

# Calculate Total Worldwide Profit For Each Release Year, Convert To Billions
year_budget_grouped_data['worldwide_profit'] = movie_data.groupby('release_year')['worldwide_profit'].sum().values
year_budget_grouped_data['worldwide_profit'] /= 1e9

# Define App Layout
layout = html.Div([
    html.H4("about-distribution"), html.Br(),
    html.H3("A Look at Profit Distribution by Year", style={'textAlign':'center', 'color':'lightblue'}), html.Br(),
    dcc.Dropdown(
        id='year-dropdown',
        options=[{'label': str(year), 'value': year} for year in year_budget_grouped_data['release_year']],
        value=year_budget_grouped_data['release_year'].iloc[0],
        clearable=False,
        style={'backgroundColor': 'white', 'color': 'black'},
    ),
    dcc.Graph(id='pie-chart')
])

# Define Callback To Update Pie Chart Based On Selected Year
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
                             width=1250,
                             height=750)
    pie_year_profit.update_traces(hovertemplate='<b>%{label}</b><br>' +
                                                    'Domestic Distributor: %{customdata[0][0]}<br>' +
                                                    'Genres: %{customdata[0][1]}<br>' +
                                                    'MPAA Rating: %{customdata[0][2]}<br>' +
                                                    'Worldwide Profit: $%{customdata[0][3]:.2f} B<br>' +
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

# Register Current Python Module As Page In The Dash Application
dash.register_page(__name__, path='/distribution')

