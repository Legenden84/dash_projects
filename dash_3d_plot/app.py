import pandas as pd
import plotly.express as px
import plotly.io as pio
import numpy as np
import plotly.graph_objects as go

e_eye = -1.25
y_eye = 2
z_eye = 0.5

df = pd.read_csv('female_labour_cleaned.csv')
df = df[df['Year'].isin(['2010'])]
df = df[df['Continent'].isin(['Africa', 'Europe'])]

df['resized_pop'] = df['population'] / 100000000

fig = px.scatter_3d(
    data_frame=df,
    x='GDP per capita',
    y='% Econ. active',
    z='Years in school (avg)',
    color='Continent',
    color_discrete_sequence=['magenta', 'green'],
    color_discrete_map={'Europe': 'black', 'Africa': 'yellow'},
    # opacity=0.3,
    # symbol='Year',
    # symbol_map={'2005': 'square-open', '2010': 3},
    # size='resized_pop',
    # size_max=50,
    log_x=True,
    # range_z=[9, 13],
    template='ggplot2',
    title='Female Labor Force Participation analysis',
    labels={'Years in school (avg)': 'Years Women are in School'},
    hover_name='Entity',
    height=700,
    # animation_frame='Year',
)

pio.show(fig)
