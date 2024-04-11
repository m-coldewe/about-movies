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
    html.H4("about-length"),html.Br(),
    html.H3("The Relationship Between Film Duration and MPAA Rating", style={'textAlign':'center', 'color':'lightblue'}), html.Br(),
    dcc.Dropdown(
        id='dropdown-menu1',
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
    dcc.Graph(id='plot1')
])

# Define Callback To Update Plot Based On Selected Dropdown Option
@callback(
    Output('plot1', 'figure'),
    [Input('dropdown-menu1', 'value')],
)

# Creation Of Function To Update Scatter Plot Based On Selected Dropdown Option
def update_plot(selected_option):

    # Scatter Plot For All Movie Data Without Filtering For MPAA Rating
    if 'All' in selected_option:
        graph_title = 'Film Duration (Minutes) vs IMDb Rating (All MPAA Ratings)'
        rating_scatter = px.scatter(movie_data,
                                    x='length_in_min',
                                    y='imdb_rating',
                                    color='imdb_rating',
                                    color_continuous_scale='Portland',
                                    size='imdb_rating',
                                    hover_name='film_title',
                                    hover_data=['film_title',
                                                'release_year',
                                                'domestic_distributor',
                                                'genres'],
                                    width=1300,
                                    height=700)
        rating_scatter.update_traces(hovertemplate='<b>%{customdata[0]}</b><br>' +
                                                    'Release Year: %{customdata[1]}<br>' +
                                                    'Domestic Distributor: %{customdata[2]}<br>' +
                                                    'IMDb Rating: %{y}<br>' +
                                                    'Film Length: %{x} Minutes<br>' +
                                                    'Genres: %{customdata[3]}')
        
    # Scatter Plot For Movie Data Based On Selected MPAA Rating
    else:
        graph_title = f"Film Duration (Minutes) vs IMDb Rating ({selected_option} MPAA Rating)"
        rating_scatter = px.scatter(movie_data[movie_data['mpaa_rating'] == selected_option],
                                    x='length_in_min',
                                    y='imdb_rating',
                                    color='imdb_rating',
                                    color_continuous_scale='Portland',
                                    size='imdb_rating',
                                    hover_name='film_title',
                                    hover_data=['film_title',
                                                'release_year',
                                                'domestic_distributor',
                                                'genres'],
                                    width=1300,
                                    height=700,
                                    trendline="ols")
        rating_scatter.data[0]['hovertemplate'] = '<b>%{customdata[0]}</b><br>'+\
            'Release Year: %{customdata[1]}<br>'+\
                'Domestic Distributor: %{customdata[2]}<br>'+\
                    'IMDb Rating: %{y}<br>'+'Film Length: %{x} Minutes<br>'+'Genres: %{customdata[3]}'
        
        # Retrieve Desired Data From The OLS Trendline Model
        line_stats = px.get_trendline_results(rating_scatter)
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
        rating_scatter.data[1]['hovertemplate'] = trendline_summary

    # Update Scatter Plot With Labels, Dynamic Title, And Formatting
    rating_scatter.update_layout(
        title=graph_title,
        title_x=0.5,
        title_font_size=22,
        xaxis_title='Duration in Minutes',
        yaxis_title='IMDb Rating',
        coloraxis_colorbar_title='IMDb Rating',
        paper_bgcolor='black',
        plot_bgcolor='WhiteSmoke',
        font=dict(color='white')
)
    return rating_scatter

# Register Current Python Module As Page In The Dash Application
dash.register_page(__name__, path='/durations')

