from dash import html, dash

# Creating the dash object
app = dash.Dash(__name__)

# Creating the Div layout
app.layout = html.Div([
    html.H1('Main Div.', style={'textAlign': 'center', 'color': 'white'}),

    html.Br(),

    html.Div([
        html.H2('First div.', style={'color': 'white'}),
        html.P('Blah blah blah blah.', style={'color': 'white'})
    ], className='card_container four columns', style={'background-color': '#1f2c56'}),

    html.Div([
        html.H2('Second div.', style={'color': 'white'})
    ], className='card_container four columns', style={'background-color': '#1f2c56'})
])


if __name__ == '__main__':
    app.run_server(debug=False)
