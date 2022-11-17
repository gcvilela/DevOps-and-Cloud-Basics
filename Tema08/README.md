# Tema 08 - Tarefa Agendada (Windows)

## Objetivo
Usando a linguagem Python e suas bibliotecas, deveríamos conectar no Twitter e recuperar os últimos 10 tweets a respeito dos 10 atores que mais fizeram filmes nos últimos 10 anos com base nas informações de catálogo fornecidas pelo IMDB. Em seguida, realizar um agendamento de tarefa em uma máquina virtual Windows para executar o programa em determinados dias e horários.

## Passo-a-Passo utilizado
1.  Realizei o sync com uma máquina Windows 10 criada com o Virtual Box, para colocar os arquivos e códigos utilizados.
2. Após realizar o download e configuração do AWS CLI, instalei as dependências necessárias dentro do requirements.txt
3. Criei o arquivo script.ps1 com os comandos necessários para ativar o ambiente virtual, executar o código python main.py e realizar o sync com o bucket s3 da aws
4. Em seguida, após entender como funcionava o agendamento pelo powershell, criei o arquivo task.ps1 com os comandos para executar o script.ps1 todos os dias que a máquina estiver ligada, às 16h 
5. Por fim, executei o arquivo task.ps1 com o powershell para a tarefa ser ativada

## Execução do Código
*  Para executar o código é necessário:
1. Instalar os requerimentos do arquivo requirements.txt em seu ambiente virtual 
        pip install -r requirements.txt
2. Realizar o download dos arquivos no site https://datasets.imdbws.com/, coloca-los no diretório files localizado na pasta IMDB e alterar o Absolute Path nos códigos movies.py, actors_nums.py e actors_names.py
3. Alterar as chaves e os tokens da API do Twitter no arquivo .env  localizado no diretório apiTwitter para as suas (Não esqueça o Bearer Token)
4. Alterar os caminhos do comando de aws s3 sync, para salvar os arquivos direto na bucket, e dos demais comandos dentro do arquivo script.ps1
5. Realizar as alterações necessárias no arquivo task.ps1 e executá-lo com o PowerShell para a tarefa ser ativada corretamente 
