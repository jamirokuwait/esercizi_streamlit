import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv('energia.csv')
# df
st.title('Carico il df da file')

st.write('inputbox per scegliere cosa caricare')
Energia = st.file_uploader("Carica il file scegliendolo dal pc", type={"csv"})

st.write('visualizzazione del CSV')
if Energia is not None:
    Energia_df = pd.read_csv(Energia)
st.write(Energia_df)

df1 = Energia_df.set_index('Territorio')

st.write('Raggruppo per Territorio')
st.write(df1)
# def main():
# if __name__ == '__main__':
#     main()
