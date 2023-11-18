import pywhatkit as pt
import streamlit as st
import win32
import pandas as pd
import threading

import sqlite3
# import datetime 
# from datetime import datetime
from datetime import datetime

class BotZap:
    def __init__(self):
        
        self.list_contatos = ['+351911172781']

        self.itens_pag()

    def itens_pag(self):
        st.title('Enviar Menssagens')
        menssagem = st.text_area('Qual a messagem que desja enviar:')
        
        if st.checkbox('Deseja agendar?'):
            # agora = datetime.now()
            
            # dia_atual = agora.day
            # horas = agora.hour
            # minuto_atual = agora.minute + 1
            # segundo_atual = agora.second
            
            selected_time = st.time_input("Selecione um horário: ")
            
            if st.button('Iniciar'):
                horas = selected_time.hour
                minutos = selected_time.minute
                segundos = selected_time.second
                self.enviar_mensagem_massa_agendada(menssagem, horas, minutos, segundos)
        else:
            if st.button('Iniciar'):
                # socket_threding = threading.Thread(target=self.enviar_mensagem_massa_instantanea, args=(menssagem,))
                # socket_threding.start()
                self.enviar_mensagem_massa_instantanea(menssagem)
        
    def enviar_mensagem_massa_instantanea(self, menssagem):
        cont = 1
        for i in range(0,2):
            agora = datetime.now()
            
            dia_atual = agora.day
            horas = agora.hour
            minuto_atual = agora.minute + 1
            segundo_atual = agora.second
            
            print(f'Menssagem para {self.list_contatos[0]} às {horas}:{minuto_atual}:{segundo_atual} do dia {dia_atual}')

            try:
                st.toast(f'Enviando messagem para {self.list_contatos[0]}')
                # pt.sendwhatmsg(i, menssagem, horas, minuto_atual)
                # self.salvar_dados('João',i,str(data_formatada),f'{horas}:{minuto_atual}', menssagem)
                pt.sendwhatmsg(self.list_contatos[0], f'{menssagem} - {cont}', horas, minuto_atual,segundo_atual, True,2)
                self.salvar_dados(self.list_contatos[0],self.list_contatos[0],str(dia_atual),f'{horas}:{minuto_atual}:{segundo_atual}', f'{menssagem} - {cont}')
                cont+=1
                st.toast(f'Menssagem enviada com sucesso para {self.list_contatos[0]}')
                
            except:
                st.toast(f'Houve um erro')
                break
    
    def enviar_mensagem_massa_agendada(self, menssagem, horas, minutos, segundos):
        cont = 1
        for i in range(0,2):
            agora = datetime.now()
            
            dia_atual = agora.day
            
            print(f'Menssagem para {self.list_contatos[0]} agendada às {horas}:{minutos}:{segundos} do dia {dia_atual}')

            try:
                st.toast(f'Menssagem para {self.list_contatos[0]} agendada às {horas}:{minutos}:{segundos} do dia {dia_atual}')
                # pt.sendwhatmsg(i, menssagem, horas, minuto_atual)
                # self.salvar_dados('João',i,str(data_formatada),f'{horas}:{minuto_atual}', menssagem)
                pt.sendwhatmsg(self.list_contatos[0], f'{menssagem} - {cont}', horas, minutos,segundos, True,2)
                self.salvar_dados(self.list_contatos[0],self.list_contatos[0],str(dia_atual),f'{horas}:{minutos}:{segundos}', f'{menssagem} - {cont}')
                cont+=1
                st.toast(f'Menssagem enviada com sucesso para {self.list_contatos[0]}')
                
            except:
                st.toast(f'Houve um erro')
                break
    
    def salvar_dados(self,nome, telefone, data, hora, mensagem):
        # Conexão com o banco de dados
        conn = sqlite3.connect('database.db')

        # Cursor para executar comandos SQL
        cursor = conn.cursor()

        # Comando SQL para inserir dados na tabela
        comando_sql = '''
            INSERT INTO Mensagens (Nome, NumeroTelefone, Data, Hora, Mensagem)
            VALUES (?, ?, ?, ?, ?)
        '''

        # Parâmetros para o comando SQL
        parametros = (nome, telefone, data, hora, mensagem)

        # Executa o comando SQL para inserir os dados
        cursor.execute(comando_sql, parametros)

        # Commit das mudanças e fechamento da conexão
        conn.commit()
        conn.close()

        st.toast("Dados salvos com sucesso!")             
            
if __name__ == '__main__':
    BotZap()