import streamlit as st
from service import Service
import time
import pandas as pd
from datetime import datetime

class MeusServicosUI: 
    def main(): 
        horarios = Service.horario_listar()
        if len(horarios) == 0: st.write("Nenhum horário registrado")
        else:
            list_dic = []
            for obj in horarios:
                if obj.get_id_cliente == st.session_state["usuario_id"]: 
                    servico = Service.servico_listar_id(obj.get_id_servico())
                    profissional = Service.profissional_listar_id(obj.get_id_profissional())
                    if cliente != None: cliente = cliente.get_nome()
                    if servico != None: servico = servico.get_descricao()
                    if profissional != None: profissional = profissional.get_nome()
                    list_dic.append({"id" : obj.get_id(), "data" : obj.get_data(),
                    "confirmado" : obj.get_confirmado(),
                    "serviço" : servico, "Profissional" : profissional})
            df = pd.DataFrame(list_dic)
            st.dataframe(df)