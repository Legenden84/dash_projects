import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import plotly.express as px
import pandas as pd

# Creating the Dash object.
app = dash.Dash(__name__, suppress_callback_exceptions=True,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )

# Creating dataframe
df = pd.read_csv('ds_salaries.csv')

# Creating layout for the dashboard
app.layout = html.Div([
    html.H1('Interactive dashboard: Computer Scientists Salary'),
    html.Div([
        html.Div([
            # Creating the left dropdown.
            html.Label('Select year:', style={'fontSize': 30}),
            dcc.Dropdown(
                id='year-drpdwn',
                options=[{'label': item, 'value': item} for item in sorted(df.work_year.unique())],
                value='value',
                clearable=False),
        ], className='six columns'),

        html.Div([
            # Creating the right dropdown.
            html.Label('Job title:', style={'fontSize': 30}),
            dcc.Dropdown(
                id='job-drpdwn',
                options=[],
                value=[],
                clearable=False),
        ], className='six columns'),
    ], className='row'),

    dcc.Graph(id='graph', figure={})
])


@app.callback(
    Output(component_id='job-drpdwn', component_property='options'),
    [Input(component_id='year-drpdwn', component_property='value')]
)
def update(year_chosen):
    df_copy = df[df.work_year == year_chosen]
    return [{'label': item, 'value': item} for item in sorted(df_copy.job_title.unique())]


@app.callback(
    Output(component_id='job-drpdwn', component_property='value'),
    [Input(component_id='job-drpdwn', component_property='options')]
)
def update(available_jobs):
    return [item['value'] for item in available_jobs]


@app.callback(
    Output(component_id='graph', component_property='figure'),
    [Input(component_id='job-drpdwn', component_property='value'),
     Input(component_id='year-drpdwn', component_property='value')]
)
def update(job_pick, year_pick):
    df_copy2 = df[(df.work_year == year_pick) & (df.job_title == job_pick)]

    fig = px.bar(
        data_frame=df_copy2,
        x='experience_level',
        y='salary_in_usd',
        opacity=0.9,
        orientation='v',
        barmode='group'
    )
    return fig


if __name__ == '__main__':
    app.run_server(debug=False)
