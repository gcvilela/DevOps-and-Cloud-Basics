# Tema10 - Docker e Container

## Objetivo
Usando a linguagem Python e suas bibliotecas, deveríamos conectar no Twitter e recuperar os últimos 10 tweets a respeito dos 10 atores que mais fizeram filmes nos últimos 10 anos com base nas informações de catálogo fornecidas pelo IMDB. Em seguida, automatizar o processo de deploy desse código com Jenkins, onde puxará do github e executará o código em um contêiner Docker.

## Passo-a-Passo utilizado
1. Aprimoramento do programa para que realize o download dos arquivos do IMDB automaticamente, e ao final os apaga.
2. Instalação e configuração do Jenkins na EC2 (Descrito no Tema09)
3. Instalação do Docker na EC2:
   * sudo apt update
   * sudo apt install apt-transport-https ca-certificates curl software-properties-common
   * curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
   * sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
   * sudo apt update
   * apt-cache policy docker-ce
   * sudo apt install docker-ce
4. Criação do Dockerfile, no qual, define a sequência de etapas necessárias para criar a imagem do Docker utilizando como base a imagem do Python 3, cria o diretório **/tema10/** para receber os códigos python com o comando **COPY**, em seguida instala, cria e ativa o **virtualenv** para realizar a instalação das dependências contidas no arquivo **requirements.txt** e declara o caminho **/tema10/Scripts/** como diretório raiz para, por fim, declarar o ponto de entrada **CMD**, no qual indica que quando o container for iniciado, o script contido nele será executado, ou seja, **python3 main.py**
5. Criação da Pipeline (Descrito no Tema09) com as seguintes etapas no **Jenkinsfile**:
  > **Checkout SMC** : passo automatico da pipeline que realiza um pull do repositório para a EC2
  
  > **Create final folder** : cria uma pasta final para receber os arquivos gerados pela execução da main.py no container e para ser sincronizado com a bucket s3, além de criar a pasta para receber os arquivos gerados pelo download 
  
  > **Build image**: cria a imagem Docker a partir do Dockerfile, atráves do script image.sh
  
  > **Run container** : cria e executa o container com o comando **docker run**, em seguida copia os arquivos finais gerados para a pasta criada na segunda etapa, e por fim, para a execução do container
  
  > **Sync** : sincroniza os arquivos finais com a bucket s3, atráves do script sync.sh
  
  > **Cleanup** : apaga todos os containers e as imagens que não estão em execução
  
  > Ao final, a pipeline deleta o workspace quando o build terminar, evitando que o armazenamento seja lotado

* **É necessário que altere as credenciais do arquivo .env no diretório apiTwitter, configurar os tokens de acesso da sua conta aws e alterar o caminho da bucket no arquivo syn.sh** 
