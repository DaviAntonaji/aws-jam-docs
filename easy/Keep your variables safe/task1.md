AWS Jam Lab – Encrypt Lambda Environment Variables with KMS
Objetivo

Configurar variáveis de ambiente de uma função Lambda para ficarem criptografadas em repouso com uma Customer Managed Key (CMK) no KMS e, opcionalmente, em trânsito utilizando os helpers do console.

Passo a Passo
1. Abrir a função Lambda

Acesse o console da AWS.

Vá em Lambda → Functions.

Selecione a função myLambdaFunction.

2. Configurar variáveis de ambiente

No menu lateral, clique em Configuration → Environment variables.

Clique em Edit.

Adicione uma variável, por exemplo:

Key: databaseUser

Value: admin

3. Ativar criptografia com KMS

Role até a seção Encryption configuration.

Em AWS KMS key to encrypt at rest, selecione:

Use a customer master key.

Informe o ARN da sua chave KMS (myKeyAlias).

Exemplo:

arn:aws:kms:ap-southeast-2:593529499886:key/1565ecdc-f0e7-4b2f-9d6d-60d545a2a40f

4. (Opcional – se o lab pedir) Habilitar criptografia em trânsito

Marque a opção Enable helpers for encryption in transit.

Ao lado do campo da variável (databaseUser), clique em Encrypt.

O console vai cifrar localmente antes de enviar.

5. Salvar a configuração

Clique em Save.

Importante: Ignore qualquer aviso de Access denied to access-analyzer:ValidatePolicy.

Esse erro aparece porque o ambiente do Jam não tem permissão de usar o Access Analyzer, mas não impacta o lab.

6. Validar no Jam

Volte para a tela do Challenge no Jam.

Clique em Check my progress.

O status deve mudar para Completed. 🎉

Notas

A role myLambdaFunctionExecutionRole precisa ter permissões kms:Encrypt, kms:Decrypt, kms:GenerateDataKey*, kms:DescribeKey na chave.

No console do Jam, a AWS já costuma pré-configurar a role — você só precisa selecionar a CMK correta e salvar.

O erro de ValidatePolicy é apenas visual; pode ser ignorado.