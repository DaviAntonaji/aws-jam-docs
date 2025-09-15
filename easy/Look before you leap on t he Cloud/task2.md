# Task 2: Lambda não consegue ler/escrever no S3

## 🎯 Objetivo

Permitir que a função Lambda consiga realizar **operações CRUD** em um bucket S3 criado via CloudFormation.

### Operações Necessárias
- ✅ **ListBucket** - Listar objetos no bucket
- ✅ **GetObject** - Ler objetos do bucket
- ✅ **PutObject** - Gravar objetos no bucket
- ✅ **DeleteObject** - Excluir objetos do bucket

## 🔎 Problema Identificado

### Permissões Insuficientes
- **Problema:** O IAM Role do Lambda estava com apenas a policy `AWSLambdaVPCAccessExecutionRole` anexada
- **Limitação:** Essa policy é suficiente para logs e acesso à VPC, mas **não concede permissões de S3**
- **Resultado:** A função não conseguia realizar `GetObject` / `PutObject` / `DeleteObject` no bucket

### Erro Típico
```
AccessDenied: User: arn:aws:sts::account:assumed-role/lambda-role/function-name 
is not authorized to perform: s3:GetObject on resource: arn:aws:s3:::bucket-name/object-key
```

## 🔧 Resolução

### Passo a Passo
Foi necessário anexar uma **policy adicional** ao IAM Role do Lambda, concedendo permissões específicas para o bucket S3:

1. **Abrir o IAM Console** → Roles → selecionar o role do Lambda
2. **Em Permissions policies**, clicar em `Add permissions` → `Attach policies`
3. **Adicionar uma policy** de acesso ao S3 (inline ou gerenciada)

### Permissões Necessárias

#### Nível de Bucket
- `s3:ListBucket` no bucket

#### Nível de Objeto
- `s3:GetObject`, `s3:PutObject`, `s3:DeleteObject` nos objetos (`/*`)

### Policy Aplicada

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "BucketLevel",
      "Effect": "Allow",
      "Action": ["s3:ListBucket"],
      "Resource": "arn:aws:s3:::labstack-prewarm-d660c976-e848-4aae-9c-task4bucket-j5bixhzmptwh"
    },
    {
      "Sid": "ObjectLevel",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject"
      ],
      "Resource": "arn:aws:s3:::labstack-prewarm-d660c976-e848-4aae-9c-task4bucket-j5bixhzmptwh/*"
    }
  ]
}
```

## ✅ Resultado

### Operações Habilitadas
- ✅ O Lambda passou a ter **acesso completo** para listar, ler, gravar e excluir objetos no bucket
- ✅ Testes confirmaram a **leitura e escrita** no S3 sem erros de `AccessDenied`
- ✅ Problema resolvido **sem necessidade** de alterar a Bucket Policy ou infraestrutura de rede

### Validação
```python
# Exemplo de código Lambda que agora funciona
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'your-bucket-name'
    
    # ListBucket
    response = s3.list_objects_v2(Bucket=bucket_name)
    
    # GetObject
    obj = s3.get_object(Bucket=bucket_name, Key='test.txt')
    
    # PutObject
    s3.put_object(Bucket=bucket_name, Key='new-file.txt', Body='Hello World')
    
    # DeleteObject
    s3.delete_object(Bucket=bucket_name, Key='old-file.txt')
    
    return {'statusCode': 200, 'body': 'Success!'}
```

## 🔍 Conceitos-Chave

### IAM Roles para Lambda
- **Execution Role:** Define o que a função pode fazer
- **Managed Policies:** Policies pré-definidas pela AWS
- **Inline Policies:** Policies customizadas específicas para o role

### S3 Permissions Model
- **Bucket-level permissions:** Operações no bucket (`ListBucket`)
- **Object-level permissions:** Operações nos objetos (`GetObject`, `PutObject`, etc.)
- **Resource ARNs:** Diferença entre `bucket-name` e `bucket-name/*`

### Least Privilege Principle
- Conceder apenas as permissões **mínimas necessárias**
- Especificar recursos específicos quando possível
- Evitar usar `*` em Actions e Resources desnecessariamente

## 🚨 Troubleshooting

### Erros Comuns
- **AccessDenied:** Verificar se a policy está anexada ao role correto
- **Resource mismatch:** Confirmar ARNs do bucket na policy
- **Action mismatch:** Verificar se as actions necessárias estão incluídas

### Ferramentas de Diagnóstico
- **CloudWatch Logs:** Verificar erros detalhados da função
- **IAM Policy Simulator:** Testar permissões antes de aplicar
- **AWS CloudTrail:** Auditar tentativas de acesso negadas