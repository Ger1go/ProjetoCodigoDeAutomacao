""" Automação de Sistemas e Processos com Python
Desafio:
Todos os dias, o nosso sistema atualiza as vendas do dia anterior. O seu trabalho diário, como analista, é enviar um e-mail para a diretoria, assim que começar a trabalhar, com o faturamento e a quantidade de produtos vendidos no dia anterior

E-mail da diretoria: seugmail+diretoria@gmail.com
Local onde o sistema disponibiliza as vendas do dia anterior: https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing

Para resolver isso, vamos usar o pyautogui, uma biblioteca de automação de comandos do mouse e do teclado """


#Passos:

import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1


# Passo 1: Entrar no sistema (no nosso caso vai ser entrando no link)

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

time.sleep(6)

# Passo 2: Navegar no sistema e encontrar a base de dados (entrar na pasta Exportar)
'''
time.sleep(6)
pyautogui.position()
print(pyautogui.position())
'''

pyautogui.click(x=2729, y=351, clicks=2)
time.sleep(2)

# Passo 3: Download de base de dados. 
pyautogui.click(x=2729, y=351)
pyautogui.click(x=3499, y=230)
pyautogui.click(x=3263, y=610)
time.sleep(5)


# Passo 4: Calcular os indicadores (faturamento, quantidade de produtos)
#pandas

import pandas as pd

tabela = pd.read_excel(r'C:\Users\germa\Downloads\Vendas - Dez.xlsx')
print(('\n')*2)
print(tabela)

quantidade = tabela['Quantidade'].sum()
faturamento = tabela['Valor Final'].sum()


# Passo 5: Entrar no email 

pyautogui.hotkey('ctrl', 't')
pyperclip.copy('https://mail.google.com/mail/u/0/#inbox')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(6)

# Passo 6: Mandar um email para diretoria com os indicadores

"""time.sleep(6)
pyautogui.position()
print(pyautogui.position())"""

pyautogui.click(x=2495, y=280)
pyautogui.write('germanungo@gmail.com')
pyautogui.press('tab')
pyautogui.write('sissiventurin@gmail.com')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.write('Relatorio de vendas')
pyautogui.press('tab')

texto = f''' 
Prezados, bom dia.

Sou o robô automatico criado por German Ungo.

O faturamento todal de ontem foi de: R$ {faturamento:,.2f}
A quantidade de produtos foi de: {quantidade:,}

Adjunto a tabela de vendas em excel para revisão. 

Abs.
Robô do Python.

'''

pyperclip.copy(texto)

pyautogui.hotkey('ctrl', 'v')

pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')



pyperclip.copy('Vendas - Dez.xlsx')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')


pyautogui.hotkey('ctrl', 'enter')



