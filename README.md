# ENVIO DE ALERTAS SMS

Sistema criado para enviar alertas via sms a partir de um e-mail gatilho analisado por bot, idealizado primeiramente para uma aplicação de monitoramento. A ideia partiu a partir da necessidade de monitorar um sensor AC conectado em um Serv-sensor que mapeava as condições de uma CPD, porém esse dispositivo permitia somente ação por e-mail. Com isso em mente, a solução foi monitorar as mensagens recebidas por um endereço e, por meio de uma automatização RPA, disparar sms para cada vez que um alerta do sensor desejado chegasse.

# FUNCIONAMENTO

O robô faz a leitura ineterrupta da caixa de entrada do e-mail analisando sempre a última mensagem recebida, porém só envia o SMS quando o conteúdo é realmente novo, evitando assim que a aplicação faça o envio do mesmo alerta. Para interromper as atividades RPA, basta arrastar o mouse para o canto superior desejado.
