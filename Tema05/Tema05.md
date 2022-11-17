# Resumo de alguns recursos da GCP:

## VPC:
Assim como a VPC da AWS, a GCP também possui Redes Virtuais na Nuvem, que são versões virtuais de uma rede física, implementadas dentro da rede de produção da Google. Além disso, também podemos separar uma VPC em Sub-Redes, controlar o tráfego de entrada e saída das instâncias pelas Regras de Firewall (parecido com o Security Group da AWS), e conectar duas VPCs com o VPC Network Peering (equivalente ao VPC Peering da AWS).

## Monitoring:
Equivalente ao CloudWatch da AWS, o Monitoring da GCP coleta métricas dos recursos utilizados, sendo possível visualizar e monitorar essas medições, além de podermos criar Políticas de Alertas para sermos notificados quando o desempenho de um serviço não atender aos critérios definidos ou atingir um limite definido.

## Google Compute Engine - GCE:
Equivalente ao EC2 (Elastic Compute Cloud) da AWS, o GCE permite a criação e gerenciamento de instâncias de máquinas virtuais hospedadas na infraestrutura da Google. 

## Google Cloud Storage - GCS:
Equivalente ao S3 da AWS, o GCS permite o armazenamento de objetos (parte imutável de dados em qualquer formato) em contêineres chamados buckets. Podemos conceder permissões para tornar os objetos acessíveis a determinados usuários ou a todos da internet pública. Além disso, o GCS possui 4 classes de armazenamento para escolhermos de acordo com a finalidade do bucket, são elas: Standard, Nearline, Coldline e Archive.

## Functions:
Equivalente ao Lambda da AWS, o Functions da GCP permite a criação, execução e gerenciamento de códigos sem o uso de servidores, ou seja, é utilizado para construir aplicações sem se preocupar com a infraestrutura por baixo dela, além de conectar serviços orientados a eventos com códigos simples e de finalidade única. Logo, a função criada é acionada quando um evento é disparado ou por uma solicitação HTTP.

