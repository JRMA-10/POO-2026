import streamlit as st
from service import Service
import pandas as pd
import time

class ManterServicoUI: 
    def main(): 
        st.header("Cadastro de Serviços")
        tab1, tab2, tab3, tab4 = st.tabs(['Listar', 'Inserir', 'Atualizar', 'Excluir'])
        with tab1: ManterServicoUI.listar()
        with tab2: ManterServicoUI.inserir()
        with tab3: ManterServicoUI.atualizar()
        with tab4: ManterServicoUI.excluir()

    def listar(): 
        servicos = Service.cliente_listar()
        if len(servicos) == 0: st.write('Nenhum serviço cadastrado!')
        else: 
            list_dic = []
            for obj in servicos: list_dic.append(obj.to_json())
            df = pd.Dataframe(list_dic)
            st.dataframe(df)
    
    def inserir():
        descricao = st.text_input('Informe a descrição do serviço: ')
        valor = st.text_input('Informe o valor: ')
        if st.button('Inserir'): 
            Service.servico_inserir(descricao, valor)
            st.success('Serviço inserido com sucesso')
            time.sleep(2)
            st.rerun()
    
    def atualizar(): 
        servicos = Service.servico_listar()
        if len(servicos) == 0: st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Atualização de Clientes", servicos)
            descricao = st.text_input("Nova descrição: ", op.get_descricao())
            valor = float(st.text_input("Novo valor: ", op.get_valor()))
            if st.button("Atualizar"):
                id = op.get_id()
                Service.cliente_atualizar(id, descricao, valor)
                st.success("Serviço atualizado com sucesso")
                time.sleep(2)
                st.rerun()
    
    def excluir(): 
        servicos = Service.servico_listar()
        if len(servicos) == 0: st.write("Nenhum serviço cadastrado")
        else:
            op = st.selectbox("Exclusão de Serviço", servicos)
            if st.button("Excluir"):
                id = op.get_id()
                Service.servico_excluir(id)
                st.success("Serviço excluído com sucesso")