import streamlit as st
import pandas as pd


def patentecheck(age, patente):
    if age >= 18 and patente == 'si':
        caso = 'puoi guidare'
        return caso
    elif age >= 18 and patente == 'no':
        caso = 'non puoi guidare'
        return caso
    elif age < 18 and age >= 0 and patente == 'no':
        caso = 'non puoi guidare'
        return caso
    else:
        caso = 'errore generale'
    return caso


def main():

    st.title('Esercizio numero 1')
    st.subheader('piccolo esercizio per determinare le condizioni di guida')
    ageinput = st.number_input('inserire età')
    patenteinput = st.radio('hai la patente?', ('si', 'no'))
    # bool(int(input('hai la patente?0 se non la hai,altro nmero se la hai')))

    caso = patentecheck(ageinput, patenteinput)

    st.text(caso)


if __name__ == '__main__':
    main()
