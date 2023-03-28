import streamlit as st
import pandas as pd

def main():
    st.title('es. numero 1')

age = int(input('inserire eta'))
patente = bool(int(input('hai la patente?0 se non la hai,altro nmero se la hai')))
if age >= 18 and patente == True:
    print('puoi guidare')
elif age >= 18 and patente == False:
    print('non puoi guidare')
elif age < 18 and age >= 0 and patente == False:
    print('non puoi guidare')
else :
    print('errore generale')
    
    
    
    if __name__ == '__main__':
        main()