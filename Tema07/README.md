# Tema 07 - Tarefa Agendada (Linux)

## Objetivo
Usando a linguagem Python e suas bibliotecas, deveríamos conectar no Twitter e recuperar os últimos 10 tweets a respeito dos 10 atores que mais fizeram filmes nos últimos 10 anos com base nas informações de catálogo fornecidas pelo IMDB. Em seguida, realizar um agendamento de tarefa em uma máquina Linux para executar o programa em determinados dias e horários.

## Passo-a-Passo utilizado
1.  Após realizar o download dos arquivos e os armazenar em uma bucket S3 da AWS, realizei o sync com uma máquina Linux t2-micro para colocar os arquivos e executar o programa.
2. Realizei as seguintes alterações no código utilizado no tema 06 para que sua execução fosse otimizada para ser executado com eficiência em uma máquina pequena:
Retirada da conexão e migração de dados para o DB MySQL.
Utilização do módulo dotenv para criar um arquivo .env que armazena as chaves e tokens de acesso da api do Twitter
Seleção das colunas ao abrir o arquivo em formato de Data Frame, que seriam utilizadas durante o programa, para que o dataframe não exigisse muito processamento.
Utilização de chunks também ao abrir os arquivos para que os dados fossem processados e tratados aos poucos, para otimizar o processamento.
Arquivos finais sendo salvos em formato csv
3. Criei o script (script.sh) que ativa o ambiente virtual, executa o código main.py e realiza o aws s3 sync com a bucket para salvar os códigos utilizados e arquivos gerados
4. Em seguida, após entender como funcionava o crontab para agendar tarefas em uma máquina Linux, agendei uma tarefa que executa o script.sh toda quinta às 10h

## Execução do Código
*  Para executar o código é necessário:
1. Instalar os requerimentos do arquivo requirements.txt em seu ambiente virtual 
        pip install -r requirements.txt
2. Realizar o download dos arquivos no site https://datasets.imdbws.com/, coloca-los no diretório files localizado na pasta IMDB e alterar o Absolute Path nos códigos movies.py, actors_nums.py e actors_names.py
3. Alterar as chaves e os tokens da API do Twitter no arquivo .env  localizado no diretório apiTwitter para as suas (Não esqueça o Bearer Token)
4. Alterar os caminhos do comando de aws s3 sync, para salvar os arquivos direto na bucket, e dos demais comandos
5. Executar o seguinte comando após alterar o script.sh:
       sudo crontab -e
6. Acrescentar a seguinte tarefa ao final do arquivo criado pelo crontab, alterando o caminho, para ser executado toda quinta às 10h:
       0 10 * * 4  /path/Scripts/crontab/script.sh > /dev/null 2 > &1 
  * !A última parte ( > /dev/null 2 > &1 ) é necessária caso os comandos executados pelo script.sh gere saídas a serem impressas na tela do computador
7. Após salvar o arquivo crontab com a tarefa agendada, verifique se o cron está ativo e rodando com o comando:
       service cron status
