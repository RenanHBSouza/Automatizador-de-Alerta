from Source.Notificacao_users import mensageiro
from Source.imap_reader import verificador_email
import time
import os

#Definição da mensagem e dos destinatários do sms
account_sid = os.environ['SID_API']
token = os.environ['TOKEN_API']
numero='numero_twilio'
wpp='numero_twilio_wpp'
destinatario=['+55123456','+55654321']

#Definição configs de busca de email
EMAIL = os.environ['ENDERECO_EMAIL']
SENHA = os.environ['SENHA_EMAIL']
IMAP_server = 'servidor_imap'
IMAP_porta = 993
BUSCA = '(UNSEEN FROM "nome_remetente")'
CAIXA = 'INBOX'
ASSUNTO = 'Assunto_buscado'
TIMER = 20

mail = verificador_email(EMAIL, SENHA,IMAP_server, IMAP_porta)      #Cria os objetos a partir das classes
send = mensageiro(account_sid, token)

def gerar_mensagem(lista):
    texto = []
    chars = list(lista)     #Gera um vetor de caracteres da string
    i = 0
    while (chars[i] != '_' or chars[i+1] != '_') and i != len(chars):        #Procura uma sequencia de - para entender que o texto necessário terminou
        texto.append(chars[i])
        i += 1
    result = ''.join(texto)     #Transforma a lista de caracteres nova em string
    return result

while True:
    flag = 0        #Flag que controla a necessidade de ligar para outro colaborador
    assunto, mensagem = mail.buscar_email(CAIXA, BUSCA)     #recebe assuntos e mensagens a partir da função buscar_email
    registros = len(assunto) 

    for indice in range(0,registros):
        if assunto[indice] == ASSUNTO:       #verifica se o assunto é 'serv-sensor notification':        
            conteudo = gerar_mensagem(mensagem[indice])
            print(conteudo)

            for indice in destinatario:     #Laço para enviar a mensagem para todos os destinatários
                retorno = send.envio_wpp(conteudo, wpp, indice)
                print(retorno)

            for indice in destinatario:     #Laço para ligar para algum dos destinatários
                if flag == 0:
                    retorno = send.ligacao(numero, indice)
                    print(retorno)
                    #Aguarda a ligação ir para um status definitivo para analisar se foi completa
                    while send.status_ligacao(retorno) == 'queued' or send.status_ligacao(retorno) == 'ringing' or send.status_ligacao(retorno) == 'in-progress':       
                        print(send.status_ligacao(retorno))
                        time.sleep(3)
                    print(send.status_ligacao(retorno))
                    if send.status_ligacao(retorno) == 'completed':
                        flag = 1        #Altera a flag para não ligar para nenhum outro usuário
        
    time.sleep(TIMER)
