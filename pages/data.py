# Import Dependencies
import dash
from dash import dash_table, html
import pandas as pd
import sqlite3

# Connect To The SQLite Database
conn = sqlite3.connect('Resources/Blockbusters_2019_1977.db')

# Read Data From The Database Into A DataFrame
query = "SELECT * FROM movie_data"
df = pd.read_sql(query, conn)

# Close The Database Connection
conn.close()

# Rename DataFrame Columns
df.rename(columns={'film_title':'Movie Title','genre_1':'Genre 1',
                   'genre_2':'Genre 2','genre_3':'Genre 3','release_year':'Release Year','domestic_distributor':'Movie Studio',
                   'mpaa_rating':'MPAA Rating','length_in_min':'Length in Minutes','imdb_rating':'IMDB Rating',
                   'film_budget':'Film Budget','domestic_gross':'Domestic Gross','domestic_profit':'Domestic Profit',
                   'worldwide_gross':'Worldwide Gross','worldwide_gross':'Worldwide Gross','worldwide_profit':'Worldwide Profit',
                   'rank_year_ww_gross':'Rank Year Worldwide Gross'
                    }, inplace=True)

# Define Layout
layout = html.Div([
    html.H4("about-data"),
    html.H3("The Data, Unabridged", style={'textAlign':'center', 'color':'lightblue'}), html.Br(),
dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[{'id': c, 'name': c,} for c in df.columns],
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        page_action="native",
        page_current= 0,
        page_size= 20,
    style_as_list_view=True,
    style_cell={'padding': '5px'},
    style_data={ 'border': '1px solid red',
                'backgroundColor': 'black',
                'color': 'white'
     },
    style_header={
        'backgroundColor': 'black',
        'color': 'white',
        'fontWeight': 'bold',
        'border': '1px solid red' 
    },
    style_cell_conditional=[
        {
            'if': {'column_id': c},
            'textAlign': 'center'
        } for c in ['Movie Title']
    ],
),

html.Div(id='datatable-interactivity-container')
])

# Register Current Python Module As Page In The Dash Application
dash.register_page(__name__)

