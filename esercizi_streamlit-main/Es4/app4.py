import json
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsbombpy as sb
from pandas.io.json import json_normalize
from FCPython import createPitch
from matplotlib.offsetbox import OffsetImage
from matplotlib.patches import Arc, Rectangle, ConnectionPatch
import seaborn as sns


st.title('SELECT YOUR CSV')

st.write('CHOOSING FROM STATSBOMB DATA')
calcio = st.file_uploader("Carica il file scegliendolo dal pc", type={"json"})

st.write('MAJOR COMPETITION RECORDED')
if calcio is not None:
    calcio_df = pd.read_json(calcio)
st.write(calcio_df)
st.write('SEARCHING FOR 2018 FIFA WORLD CUP MATCHES')
st.write(calcio_df[calcio_df.competition_name == 'FIFA World Cup'])


# with open('open-data-master/data/matches/43/3.json') as f:
# carica idati delle squadre,match,dati sulle partite generali
# data = json.load(f)
# salto questa parte per il retrieve degli id delle partite della competizione
# st.write('displaying every match,with ID and group')
# for i in data:
#     x = st.write('ID:', i['match_id'],  i['home_team']['home_team_name'],  # carico i dati relativi a squadre e risultato
#                  i['home_score'], '-', i['away_score'], i['away_team']['away_team_name'], '-', i['home_team']['home_team_group'])

with open('open-data-master/data/events/7567.json') as f:
    korger = json.load(f)  # carico eventi partita specifica

df = pd.json_normalize(korger, sep='_').assign(match_id="7567")


cols = list(df.columns.values)  # Make a list of all of the columns in the df
cols.pop(cols.index('id'))  # Remove b from list
cols.pop(cols.index('index'))  # Remove b from list
cols.pop(cols.index('period'))  # Remove b from list
cols.pop(cols.index('minute'))  # Remove b from list
cols.pop(cols.index('second'))  # Remove b from list
cols.pop(cols.index('possession'))  # Remove b from list
cols.pop(cols.index('tactics_formation'))  # Remove b from list
cols.pop(cols.index('tactics_lineup'))  # Remove b from list
cols.pop(cols.index('play_pattern_id'))  # Remove b from list
cols.pop(cols.index('type_id'))  # Remove b from list
cols.pop(cols.index('team_id'))  # Remove b from list
cols.pop(cols.index('player_id'))  # Remove b from list
cols.pop(cols.index('position_id'))  # Remove b from list
cols.pop(cols.index('possession_team_id'))  # Remove b from list
df = df[cols+['id', 'index', 'period', 'minute',
              'second', 'possession', 'possession_team_id', 'tactics_formation', 'tactics_lineup', 'play_pattern_id', 'type_id', 'team_id', 'player_id', 'position_id']]  # addo alla fine

home_team = 'South Korea'
away_team = 'Germany'
Actionpass = 'Pass'
Actionshot = 'Shot'
Actionpress = 'Pressure'
p1 = '1st period'
p2 = '2nd period'

# playerskor = df[df.team_name == 'South Korea']
# questo prende tutto il df.unique e drop non funziano sul df intero
# playersger = df[df.team_name == 'Germany']

team_1 = df['team_name'].unique()[0]
mask_1 = df.loc[df['team_name'] == team_1]
player_names_1 = mask_1['player_name'].dropna().unique()

team_2 = df['team_name'].unique()[1]
mask_2 = df.loc[df['team_name'] == team_2]
player_names_2 = mask_2['player_name'].dropna().unique()


menu_team = st.sidebar.selectbox('Select Team', (team_1, team_2))
menu_action = st.sidebar.selectbox(
    'Select action', (Actionpass, Actionshot, Actionpress))

if menu_team == team_1:
    menu_player = st.sidebar.selectbox('Select Player', player_names_1)
else:
    menu_player = st.sidebar.selectbox('Select Player', player_names_2)

menu_time = st.sidebar.selectbox('Select period', (p1, p2))


pressure = df[df.type_name == 'Pressure']
pressureger = pressure[pressure.team_name == 'Germany']
pressurekor = pressure[pressure.team_name == 'South Korea']
pressure1 = pressure[pressure.period == 1]
pressure2 = pressure[pressure.period == 2]

pressure1ger = pressure1[pressure1.team_name == 'Germany']
pressure2ger = pressure2[pressure2.team_name == 'Germany']
pressure1kor = pressure1[pressure1.team_name == 'South Korea']
pressure2kor = pressure2[pressure2.team_name == 'South Korea']

press1ger = pressure1ger[pressure1ger.player_name == menu_player]
press2ger = pressure2ger[pressure2ger.player_name == menu_player]
press1kor = pressure1kor[pressure1kor.player_name == menu_player]
press2kor = pressure2kor[pressure2kor.player_name == menu_player]


passages = df[df.type_name == 'Pass']
passages1 = passages[passages.period == 1]
passages2 = passages[passages.period == 2]

passages1ger = passages1[passages1.team_name == 'Germany']
passages1kor = passages1[passages1.team_name == 'South Korea']
passages2ger = passages2[passages2.team_name == 'Germany']
passages2kor = passages2[passages2.team_name == 'South Korea']

pass1ger = passages1ger[passages1ger.player_name == menu_player]
pass2ger = passages2ger[passages2ger.player_name == menu_player]
pass1kor = passages1kor[passages1kor.player_name == menu_player]
pass2kor = passages2kor[passages2kor.player_name == menu_player]

shots = df[df.type_name == 'Shot']

shots1 = shots[shots.period == 1]
shots2 = shots[shots.period == 2]

shotskor = shots[shots.team_name == 'South Korea']
shots1kor = shots1[shots1.team_name == 'South Korea']
shots2kor = shots2[shots2.team_name == 'South Korea']

shotsger = shots[shots.team_name == 'Germany']
shots1ger = shots1[shots1.team_name == 'Germany']
shots2ger = shots2[shots2.team_name == 'Germany']

sht1ger = shots1ger[shots1ger.player_name == menu_player]
sht2ger = shots2ger[shots2ger.player_name == menu_player]
sht1kor = shots1kor[shots1kor.player_name == menu_player]
sht2kor = shots2kor[shots2kor.player_name == menu_player]


golkor = shotskor[shotskor.shot_outcome_name == 'Goal']


st.subheader('visualizzo i tiri effettuati dalla Corea')
shotskor
st.subheader('visualizzo passaggi Korea')
passages1kor
st.subheader('Pressure Korea')
pressurekor
st.header('Goal event')
golkor
st.subheader('visualizzo i tiri effettuati dalla Germania')
shotsger
st.subheader('visualizzo passaggi Germania')
passages1ger
st.subheader('Pressure Germania')
pressureger


pitch_width = 120
pitch_height = 80

fig, ax = createPitch(pitch_width, pitch_height, 'yards', 'gray')


############# GRAFICO TIRI###################


color = 'blue' if menu_team == home_team else 'red'


if menu_action == Actionshot:
    plt.text(5, 75, away_team + ' shots')
    plt.text(80, 75, home_team + ' shots')
    if menu_time == p1:

        if menu_team == home_team:

            for i, shot in sht1kor.iterrows():
                x = shot['location'][0]
                y = shot['location'][1]

                goal = shot['shot_outcome_name'] == 'Goal'
                team_name = shot['team_name']

                circle_size = 2
                circle_size = np.sqrt(shot['shot_statsbomb_xg'] * 15)

                if goal:
                    shot_circle = plt.Circle(
                        (x, pitch_height-y), circle_size, color='blue')
                    plt.text((x+1), pitch_height-y+1, shot['player_name'])

                else:
                    shot_circle = plt.Circle(
                        (x, pitch_height-y), circle_size, color='blue')
                    shot_circle.set_alpha(.2)
                if menu_team == home_team:
                    ax.add_patch(shot_circle)
        elif menu_team == away_team:

            for i, shot in sht1ger.iterrows():
                x = shot['location'][0]
                y = shot['location'][1]

                goal = shot['shot_outcome_name'] == 'Goal'
                team_name = shot['team_name']

                circle_size = 2
                circle_size = np.sqrt(shot['shot_statsbomb_xg'] * 15)
                if goal:
                    shot_circle = plt.Circle(
                        (pitch_width-x, y), circle_size, color='red')
                    plt.text((pitch_width-x+1), y+1, shot['player_name'])
                else:
                    shot_circle = plt.Circle(
                        (pitch_width-x, y), circle_size, color='red')
                    shot_circle.set_alpha(.2)
                if menu_team == away_team:
                    ax.add_patch(shot_circle)
    elif menu_time == p2:
        if menu_team == home_team:

            for i, shot in sht2kor.iterrows():
                x = shot['location'][0]
                y = shot['location'][1]

                goal = shot['shot_outcome_name'] == 'Goal'
                team_name = shot['team_name']

                circle_size = 2
                circle_size = np.sqrt(shot['shot_statsbomb_xg'] * 15)

                if goal:
                    shot_circle = plt.Circle(
                        (x, pitch_height-y), circle_size, color='blue')
                    plt.text((x+1), pitch_height-y+1, shot['player_name'])

                else:
                    shot_circle = plt.Circle(
                        (x, pitch_height-y), circle_size, color='blue')
                    shot_circle.set_alpha(.2)
                if menu_team == home_team:
                    ax.add_patch(shot_circle)
        elif menu_team == away_team:

            for i, shot in sht2ger.iterrows():
                x = shot['location'][0]
                y = shot['location'][1]

                goal = shot['shot_outcome_name'] == 'Goal'
                team_name = shot['team_name']

                circle_size = 2
                circle_size = np.sqrt(shot['shot_statsbomb_xg'] * 15)
                if goal:
                    shot_circle = plt.Circle(
                        (pitch_width-x, y), circle_size, color='red')
                    plt.text((pitch_width-x+1), y+1, shot['player_name'])
                else:
                    shot_circle = plt.Circle(
                        (pitch_width-x, y), circle_size, color='red')
                    shot_circle.set_alpha(.2)
                if menu_team == away_team:
                    ax.add_patch(shot_circle)
elif menu_action == Actionpass:
    plt.text(5, 75, away_team + ' pass')
    plt.text(80, 75, home_team + ' pass')
    if menu_time == p1:
        if menu_team == away_team:
            for i, pas in pass1ger.iterrows():
                x = pas['location'][0]
                y = pas['location'][1]
                x1 = pas['pass_end_location'][0]
                y1 = pas['pass_end_location'][1]
                u = x1-x
                v = y1-y

                # passage = pas['type_name'] == 'Pass'
                # team_name = pas['team_name']
                ax.quiver(x, y, u, v, color=color, width=0.003, headlength=4.5)
        elif menu_team == home_team:
            for i, pas in pass1kor.iterrows():
                x = pas['location'][0]
                y = pas['location'][1]
                x1 = pas['pass_end_location'][0]
                y1 = pas['pass_end_location'][1]
                u = x1-x
                v = y1-y

                # passage = pas['type_name'] == 'Pass'
                # team_name = pas['team_name']
                ax.quiver(x, y, u, v, color=color, width=0.003, headlength=4.5)

    elif menu_time == p2:
        if menu_team == home_team:
            for i, pas in pass2kor.iterrows():
                x = pas['location'][0]
                y = pas['location'][1]
                x1 = pas['pass_end_location'][0]
                y1 = pas['pass_end_location'][1]
                u = x1-x
                v = y1-y

                passage = pas['type_name'] == 'Pass'
                team_name = pas['team_name']

                ax.quiver(x, y, u, v, color=color, width=0.003, headlength=4.5)
        elif menu_team == away_team:
            for i, pas in pass2ger.iterrows():
                x = pas['location'][0]
                y = pas['location'][1]
                x1 = pas['pass_end_location'][0]
                y1 = pas['pass_end_location'][1]
                u = x1-x
                v = y1-y

                passage = pas['type_name'] == 'Pass'
                team_name = pas['team_name']

                ax.quiver(x, y, u, v, color=color, width=0.003, headlength=4.5)
elif menu_action == Actionpress:
    plt.text(5, 75, away_team + ' pressing')
    plt.text(80, 75, home_team + ' pressing')
    dot_size = 2
    if menu_time == p1:

        if menu_team == home_team:

            for i, pres in press1kor.iterrows():
                x = pres['location'][0]
                y = pres['location'][1]
                dot_size = 2

                dot = plt.Circle((x, y), dot_size, color=color, alpha=0.5)
                ax.add_patch(dot)

        elif menu_team == away_team:

            for i, pres in press1ger.iterrows():
                x = pres['location'][0]
                y = pres['location'][1]
                dot_size = 2

                dot = plt.Circle((x, y), dot_size, color=color, alpha=0.5)
                ax.add_patch(dot)
    elif menu_time == p2:
        if menu_team == home_team:

            for i, pres in press2kor.iterrows():
                x = pres['location'][0]
                y = pres['location'][1]
                dot_size = 2
                dot = plt.Circle((x, y), dot_size, color=color, alpha=0.5)
                if menu_team == home_team:
                    ax.add_patch(dot)
        elif menu_team == away_team:

            for i, pres in press2ger.iterrows():
                x = pres['location'][0]
                y = pres['location'][1]
                dot_size = 2
                dot = plt.Circle((x, y), dot_size, color=color, alpha=0.5)
                if menu_team == away_team:
                    ax.add_patch(dot)

plt.title('Germany vs South Korea at 2018 FIFA World Cup')
fig.set_size_inches(10, 7)
fig.savefig('korger_shots.png', dpi=300)
st.pyplot(fig)

st.header(menu_player)

df_selection = df.query(
    'player_name == @menu_player')
df_selection1 = df_selection[df_selection.period == 1]
df_selection2 = df_selection[df_selection.period == 2]

df_pass1 = df_selection1[df_selection1.type_name == 'Pass']
df_pass2 = df_selection2[df_selection2.type_name == 'Pass']

df_shot1 = df_selection1[df_selection1.type_name == 'Shot']
df_shot2 = df_selection2[df_selection2.type_name == 'Shot']


if menu_action == Actionpass:
    if menu_time == p1:
        st.subheader('Full pass event about selected player(1st half)')
        df_pass1
    elif menu_time == p2:
        st.subheader('Full pass event about selected player(2nd half)')
        df_pass2
elif menu_action == Actionshot:
    if menu_time == p1:
        st.subheader('Full shot event about selected player(1st half)')
        df_shot1
    elif menu_time == p2:
        st.subheader('Full shot event about selected player(2nd half)')
        df_shot2
else:
    if menu_time == p1:
        st.subheader('Full event list about selected player(1st half)')
        df_selection1
    elif menu_time == p2:
        st.subheader('Full event list about selected player(2nd half)')
        df_selection2

# df_selection1
# df_selection2

# def main():
# if __name__ == '__main__':
#     main()
