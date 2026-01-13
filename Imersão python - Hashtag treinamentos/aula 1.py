from time import sleep
import pyautogui
import pandas as pd
#Principais funcionalidades:
#pyautogui.click -> clica
#pyautogui.write -> escreve um texto
#pyautogui.press -> aperta uma tecla
#pyautogui.hotkey -> aperta um atalho (hotkey)
pyautogui.PAUSE = 0.5 #vai colocar uma pausa entre um comando e outro
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
email = 'lreisfreitas@gmail.com'
senha = 'LuK@ryna2805'
pyautogui.press('win') #tecla windowns
pyautogui.write('edge') 
pyautogui.press('enter')
pyautogui.write(link)
pyautogui.press('enter')
sleep(3) #É recomendado uma pausa maior para esperar o site carregar, além de dificultar a percepção de sites para bot
pyautogui.click(x=517, y=369) #posição do email
pyautogui.write(email)
#a tecla TAB pula de uma parte do formulário para a próxima
pyautogui.press('tab') #passa pra senha
pyautogui.write(senha) #digita a senha
pyautogui.press('tab') #passa pro login
pyautogui.press('enter')#faz o login
sleep(4) #pausa pro sistema carregar

tabela = pd.read_csv('C:\Users\LuKa\Documents\MeusProjetos\Imersoes\Imersão python - Hashtag treinamentos\produtos.csv')

print(tabela)