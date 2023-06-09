import streamlit as st
import pandas as pd

    #FUNZIONE PER IL RETRIEVE DEL MAGGIORE DA SLIDER
def checknummax(a, b, c):
       if a > b and a > c:
            caso = st.write(a, 'è il numero maggiore dei tre')
            return caso
       elif b > a and b > c:
           caso = st.write(b, 'è il numero maggiore dei tre')
           return caso
       elif c > a and c > b:
            caso = st.write(c, 'è il numero maggiore dei tre')
            return caso
    #FUNZIONE PER IL RETRIEVE DEL MAGGIORE DA INPUT
def checknummax_(a, b, c):
       if a > b and a > c:
            caso = st.write(a, 'è il numero maggiore dei tre(input)')
            return caso
       elif b > a and b > c:
           caso = st.write(b, 'è il numero maggiore dei tre(input)')
           return caso
       elif c > a and c > b:
            caso = st.write(c, 'è il numero maggiore dei tre(input)')
            return caso
        #FUNZIONE PER IL RETRIEVE DEL MINORE DA SLIDER
def checknummin(a, b, c):
       if a < b and a < c:
           caso = st.write(a, 'è il numero minore dei tre')
           return caso
       elif b < a and b < c:
           caso = st.write(b, 'è il numero minore dei tre')
           return caso
       elif c < a and c < b:
           caso = st.write(c, 'è il numero minore dei tre')
           return caso
       #FUNZIONE PER IL RETRIEVE DEL MINORE DA INPUT
def checknummin_(a, b, c):
       if a < b and a < c:
           caso = st.write(a, 'è il numero minore dei tre(input)')
           return caso
       elif b < a and b < c:
           caso = st.write(b, 'è il numero minore dei tre(input)')
           return caso
       elif c < a and c < b:
           caso = st.write(c, 'è il numero minore dei tre(input)')
           return caso

def main():
    st.title('Esercizio numero 2')
#PRENDO DATI DA SLIDER PRIMA E DA INPUT DOPO(1 CASO)
    num1 = st.slider('inserire il primo numero', 0, 100)
    num1_1 = st.number_input('inserisci il primo numero!',0,1000)
    st.write("ho ", num1, ' anni')
    st.write("ho ", num1_1, ' anni','(numb input)')
#PRENDO DATI DA SLIDER PRIMA E DA INPUT DOPO(2 CASO)
    num2 = st.slider('inserire il secondo numero', 0, 100)
    num2_1 = st.number_input('inserisci il secondo numero!',0,1000)
    st.write("ho ", num2, ' anni')
    st.write("ho ", num2_1, ' anni','(numb input)')
#PRENDO DATI DA SLIDER PRIMA E DA INPUT DOPO(3 CASO)
    num3 = st.slider('inserire il terzo numero', 0, 100)
    num3_1 = st.number_input('inserisci il terzo numero!',0,1000)
    st.write("ho ", num3, ' anni')
    st.write("ho ", num3_1, ' anni','(numb input)')
#CHIAMO LE FUNZIONI
    checknummax(num1, num2, num3)
    checknummax_(num1_1, num2_1, num3_1)
    checknummin(num1,num2,num3)
    checknummin_(num1_1,num2_1,num3_1)
    
    # caso = checknummax(num1, num2, num3),checknummin(num1,num2,num3)
    # caso2 = checknummax(num1_1, num2_1, num3_1),checknummin(num1_1,num2_1,num3_1)
    
    # st.write('input slide:',checknummax(num1, num2, num3),'input slide:',checknummin(num1,num2,num3),'input slide:',checknummax(num1_1, num2_1, num3_1),'input slide:',checknummin(num1_1,num2_1,num3_1))
    #st.write('input:',checknummax(num1_1, num2_1, num3_1),'input:',checknummin(num1_1,num2_1,num3_1))

if __name__ == '__main__':
    main()
