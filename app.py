import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG], use_pages=True)

# app.layout = dbc.Container([
#     dbc.Row([
#         dbc.Col(html.H1('about-movies'),
#                 width=2),
#         dbc.Col(Nav = dbc.Nav(
#     [
#         dbc.NavItem(dbc.NavLink("Home", active="exact", href="/")),
#         dbc.NavItem(dbc.NavLink("Map", active="exact", href="/map")),
#         dbc.NavItem(dbc.NavLink("Profit", active="exact", href="/profit")),
#         dbc.NavItem(dbc.NavLink("Disabled", disabled=True, href="#")),
#     ],
#     pills=True,
# ))
#     ]),

# ])

#app = Dash(__name__, use_pages=True)


nav = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("Home", active="exact", href="/")),
        dbc.NavItem(dbc.NavLink("Map", active="exact", href="/map")),
        dbc.NavItem(dbc.NavLink("Profit", active="exact", href="/profit")),
        dbc.NavItem(dbc.NavLink("Disabled", disabled=True, href="#")),
    ],
    pills=True,
)

app.layout = dbc.Container([
    nav,
    dash.page_container
    ])


# app.layout = dbc.Container([
#     nav,
#     dash.page_container,
#     html.H1('about-movies')])


if __name__ == '__main__':
    app.run(debug=True)