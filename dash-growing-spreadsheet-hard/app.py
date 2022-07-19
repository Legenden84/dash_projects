from dash import dcc, html, dash, dash_table
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Creating the dataframe
df = pd.read_csv('internet_cleaned.csv')
df = df[df['year'] == 2019]

# Creating new column names
df['id'] = df['iso_alpha3']
df.set_index('id', inplace=True, drop=False)

# Creating the dash object
app = dash.Dash(__name__, prevent_initial_callbacks=True)

# Creating the app layout & sorting operators (https://dash.plotly.com/datatable/filtering)
app.layout = html.Div([
    dash_table.DataTable(
        id='datatable-interactivity',
        columns=[
            {"name": i, "id": i, "deletable": True, "selectable": True, "hideable": True}
            if i == "iso_alpha3" or i == "year" or i == "id"
            else {"name": i, "id": i, "deletable": True, "selectable": True}
            for i in df.columns
        ],
        data=df.to_dict('records'),  # the contents of the table
        editable=True,              # allow editing of data inside all cells
        filter_action="native",     # allow filtering of data by user ('native') or not ('none')
        sort_action="native",       # enables data to be sorted per-column by user or not ('none')
        sort_mode="single",         # sort across 'multi' or 'single' columns
        column_selectable="multi",  # allow users to select 'multi' or 'single' columns
        row_selectable="multi",     # allow users to select 'multi' or 'single' rows
        row_deletable=True,         # choose if user can delete a row (True) or not (False)
        selected_columns=[],        # ids of columns that user selects
        selected_rows=[],           # indices of rows that user selects
        page_action="native",       # all data is passed to the table up-front or not ('none')
        page_current=0,             # page number that user is on
        page_size=6,                # number of rows visible per page
        style_cell={                # ensure adequate header width when text is shorter than cell's text
            'minWidth': 95, 'maxWidth': 95, 'width': 95
        },
        style_cell_conditional=[    # align text columns to left. By default they are aligned to right
            {
                'if': {'column_id': c},
                'textAlign': 'left'
            } for c in ['country', 'iso_alpha3']
        ],
        style_data={                # overflow cells' content into multiple lines
            'whiteSpace': 'normal',
            'height': 'auto'
        }
    ),

    html.Br(),
    html.Br(),
    html.Div(id='bar-container'),
    html.Div(id='choromap-container')

])


# Create bar chart
@app.callback(
    Output(component_id='bar-container', component_property='children'),
    [Input(component_id='datatable-interactivity', component_property='derived_virtual_data'),
     Input(component_id='datatable-interactivity', component_property='derived_virtual_selected_rows')]
)
def update_bar(all_rows_data, slctd_row_indices):

    df_copy = pd.DataFrame(all_rows_data)

    colors = ['#7FDBFF' if i in slctd_row_indices else '#0074D9'
              for i in range(len(df_copy))]

    if "country" in df_copy and "did online course" in df_copy:
        return [
            dcc.Graph(id='bar-chart',
                      figure=px.bar(
                          data_frame=df_copy,
                          x="country",
                          y='did online course',
                          labels={"did online course": "% of Pop took online course"}
                      ).update_layout(showlegend=False, xaxis={'categoryorder': 'total ascending'})
                      .update_traces(marker_color=colors, hovertemplate="<b>%{y}%</b><extra></extra>")
                      )
        ]


# Creating choropleth map
@app.callback(
    Output(component_id='choromap-container', component_property='children'),
    [Input(component_id='datatable-interactivity', component_property="derived_virtual_data"),
     Input(component_id='datatable-interactivity', component_property='derived_virtual_selected_rows')]
)
def update_map(all_rows_data, slctd_row_indices):
    df_copy = pd.DataFrame(all_rows_data)

    # Highlights selected countries on map
    borders = [5 if i in slctd_row_indices else 1 for i in range(len(df_copy))]

    if 'iso_alpha3' in df_copy and 'internet daily' in df_copy and 'country' in df_copy:
        return [
            dcc.Graph(id='choropleth',
                      style={'height': 700},
                      figure=px.choropleth(
                          data_frame=df_copy,
                          locations='iso_alpha3',
                          scope='europe',
                          color='internet daily',
                          title='% of Pop that Uses Internet Daily',
                          template='plotly_dark',
                          hover_data=['country', 'internet daily'],
                      ).update_layout(showlegend=False, title=dict(font=dict(size=28), x=0.5, xanchor='center'))
                      .update_traces(marker_line_width=borders, hovertemplate="<b>%{customdata[0]}</b><br><br>" + "%{customdata[1]}" + "%")
                      )
        ]


# Highlights selected column
@app.callback(
    Output(component_id='datatable-interactivity', component_property='style_data_conditional'),
    [Input(component_id='datatable-interactivity', component_property='selected_columns')]
)
def update_styles(selected_columns):
    return [{
        'if': {'column_id': i},
        'background_color': '#D2F3FF'
    } for i in selected_columns]


if __name__ == '__main__':
    app.run_server(debug=True)
