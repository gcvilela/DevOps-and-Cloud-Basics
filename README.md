# DevOps and Cloud Basics

Nesta trilha de aprendizado aprendemos que tão importante quanto saber um conceito é saber repassar o conhecimento. Além disso, aprendemos o básico de AWS e GCP e aprender a evoluir um programa simples em Python dentro dos conceitos de DevOps.

## Tema 01: DevOps Culture Principles
Artigo sobre as vantagens que uma cultura DevOps pode trazer para o seu time técnico e como implementá-la.

## Tema 02 e 03: Arquiteturas On Premises e 03 - Arquiteturas Cloud
Artigo sobre as Melhores práticas de Arquiteturas de On Premises e Cloud e quando utilizá-las.

## Tema 04: AWS Basic
Criação de uma EC2 free-tier dentro da AWS e de um bucket no S3, no qual realizei o upload de um arquivo para dentro dele e realizei o sync entre o arquivo do bucket com a EC2 criada, em seguida, realizei o caminho inverso, criei um arquivo dentro da instância e fiz o sync com o bucket.
Além disso, criação de um markdown com um breve resumo para que serve a VPC, Roles, NAT, Security Gateways e Routes. Além de descrever o que é um VPC Peering e quando devemos utilizá-lo.

## Tema 05: GCP Basic
Criação de uma GCE free-tier dentro da GCP e de um bucket no GCS, no qual realizei o upload de um arquivo para dentro dele e realizei o sync entre o arquivo do bucket com a GCE criada, em seguida, realizei o caminho inverso, criei um arquivo dentro da instância e fiz o sync com o bucket.
Além disso, criação um md com um breve resumo para que serve a VPC, Monitoring, GCE, GCS e Functions.

## Tema 06: Python
Programa usando Python e suas bibliotecas, que conecta no Twitter e recupera os últimos 10 tweets a respeitos
dos 10 atores que mais fizeram filmes nos últimos 10 anos com base nas informações de catálogo fornecidas pelo IMDB.
 
## Tema 07 e Tema 08: Tarefas Agendadas em Linux e Windows
> Tema 07: criação de uma máquina linux no free-tier dentro da AWS, no qual roda de forma agendada o código criado no exercício 06. Além da realização de melhorias no código para gerar arquivos texto com resultado, e esses, forão sincronizados com minha bucket na conta AWS.

 > Tema 08: após instalar uma VM com Windows usando o software o VirtualBox, realizei o mesmo processo do exercício anterior. A diferença é que o agendamento dentro do Windows é realizado executando um script powershell.
 
## Tema 09: Jenkins
Automatização do processo de deploy do código, onde puxa do meu github e faz o deploy dentro da minha EC2 Linux.

## Tema 10: Docker and Containers
Tranformação do código para rodar em um contêiner Docker.

## Tema 11: Stack ELK
Instalação em conteneires Docker da Stack ELK, gerando uma URL para o Kibana, capturando os logs do processo de pesquisa do twitter, além dos termos resultados e a quantidade de resultados.

## Tema 12: Terraform
Finalizando a solução completa, o último passo foi a criação de um código de infra as a code. Por isso, usando Terraform, gerei o código para criar todo o meu ambiente dentro da AWS do zero.
