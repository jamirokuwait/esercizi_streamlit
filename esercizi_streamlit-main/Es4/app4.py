import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv('energia.csv')
# df

Energia = st.file_uploader("upload file", type={"csv", "txt"})
if Energia is not None:
    Energia_df = pd.read_csv(Energia)
st.write(Energia_df)
# def main():
# if __name__ == '__main__':
#     main()
