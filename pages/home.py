import dash
from dash import html, Dash, html, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template


dash.register_page(__name__, path='/')


layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H2("Welcome to about-movies:",
                        className='text-center text-primary'),
                        width=12)
    ]),
    dbc.Row([
        dbc.Col(html.H2("A Data Visualization Project",
                        className='text-center text-primary, mb-4'),
                        width=12)
    ]),
    dbc.Row([
        dbc.Col(html.H4("By perfectionists-under-pressure",
                        className='text-center text-primary text-success, mb-4'),
                        width=12)
    ]),
    dbc.Row([
        dbc.Col([

        ], width=3),
        dbc.Col([
            dbc.Carousel(
    items=[
        {"key": "1", "src": "/assets/word_cloud.png", "img_style":{"max-height":"500px"}},
        {"key": "2", "src": "/assets/maxtrix_background.png", "img_style":{"max-height":"500px"}},
        {"key": "3", "src": "/assets/test.png", "img_style":{"max-height":"500px"}},
    ],
    controls=False,
    indicators=False,
    interval=3000,
    ride="carousel",
    className='pb-4'
)
        ], width=6),
        dbc.Col([

        ], width=3)
    ])
])


carousel = dbc.Carousel(
    items=[
        {"key": "1", "src": "/static/images/slide1.svg"},
        {"key": "2", "src": "/static/images/slide2.svg"},
        {"key": "3", "src": "/static/images/slide3.svg"},
    ],
    controls=False,
    indicators=False,
    interval=2000,
    ride="carousel",
)