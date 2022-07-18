from dash import dcc
from dash import html
from dash.dependencies import Input, Output

from app import app
from app import server

from apps import mcdonalds


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('McDonalds(tm) nutrition table | ', href='/apps/mcdonalds', style={'fontSize': 20})
    ], className='row'),
    html.Div(id='page-content', children=[])
])


@app.callback(
    Output(component_id='page-content', component_property='children'),
    [Input(component_id='url', component_property='pathname')]
)
def update_mainpage(pathname):
    if pathname == '/apps/mcdonalds':
        return mcdonalds.layout


if __name__ == '__main__':
    app.run_server(debug=True)
