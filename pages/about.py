import dash
from dash import html, Dash, html, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

dash.register_page(__name__, path='/about')


# define tab content

tab1content = dbc.Card([
    dbc.CardBody([
        html.H4("p-u-p", className="card-title"),
        html.P("Cesar needs to put his information here.", className="card-text"),
        html.P("Harsh needs to put his information here.", className="card-text"),
        html.P("Meagan needs to put her information here.", className="card-text")
    ])
])

tab2content = dbc.Card([
    html.H4('the-dataset', className="card-title"),
    html.P("We found our dataset on Kaggle.com", className="card-text"),
    html.P(html.A("https://www.kaggle.com/datasets/narmelan/top-ten-blockbusters-20191977", href="https://www.kaggle.com/datasets/narmelan/top-ten-blockbusters-20191977"), className="card-text")
])


# define layout
layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H2("Welcome to about-movies", className='text-center text-primary'), width=12)
    ]),
    dbc.Row([
        dbc.Col(tab1content, width=12)
    ]),
    dbc.Row([
        dbc.Col(tab2content, width=12)
    ]),
    dbc.Row([
        dbc.Col(dbc.Tabs([
            dbc.Tab(tab1content, label="p-u-p"),
            dbc.Tab(tab2content, label="the-dataset"),
            dbc.Tab("This tab's content is", label="Tab 3", disabled=True)
        ]), width=12)
    ])
])

