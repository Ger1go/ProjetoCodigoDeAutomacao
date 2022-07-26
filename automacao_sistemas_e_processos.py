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

pyautogui.PAUSE = 0.5


# Passo 1: Entrar no sistema (no nosso caso vai ser entrando no link)

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

time.sleep(6)

# Passo 2: Navegar no sistema e encontrar a base de dados (entrar na pasta Exportar)
'''time.sleep(6)
print(pyautogui.position())'''

pyautogui.click(x=2729, y=351, clicks=2)
time.sleep(2)

# Passo 3: Download de base de dados. 
pyautogui.click(x=2729, y=351)
pyautogui.click(x=3499, y=230)
pyautogui.click(x=3263, y=610)
time.sleep(7)


# Passo 4: Calcular os indicadores (faturamento, quantidade de produtos)
#pandas





# Passo 5: Entrar no email
# Passo 6: Mandar um email para diretoria com os indicadores


