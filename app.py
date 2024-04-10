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
        dbc.NavItem(dbc.NavLink("Financials", active="exact", href="/profit")),
        dbc.NavItem(dbc.NavLink("Durations", active="exact", href="/film_length")),
        dbc.NavItem(dbc.NavLink("Genres", active="exact", href="/genre")),
        dbc.NavItem(dbc.NavLink("Ratings", active="exact", href="/worldwide_profit")),
        dbc.NavItem(dbc.NavLink("Distribution", active="exact", href='/films_years'))
        ],
    pills=True,
)

app.layout = dbc.Container([
    nav,
    dash.page_container
    ])



if __name__ == '__main__':
    app.run_server(debug=True)