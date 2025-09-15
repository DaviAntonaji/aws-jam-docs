# Task 4: Cross-account access no bucket S3

## 🎯 Objetivo

Garantir que **somente a role S3CrossAccountAccess** da conta parceira (`739275461757`) pudesse acessar os dados no bucket `labstack-prewarm-d660c976-e848-4aae-9c-task4bucket-j5bixhzmptwh`, evitando que **todos os usuários da conta inteira** tivessem acesso.

### Princípio de Segurança
- ✅ **Least Privilege:** Acesso restrito apenas ao role necessário
- ✅ **Cross-Account Security:** Controle granular entre contas AWS
- ✅ **Auditabilidade:** Saber exatamente quem pode acessar os dados

## 🔎 Problema Identificado

### Configuração Insegura
A **Bucket Policy** estava assim:

```json
"Principal": {
  "AWS": "arn:aws:iam::739275461757:root"
}
```

### Por que isso é problemático?
- **Escopo muito amplo:** `root` significa **qualquer usuário ou role** da conta `739275461757`
- **Violação de segurança:** Todos conseguiam acessar, não apenas a role esperada
- **Falta de controle:** Impossível auditar ou restringir acesso específico

### Impacto de Segurança
```
❌ Antes: Conta inteira (root) → Acesso total
✅ Depois: Role específico → Acesso controlado
```

### Quem tinha acesso indevido?
- Usuários IAM da conta `739275461757`
- Outros roles da mesma conta
- Qualquer serviço assumindo roles daquela conta
- Potencialmente centenas de entidades

## 🛠️ O que fizemos

### Análise e Diagnóstico
1. **Revisamos a Bucket Policy atual** no console do S3
2. **Identificamos o uso incorreto** de `root` como principal
3. **Mapeamos o role correto** (`S3CrossAccountAccess`)
4. **Analisamos as permissões necessárias** (ListBucket + GetObject)

### Correções Implementadas
1. **Substituímos o Principal** para referenciar diretamente a role `S3CrossAccountAccess`
2. **Corrigimos os Resources**, separando permissões de bucket e objetos:
   - `s3:ListBucket` → recurso = apenas o bucket
   - `s3:GetObject` → recurso = `bucket/*`

## 🔧 Policy Corrigida

### Solução Final
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowCrossAccountRoleList",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::739275461757:role/S3CrossAccountAccess"
      },
      "Action": ["s3:ListBucket"],
      "Resource": "arn:aws:s3:::labstack-prewarm-d660c976-e848-4aae-9c-task4bucket-j5bixhzmptwh"
    },
    {
      "Sid": "AllowCrossAccountRoleGetObject",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::739275461757:role/S3CrossAccountAccess"
      },
      "Action": ["s3:GetObject"],
      "Resource": "arn:aws:s3:::labstack-prewarm-d660c976-e848-4aae-9c-task4bucket-j5bixhzmptwh/*"
    }
  ]
}
```

### Passo a Passo da Correção
1. **Acessar S3 Console** → Buckets → selecionar o bucket
2. **Ir em Permissions** → Bucket policy
3. **Editar a policy** existente
4. **Substituir** `"arn:aws:iam::739275461757:root"` por `"arn:aws:iam::739275461757:role/S3CrossAccountAccess"`
5. **Verificar** os recursos (bucket vs bucket/*)
6. **Salvar** e testar o acesso

## ✅ Resultado

### Segurança Restaurada
- ✅ **Apenas a role S3CrossAccountAccess** da conta `739275461757` manteve o acesso
- ✅ **Usuários comuns** daquela conta perderam o acesso
- ✅ A **validação do Jam** confirmou a correção

### Teste de Validação
```bash
# Role autorizado - deve funcionar
aws s3 ls s3://bucket-name/ --profile cross-account-role

# Usuário comum - deve falhar
aws s3 ls s3://bucket-name/ --profile regular-user
# Resultado: AccessDenied
```

### Comparação de Acesso

| Entidade | Antes (root) | Depois (role específico) |
|----------|--------------|--------------------------|
| **S3CrossAccountAccess role** | ✅ Permitido | ✅ Permitido |
| **Usuários IAM** | ❌ Permitido | ✅ Negado |
| **Outros roles** | ❌ Permitido | ✅ Negado |
| **Serviços AWS** | ❌ Permitido | ✅ Negado |

## 🔍 Conceitos-Chave

### Cross-Account Access Patterns

#### ❌ Padrão Inseguro (root)
```json
{
  "Principal": {
    "AWS": "arn:aws:iam::ACCOUNT-ID:root"
  }
}
```
- Permite **qualquer entidade** da conta
- **Alto risco** de acesso não autorizado
- Difícil de **auditar** e **controlar**

#### ✅ Padrão Seguro (role específico)
```json
{
  "Principal": {
    "AWS": "arn:aws:iam::ACCOUNT-ID:role/SPECIFIC-ROLE"
  }
}
```
- Permite **apenas o role** especificado
- **Controle granular** de acesso
- **Auditabilidade** completa

### S3 Resource Types
| Action | Resource Type | Example |
|--------|---------------|---------|
| `s3:ListBucket` | **Bucket** | `arn:aws:s3:::bucket-name` |
| `s3:GetObject` | **Object** | `arn:aws:s3:::bucket-name/*` |
| `s3:PutObject` | **Object** | `arn:aws:s3:::bucket-name/*` |

### Best Practices
- **Principle of Least Privilege:** Conceder apenas permissões mínimas necessárias
- **Role-based Access:** Preferir roles a usuários individuais
- **Resource Specificity:** Usar ARNs específicos, não wildcards
- **Regular Auditing:** Revisar policies periodicamente

## 🚨 Troubleshooting

### Problemas Comuns
- **AccessDenied após correção:** Verificar se o role está assumindo corretamente
- **Policy malformed:** Validar sintaxe JSON
- **Resource mismatch:** Confirmar ARNs do bucket
- **Cross-account trust:** Verificar trust policy do role

### Ferramentas de Diagnóstico
- **S3 Console:** Verificar bucket policy atual
- **CloudTrail:** Auditar tentativas de acesso
- **AWS CLI:** Testar acesso com diferentes profiles
- **IAM Policy Simulator:** Simular permissões cross-account

### Comandos Úteis
```bash
# Verificar bucket policy
aws s3api get-bucket-policy --bucket bucket-name

# Testar acesso com role específico
aws sts assume-role --role-arn arn:aws:iam::ACCOUNT:role/ROLE --role-session-name test

# Listar objetos (teste de permissão)
aws s3 ls s3://bucket-name/ --profile assumed-role
```

## 🎯 Lições Aprendidas

### Segurança Cross-Account
1. **Nunca use `root`** como principal em policies cross-account
2. **Sempre especifique roles** ou usuários exatos
3. **Separe permissões** por tipo de recurso (bucket vs objects)
4. **Teste regularmente** o acesso de diferentes entidades

### Compliance e Governança
- **Documentar** todas as permissões cross-account
- **Revisar periodicamente** os acessos concedidos
- **Implementar alertas** para mudanças em bucket policies
- **Manter logs** de todos os acessos cross-account