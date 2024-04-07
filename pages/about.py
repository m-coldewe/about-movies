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

dataset_content = "Retrived from kaggle.com, the Worldwide Blockbuster 2019-1977 dataset provides information on the top ten highest grossing films worldwide between the years 2019 and 1977. Further information on the sources of information and exceptions can be found at the link provided below."
dataset_content2 = "The dataset includes the following attributes: release_year, rank_in_year, imdb_rating, mpaa_rating, film_title, film_budget, lengh_in_min, domestic_distributor, worldwide_gross, domestic_gross, and up to three associated genres."

card4 = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H3("Worldwide Blockbusters 2019-1977", className="card-title"),
                html.P([dataset_content, html.Br(), html.Br(), html.P(dataset_content2)],
                    className="card-text",
                ),
                dbc.Button("Click for further information", color="secondary", href="https://www.kaggle.com/datasets/narmelan/top-ten-blockbusters-20191977"),
            ]
        ),
    ],
)

layout = dbc.Container([
    dbc.Row([
        html.H2("Perfectionists-under-pressure (aka P-U-P):")
    ], className="pb-4"),
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
    ], className="pb-5"),
    dbc.Row([
        html.H2("The dataset:")
    ]),
    dbc.Row([
       dbc.Col([
           card4
       ]) 
    ])
])
