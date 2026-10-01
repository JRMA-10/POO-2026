import streamlit as st
from service import Service
import time
import pandas as pd
from datetime import datetime

class ConfirmarServicoUI: 
    def main(): 
        st.header("Abrir minha agenda")
        horarios = Service.visualizar_agenda(st.session_state["usuario_id"])
        horario = st.selectbox("Selecione o horário", horarios, index = None)
        id_cliente = horario.get_id_cliente()
        cliente = st.selectbox(Service.cliente_listar_id(id_cliente))
        if st.button("Confirmar"): 
            Service.horario_atualizar(horario.get_id(), horario.get_data(), True, horario.get_id_cliente(), horario.get_id_servico(), horario.get_id_profissional())