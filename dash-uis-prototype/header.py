from dash import html

# header layout
header = html.Div(
    children=[html.H1("Aula prototype")],
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