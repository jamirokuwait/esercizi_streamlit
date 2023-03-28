import streamlit as st
import pandas as pd

# def main():
st.title('Esercizio numero 2')

num1 = st.slider('inserire un numero',0,100)
st.write("I'm ", num1, 'years old')
num2 = st.slider('inserire un altro numero',0,100)
num3 = st.slider('inserire un terzo numero',0,100)


# if __name__ == '__main__':
#     main()