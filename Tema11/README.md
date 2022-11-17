# Tema11 - Stack ELK

## Objetivo
Usando a linguagem Python e suas bibliotecas, deveríamos conectar no Twitter e recuperar os últimos 10 tweets a respeito dos 10 atores que mais fizeram filmes nos últimos 10 anos com base nas informações de catálogo fornecidas pelo IMDB. Em seguida, fazer a instalação em conteneires Docker da Stack ELK, gerando uma URL para o Kibana, capturando os logs do processo de pesquisa do twitter, como os termos resultados e a quantidade de resultados.

## Passo-a-Passo utilizado
1. Aprimoramento do código para armazenar os logs de todo o processo de deploy em um arquivo .log
2. Criação da imagem do container python a partir do Dockerfile, que roda a aplicação do Twitter, e realização do comando docker push para armazenar a imagem no Docker Hub
3. Criação do arquivo docker-compose.yml para subir os containers da Stack ELK
4. Criação dos scripts batch:
   * **folders.bat** : realiza a criação das subpastas finais dentro da pasta Scripts e também na pasta do Docker-ELK
   * **containerpython.bat** : realiza o comando docker pull para puxar a imagem criada anteriormente e armazenada no DockerHub, sobe um container a partir dessa imagem para executar a aplicação python e por fim, realiza a cópia dos resultados finais para a subpasta logstash na pasta Docker-ELK
   * **sync.bat** : realiza a sincronização da pasta de resultados finais com a bucket s3 da aws
   * **docker-compose.bat** : sobe os container da Stack ELK, nos quais, o logstash envia o arquivo **tweets.csv** para o elasticsearch e é mostrado graficamente em um dashboard do kibana.
5. Execução dos scripts batch na ordem descrita acima
6. Criação do dashboard no **Kibana** através da url gerada **localhost:5061**

* **É necessário que altere as credenciais do arquivo .env no diretório apiTwitter, configurar os tokens de acesso da sua conta aws e alterar o caminho da bucket no arquivo sync.bat** 