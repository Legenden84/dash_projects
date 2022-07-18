import pandas as pd
import plotly.express as px
from dash import dcc, html, dash
from dash.dependencies import Input, Output

app = dash.Dash(__name__, suppress_callback_exceptions=True,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )
server = app.server

# Creating dataframe
df = pd.read_csv('intro_bees.csv')

df = df.groupby(['State', 'ANSI', 'Affected_by', 'Year', 'state_code'])[['Pct of Colonies Impacted']].mean()
df.reset_index(inplace=True)

# App layout
app.layout = html.Div([
    html.H1('Interactive dashboard: Choropleth Map for bee colonies affected by various diseases', style={'text-align': 'center'}),

    html.Div([
        html.Div([
            html.Label('Year', style={'fontSize': 30}),

            dcc.Dropdown(id='select-year',
                         options=[{'label': x, 'value': x} for x in sorted(df.Year.unique())],
                         multi=False,
                         value=2015,
                         clearable=False),
        ], className='six columns'),

        html.Div([
            html.Label('Affected by', style={'fontSize': 30}),

            dcc.Dropdown(id='select-disease',
                         options=[],
                         value=[],
                         clearable=False),
        ], className='six columns'),
    ], className='row'),

    dcc.Graph(id='bee-map', figure={})
])


# Creating the callback
@app.callback(
    Output(component_id='select-disease', component_property='options'),
    [Input(component_id='select-year', component_property='value')]
)
def update(year_pick):
    df_copy = df[df.Year == year_pick]
    return [{'label': x, 'value': x} for x in sorted(df_copy.Affected_by.unique())]


@app.callback(
    Output(component_id='select-disease', component_property='value'),
    [Input(component_id='select-disease', component_property='options')]
)
def update_disease(items):
    return [item['value'] for item in items]


@app.callback(
    Output(component_id='bee-map', component_property='figure'),
    [Input(component_id='select-disease', component_property='value'),
     Input(component_id='select-year', component_property='value')]
)
def update_map(disease_pick, year_pick):
    df_copy = df.copy()
    df_copy = df_copy[df_copy['Year'] == year_pick]
    df_copy = df_copy[df_copy['Affected_by'] == disease_pick]

    fig = px.choropleth(
        data_frame=df_copy,
        locationmode='USA-states',
        locations='state_code',
        scope='usa',
        color='Pct of Colonies Impacted',
        hover_data=['State', 'Pct of Colonies Impacted'],
        color_continuous_scale=px.colors.sequential.YlOrRd,
        labels={'Pct of Colonies Impacted': '% of Bee Colonies'},
        template='plotly_dark'
    )
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
