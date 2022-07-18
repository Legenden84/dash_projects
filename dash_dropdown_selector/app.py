from dash import dcc, html, dash
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Creating dash object
app = dash.Dash(__name__)

# Creating dataframe
df = pd.read_csv('Urban_Park_Ranger_Animal_Condition.csv')

# Creating app layout
app.layout = html.Div([
    html.Div([
        dcc.Graph(id='my-graph')
    ], className='nine columns'),

    html.Div([
        html.Br(),
        html.Div(id='output-data'),
        html.Br(),

        html.Label(['Choose data:'], style={'font-weight': 'bold', 'text-align': 'center'}),

        dcc.Dropdown(id='my-drpdwn',
                     options=[
                         {'label': 'Species', 'value': 'Animal Class'},
                         {'label': 'Final Ranger Action', 'value': 'Final Ranger Action'},
                         {'label': 'Age', 'value': 'Age', 'disabled': True},
                         {'label': 'Animal Condition', 'value': 'Animal Condition'},
                         {'label': 'Borough', 'value': 'Borough'},
                         {'label': 'Species Status', 'value': 'Species Status'}
                     ],
                     optionHeight=35,
                     value='Borough',
                     disabled=False,
                     multi=False,
                     searchable=True,
                     search_value='',
                     placeholder='Please select...',
                     clearable=True,
                     className='select_box',
                     persistence=True,
                     persistence_type='memory'
                     ),
    ], className='three columns'),
])


# Creating the call for the value and graph
@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    [Input(component_id='my-drpdwn', component_property='value')]
)
def update_graph(column_chosen):
    df_copy = df
    fig = px.pie(data_frame=df_copy, names=column_chosen)
    fig.update_traces(textinfo='percent+label')
    fig.update_layout(title={'text': 'NYC Calls for Animal Rescue',
                             'font': {'size': 28}, 'x': 0.5, 'xanchor': 'center'})
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
