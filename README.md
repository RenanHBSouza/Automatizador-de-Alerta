
# Sistema de Monitoramento e Notificação de Alertas via E-mail e Chamadas Telefônicas


## 1. Motivação:

O desenvolvimento deste sistema visa automatizar o processo de monitoramento e notificação de alertas gerados por sensores no CPD de uma empresa. O objetivo principal é garantir a rápida identificação e resolução de problemas que possam comprometer a infraestrutura crítica vigiada por um serv-sensor, minimizando o tempo de inatividade e os impactos negativos nos negócios.

## 2. Descrição do Sistema:

O sistema funciona ineterruptamente da seguinte maneira:

### Verificação de Emails:
O sistema se conecta ao servidor de e-mail via IMAP para verificar se há novos emails não lidos.
A busca é focada em mensagens de um remetente específico (que envia a notificação) com um assunto específico (definido nas configurações de alerta do dispositivo).
### Processamento de Emails:
Ao encontrar um email correspondente aos critérios de busca, o sistema extrai o corpo do email contendo os detalhes do alerta.
### Notificação via WhatsApp:
O corpo do email com os detalhes do alerta é enviado para destinatários no WhatsApp previamentes definido, informando-os sobre a situação.
### Notificação via Chamada Telefônica:
Uma fila de chamadas telefônicas é criada, o sistema tenta ligar para cada número na fila, um por um, até que um colaborador atenda.
Ao atender, o colaborador recebe um alerta via mensagem de voz.

## 3. Tecnologias Utilizadas:

### Linguagem de Programação: 
Python
### Bibliotecas:
imaplib: para conexão com servidor IMAP
email: para processamento de emails
twilio: para realizar chamadas telefônicas e envio de mensagens Whatsapp
### Serviços:
Servidor IMAP
Conta Twilio

## 4. Passo a Passo de Utilização:

### Instalação:
Clonar o repositório do GitHub contendo o código do sistema.
Instalar as bibliotecas necessárias utilizando o arquivo **install.bat**.
### Configuração:
Editar o cabeçalho do arquivo main.py com as seguintes informações:
__Endereço de e-mail analisado__
__Senha do e-mail analisado__
__Servidor e porta IMAP__
__Busca a ser feita__
__Caixa do e-mail a ser verificada__
__Assunto dos emails de alerta__
__Lista de números de telefone para notificação__
__Credenciais da conta Twilio__
### Execução:
Executar o script principal (main.py) utilizando o arquivo start.bat.

## 5. Observações:

O sistema está configurado para verificar emails a cada 20 segundos. Essa periodicidade pode ser ajustada de acordo com a necessidade.

Utilize de variáveis de ambiente para aumentar a segurança de suas informações, principalmente de e-mail e conta Twilio (TOKEN e SID).

## 6. Considerações Finais:

Este sistema de monitoramento e notificação automatiza o processo de comunicação de alertas gerados por sensores no CPD da empresa, garantindo uma resposta rápida e eficiente a eventuais problemas na infraestrutura crítica. A utilização de tecnologias como Python, bibliotecas especializadas e serviços em nuvem permite a implementação de um sistema robusto, escalável e de fácil manutenção.