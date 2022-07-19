# LORT!!!!

import dash
import plotly.express as px
import pandas as pd

df = pd.read_csv("vgsales.csv")


fig_lort = px.pie(data_frame=df, names='Genre', values='Japan Sales')
fig_lort.show()
