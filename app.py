import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG], use_pages=True)



#app = Dash(__name__, use_pages=True)

app.layout = html.Div([
    html.Div(
        className="app-header",
        children=[
            html.Div("Plotly Dash", className="app-header--title")
        ]
    ),
    html.Div(
        children=html.Div([
            html.H1("Overview"),
            html.Div('''
                This is exceptionally frustrating.
            ''')
        ])
    )
])


nav = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("Home", active="exact", href="/")),
        dbc.NavItem(dbc.NavLink("Map", active="exact", href="/map")),
        dbc.NavItem(dbc.NavLink("Profit", active="exact", href="/profit")),
        dbc.NavItem(dbc.NavLink("Disabled", disabled=True, href="#")),
    ],
    pills=True,
)



app.layout = html.Div([
    html.H1('about-movies'),
    nav,
    dash.page_container
])

if __name__ == '__main__':
    app.run(debug=True)