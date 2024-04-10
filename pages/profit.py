import dash
from dash import html, dcc, callback
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import sqlite3

# Initialize Dash app
app = dash.Dash(__name__)

# Connect To The SQLite Database
conn=sqlite3.connect('../Resources/Blockbusters_2019_1977.db')

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
bar_year_budget = px.bar(year_budget_grouped_data,
                         x='release_year',
                         y='film_budget',
                         text='film_budget',
                         title='Total Film Budget per Year',
                         labels={'release_year': 'Release Year',
                                 'film_budget': 'Total Budget (Billions)'},
                         color='film_budget',
                         color_continuous_scale='agsunset',
                         custom_data=['worldwide_profit']
                        )
bar_year_budget.update_traces(texttemplate='%{text:$,.2f}B', textposition='inside', 
                               hovertemplate='<b>Release Year:</b> %{x}<br>' +
                                             '<b>Total Budget:</b> $%{text:.2f} B<br>' +
                                             '<b>Total Worldwide Profit:</b> $%{customdata:.2f} B')
bar_year_budget.update_layout(height=900,
                              paper_bgcolor='black',
                              font=dict(color='white'),
                              title_x=0.5,
                              title_font_size=26)
bar_year_budget.show()

bar_year_profit = px.bar(year_budget_grouped_data,
                         x='release_year',
                         y='worldwide_profit',
                         text='worldwide_profit',
                         title='Total Film Worldwide Profit per Year',
                         labels={'release_year': 'Release Year',
                                 'worldwide_profit': 'Total Worldwide Profit (Billions)'},
                         color='worldwide_profit',
                         color_continuous_scale='aggrnyl',
                         custom_data=['film_budget']
                        )
bar_year_profit.update_traces(texttemplate='%{text:$,.2f}B', textposition='inside', 
                               hovertemplate='<b>Release Year:</b> %{x}<br>' +
                                             '<b>Total Budget:</b> $%{customdata:.2f} B<br>' +
                                             '<b>Total Worldwide Profit:</b> $%{text:.2f} B')
bar_year_profit.update_layout(height=900,
                              paper_bgcolor='black',
                              font=dict(color='white'),
                              title_x=0.5,
                              title_font_size=26)
bar_year_profit.show()

# Define App Layout
app.layout = html.Div([
    html.Div([
        dcc.Graph(id='budget-plot', figure=bar_year_budget)
    ]),
    html.B(),
    html.Div([
        dcc.Graph(id='profit-plot', figure=bar_year_profit)
    ])
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
