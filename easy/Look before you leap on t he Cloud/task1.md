Task 1: VPC Lambda doesn’t work
🎯 Objetivo

Corrigir a execução da função MyFunction em um ambiente VPC, garantindo que o Lambda consiga:

Acessar a internet (ex.: http://example.com).

Acessar um servidor web hospedado em uma instância EC2 em subnet privada.

🔎 Problema Identificado

O Lambda estava associado a subnets públicas.

Lambdas não recebem IP público mesmo em subnet pública.

Resultado: sem conectividade com a internet e falha no acesso ao EC2 privado.

🔧 Resolução

Sem alterar recursos de rede (ENI, IGW, NAT, route tables), a solução foi feita apenas no Lambda Configuration:

Acessar AWS Lambda Console → Functions → MyFunction.

Ir em Configuration → VPC → Edit.

Selecionar a VPC correta.

Escolher as duas subnets privadas do ambiente.

Manter o Security Group padrão (nenhuma alteração necessária).

Salvar e reexecutar a função.

✅ Resultado

Lambda passou a usar as subnets privadas, que já possuíam rota para o NAT Gateway.

Conseguiu acessar tanto a internet quanto o EC2 privado.

Erros de rede desapareceram dos logs do CloudWatch.

Nenhuma alteração de Security Group foi necessária.