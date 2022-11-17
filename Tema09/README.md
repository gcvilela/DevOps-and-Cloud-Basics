# Tema09 - Jenkins

## Objetivo
Usando a linguagem Python e suas bibliotecas, deveríamos conectar no Twitter e recuperar os últimos 10 tweets a respeito dos 10 atores que mais fizeram filmes nos últimos 10 anos com base nas informações de catálogo fornecidas pelo IMDB. Em seguida, automatizar o processo de deploy desse código com Jenkins, onde puxará do github e fará o deploy dentro de uma EC2 Linux.

## Passo-a-Passo utilizado
1. Aprimoramento do programa para que realize o download dos arquivos do IMDB automaticamente, e ao final os apaga.
2. Criação de 3 scripts a serem executados em etapas da pipeline, sendo eles:
   * build.sh : ativa o ambiente virtual e instala as dependências do arquivo requirements.txt
   * deploy.sh : ativa o ambiente virtual e executa o arquivo main.py
   * sync.sh : sincroniza os arquivos com a bucket s3
3. Instalação do Jenkins na EC2:
   * sudo apt-get update -y 
   * wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
   * sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
   * sudo apt update
   * sudo apt install default-jdk
   * sudo apt install default-jre
   * sudo apt install jenkins -y
   * sudo systemctl start jenkins
   * sudo systemctl status jenkins
   * sudo ufw allow 8080
   * sudo ufw allow OpenSSH 
   * sudo ufw enable
   * sudo ufw status
   * Verificar se a EC2 está permitindo a entrada da **porta 8080** (Caso não esteja: EC2 -> Segurança -> Grupo de Segurança -> Editar Regras de Entrada)
4. Configuração do Jenkins:
   * Acesse o arquivo **/etc/sudoers** como editor de texto e insira:
     **jenkins ALL=(ALL) NOPASSWD: ALL**
     ! Para o jenkins ter privilégios do usuário root sem precisar de uma senha
   * Digite em seu navegador: **https://*ec2-public-ipv4*:8080**
   * Volte na EC2 para pegar a senha com : **sudo cat /var/lib/jenkins/secrets/initialAdminPassword**
   * Instale os Plugins sugeridos
   * Crie seu usuário e entre no Jenkins Dashboard
   * Instale o **Git Plugin** (Manage Jenkins -> Manage Plugins -> Available -> Git Plugin -> Download now and install after restart)
5. Criação do Webhook no Repositorio do GitHub:
   * Dentro do seu repositorio vá em **Settings -> Webhooks -> Add webhook**
   * Em 'Payload URL' coloque : **http://<ec2-public-ipv4>/github-webhook/**
   * Em 'Content Type' selecione **application/json**
   * Em 'Which events would you like to trigger this webhook?' selecione: **Let me select individual events.** e marque **Pushes** e **Pull requests**
   * Clique em Update Webhook
6. Criação da Pipeline
   * Clique em **New Item** no Dashboard
   * Dê um nome ao seu item e escolha a opção **Pipeline**
   * Em General escolha **GitHub Project** e insira o link do seu repositorio (https://github.com/usuario/repositorio)
   * Em Build Triggers selecione **GitHub hook trigger for GITScm polling**
   * Em Pipeline selecione **Pipeline from SCM** -> SCM **Git** -> Repository URL **https://token@github.com/usuario/repositorio.git** -> Credentials **none** -> Branch Specifier ** -> Script Path *caminho para o Jenkinsfile* -> Desative **Lightweight checkout**
   > ! Não esqueça de gerar seu token do github e acrescenta-lo ao link do repositorio
   
## Jenkinsfile
A pipeline executa os seguintes passos:
1. **Checkout SMC** : passo automatico da pipeline que realiza um pull do repositório para a EC2
2. **Prepare the environment** : instala os programas necessários para a execução dos códigos seguintes
3. **Build the environment**: ativa o ambiente virtual e instala as dependências necessárias contidas no requirements.txt, atráves do script build.sh
4. **Deploy** : ativa o ambiente virtual e executa o codigo main.py, atráves do script deploy.sh
5. **Sync** : sincroniza alguns arquivos com a bucket s3, atráves do script sync.sh
6. Ao final, a pipeline deleta o workspace quando o build terminar, evitando que o armazenamento seja lotado
