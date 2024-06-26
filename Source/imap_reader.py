import imaplib
import email
from email.header import decode_header

class verificador_email:
    def __init__(self, EMAIL, SENHA, IMAP_SERVER, PORTA):      #Inicia a classe com os construtores necessários para conexão
        self.email = EMAIL
        self.senha = SENHA
        self.imap = IMAP_SERVER
        self.porta = PORTA

        self.config()

    def config(self):       #Faz a conexão por IMAP
        self.account = imaplib.IMAP4_SSL(self.imap,self.porta)        #Inicia conexão e faz login a partir das credenciais
        status = self.account.login(self.email,self.senha)
        print("Status:",status[0])
        return
    
    def status(self, CAIXA, BUSCA):
        print(self.account.status(CAIXA, BUSCA))   #Verifica o Status da caixa selecionada a partir de certa busca
        return
    
    def buscar_email(self, CAIXA, BUSCA):
        ret_assunto = []
        ret_corpo = []
    
        try:
            self.account.select(CAIXA)       #Escolhe qual caixa de email irá verificar
        except:
            print("caixa selecionada incorreta!")   #Retorna um erro caso não encontre a caixa

        status, dados = self.account.search(None, BUSCA)    #Busca emails não vistos recebidos de suportebrazil
        nlidos_ids = dados[0].split()       #Separa as tuplas em uma lista com os ids dos emails

        for ids in nlidos_ids:      #Faz analise de cada um dos emails a partir dos ids
            status, dados = self.account.fetch(ids, '(RFC822)')     #Recupera os dados do email a partir da id, RFC822 especifica que queremos o conteudo completo (cabeçalho,corpo e estrutura)

            for resposta in dados:
                if isinstance(resposta, tuple):     #Para cada elemento dos dados verifica se seu tipo é tupla
                    dados = email.message_from_bytes(resposta[1])       #Recupera o conteudo do email a partir da posição 1 da resposta atual
                    assunto, encoding = decode_header(dados["Subject"])[0]      #Extrai o Subject do email e armazena ele e sua codificação

                    if isinstance(assunto, bytes):      #Se o assunto está no formato de bytes, decodifica o conteudo
                        if encoding != None:
                            assunto = assunto.decode(encoding)      
                    ret_assunto.append(assunto)      #Retorna o assunto do email

                    if dados.is_multipart() == False:       #Verifica se o email não é feito de multiplas partes (texto, anexos, etc)
                        tipo_conteudo = dados.get_content_type()    

                        if tipo_conteudo == "text/plain": 
                            try:
                                corpo = dados.get_payload(decode=True).decode()     #Usa o método try para decodificar o corpo do email caso ele seja do tipo texto simples
                                ret_corpo.append(corpo)
                            except:
                                print("Falha ao extrair o corpo do email")

                        if tipo_conteudo == "application/octet-stream":     
                            try:
                                corpo = dados.get_payload(decode=True).decode()     #Usa o método try para decodificar o corpo do email caso ele seja do tipo application/octet-stream  
                                ret_corpo.append(corpo)
                            except:
                                print("Falha ao extrair corpo do email")

            self.account.store(ids, '+FLAGS','\\Seen')      #Marca o email como lido

        return ret_assunto,ret_corpo
        
    def __del__(self):
        self.account.logout()
