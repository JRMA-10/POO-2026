import streamlit as st
from service import Service
import pandas as pd
import time

class ManterClienteUI: 
    def main(): 
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(['Listar', 'Inserir', 'Atualizar', 'Excluir'])
        with tab1: ManterClienteUI.listar()
        with tab2: ManterClienteUI.inserir()
        with tab3: ManterClienteUI.atualizar()
        with tab4: ManterClienteUI.excluir()

        def listar(): 
            clientes = Service.cliente_listar()
            if len(clientes) == 0: st.write('Nenhum cliente cadastrado!')
            else: 
                list_dic = []
                for obj in clientes: list_dic.append(obj.to_json())
                df = pd.Dataframe(list_dic)
                st.dataframe(df)
        def inserir():
            nome = st.text_input('Informe o nome: ')
            email = st.text_input('Informe o email: ')
            fone = st.text_input('Informe o número: ')
            if st.button('Inserir'): 
                Service.cliente_inserir(nome, email, fone)
                st.sucess('Cliente inserido com sucesso')
                time.sleep(2)
                st.rerun()
        def atualizar(): 
            pass
        def inserir(): 
            pass