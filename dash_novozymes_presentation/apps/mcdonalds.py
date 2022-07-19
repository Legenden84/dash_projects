from app import app
from dash import dcc, html
from dash.dependencies import Output, Input
import plotly.express as px
import pandas as pd
import pathlib

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath('../datasets').resolve()

# Creating datafile
df = pd.read_csv(DATA_PATH.joinpath('mcdonalds.csv'))

# Creating layout of the dashboard.
layout = html.Div([
    # Dashboard header.
    html.H1('Interactive dashboard: McDonalds(tm) nutrition table'),
    html.Div([
        html.Div([

            # Creating the label for the first (left) dropdown menu.
            html.Label('Menu category:', style={'fontSize': 30}),

            # Creating the first (left) dropdown menu.
            dcc.Dropdown(
                id='category-drpdwn',
                options=[{'label': x, 'value': x} for x in sorted(df.Category.unique())],
                value='value',
                clearable=False),
        ], className='six columns'),

        html.Div([
            # Creating the label for the second (right) dropdown menu.
            html.Label("Menu item:", style={'fontSize': 30}),

            # Creating the second (right) dropdown menu.
            dcc.Dropdown(
                id='item-drpdwn',
                options=[],
                value=[],
                clearable=False),
        ], className='six columns'),
    ], className='row'),

    # Creating the graph (bar chart) for the dashboard.
    dcc.Graph(id='bar-graph', figure={})
])


# Chained callbacks (3).

# First callback.
# Inputs category-drpdwn (options).
# Outputs item-drpdwn (value).
# Callback return a list if items, depending on the input from the item dropdown.
@app.callback(
    Output(component_id='item-drpdwn', component_property='options'),
    [Input(component_id='category-drpdwn', component_property='value')]
)
def update_category(category_chosen):
    df_copy1 = df[df.Category == category_chosen]
    try:
        return [{'label': item, 'value': item} for item in sorted(df_copy1.Item.unique())]
    except NameError:
        print('menu category is not present in data.')


# Second callback.
# Inputs item drpdwn (options).
# Outputs item drpdwn (value).
# Callback returns a list items depending on available items.
@app.callback(
    Output(component_id='item-drpdwn', component_property='value'),
    [Input(component_id='item-drpdwn', component_property='options')]
)
def update_item(available_items):
    try:
        return [item['value'] for item in available_items]
    except NameError:
        print('Menu item is not present in data.')


# Third callback.
# Input 1 : item-drpdwn (value).
# Input 2 : category-drpdwn (value).
# Returns a plotly express bar chart.
@app.callback(
    Output(component_id='bar-graph', component_property='figure'),
    [Input(component_id='item-drpdwn', component_property='value'),
     Input(component_id='category-drpdwn', component_property='value')]
)
def update_graph(item_pick, category_pick):
    df_copy2 = df[(df.Category == category_pick) & (df.Item == item_pick)]

    fig = px.bar(
        data_frame=df_copy2,
        x='Item',
        y=['Total Fat', 'Carbohydrates', 'Protein'],
        opacity=0.9,
        orientation='v',
        barmode='group'
    )
    return fig
