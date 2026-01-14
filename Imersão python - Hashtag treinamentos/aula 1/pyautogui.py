from time import sleep
import pyautogui
import pandas as pd
#Principais funcionalidades:
#pyautogui.click -> clica
#pyautogui.write -> escreve apenas texto (se for usar números, transformar em string!!!)
#pyautogui.press -> aperta uma tecla
#pyautogui.hotkey -> aperta um atalho (hotkey) -> combinação de teclas

##PARÂMETROS
pyautogui.PAUSE = 0.5 #vai colocar uma pausa entre um comando e outro
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
email = 'lreis0364@gmail.com'
senha = 'SENHA_SUPER_DIFICIL'

## ABRE O SITE
pyautogui.press('win') #tecla windowns
pyautogui.write('edge') 
pyautogui.press('enter')
pyautogui.write(link)
pyautogui.press('enter')
sleep(3) #É recomendado uma pausa maior para esperar o site carregar, além de dificultar a percepção de sites para bot

## FAZ O LOGIN
pyautogui.click(x=517, y=369) #posição do email
pyautogui.write(email)
pyautogui.press('tab')
#a tecla TAB pula de uma parte do formulário para a próxima
pyautogui.write(senha) #digita a senha
pyautogui.press('tab') #passa pro login
pyautogui.press('enter') #clica no login
sleep(4) #pausa pro sistema carregar

##PREENCHENDO OS DADOS
tabela = pd.read_csv('produtos.csv')#Não deixar o arquivo na mesma pasta, colocar na pasta de 'fora' -> pega os dados da tabela
for linha in tabela.index: #para cada linha na tabela repita:
    #codigo
    codigo = tabela.loc[linha]['codigo']
    pyautogui.click(x=319, y=250) #Clica no primeiro item para preencher
    pyautogui.write(codigo)
    #marca
    marca = str(tabela.loc[linha]['marca'])
    pyautogui.press('tab')
    pyautogui.write(marca)
    #tipo
    tipo = str(tabela.loc[linha]['tipo'])
    pyautogui.press('tab')
    pyautogui.write(tipo)
    #categoria
    categoria = str(tabela.loc[linha]['categoria'])
    pyautogui.press('tab')
    pyautogui.write(categoria)
    #preço
    preco = str(tabela.loc[linha]['preco_unitario'])
    pyautogui.press('tab')
    pyautogui.write(preco)
    #custo
    custo = str(tabela.loc[linha]['custo'])
    pyautogui.press('tab')
    pyautogui.write(custo)
    #obs
    obs = str(tabela.loc[linha]['obs'])
    pyautogui.press('tab')
    if obs != 'nan':
        pyautogui.write(obs)
    #cadastrar
    pyautogui.press('tab')
    pyautogui.press('enter')
    #precisa fazer o scroll voltar ao topo:
    #tecla 'home' faz o scroll ir para o topo da página
    #pyautogui.press('home')
    pyautogui.scroll(5000) #se número positivo, rola pra cima, negativo para baixo, foi posto número muito alto para ter certeza que irá ao início da página.
print('A automação chegou ao fim!')
