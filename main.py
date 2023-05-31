#módulo de geração de log
import logging

import pyautogui as pyg

from datetime import date

#módulo de tempo de espera
import time

#**************************** Inicio ****************************

# Achando a data de hoje
today = date.today()
hoje = today.strftime("%d/%m/%Y")

#Tempo para inicio, deixar a tela ativa no oracle
print("Iniciando em: 3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)



# Primeiro, fecha as duas janelinhas que não serão usadas
proc = "sim"

while proc == "sim":
    try:
        img = pyg.locateCenterOnScreen('Extras\c8.png', confidence=0.9)
        pyg.click(img.x, img.y)
        proc = "não"
        pyg.moveRel(50, 50)
    except:
        time.sleep(1)
        print("Botâo 'Fechar' Não localizado")

time.sleep(2)   
proc = "sim"     

while proc == "sim":
    try:
        img = pyg.locateCenterOnScreen('Extras\c8.png', confidence=0.9)
        pyg.click(img.x, img.y)
        proc = "não"
        pyg.moveRel(50, 50)
    except:
        time.sleep(1)
        print("Botâo 'Fechar' Não localizado")
        
        
        
        
# Agora, abre a parte de solicitações e abre uma requisição       
time.sleep(1.5)
proc = "sim"

while proc == "sim":
    try:
        img = pyg.locateCenterOnScreen('Extras\c1.png', confidence=0.8)
        pyg.click(img.x, img.y)
        proc = "não"
        pyg.moveRel(50, 50)
    except:
        time.sleep(1)
        print("Botâo 'Verificar' Não localizado")

time.sleep(1)
proc = "sim"

while proc == "sim":
    try:
        img = pyg.locateCenterOnScreen('Extras\c2.png', confidence=0.8)
        pyg.click(img.x, img.y)
        proc = "não"
        pyg.moveRel(50, 50)
    except:
        time.sleep(1)
        print("Botâo 'Solicitações' Não localizado")

proc = "sim"
time.sleep(1)

while proc == "sim":
    try:
        img = pyg.locateCenterOnScreen('Extras\c3.png', confidence=0.8)
        pyg.click(img.x, img.y)
        proc = "não"
        pyg.moveRel(50, 50)
    except:
        time.sleep(1)
        print("Botâo 'Submeter nova solicitação' Não localizado")



# Começo do cadastro! *********************************

time.sleep(1)
pyg.press("Enter")
time.sleep(1.5)
pyg.write("XXML - Lancamentos Despesas de Contrato Property Manager")
time.sleep(0.7)
pyg.press("TAB")
time.sleep(2.3)


# Coleta dos dados na planilha
lease = "5321"
gabarito = "- COND" # 43422 - Encargos / IMP #  15857 - Energia 
dia_prog = "01"
freq = "MON"
data_inicio = "01/06/2023"
data_fim = "30/06/2023"
tipo = "INDX" # PRCT = Encargo, RET = energia, OEXP = Iptu
valor = "442,53"

#VÊ se imposto >0, energia > 0 e etc. Se for, coloca uma opção a mais (copiando e colando código mesmo, fds)

# Inicio do cadastro

pyg.write(lease, interval=0.15)
pyg.press("TAB")
time.sleep(1)

proc = "sim"

while proc == "sim":
    try:
        img = pyg.locateCenterOnScreen('Extras\c3ponto.png', confidence=0.8)
        pyg.click(img.x, img.y)
        proc = "não"
        pyg.moveRel(50, 50)
    except:
        time.sleep(1)
        print("Botâo '3 Pontinhos' Não localizado")
        
        
time.sleep(1)

proc = "sim"

while proc == "sim":
    try:
        img = pyg.locateCenterOnScreen('Extras\clocalizar.png', confidence=0.8)
        pyg.click(img.x, img.y)
        proc = "não"
        pyg.moveRel(50, 50)
    except:
        time.sleep(1)
        print("Bara de pesquisa 'Localizar' Não encontrado")

pyg.write(gabarito, interval=0.15)
pyg.press("Enter")
time.sleep(1.5)

pyg.write(dia_prog, interval=0.15)
time.sleep(0.7)

pyg.write(freq, interval=0.15)
pyg.press("TAB")
time.sleep(0.7)

pyg.write(data_inicio, interval=0.15)
pyg.press("TAB")
time.sleep(0.7)

pyg.write(data_fim, interval=0.15)
pyg.press("TAB")
time.sleep(0.7)

pyg.write(hoje, interval=0.15)
pyg.press("TAB")
time.sleep(0.7)

pyg.write(tipo, interval=0.15)
pyg.press("TAB")
time.sleep(0.7)

pyg.write(valor, interval=0.15)
pyg.press("TAB")
time.sleep(0.7)

pyg.press("Enter")
time.sleep(1)


#****************************se tiver mais uma despesa, clica sim (enter), loop depois do XXML

proc = "sim"

while proc == "sim":
    try:
        img = pyg.locateCenterOnScreen('Extras\sub.png', confidence=0.8)
        pyg.click(img.x, img.y)
        proc = "não"
        pyg.moveRel(50, 50)
    except:
        time.sleep(1)
        print("Botão de 'Submeter' Não localizado")
        
        
# Apertando o botâo de "Não submeter outra requisição"
time.sleep(1)
pyg.press("TAB")
time.sleep(0.7)
pyg.press("Enter")


# Fechando a parte atual, e partindo para a próxima     
time.sleep(1.5)
pyg.press("F4")
time.sleep(1.5)

proc = "sim"

while proc == "sim":
    try:
        img = pyg.locateCenterOnScreen('Extras\chapeu.png', confidence=0.8)
        pyg.click(img.x, img.y)
        proc = "não"
        pyg.moveRel(50, 50)
    except:
        time.sleep(1)
        print("Botão 'Chapeu' Não localizado")
        
time.sleep (2)
pyg.press("M")
time.sleep (1.5)
pyg.press("Down", presses=11, interval=0.1)
pyg.press("Enter")
time.sleep(1.3)

proc = "sim"

while proc == "sim":
    try:
        img = pyg.locateCenterOnScreen('Extras\c5.png', confidence=0.8)
        pyg.doubleClick(img.x, img.y)
        proc = "não"
        pyg.moveRel(50, 50)
    except:
        time.sleep(1)
        print("Botão 'Autorizar Pagamentos' Não localizado")

time.sleep(1.5)


# Parte de aprovação
pyg.press("Tab", presses=2)
time.sleep(1)
pyg.write(lease, interval=0.1)
pyg.press("Tab")
time.sleep(1)
pyg.write(data_inicio, interval=0.1)
pyg.press("Tab")
time.sleep(1)
pyg.write(data_fim, interval=0.1)
pyg.press("Enter")

time.sleep(1.5)



# abrindo os detalhes
pyg.press("Enter")
time.sleep(1.5)


proc = "sim"

while proc == "sim":
    try:
        img = pyg.locateCenterOnScreen('Extras\preliminar.png', confidence=0.8)
        pyg.click(img.x, img.y)
        proc = "não"
        pyg.moveRel(50, 50)
    except:
        time.sleep(1)
        print("Botão 'Preliminar' Não localizado")
        
time.sleep(1.5)


proc = "sim"

while proc == "sim":
    try:
        img = pyg.locateCenterOnScreen('Extras\caprovado.png', confidence=0.8)
        pyg.click(img.x, img.y)
        proc = "não"
        pyg.moveRel(50, 50)
    except:
        time.sleep(1)
        print("Botão 'Aprovado' Não localizado")
        
time.sleep(1.4)


proc = "sim"

while proc == "sim":
    try:
        img = pyg.locateCenterOnScreen('Extras\Yes.png', confidence=0.8)
        pyg.click(img.x, img.y)
        proc = "não"
        pyg.moveRel(50, 50)
    except:
        time.sleep(1)
        print("Botão 'Yes' Não localizado")        
        
time.sleep(1.3)
pyg.write("YES", interval=0.1)
pyg.press("Tab")
time.sleep(0.5)
pyg.press("Enter")


# Salvando o progresso
proc = "sim"

while proc == "sim":
    try:
        img = pyg.locateCenterOnScreen('Extras\disquete.png', confidence=0.8)
        pyg.click(img.x, img.y)
        proc = "não"
        pyg.moveRel(50, 50)
    except:
        time.sleep(1)
        print("Botão 'Disquete' Não localizado")  
        
# Saindo, e indo para a terceira parte
time.sleep(1.2)        
pyg.press("F4")
time.sleep(1.5)
pyg.press("Down")
pyg.press("Enter")



# Parte 3 - Exportando

time.sleep(1.5)
pyg.press("Tab", presses=2)

pyg.write(lease, interval=0.1)
pyg.press("Tab")
time.sleep(1)
pyg.write(data_inicio, interval=0.1)
pyg.press("Tab")
time.sleep(1)
pyg.write(data_fim, interval=0.1)
pyg.press("Enter")
time.sleep(1)


proc = "sim"

while proc == "sim":
    try:
        img = pyg.locateCenterOnScreen('Extras\exportar.png', confidence=0.8)
        pyg.click(img.x, img.y)
        proc = "não"
        pyg.moveRel(50, 50)
    except:
        time.sleep(1)
        print("Botão 'Exportar' Não localizado")  
        
        
time.sleep(1)
pyg.press("Enter")
time.sleep(1)



# Preparando para reiniciar!
pyg.press("F4")


proc = "sim"

while proc == "sim":
    try:
        img = pyg.locateCenterOnScreen('Extras\chapeu.png', confidence=0.8)
        pyg.click(img.x, img.y)
        proc = "não"
        pyg.moveRel(50, 50)
    except:
        time.sleep(1)
        print("Botão 'Chapeu' Não localizado")
        
time.sleep(2)        
pyg.press("M")
time.sleep(1.5)
pyg.press("Down", presses=12, interval=0.1)
pyg.press("Enter")
time.sleep(1.5)
pyg.press("Down")
pyg.press("Enter")
time.sleep(1.5)
pyg.press("Enter")
time.sleep(1.5)
pyg.press("Enter")