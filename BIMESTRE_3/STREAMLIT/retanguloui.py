from retangulo import Retangulo
import streamlit as st

class RetanguloUI:
    def main(): 
        st.header('Cálculos com retângulo: ')
        b = st.text_input('Informe a base: ')
        h = st.text_input('Informe a altura: ')
        if st.button('Calcular'): 
            r = Retangulo(float(b), float(h))
            st.write(f'Área = {r.area():.2f}')
            st.write(f'Diagonal = {r.diagonal():.2f}')
            st.write(r)