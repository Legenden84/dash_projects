from dash import dcc, html

# tab 1 - overblik
overblik = [
    html.P("This is tab 1.",
           style={
                "margin-top": "0px",
                "padding-top": "0px",
                "height": "536px",
                "backgroundColor":
                   "#D8E1E8", "font-family": "Ubuntu"})
]

# tab 2 - fravær
absence = [
    dcc.Tabs(
        id="absence-tab",
        value="tab-2-main",
        children=[
            dcc.Tab(
                label="SFO",
                value="tab-2-sfo",
                children=[
                    dcc.Markdown(
                        """
                        Bemærk, at dit barn automatisk raskmeldes, så hvis dit barn fortsat er syg, skal
                        du registrere sygdom næste morgen.
                        """,
                        style={
                            "margin-top": "0px",
                            "padding-top": "0px",
                            "backgroundColor": "#D8E1E8",
                            "font-family": "Ubuntu"}
                    ),
                    dcc.Checklist(
                        options=["barn 1", "barn 2", "barn 3"],
                        labelStyle={'display': 'block', 'margin-bottom': '10px'},
                        style={'margin-left': '10px', "font-family": "Ubuntu"},
                    ),
                    dcc.Markdown(
                        """
                        Eventuelle bemærkninger kan skrives i besked feltet nedenfor.
                        """,
                        style={
                            "margin-bottom": "0px",
                            "backgroundColor": "#D8E1E8",
                            "font-family": "Ubuntu"}
                    ),
                    dcc.Textarea(
                        id="text-area",
                        value="Kommentar felt.",
                        style={"margin-left": "8px", 'width': '94%', 'height': 200},
                    ),
                    html.Div([
                        html.Button(
                            "Registrer fravær",
                            id="button",
                            n_clicks=0,
                        ),
                    ],
                        className="centered-button"
                    ),
                ],
                style={
                    "padding": "5px",
                    "height": "30px",
                    "backgroundColor": "#F7F7F7",
                    "font-family": "Ubuntu"},
                selected_style={
                    "color": "white",
                    "padding": "5px",
                    "height": "30px",
                    "backgroundColor": "#16425D",
                    "font-family": "Ubuntu"},
                className="custom-tabs-container",
                selected_className="custom-tab--selected"
            ),
            dcc.Tab(
                label="SKOLE",
                value="tab-2-skole",
                children=[
                    dcc.Markdown(
                        """
                        Bemærk, at dit barn automatisk raskmeldes, så hvis dit barn fortsat er syg, skal
                        du registrere sygdom næste morgen.
                        """,
                        style={
                            "margin-bottom": "0px",
                            "backgroundColor": "#D8E1E8",
                            "font-family": "Ubuntu"}
                    ),
                    dcc.Checklist(
                        options=["barn 1", "barn 2", "barn 3"],
                        labelStyle={'display': 'block', 'margin-bottom': '10px'},
                        style={'margin-left': '10px', "font-family": "Ubuntu"},
                    ),
                    dcc.Markdown(
                        """
                        Eventuelle bemærkninger kan skrives i besked feltet nedenfor.
                        """,
                        style={
                            "margin-bottom": "0px",
                            "backgroundColor": "#D8E1E8",
                            "font-family": "Ubuntu"}
                    ),
                    dcc.Textarea(
                        id="text-area",
                        value="Kommentar felt.",
                        style={"margin-left": "8px", 'width': '94%', 'height': 200},
                    ),
                    html.Div([
                        html.Button(
                            "Registrer fravær",
                            id="button",
                            n_clicks=0,
                        ),
                    ],
                        className="centered-button"
                    ),
                ],
                style={
                    "padding": "5px",
                    "height": "30px",
                    "backgroundColor": "#F7F7F7",
                    "font-family": "Ubuntu"},
                selected_style={
                    "color": "white",
                    "padding": "5px",
                    "height": "30px",
                    "backgroundColor": "#16425D",
                    "font-family": "Ubuntu"},
                className="custom-tabs-container",
                selected_className="custom-tab--selected"
            ),
        ],
        style={
            "margin-bottom": "0px",
            "padding-bottom": "0px",
            "height": "30px",
        },
        className="custom-tabs-container",
    ),
]

# tab 3 - tid
time = [
    html.P("This is tab 3.",
           style={
                "margin-top": "0px",
                "height": "536px",
                "backgroundColor": "#D8E1E8",
                "font-family": "Ubuntu"}),
]