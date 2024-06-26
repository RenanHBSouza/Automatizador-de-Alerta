import twilio.rest as tw

#Classe que apresenta a função de envio de sms
class mensageiro:
    def __init__(self, SID, TOKEN):     #Inicia a partir dos construtores necessário para conexão
        self.sid  = SID
        self.token = TOKEN
        self.cliente = tw.Client(self.sid, self.token)

    def envio_wpp(self, msg, wpp, destino):
        alerta = self.cliente.messages.create(       #Cria WPP a partir dos argumentos da função
            body=msg,
            from_='whatsapp:'+wpp,
            to='whatsapp:'+destino  
        )
        return alerta.sid       #Retorna identifacação do WPP
    
    def ligacao(self, numero, destino):
        chamada = self.cliente.calls.create(     #Cria ligação utilizando twiml para especificar o que vai ser dito e as caracteristicas da chamada
                                    twiml='<Response><Say language="pt-BR" voice="alice">Atenção, há novos avisos acerca do Serv-Sensor, favor verificar mensagens!</Say></Response>',
                                    to=destino,
                                    from_=numero
        )
        sid = chamada.sid
        return sid      #Retorna identificação da chamada
   
    
    def status_ligacao(self, sid):      #Verifica o status da chamada a partir do sid dela (queued, ringing, in-progress, completed, error, busy)
        chamada = self.cliente.calls(sid).fetch()
        return chamada.status