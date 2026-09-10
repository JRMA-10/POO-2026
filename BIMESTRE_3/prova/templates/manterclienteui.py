import streamlit as st
import pandas as pd
import time
from service import Service

class ManterClienteUI:
    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterClienteUI.listar()
        with tab2: ManterClienteUI.inserir()
        with tab3: ManterClienteUI.atualizar()
        with tab4: ManterClienteUI.excluir()
    def listar():
        clientes = Service.cliente_listar()
        if len(clientes) == 0: st.write("Nenhum cliente cadastrado")
        else:
            list_dic = []
            for obj in clientes:
                convenio = Service.convenio_listar_id(obj.get_id_convenio())
                if convenio != None: convenio = convenio.get_nome()
                list_dic.append({"id": obj.get_id(), "nome" : obj.get_nome(), "email" : obj.get_email(), "fone" : obj.get_fone(), "convenio" : convenio})
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    def inserir():
        convenios = Service.convenio_listar()
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        convenio = st.selectbox("Informe o convênio", convenios, index = None)
        if st.button("Inserir"):
            id_convenio = None
            if convenio != None: id_convenio = convenio.get_id()
            Service.cliente_inserir(nome, email, fone, id_convenio)
            st.success("Cliente inserido com sucesso")
            time.sleep(2)
            st.rerun()
    def atualizar():
        clientes = Service.cliente_listar()
        if len(clientes) == 0: st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Atualização de Clientes", clientes)
            nome = st.text_input("Novo nome", op.get_nome())
            email = st.text_input("Novo e-mail", op.get_email())
            fone = st.text_input("Novo fone", op.get_fone())
            if st.button("Atualizar"):
                id = op.get_id()
                Service.cliente_atualizar(id, nome, email, fone)
                st.success("Cliente atualizado com sucesso")
                time.sleep(2)
                st.rerun()
    def excluir():
        clientes = Service.cliente_listar()
        if len(clientes) == 0: st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Exclusão de Clientes", clientes)
            if st.button("Excluir"):
                id = op.get_id()
                Service.cliente_excluir(id)
                st.success("Cliente excluído com sucesso")
                time.sleep(2)
                st.rerun()