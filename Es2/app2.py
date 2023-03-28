import streamlit as st
import pandas as pd

def main():
    st.title('Esercizio numero 2')

    num1 = st.slider('inserire il primo numero',0,100)
    st.write("ho ", num1, ' anni')
    
    num2 = st.slider('inserire il secondo numero',0,100)
    st.write("ho ", num2, ' anni')
    
    num3 = st.slider('inserire il terzo numero',0,100)
    st.write("ho ", num3, ' anni')
    

    def checknum (a,b,c):
        if a > b and a > c:
            caso = st.write(a,'è il numero maggiore dei tre')
            return caso
        elif b > a and b > c:
            caso = st.write(b,'è il numero maggiore dei tre')
            return caso
        elif c > a and c > b:
            caso = st.write(c,'è il numero maggiore dei tre')
            return caso
        
    caso = checknum(num1,num2,num3)

    st.write(caso)
    
if __name__ == '__main__':
    main()