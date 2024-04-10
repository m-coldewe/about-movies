import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG], use_pages=True, suppress_callback_exceptions=True)



nav = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("Home", active="exact", href="/")),
        dbc.NavItem(dbc.NavLink("About", active="exact", href="/about")),
        dbc.NavItem(dbc.NavLink("Data", active="exact", href="/table")),
        dbc.NavItem(dbc.NavLink("Map", active="exact", href="/map")),
        dbc.NavItem(dbc.NavLink("Profit", active="exact", href="/profit")),
        dbc.NavItem(dbc.NavLink("Film Length", active="exact", href="/film_length")),
        dbc.NavItem(dbc.NavLink("Genres", active="exact", href="/genre"))
        ],
    pills=True,
)

app.layout = dbc.Container([
    nav,
    dash.page_container
    ])



if __name__ == '__main__':
    app.run_server(debug=True)