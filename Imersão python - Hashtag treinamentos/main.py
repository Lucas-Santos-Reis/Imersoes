import streamlit as st
#Streamlit permite a criação de front e back juntos
from openai import OpenAI
modelo_ia = OpenAI(api_key='')


st.write('# Chatbot com IA') #O método write do streamlit é markdown
if not 'lista_mensagens' in st.session_state: 
    st.session_state['lista_mensagens'] = [{'role':'system', 'content': 'Prompt inicial com orientações'}]
#Confere se o usuário já executou o chatbot, se não executou, cria uma lista vazia para armazenar as mensagens enquanto a sessão está ativa, esse armazenamento ocorre nos cookies do site.

texto_usuario = st.chat_input('Digite sua mensagem: ') #Cria uma caixa de texto para o usuário digitar e armazena a mensagem em uma variável

for mensagem in st.session_state['lista_mensagens']:
    role = mensagem['role']
    content = mensagem['content']
    st.chat_message(role).write(content)
#percorre a lista de mensagem e os dicionários contidos, buscando os dados e apresentando eles na tela.

if texto_usuario: #Se o usuário digitou algo:    
    st.chat_message('user').write(texto_usuario)
    #Parâmetros do chat_message:
    #nome -> Aparece a inicial do nome que você passar
    #user -> Aparece um ícone de usuário
    #assistant -> Aparece um ícone de robô
    #system -> prompt inicial com orientações para a IA

    mensagem_usuario = {'role': 'user', 'content': texto_usuario}
    st.session_state['lista_mensagens'].append(mensagem_usuario)
    #Salva a mensagem do usuário em um dicionário e este dicionário na lista
    #ia respondeu:
    resposta_ia = modelo_ia.chat.completions.create(st.session_state['lista_mensagens'], model='gpt-4o')
    texto_ia = resposta_ia[0].message.content
    #a resposta da IA vem com várias informações, n° de tokens gastos, quem mandou, porcentagem de ser veridico e a resposta.
    texto_ia = 'você perguntou: ' + texto_usuario
    st.chat_message('assistant').write(texto_ia)
    mensagem_ia = {'role': 'assistant', 'content': texto_ia}
    st.session_state['lista_mensagens'].append(texto_ia)
    #Salva a mensagem da IA em um dicionário e este dicionário na lista


print(st.session_state['lista_mensagens'])




#Para rodar o streamlit deve abrir o terminal e digitar streamlit run nome do aquivo, no caso:
#streamlit run main.py
