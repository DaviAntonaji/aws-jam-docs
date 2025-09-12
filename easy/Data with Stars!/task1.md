# Data with the Stars – Task 1

## 🎯 Objetivo

Restringir o acesso a dados de pacientes (ePHI) em conformidade com HIPAA:

- USER-B não pode visualizar nem interagir com nenhum dado do bucket de pacientes.
- USER-A deve ter acesso total ao bucket de pacientes.

## ⚠️ Contexto e Limitação

Tentamos criar políticas IAM para gerenciar permissões (Deny para USER-B e Allow para USER-A), mas encontramos erros devido à falta de permissão para gerenciamento de IAM no ambiente de lab:

```
Access denied to iam:CreatePolicy
You don't have permission to iam:CreatePolicy
```

Também não foi possível aplicar políticas via operações `iam:Put*`. Portanto, não havia privilégios de IAM Admin para criar ou anexar políticas a usuários.

## ✅ Solução (Bucket Policy no S3)

Identificamos o bucket de pacientes e aplicamos diretamente uma Bucket Policy, evitando depender de permissões IAM:

- Bucket de pacientes: `jam-challenge-patientdata-us-east-1-192311737766`

### Policy aplicada

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyAllToUserB",
      "Effect": "Deny",
      "Principal": { "AWS": "arn:aws:iam::192311737766:user/USER-B" },
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::jam-challenge-patientdata-us-east-1-192311737766",
        "arn:aws:s3:::jam-challenge-patientdata-us-east-1-192311737766/*"
      ]
    },
    {
      "Sid": "AllowAllToUserA",
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::192311737766:user/USER-A" },
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::jam-challenge-patientdata-us-east-1-192311737766",
        "arn:aws:s3:::jam-challenge-patientdata-us-east-1-192311737766/*"
      ]
    }
  ]
}
```

## 🔎 Validação

- USER-A: conseguiu listar e interagir com os objetos do bucket.
- USER-B: recebeu `AccessDenied` em todas as tentativas.

## 📌 Conclusão

- IAM Policies não puderam ser usadas por falta de permissões no ambiente.
- A alternativa viável foi aplicar uma Bucket Policy diretamente no S3.
- O controle de acesso atende aos requisitos de HIPAA: apenas usuários autorizados acessam ePHI e tentativas não autorizadas são negadas e registradas.