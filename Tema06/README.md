# Tema 06 - Python

## Objetivo
Usando a linguagem Python e suas bibliotecas, deveriamos conectar no Twitter e recuperar os últimos 10 tweets a respeitos
dos 10 atores que mais fizeram filmes nos últimos 10 anos com base nas informações de catálogo fornecidas pelo IMDB.

## Passo-a-Passo utilizado
1. Busquei entender os arquivos que o IMDB fornecia para download no site https://www.imdb.com/interfaces/, com isso, percebi que para atingir o objetivo, precisaria relacionar algumas informações de três DataSets do site, sendo eles:
* title_basics.tsv : possuia as informações sobre os filmes lançados (bem como séries, tv shows, etc), como a data de lançamento, identificador do filme, categoria, etc.
* title_principals.tsv : possuia o elenco/equipe principal dos títulos, mas relacionava apenas o identificador do filme com o identificador da pessoa
* name_basics.tsv : possuia as informações sobre o elenco, como o nome e seu identificador
2. Gerei a API do Twitter e busquei entender como ela funcionava
3. Após realizar o download dos arquivos e criar um ambiente virtual (.venv) na IDE Pycharm, utilizei a biblioteca pandas para extrair, analisar, transformar e relacionar os três arquivos
4. Tendo os nomes dos 10 atores/atrizes que mais fizeram filmes nos últimos 10 anos, realizei uma migração deste DataFrame final para uma tabela no MySQL
5. Realizei a autenticação da API do Twitter 
6. Extrai os nomes da tabela do MySQL para pesquisar os últimos tweets relacionados a eles 
7. Após conectar e receber o retorno das pesquisas com os nomes, salvei em um dicionário cada tweet como valor e o nome do ator/atriz relacionado como chave

## Execução do Código
* Para executar o código é necessário:
1. Instalar os requerimentos do arquivo requerimentos.txt em seu ambiente virtual (.venv)
2. Realizar o download dos arquivos no site https://datasets.imdbws.com/, coloca-los no diretório files localizado na pasta IMDB e alterar o Absolute Path nos códigos movies.py, actors_nums.py e actors_names.py
3. Alterar as chaves e os tokens da API do Twitter em tokens.py localizado no diretório apiTwitter para as suas (Não esqueça o Bearer Token)
4. Criar uma tabela em seu db MySQL com os campos nconst, qtdMovies e name
5. Alterar os dados de acesso ao banco MySQL em mysql_connection.py localizado no diretório dbConnection 
6. Executar o arquivo main.py 
7. Ver a mágica acontecer :p

