# Resumo de alguns recursos da AWS:

## Roles: 
Uma função ou papel do IAM (Gerenciador de acesso e identidade) é uma identidade em uma conta AWS que possui permissões específicas com credenciais de segurança temporárias, ou seja, ao contrário dos usuários do IAM, as roles não possuem senhas e são utilizadas para delegar acesso a usuários, aplicativos e serviços que normalmente não possuem acesso a certos recursos da AWS.

## VPC:
A Virtual Private Cloud é uma rede virtual totalmente dedicada para uma conta, para se ter acesso a uma parte isolada da infraestrutura de toda a AWS, e assim provisionar os recursos da nuvem. Além disso, a VPC define como será o acesso de rede das aplicações para redes externas, como a Internet.

## VPC Peering:
O VPC Peering estabelece uma conexão entre duas VPCs, permitindo rotear o tráfego entre elas usando endereços IPV4 privados ou endereços IPV6. Com ele, as instâncias, em qualquer uma das VPCs, podem se comunicar umas com as outras como se estivessem na mesma rede. Podemos utilizá-lo para realizar transferências de dados entre diferentes contas da AWS através do emparelhamento das VPCs, e também utilizá-lo entre VPCs de diferentes regiões para que os recursos executados em diversos locais comuniquem entre si sem precisar de gateways, VPN ou equipamentos de rede separados.  

## Security Gateway:
O Security Gateway (ou Internet Gateway) é responsável por conectar as subnets públicas da VPC à internet, ou seja, todo o tráfego de entrada e saída externo da subnet passa por ele. Além disso, fornecem um destino nas routes tables da VPC para o tráfego na internet e executam o NAT Gateway para instâncias com endereços IPv4 públicos.

## Nat Gateway:
Assim como o Internet Gateway conecta as subnets públicas a internet, o Nat Gateway conecta subnets privadas a internet expondo um único endereço IP para os endereços externos, porém é utilizado apenas para tráfego de saída,ou seja, a internet não possui permissão para acessar as subnets privadas. Além disso, é provisionado em uma subnet pública e todo o tráfego externo das subnets privadas passa por ele.

## Routes:
As rotas são um conjunto de regras que direcionam para que lugar o tráfego de rede de uma sub-rede ou gateway deve ir, funciona como um roteador, gerenciando as entradas e saídas internas e externas da rede.

