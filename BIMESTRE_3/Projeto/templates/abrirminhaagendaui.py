import streamlit as st
from service import Service
import time
import pandas as pd
from datetime import datetime

class AbrirMinhaAgendaUI: 
    def main(): 
        st.header("Abrir minha agenda")
        tab1, tab2 = st.tabs(["Listar", "Inserir"])
        with tab1: AbrirMinhaAgendaUI.listar()
        with tab2: AbrirMinhaAgendaUI.inserir()

    def listar(): 
        agendamentos = Service.visualizar_agenda(st.session_state["usuario_id"])
        if len(agendamentos) == 0: st.write("Nenhum agendamento registrado")
        else:
            list_dic = []
            for obj in agendamentos: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    
    def inserir(): 
        data = st.text_input("Informe a data no formato dd/mm/aaaa", datetime.now().strftime("%d/%m/%Y"))
        horario_inicio = st.text_input("Informe o horário inicial no formato HH:MM")
        horario_fim = st.text_input("Informe o horário final no formato HH:MM")
        intervalo = st.text_input("Informe o intervalo entre cada consulta")
        if st.button("Abrir agenda"): 
            Service.horario_abrir_minha_agenda(data, horario_inicio, horario_fim, int(intervalo), st.session_state["usuario_id"])
            st.success("Horários inseridos com sucesso")
            time.sleep(2)
            st.rerun()