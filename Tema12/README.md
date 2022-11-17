# Tema12 - Terraform e Ansible

## Objetivo
Usando a linguagem Python e suas bibliotecas, deveríamos conectar no Twitter e recuperar os últimos 10 tweets a respeito dos 10 atores que mais fizeram filmes nos últimos 10 anos com base nas informações de catálogo fornecidas pelo IMDB. Além de gerar um código para criar todo o ambiente dentro da AWS do zero (Iaas)

## Resolução
Utilizando a ferramenta Terraform, criei um código que utilizando as chaves de acesso da AWS cria um bucket s3 e envia os scripts python da aplicação para o mesmo, além de criar uma máquina EC2 com tags e com um script .sh com os comandos para configurar as chaves de acesso da AWS nessa EC2, instalar o docker, pegar os arquivos da aplicação python na bucket gerada anteriormente com o sync, criar uma imagem python a partir do Dockerfile, subir um container para executar a aplicação python e por fim, enviar os resultados finais gerados para uma bucket s3.

## Passo-a-Passo utilizado
1. Aprimoramento do código para criar as pastas files e finalResults durante a execução do código
2. Instalação do terraform na minha própria máquina, e após extrair, adicionei o caminho no PATH do Sistema
3. Criação do arquivo var.tf que armazena as váriavéis utilizadas no arquivo main.tf
4. Criação do arquivo main.tf com o provider aws configurando inicialmente as chaves de acesso, depois pega a key_pair, cria a bucket s3, envia os arquivos da pasta Scripts para essa bucket criada, e cria a EC2 com algumas especificações, tags e enviando o arquivo run.sh para ser executado assim que subir a instância criada
5. Criação do arquivo run.sh com os comandos para serem executados automaticamente quando a EC2 for criada:
  * Armazena na máquina as credenciais da AWS e a região com o export
  * Instala o docker 
  * Pega, com o sync, os scripts Python da aplicação da bucket s3
  * Cria a imagem com o Dockerfile
  * Cria e sobe o container para executar a aplicação
  * Envia os arquivos finais do container para a EC2
  * Envia, com o sync, os arquivos finais para a bucket s3

## Para executar o código:
> **É necessário que altere as credenciais do arquivo .env no diretório apiTwitter, além de configurar os tokens de acesso da sua conta aws no arquivo var.tf, alterar as variáveis que desejar para personalizar a EC2 no arquivo var.tf, alterar a chave pública para da variável pk no arquivo var.tf e alterar o caminho da bucket no arquivo run.sh** 

> Executar os seguintes comandos:
  * Iniciar o terraform: **terraform init**
  * Criar o plano de execução: **terraform plan -out main.plan**
  * Buildar a infraestrutura: **terraform apply main.plan**
  * Destruir a infraestrutura (após confirmar se todos os passos da EC2 foram executados): **terraform destroy -auto-approve**  

