import twilio.rest as tw

#Configuração inicial com requerimentos da API
account_sid = 'your_sid'
token = 'your_token'
numero='+5555555555'
cliente = tw.Client(account_sid, token)

#Classe que apresenta a função de envio de sms
class mensageiro_sms:
    def __init__(self):
        super().__init__()

    def envio_sms(self, msg, destino):
        alerta = cliente.messages.create(       #Cria SMS a partir dos argumentos da função
            body=msg,
            from_=numero,
            to=destino  
        )
        return alerta.sid       #Retorna identifacação do SMS
