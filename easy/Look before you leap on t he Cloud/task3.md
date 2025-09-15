# Task 3: Perda de controle administrativo da chave KMS

## 🎯 Objetivo

Recuperar o **controle administrativo** da chave `jam-data-encryption-key`, garantindo que o Security Admin Role (`AWSLabsUser-...`) voltasse a ter poderes de administração após o término da fase de desenvolvimento.

### Meta Principal
- ✅ Restaurar acesso administrativo para o Security Admin Role
- ✅ Manter acesso do role temporário durante a transição
- ✅ Permitir operações de gerenciamento da chave (rotação, tags, descrição)

## 🔎 Problema Identificado

### Configuração Problemática
- **Problema:** A Key Policy só incluía o role temporário `jam-aws-tmp-admin-role` como administrador
- **Limitação:** KMS ignora as permissões de IAM policy e se baseia **apenas na Key Policy**
- **Resultado:** O Security Admin (`AWSLabsUser-...`) não tinha nenhuma entrada de Principal

### Por que isso é crítico?
```
IAM Policies ❌ → KMS Key Policy ✅
```
Diferente de outros serviços AWS, o **KMS usa exclusivamente a Key Policy** para controle de acesso, ignorando IAM policies anexadas aos usuários/roles.

### Erro Típico
```
AccessDenied: User: arn:aws:sts::account:assumed-role/AWSLabsUser-xxx 
is not authorized to perform: kms:DescribeKey on resource: arn:aws:kms:region:account:key/key-id
```

## 🛠️ O que fizemos inicialmente (e estava certo)

### Abordagem Técnica Correta
1. **Assumimos o role temporário** (`jam-aws-tmp-admin-role`) para editar a Key Policy
2. **Adicionamos um novo bloco separado**, dando `"kms:*"` para o `AWSLabsUser-...`
3. **Com isso, tecnicamente** o Security Admin já teria acesso administrativo
4. **Também testamos** ações administrativas (ex.: alterar rotação, descrição, tags)

### Policy que Criamos (Funcionalmente Correta)
```json
{
  "Sid": "Allow Security Admin Full Access",
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::537782114215:role/AWSLabsUser-hPngNqy5a6LfNCxmviPGG7"
  },
  "Action": "kms:*",
  "Resource": "*"
}
```

## ❌ O que estava "errado"

### Problema de Validação (não de Segurança)
- **Issue:** O validador do Jam não aceitava um **bloco separado** para o Security Admin
- **Expectativa:** Ele esperava que o ARN do Security Admin fosse incluído no **mesmo bloco** `"Sid": "Allow access for Key Administrators"`
- **Realidade:** Era um detalhe de **formato da Key Policy**, não de permissões em si

### Lição Aprendida: Labs vs Mundo Real
```
Mundo Real: ✅ Múltiplos statements são válidos e seguros
AWS Jam Lab: ❌ Validador espera formato específico
```

## 💡 Por que pegamos a dica

### Frustração Técnica
- Mesmo com a policy **correta em termos de permissão**, o desafio não concluía
- Ao usar a dica, entendemos que o validador exige que a correção seja feita na **mesma declaração** já existente de administradores
- **Lado a lado** com o role temporário, não em statement separado

## 🔧 Resolução Final (Policy Corrigida)

### Solução Aceita pelo Validador
Adicionamos o Security Admin role no **array de Principals** do mesmo bloco `Allow access for Key Administrators`:

```json
{
  "Sid": "Allow access for Key Administrators",
  "Effect": "Allow",
  "Principal": {
    "AWS": [
      "arn:aws:iam::537782114215:role/jam-aws-tmp-admin-role",
      "arn:aws:iam::537782114215:role/AWSLabsUser-hPngNqy5a6LfNCxmviPGG7"
    ]
  },
  "Action": [
    "kms:Create*",
    "kms:Describe*",
    "kms:Enable*",
    "kms:List*",
    "kms:Put*",
    "kms:Update*",
    "kms:Revoke*",
    "kms:Disable*",
    "kms:Get*",
    "kms:Delete*",
    "kms:Tag*",
    "kms:Untag*",
    "kms:ScheduleKeyDeletion",
    "kms:CancelKeyDeletion"
  ],
  "Resource": "*"
}
```

### Passo a Passo da Correção
1. **Assumir o role temporário** com `aws sts assume-role`
2. **Editar a Key Policy** via KMS Console ou CLI
3. **Localizar o statement** `"Allow access for Key Administrators"`
4. **Converter Principal** de string para array
5. **Adicionar o ARN** do Security Admin ao array
6. **Salvar** e testar as permissões

## ✅ Resultado

### Controle Restaurado
- ✅ O Security Admin role (`AWSLabsUser-...`) **recuperou plenos poderes** administrativos sobre a chave
- ✅ Foi possível **editar a chave** e executar ações como ativar/desativar rotação, alterar descrição e adicionar tags
- ✅ O desafio foi **marcado como concluído** após a correção

### Validação das Operações
```bash
# Testes que passaram a funcionar
aws kms describe-key --key-id jam-data-encryption-key
aws kms put-key-policy --key-id jam-data-encryption-key --policy-name default --policy file://policy.json
aws kms enable-key-rotation --key-id jam-data-encryption-key
aws kms tag-resource --key-id jam-data-encryption-key --tags TagKey=Environment,TagValue=Production
```

## 🔍 Conceitos-Chave

### KMS Key Policies vs IAM Policies
| Aspecto | KMS Key Policy | IAM Policy |
|---------|----------------|------------|
| **Precedência** | ✅ Primária | ❌ Ignorada pelo KMS |
| **Escopo** | Por chave | Por usuário/role |
| **Controle** | Granular por recurso | Amplo por serviço |

### Principal Types em KMS
```json
{
  "Principal": {
    "AWS": [
      "arn:aws:iam::account:root",           // Conta inteira
      "arn:aws:iam::account:role/role-name", // Role específico
      "arn:aws:iam::account:user/user-name"  // Usuário específico
    ]
  }
}
```

### Best Practices para Key Policies
- **Least Privilege:** Conceder apenas permissões necessárias
- **Multiple Admins:** Sempre ter múltiplos administradores
- **Role-based:** Preferir roles a usuários individuais
- **Documentation:** Documentar mudanças e justificativas

## 🚨 Troubleshooting

### Problemas Comuns
- **AccessDenied:** Verificar se o principal está na Key Policy
- **Cannot assume role:** Verificar trust relationship do role temporário  
- **Policy malformed:** Validar JSON syntax
- **Lab não aceita:** Seguir formato específico do validador

### Ferramentas de Diagnóstico
- **KMS Console:** Visualizar Key Policy atual
- **AWS CLI:** `aws kms get-key-policy --key-id <key-id> --policy-name default`
- **CloudTrail:** Auditar tentativas de acesso à chave
- **IAM Policy Simulator:** Testar permissões (limitado para KMS)