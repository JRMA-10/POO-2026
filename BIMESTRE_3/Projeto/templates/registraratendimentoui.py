import streamlit as st
import pandas as pd
from service import Service
import time
from datetime import datetime

class RegistrarAtendimentoUI:
    def main():
        st.header("Atendimentos")
        tab1, tab2, tab3 = st.tabs(["Listar", "Inserir", "Valores", "Visualizar"]) # Abas
        with tab1: RegistrarAtendimentoUI.listar()
        with tab2: RegistrarAtendimentoUI.inserir()
        with tab3: RegistrarAtendimentoUI.valores()
        with tab4: RegistrarAtendimentoUI.visualizar()

    def listar(): 
        atendimentos = Service.atendimento_listar()
        if len(atendimentos) == 0: st.write("Nenhum atendimento cadastrado")
        else:
            list_dic = []
            for obj in atendimentos: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    
    def inserir():
        data = st.text_input("Informe a Data", datetime.strftime(datetime.now(), "%d/%m/%Y"))
        queixa_principal = st.text_input("Informe a queixa principal")
        historico_saude = st.text_input("Informe o histórico de saúde")
        avaliacao = st.text_input("Informe a avaliação")
        prescricao = st.text_input("Informe a prescrição")
        horarios = Service.horario_listar()
        horario = st.selectbox("Selecione o horário", horarios)
        pago = st.checkbox("Pago")
        if st.button("Atualizar"):
            Service.atendimento_inserir(data, queixa_principal, historico_saude, avaliacao, prescricao, horario.get_id())
            st.success("Atendimento atualizado com sucesso")
            time.sleep(2)
            st.rerun()
    def valores(): 
        atendimentos = Service.atendimento_listar()
        servicos = Service.servico_listar()
        atendimento = st.selectbox("Selecione um atendimento", atendimentos)
        servico = st.selectbox("Selecione um serviço", servicos)
        qnt = int(st.text_input("Informe a quantidade"))
        valor = st.text_input(f"{servico.get_valor() * qnt}", disabled = True)
        if st.button('Enviar'): 
            Service.atendimento_itens_inserir(atendimento.get_id(), servico.get_id(), qnt, valor)
    def visualizar():
        atendimentos = Service.atendimento_listar()
        atendimento = st.selectbox("Selecione o atendimento", atendimentos)
        