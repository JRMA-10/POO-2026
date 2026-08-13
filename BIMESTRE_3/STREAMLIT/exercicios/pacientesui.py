import streamlit as st
from pacientes import Paciente

class PacienteUI: 
    def main():
        st.header('Dados do paciente: ')
        nome = st.text_input('Informe o seu nome: ')
        cpf = st.text_input('Informe o seu CPF: ')
        telefone = st.text_input('informe o seu telefone: ')
        nascimento = st.text_input('Informe a sua data de nascimento: ')
        if st.button('Ver idade'): 
            o = Paciente(nome, cpf, telefone, nascimento)
            st.write(o)
            st.write(o.idade())


PacienteUI.main()