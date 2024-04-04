import dash
from dash import html


dash.register_page(__name__, path='/')

layout = html.Div([
    html.H1('This is our Home page'),
    html.Img(src=dash.get_asset_url('test.png')),
])
