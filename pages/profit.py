# Import Dependencies
import dash
from dash import html, dcc, callback
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import sqlite3

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

# Create Bar Graph For Total Budget Per Year
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
bar_year_budget.update_layout(height=850,
                              width=1350,
                              paper_bgcolor='black',
                              font=dict(color='white'),
                              title_x=0.5,
                              title_font_size=26)

# Create Bar Graph For Total Profit Per Year
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
bar_year_profit.update_layout(height=850,
                              width=1350,
                              paper_bgcolor='black',
                              font=dict(color='white'),
                              title_x=0.5,
                              title_font_size=26)


# Define App Layout
layout = html.Div([
    dbc.Row([
        dbc.Col([
            html.H4("about-profit", className='mb-4')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.H3("A Look at Budget and Worldwide Profit from 1977 - 2019", className='mb-4', style={'color':'lightblue', 'textAlign':'center'})
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='budget-plot', figure=bar_year_budget, className='mb-4')
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='profit-plot', figure=bar_year_profit)
        ])
    ])
])

# Register Current Python Module As Page In The Dash Application
dash.register_page(__name__, path='/profit')

