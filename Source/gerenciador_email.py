#ir com o mouse até a primeira mensagem
#clique para entrar na mensagem
#Triplo clique para selecionar todo conteudo do email
#Clicar no botão de voltar
#atualizar caixa de email

import time
import pyautogui as bot
import pyperclip as clip



class robo_autonomo:
    def __init__(self):
        super().__init__()
        bot.PAUSE = 0.5     #Define tempo de pause padrão entre ações do bot
        bot.FAILSAFE = True     #Ativa o Failsafe para interromper a automação assim que o mouse for levado para algum canto superior

    def leitor_texto(self):
             
        time.sleep(1)
        bot.leftClick(612,526)      #Clica no espaço de último e-mail recebido
        time.sleep(1.5)
        bot.moveTo(493, 608)        #Move o mouse para o inicio do conteudo
        time.sleep(1.5)
        bot.mouseDown(button='left')        #Pressiona o botão esquerdo e move para selecionar
        bot.moveTo(1365, 874, duration=1.5)
        bot.mouseUp(button='left')
        bot.hotkey('ctrl','c')      #Copia o conteudo
        bot.click("Source/voltar.PNG")     #Clica no botão de voltar
        time.sleep(1.5)
        bot.click("Source/refresh.PNG")        #Atualiza o email
        time.sleep(1)
        texto = clip.paste()        #Variavel texto recebe a string copiada
        return texto



