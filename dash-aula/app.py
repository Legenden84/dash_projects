from dash import dcc, html
import dash

external_stylesheets = [
    "assets/style.css",
    "https://raw.githubusercontent.com/plotly/dash-sample-apps/",
    "master/apps/dash-oil-and-gas/assets/styles.css"
]

header = html.Div(
    children=[html.H1("Aula demo")],
    style={
        "display": "flex",
        "color": "white",
        "textAlign": "center",
        "backgroundColor": "#18638D",
        "padding": "10px",
        "borderBottom": "1px solid #CCC",
        "font-family": "Ubuntu"
    },
)

overblik = [
    html.P("This is tab 1.",
           style={
               "height": "478px",
               "backgroundColor":
                   "#D8E1E8", "font-family": "Ubuntu"})
]

absence = [
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
]

time = [
    html.P("This is tab 3.",
           style={
               "height": "478px",
               "backgroundColor": "#D8E1E8",
               "font-family": "Ubuntu"}),
]

body = html.Div([
    dcc.Tabs(
        id="tabs",
        value="tab-1",
        children=[
            dcc.Tab(
                label="OVERBLIK",
                value="tab-1",
                children=overblik,
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
                label="FRAVÆR",
                value="tab-2",
                children=absence,
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
                label="TID",
                value="tab-3",
                children=time,
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
            "padding": "5px",
            "height": "15px",
        },
        className="custom-tabs-container",
    ),
])

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([header, body],
                      style={
                          "width": "375px",
                          "height": "667px",
                          "margin": "auto",
                          "border": "1px solid black",
                          "font-family": "Ubuntu", },
                      )

if __name__ == "__main__":
    app.run_server(debug=True)
