import streamlit as st
import pandas as pd


def paridispari(a):
    if a % 2 == 0:
        pari = 'il numero è pari'
        return pari
    else:
        dispari = 'il numero è dispari'
        return dispari


def main():


    st.title('es. numero 3')

    num1 = st.slider('inserisci un numero!', 1, 100)

    caso1 = paridispari(num1)

    st.write(caso1)

    num2 = st.slider('inserisci un altro numero!', 1, 100)

    caso2 = paridispari(num2)

    st.write(caso2)

    par1 = st.number_input('inserisci un numero!',0,1000)
    
    

    parole1 = paridispari(par1)

    st.write(parole1)
  

if __name__ == '__main__':
    main()

    # Es3) Inserendo un numero intero determinare se è pari o dispari
    # (anche qui input come slicer ed input come cella testo)
