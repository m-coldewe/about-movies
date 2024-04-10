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

# Define App Layout
layout = html.Div([
    html.H4("about-ratings"),html.Br(),
    html.H3("The Relationship Between IMDb Rating and Worlwide Profit", style={'textAlign':'center', 'color':'lightblue'}), html.Br(),
    dcc.Dropdown(
        id='dropdown-menu2',
        options=[
            {'label': 'All Ratings', 'value': 'All'},
            {'label': 'Rated G', 'value':'G'},
            {'label': 'Rated PG', 'value': 'PG'},
            {'label': 'Rated PG-13', 'value': 'PG-13'},
            {'label': 'Rated R', 'value': 'R'}
        ],
        value='All',
        clearable=False,
        style={'backgroundColor': 'white', 'color': 'black'},
    ),
    dcc.Graph(id='plot2')
])

# Define Callback To Update Plot Based On Selected Dropdown Option
@callback(
    Output('plot2', 'figure'),
    [Input('dropdown-menu2', 'value')]
)

# Creation Of Function To Update Scatter Plot Based On Selected Dropdown Option
def update_plot(selected_option):

    # Scatter Plot For All Movie Data Without Filtering For MPAA Rating
    if 'All' in selected_option:
        graph_title = 'IMDb Rating vs Worldwide Profit ($) (All MPAA Ratings)'
        profit_scatter = px.scatter(movie_data,
                                    x='imdb_rating',
                                    y='worldwide_profit',
                                    color='worldwide_profit',
                                    color_continuous_scale='Inferno',
                                    size='worldwide_profit',
                                    hover_name='film_title',
                                    hover_data=['film_title',
                                                'release_year',
                                                'domestic_distributor',
                                                'genres'],
                                    width=1300,
                                    height=700)
        profit_scatter.update_traces(hovertemplate='<b>%{customdata[0]}</b><br>' +
                                                    'Release Year: %{customdata[1]}<br>' +
                                                    'Domestic Distributor: %{customdata[2]}<br>' +
                                                    'Worldwide Profit: $%{y:,.0f}<br>' +
                                                    'IMDb Rating: %{x}<br>' +
                                                    'Genres: %{customdata[3]}')
        
    # Scatter Plot For Movie Data Based On Selected MPAA Rating
    else:
        graph_title = f"IMDb Rating vs Worldwide Profit ($) ({selected_option} MPAA Rating)"
        profit_scatter = px.scatter(movie_data[movie_data['mpaa_rating'] == selected_option],
                                    x='imdb_rating',
                                    y='worldwide_profit',
                                    color='worldwide_profit',
                                    color_continuous_scale='Inferno',
                                    size='worldwide_profit',
                                    hover_name='film_title',
                                    hover_data=['film_title',
                                                'release_year',
                                                'domestic_distributor',
                                                'genres'],
                                    width=1300,
                                    height=700,
                                    trendline="ols")
        profit_scatter.data[0]['hovertemplate'] = '<b>%{customdata[0]}</b><br>'+\
            'Release Year: %{customdata[1]}<br>'+\
                'Domestic Distributor: %{customdata[2]}<br>'+\
                'Worldwide Profit: $%{y:,.0f}<br>'+\
                'IMDb Rating: %{x}<br>'+'Genres: %{customdata[3]}'
        
        # Retrieve Desired Data From The OLS Trendline Model
        line_stats = px.get_trendline_results(profit_scatter)
        line_stats = line_stats.iloc[0]['px_fit_results']
        y_intercept = line_stats.params[0]
        slope = line_stats.params[1]
        p_value = line_stats.pvalues[1]
        r_squared = line_stats.rsquared

        # Input OLS Trendline Information As Hover Data
        regression_equation = f'y = {slope:.4f} * x + {y_intercept:.4f}'
        p_value_display = f'P-Value = {p_value:.5f}'
        r_squared_display = f'R^2 = {r_squared:.3f}'
        trendline_summary = f'Ordinary Least Squares Trendline Summary:<b><br>{regression_equation}\
            <br>{p_value_display}<br>{r_squared_display}'
        profit_scatter.data[1]['hovertemplate'] = trendline_summary

    # Update Scatter Plot With Labels, Dynamic Title, And Formatting
    profit_scatter.update_layout(
        title=graph_title,
        title_x=0.5,
        title_font_size=22,
        xaxis_title='IMDb Rating',
        yaxis_title='Worldwide Profit ($)',
        coloraxis_colorbar_title='Worldwide Profit ($)',
        paper_bgcolor='black',
        plot_bgcolor='WhiteSmoke',
        font=dict(color='white')
)
    return profit_scatter

# Register Current Python Module As Page In The Dash Application
dash.register_page(__name__, path='/worldwide_profit')

