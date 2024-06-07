from Source.sms import mensageiro_sms
from Source.gerenciador_email import robo_autonomo

#Definição da mensagem e dos destinatários do sms
mensagem_old = ' '
destinatario=['+55555555555']

bot = robo_autonomo()
send = mensageiro_sms()

#Loop para rodar enquanto o fail-safe não é acionado (mover o mouse para algum canto superior)
while True:
    mensagem = bot.leitor_texto()     #Mensagem recebe o texto copiado da função leitor_texto()

    if mensagem != mensagem_old:        #Caso a mensagem seja diferente da última copiada, envia notificação
        
        #Laço para enviar a mensagem para todos os destinatários
        for indice in destinatario:
            retorno = send.envio_sms(mensagem, indice)
            print(retorno)

        print(mensagem)
        mensagem_old = mensagem     #Altera ultimo texto copiado
