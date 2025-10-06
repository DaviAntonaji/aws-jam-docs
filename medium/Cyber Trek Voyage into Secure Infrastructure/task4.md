# Task 4: Version Control Vigilance Assignment

**Pontos Possíveis:** 30  
**Penalidade por Dica:** 0  
**Pontos Disponíveis:** 30

## 🎯 Background

O website sofreu uma interrupção que foi causada pela exclusão acidental de um dos objetos no bucket Amazon S3. A equipe teve que criar o objeto do zero porque eles não tinham outra versão do objeto armazenada com eles.

## 📋 Your Task

Proteja-se contra os ventos da mudança ativando o controle de versão para o bucket S3 que hospeda a fortaleza digital. Sua tarefa é manter um registro histórico de mudanças, capacitando a recuperação rápida de modificações não intencionais, exclusões ou ataques cibernéticos.

## 🚀 Getting Started

Use o botão **Open AWS Console** no topo da tela do desafio para abrir seu console AWS e obter acesso ao bucket Amazon S3.

## 📦 Inventory

- **Amazon S3 bucket:** O nome do Amazon S3 Bucket começa com `static-website-jam`

## 🛠️ Services You Should Use

- Amazon S3

## ✅ Task Validation

A tarefa será concluída automaticamente assim que você encontrar a solução. Além disso, você sempre pode verificar seu progresso pressionando o botão "Check my progress" na tela de detalhes do desafio.

---

## 🔍 Resolução Detalhada

### 🧩 Contexto do Problema

Durante uma falha recente, um dos objetos críticos do site hospedado no Amazon S3 foi acidentalmente excluído, causando uma interrupção no serviço.

A equipe precisou recriar o objeto manualmente, pois não havia nenhuma versão anterior armazenada.

Para evitar que situações semelhantes voltem a ocorrer, foi solicitado habilitar o **Versioning** no bucket S3 utilizado pela aplicação, assegurando histórico de alterações e proteção contra exclusões acidentais ou ataques maliciosos.

### ⚙️ Causa Raiz

O bucket S3 não possuía controle de versão habilitado, o que impedia:

- ❌ Recuperar versões anteriores de arquivos
- ❌ Restaurar objetos deletados
- ❌ Manter um histórico de modificações

Como resultado, qualquer exclusão resultava em perda permanente de dados.

### 🧠 Etapas da Solução

#### 1. Identificação do Recurso

- **Amazon S3 Bucket:** static-website-jam-XXXXXX

#### 2. Habilitação do Versionamento

No AWS Management Console:

1. Acesse o serviço **Amazon S3**
2. Selecione o bucket `static-website-jam-XXXXXX`
3. Navegue até a aba **Properties**
4. Localize a seção **Bucket Versioning**
5. Clique em **Edit**
6. Selecione a opção **Enable**
7. **Save changes**

### 🔧 Passo a Passo Detalhado

#### No Console AWS:

```
1. S3 Console → Buckets
2. Clique no bucket "static-website-jam-XXXXXX"
3. Aba "Properties" (Propriedades)
4. Role até "Bucket Versioning"
5. Click "Edit"
6. Selecione "Enable"
7. Click "Save changes"
8. Confirme que o status mudou para "Enabled"
```

#### Via AWS CLI:

```bash
# Habilitar versioning
aws s3api put-bucket-versioning \
  --bucket static-website-jam-XXXXXX \
  --versioning-configuration Status=Enabled

# Verificar se foi habilitado
aws s3api get-bucket-versioning \
  --bucket static-website-jam-XXXXXX

# Resultado esperado:
# {
#     "Status": "Enabled"
# }
```

### 🧾 Resultado Obtido

Após a ativação, o bucket S3 passou a:

- ✅ Manter todas as versões de cada objeto
- ✅ Incluir exclusões e atualizações no histórico
- ✅ Permitir reverter facilmente alterações indesejadas
- ✅ Restaurar qualquer arquivo removido

### 🔍 Verificação

| Ação | Resultado | Status |
|------|-----------|--------|
| Bucket Versioning habilitado | Status: "Enabled" | ✅ |
| Upload de arquivo | Versão ID gerado | ✅ |
| Atualização de arquivo | Nova versão criada | ✅ |
| Exclusão de arquivo | Delete marker criado | ✅ |
| Validação "Check my progress" | Task concluída com sucesso (30 pontos) | ✅ |

### 📊 Como o Versioning Funciona

```
Timeline do Objeto "index.html":

┌────────────────────────────────────────────┐
│ V1 (inicial)     → ID: abc123             │
│ ├─ Conteúdo: "Hello World"               │
│                                           │
│ V2 (atualização) → ID: def456             │
│ ├─ Conteúdo: "Hello AWS"                 │
│                                           │
│ V3 (exclusão)    → Delete Marker: ghi789  │
│ ├─ Objeto "aparentemente" deletado        │
│ ├─ Mas versões anteriores ainda existem! │
│                                           │
│ Restauração: Deletar o Delete Marker     │
│ ├─ V2 volta a ser a versão atual         │
└────────────────────────────────────────────┘
```

### 🛡️ Benefícios do Versioning

**Proteção contra:**
- ✅ Exclusões acidentais
- ✅ Sobrescritas não intencionais
- ✅ Ataques de ransomware
- ✅ Erros humanos

**Recursos adicionais:**
- ✅ Histórico completo de mudanças
- ✅ Recuperação rápida de qualquer versão
- ✅ Auditoria de modificações
- ✅ Compliance com regulamentações

## 🏁 Conclusão

✅ **Version Control Vigilance Assignment concluída com sucesso.**

O bucket S3 agora possui proteção completa contra perda de dados, permitindo recuperação rápida de qualquer versão anterior de arquivos.

---

## 🔧 Troubleshooting

### Problema: Não consigo habilitar Versioning

**Possíveis causas:**
1. Permissões IAM insuficientes
2. Bucket em região incorreta
3. MFA Delete já configurado

**Soluções:**
```bash
# Verificar permissões necessárias:
# - s3:PutBucketVersioning
# - s3:GetBucketVersioning

# Verificar via CLI
aws s3api get-bucket-versioning --bucket static-website-jam-XXXXXX
```

### Problema: Como ver todas as versões?

**No Console:**
1. Entre no bucket
2. Aba **Objects**
3. Toggle **Show versions** (no canto superior direito)
4. Agora você verá todas as versões de cada objeto

**Via CLI:**
```bash
aws s3api list-object-versions \
  --bucket static-website-jam-XXXXXX
```

### Problema: Como restaurar um arquivo deletado?

**Método 1: Deletar o Delete Marker (Recomendado)**
1. No console, habilite **Show versions**
2. Encontre o Delete Marker (tipo: "Delete marker")
3. Selecione e delete o Delete Marker
4. A versão anterior volta a ser a atual

**Método 2: Restaurar Versão Específica**
```bash
# Listar versões
aws s3api list-object-versions \
  --bucket static-website-jam-XXXXXX \
  --prefix index.html

# Copiar versão específica para restaurar
aws s3api copy-object \
  --bucket static-website-jam-XXXXXX \
  --copy-source static-website-jam-XXXXXX/index.html?versionId=abc123 \
  --key index.html
```

### Problema: Versioning aumenta custos

**Sim, versioning consome armazenamento adicional:**
- Cada versão é um objeto completo armazenado
- Recomendado: Configure Lifecycle Policies

**Exemplo de Lifecycle Policy:**
```json
{
  "Rules": [
    {
      "Id": "DeleteOldVersions",
      "Status": "Enabled",
      "NoncurrentVersionExpiration": {
        "NoncurrentDays": 90
      }
    }
  ]
}
```

Isso manterá versões por 90 dias e depois as deletará automaticamente.

## 📚 Conceitos Aprendidos

### S3 Versioning
- **Estados:** Unversioned (padrão), Enabled, Suspended
- **Version ID:** Identificador único para cada versão
- **Delete Markers:** Marcadores de exclusão lógica
- **Permanente:** Uma vez habilitado, não pode ser desabilitado (apenas suspenso)

### Operações com Versões

| Operação | Sem Versioning | Com Versioning |
|----------|----------------|----------------|
| Upload novo | Substitui objeto | Cria nova versão |
| Upload mesmo nome | Sobrescreve | Adiciona nova versão |
| Delete | Remove permanente | Cria Delete Marker |
| Recuperação | Impossível | Simples |

### MFA Delete (Opcional)
- Adiciona camada extra de segurança
- Requer MFA para deletar versões
- Requer MFA para desabilitar versioning
- Útil para ambientes de alta segurança

### Integração com CloudFront
- CloudFront sempre busca versão mais recente
- Delete Markers fazem CloudFront retornar 404
- Restauração reflete no CloudFront após TTL expirar

## 🎯 Boas Práticas

### ✅ DO (Faça)
- Habilite versioning em buckets críticos
- Configure Lifecycle Policies para gerenciar custos
- Use MFA Delete para ambientes sensíveis
- Monitore custos de armazenamento
- Documente processo de recuperação

### ❌ DON'T (Não Faça)
- Não deixe versões antigas acumularem sem controle
- Não dependa apenas de versioning (faça backups também)
- Não esqueça de testar recuperação regularmente
- Não habilite em buckets temporários/não críticos

### 💰 Gerenciamento de Custos

```bash
# Ver tamanho total do bucket incluindo versões
aws s3api list-object-versions \
  --bucket static-website-jam-XXXXXX \
  --output json \
  --query '[sum(Versions[].Size), sum(DeleteMarkers[].Size)]'
```

**Estratégias de otimização:**
1. **Lifecycle transitions:** Mova versões antigas para Glacier
2. **Expiration rules:** Delete versões muito antigas
3. **Delete markers cleanup:** Remova markers órfãos
4. **Monitoring:** Use S3 Storage Lens

## 🎯 Próximo Nível

Após completar esta task, considere:
- **S3 Object Lock:** Proteção WORM (Write Once Read Many)
- **Cross-Region Replication:** Replicação para outra região
- **S3 Intelligent-Tiering:** Otimização automática de custos
- **AWS Backup:** Backups automatizados e centralizados

## 📖 Recursos Adicionais

- [S3 Versioning Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html)
- [S3 Lifecycle Policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
- [S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html)
- [MFA Delete](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.html)
