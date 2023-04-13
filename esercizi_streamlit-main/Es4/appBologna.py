
from matplotlib.offsetbox import OffsetImage
from matplotlib.patches import Arc, Rectangle, ConnectionPatch
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.io.json import json_normalize
import json
import streamlit as st
from FCPython import createPitch



 

pitch_width = 120
pitch_height = 80
fig, ax = createPitch(pitch_width, pitch_height, 'yards', 'gray')

fig

# st.set_page_config(layout="wide")

st.title('Bologna Calcio 2021-2022')
st.subheader('Players by G+A')
df = pd.read_csv('Es4/Bologna_22.csv')
df1 = df.sort_values(by=['G+A'], ascending=False)
df2 = df.sort_values(by=['Nation'])
df2 = df2.dropna()
df3 = df.sort_values(by=['Min'], ascending=False)
df3 = df3.dropna()
df1 = df1.dropna()
df1
st.subheader('Players by Nation')
df2
st.write('Bologna players by nationality(players with at least 1 min)')
st.subheader('Players by Min')
df3
st.write('Bologna players by min played(players with at least 1 min)')


# dfplayer = df['Player']
# dflist = dfplayer.values.tolist()
# playerlist = []

# for i in dflist:
#     playerfiltered = i.split("\\")
#     playerlist.append(playerfiltered[0])

# df['Player'] = playerlist
# nation = df['Nation']
# nation

# SETTING THE TITLE
title = "Player selector"  # SETTING LAYOUT
#
# using whole page#DISPLAYING THE TITLE
st.title(title)
# DISPLAYING A HORIZONTAL LINE TO SEPERATE CONTENT
st.markdown("---")
# CREATING A SIDEBAR WITH FILTER FOR PLAYERS
st.header("Choose a player:")
player = st.selectbox(
    'Select here:',
    options=df["Player"].unique())  # posso scegliere come opzione ogni valore univoco sulla colonna players

df_selection = df.query(  # seleziona tutta la riga
    # @ si riferisce ad una variabile creata da me,gli sto dicendo di assegnare a df_selections la riga dove avviene la query,che entry ho scelto sulla colonna Players
    "Player == @player"
)
st.subheader('Full player stats')
df_selection
# SELECTING THE STATS FROM THE DATA THAT WILL BE DISPLAYED

# seleziono gls dalla riga corrispondente del giocatore
goals = df_selection["Gls"].sum()
assists = df_selection["Ast"].sum()
expectedgoals = df_selection["xG"].sum()
# DISPLAYING THE SELECTED STATS INSIDE COLUMNS
left_column, middle_column, right_column, rightright_column = st.columns(4)
with left_column:
    st.subheader("Goals")
    st.subheader(f"{goals}")
with middle_column:
    st.subheader("Assists")
    st.subheader(f"{assists}")
with right_column:
    st.subheader("Expected goals")
    st.subheader(f"{expectedgoals}")
with rightright_column:
    st.subheader("Player Name")
    st.subheader(f"{player}")


# set up the figures
