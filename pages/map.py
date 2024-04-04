import dash
import dash_leaflet as dl
from jupyter_dash import JupyterDash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_leaflet.express as dlx
from dash_extensions.javascript import assign
import json


dash.register_page(__name__)

layout = dl.Map(dl.TileLayer(),
                    center=[39, -98],
                    zoom=4,
                    style={'width': '1000px', 'height': '500px'})
