from dash import dcc, html, dash
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Creating the dataframe
df = px.data.gapminder()

# Importing assets
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Creating the dash object
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# Creating the app layout
app.layout = html.Div([
    dcc.Dropdown(id='drpdwn2',
                 value=['Germany', 'Brazil'],
                 multi=True,
                 options=[{'label': x, 'value': x} for x in df.country.unique()]),
    html.Div([
        dcc.Graph(id='pie-chart', figure={}, className='six columns'),
        dcc.Graph(id='my-graph', figure={}, clickData=None,
                  config={
                      'staticPlot': False,
                      'scrollZoom': True,
                      'doubleClick': 'reset',
                      'showTips': False,
                      'displayModeBar': True,
                      'watermark': True,
                      # 'modeBarButtonsToRemove': ['pan2d', 'select2d']
                  },
                  className='six columns'
                  )
    ])
])


@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    [Input(component_id='drpdwn2', component_property='value')]
)
def update_graph(country_chosen):
    df_copy = df[df.country.isin(country_chosen)]
    fig = px.line(data_frame=df_copy,
                  x='year',
                  y='gdpPercap',
                  color='country',
                  custom_data=['country', 'continent', 'lifeExp', 'pop'])
    fig.update_traces(mode='lines+markers')
    return fig


@app.callback(
    Output(component_id='pie-chart', component_property='figure'),
    [Input(component_id='my-graph', component_property='hoverData'),
     Input(component_id='my-graph', component_property='clickData'),
     Input(component_id='my-graph', component_property='selectedData'),
     Input(component_id='drpdwn2', component_property='value')]
)
def update_side_graph(hov_data, clk_data, slct_data, country_chosen):
    if hov_data is None:
        df_copy2 = df[df.country.isin(country_chosen)]
        df_copy2 = df_copy2[df_copy2.year == 1952]
        fig2 = px.pie(data_frame=df_copy2,
                      values='pop',
                      names='country',
                      title='Population for 1952')
        return fig2
    else:
        print(f'hover data: {hov_data}')
        print(hov_data['points'][0]['customdata'][0])
        print(f'click data: {clk_data}')
        print(f'selected data: {slct_data}')
        df_copy2 = df[df.country.isin(country_chosen)]
        hov_year = hov_data['points'][0]['x']
        df_copy2 = df_copy2[df_copy2.year == hov_year]
        fig2 = px.pie(data_frame=df_copy2,
                      values='pop',
                      names='country',
                      title=f'Population for: {hov_year}')
        return fig2


if __name__ == '__main__':
    app.run_server(debug=True)
