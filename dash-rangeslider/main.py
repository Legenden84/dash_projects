from dash import dcc, html, dash
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Creating the dash object
app = dash.Dash(__name__)

# Creating the dataframe
df = pd.read_csv('Border_Crossing_Entry_Data.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = df['Date'].dt.year
df = df.set_index('Date')

# Creating the app layout
app.layout = html.Div([
    html.Div([
        dcc.Graph(id='graph')
    ]),

    html.Div([
        html.Label(['Choose Years of Border Crossings into the USA'],
                   style={'font-weight': 'bold'}),
        html.P(),
        dcc.RangeSlider(
            id='range-slider',
            marks={
                1996: '1996',
                2000: '2000',
                2004: '2004',
                2008: '2008',
                2012: '2012',
                2016: {'label': '2016', 'style': {'color': '#f50', 'font-weight': 'bold'}},
                2018: '2018',
            },
            step=1,
            min=1996,
            max=2016,
            value=[1998, 2000],
            dots=True,
            allowCross=False,
            disabled=False,
            pushable=2,
            updatemode='mouseup',
            included=True,
            vertical=False,
            verticalHeight=900,
            className='None',
            tooltip={'always_visible': False, 'placement': 'bottom'},
        ),
    ]),
])

# Creating the callback
@app.callback(
    Output(component_id='graph', component_property='figure'),
    [Input(component_id='range-slider', component_property='value')]
)
def update_graph(rangeslider):
    df_copy = df.loc[rangeslider[1]:rangeslider[0]]
    df_copy = df_copy[(df_copy['Measure'] == 'Personal Vehicles')]
    df_copy = df_copy[(df_copy['State'] == 'Vermont') | (df_copy['State'] == 'Idaho')]

    fig = px.bar(
        data_frame=df_copy,
        x='State',
        y='Value',
        color='Port Name')

    fig.update_layout(yaxis={'title': 'Incoming Border Crossings'},
                      title={'text': 'Border Crossings into the United States',
                             'font': {'size': 28}, 'x': 0.5, 'xanchor': 'center'})
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
