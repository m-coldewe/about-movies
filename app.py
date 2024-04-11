# Import Dependencies
import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template


# Initialize Dash Application Instance
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG], use_pages=True, suppress_callback_exceptions=True)


# Define Navigation Bar Using Dash Bootstrap Components
nav = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("Home", active="exact", href="/")),
        dbc.NavItem(dbc.NavLink("About", active="exact", href="/about")),
        dbc.NavItem(dbc.NavLink("Data", active="exact", href="/data")),
        dbc.NavItem(dbc.NavLink("Map", active="exact", href="/map")),
        dbc.NavItem(dbc.NavLink("Financials", active="exact", href="/financials")),
        dbc.NavItem(dbc.NavLink("Durations", active="exact", href="/durations")),
        dbc.NavItem(dbc.NavLink("Genres", active="exact", href="/genres")),
        dbc.NavItem(dbc.NavLink("Ratings", active="exact", href="/ratings")),
        dbc.NavItem(dbc.NavLink("Distribution", active="exact", href='/distribution'))
        ],
    pills=True,
)


# Define Layout Of Dash Application Using Dash Bootstrap Components
app.layout = dbc.Container([
    nav,
    dash.page_container
    ])


# Conditionally Execute Dash Application If This Script Is Run Directly
if __name__ == '__main__':
    app.run_server(debug=True)

    