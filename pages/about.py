# Import Dependencies
import dash
from dash import html, Dash, html, Input, Output, State, callback
import dash_bootstrap_components as dbc

# Assigning Descriptions For Each Team Member
content_card_1 = "Maui enjoys photography and following his person around. He's detail-oriented, and enjoys problem-solving."
content_card_2 = "Rush enjoys pursuing knowledge down rabbit holes and arguing with TAs. He's focused, and purses understanding whereever his inquiries take him."
content_card_3 = "Lady enjoys long walks and good stories. She's persistent, and enjoys seeing her ideas bear fruit."

card1 = dbc.Card(
    [
        dbc.CardImg(src="/assets/static/images/cesar_test.jpg", top=True, className="card-img-top"),
        dbc.CardBody(
            [
                html.H4("Maui"), html.H4("aka Cesar", className="card-title"),
                html.P([content_card_1, html.Br(), html.Br(), html.P("Favorite movie: 'Back to the Future'")],
                    className="card-text",
                ),
                dbc.Button("Find Cesar on Github", color="secondary", href="https://github.com/carojasp12"),
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
                html.P([content_card_2, html.Br(), html.Br(), html.P("Favorite movie: 'Men in Black'")],
                    className="card-text",
                ),
                dbc.Button("Find Harsh on Github", color="secondary", href="https://github.com/10H-K"),
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
                dbc.Button("Find Meagan on Github", color="secondary", href="https://github.com/m-coldewe"),
            ]
        ),
    ],
)

# Assigning Descriptions And Disclaimers For Dataset
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

# Assigning Descriptions And Disclaimers For Team Member's Puppy Pictures
disclaimer = "Puppy pictures taken from unsplash.com; the real names of the puppies are unknown. Credit for the photos is as follows:"
disclaimer1 = "For 'Maui', Photo by:" 
dis_link1 = dbc.CardLink("Victor Grabarczyk", href="https://unsplash.com/@victor_vector?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash")
disclaimer2 = "For 'Rush', Photo by:"
dis_link2 = dbc.CardLink("charlesdeluvio", href="https://unsplash.com/@charlesdeluvio?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash")
disclaimer3 = "For 'Lady', Photo by:" 
dis_link3 = dbc.CardLink("Julio Bernal", href="https://unsplash.com/@jbernals?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash")

# Define A Collapsible Component Using Dash Bootstrap Components (dbc)
collapse = dbc.Col(
    [
        dbc.Button(
            "Disclaimer - Puppy Pics",
            id="collapse-button",
            className="mb-3",
            color="secondary",
            n_clicks=0,
        ),
        dbc.Collapse(
            dbc.Card(dbc.CardBody([
                html.P([
                    disclaimer, html.Br(),
                    html.P([disclaimer1, dis_link1]),
                    html.P([disclaimer2, dis_link2]),
                    html.P([disclaimer3, dis_link3])
                ], className="card-text")
            ])),
            id="collapse",
            is_open=False,
        ),
    ]
)

# Define Callback Function That Toggles Visibility Of The Collapse Element
@callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

# Define Layout Of The Dash Application Using Dash Bootstrap Components (dbc)
layout = dbc.Container([
    dbc.Row([
        html.H2("Perfectionists-under-pressure (aka P-U-P):")
    ], className="pb-4 pt-4"),
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
    ], className="pb-3"),
    dbc.Row([
        dbc.Col([

        ]),
        collapse,
        dbc.Col([

        ]),
    ], className="pb-4"),
    dbc.Row([
        html.H2("The dataset:")
    ]),
    dbc.Row([
       dbc.Col([
           card4
       ]) 
    ])
])

# Register Current Python Module As Page In The Dash Application
dash.register_page(__name__, path='/about')

