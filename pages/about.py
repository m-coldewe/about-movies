import dash
from dash import html, Dash, html, dcc
import dash_bootstrap_components as dbc


dash.register_page(__name__, path='/about')

content_card_1 = "Paolo enjoys photography and following his person around. He's detail-oriented, and enjoys problem-solving."
content_card_2 = "Rush enjoys pursuing knowledge down rabbit holes and arguing with TAs. He's focused, and purses understanding whereever his inquiries take him."
content_card_3 = "Lady enjoys long walks and good stories. She's persistent, and enjoys seeing her ideas bear fruit."

card1 = dbc.Card(
    [
        dbc.CardImg(src="/assets/static/images/cesar_test.jpg", top=True, className="card-img-top"),
        dbc.CardBody(
            [
                html.H4("Paolo"), html.H4("aka Cesar", className="card-title"),
                html.P([content_card_1, html.Br(), html.Br(), html.P("Favorite movie: 'Back to the Future'")],
                    className="card-text",
                ),
                dbc.Button("Click to Find Cesar", color="secondary", href="https://google.com"),
            ]
        ),
    ],
)

card2 = dbc.Card(
    [
        dbc.CardImg(src="/assets/static/images/harsh_test.jpg", top=True, className="card-img-top"),
        dbc.CardBody(
            [
                html.H4("Rush"), html.H4("aka Harsh", className="card-title"),
                html.P([content_card_2, html.Br(), html.Br(), html.P("Favorite movie: 'Transformers: End of Days'")],
                    className="card-text",
                ),
                dbc.Button("Click to Find Harsh", color="secondary", href="https://google.com"),
            ]
        ),
    ],
)

card3 = dbc.Card(
    [
        dbc.CardImg(src="/assets/static/images/meagan_test.jpg", top=True, className="card-img-top"),
        dbc.CardBody(
            [
                html.H4("Lady"), html.H4("aka Meagan", className="card-title"),
                html.P([content_card_3, html.Br(), html.Br(), html.P("Favorite movie: 'Lord of the Rings: Fellowship of the Ring'")],
                    className="card-text",
                ),
                dbc.Button("Click to Find Meagan", color="secondary", href="https://google.com"),
            ]
        ),
    ],
)


layout = dbc.Container([
    dbc.Row([
        html.H2("Perfectionists-under-pressure (aka P-U-P):")
    ]),
    dbc.Row([
        dbc.Col([
            card1
        ]),
        dbc.Col([
            card2
        ]),
        dbc.Col([
            card3
        ])
    ]),
    dbc.Row([
        html.H2("The dataset:")
    ]),
])
