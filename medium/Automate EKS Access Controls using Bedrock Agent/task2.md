# Task 2 – Delete EKS Access Entry with Bedrock Agent

## 🎯 Objetivo

Completar o OpenAPI schema usado no Bedrock Agent para permitir que o agente invoque a Lambda e delete Access Entries no EKS.

## 🔑 Pré-requisitos

- Account ID e Region do AWS JAM
- Credenciais temporárias exportadas no EC2 (mesmo procedimento da Task 1)
- Arquivo `openapi-schema.yaml` baixado do S3

## 📝 Passos Executados

### 1. Conectar no EC2 e Configurar Credenciais

```bash
cd ~
# Cole/exporte novamente as credenciais do JAM
export AWS_ACCESS_KEY_ID=...
export AWS_SECRET_ACCESS_KEY=...
export AWS_SESSION_TOKEN=...
export AWS_DEFAULT_REGION=us-east-1
```

### 2. Baixar o Schema Original

```bash
aws s3 cp s3://aws-jam-challenge-resources-us-east-1/eks-access-controls-bedrock/openapi-schema.yaml .
```

### 3. Editar o Schema

Abra `openapi-schema.yaml` e adicione a definição do Delete Access Entry.

**Exemplo de como deve ficar a nova rota:**

```yaml
paths:
  /createAccessEntry:
    post:
      summary: Create an EKS Access Entry
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                clusterName:
                  type: string
                  description: The name of the EKS cluster
                principalArn:
                  type: string
                  description: The ARN of the IAM role or user
      responses:
        '200':
          description: Access entry created successfully

  /deleteAccessEntry:
        post:
            summary: API to delete an EKS Access Entry
            description: Delete the access entry for the given IAM principal from the specified EKS cluster.
            operationId: deleteAccessEntry
            requestBody:
              required: true
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      clusterName:
                        type: string
                        description: Name of the EKS cluster to delete the access entry from.
                      principalArn:
                        type: string
                        description: The ARN of the IAM principal whose access entry will be deleted.
                    required:
                      - clusterName
                      - principalArn
            responses:
                '200':
                    description: Access entry deleted successfully
                '400':
                    description: Bad request. One or more required fields are missing or invalid.

```

> **Observação:** O Lambda já implementa `/deleteAccessEntry`. O schema só precisa expor essa rota para o agente saber chamar.

### 4. Atualizar o Agente (Action Group)

**Navegação no Console:**
- Console → Amazon Bedrock → Agents → `eks-bedrock-agent` → Edit

**Configuração:**
- Em Action groups → `Action_Group_1`, selecione **Define with API schemas**
- Cole o `openapi-schema.yaml` atualizado (com o bloco do `/deleteAccessEntry` que você adicionou)
- **Deploy:** Save → Prepare → Deploy (garanta que uma alias esteja selecionada/atualizada)

> **Dica:** Se o console apontar erro de schema, confira a indentação YAML e se `paths:/deleteAccessEntry: delete:` está no mesmo nível de `/createAccessEntry`.

### 5. Validação via Test Agent

**Navegação:**
- Agents → `eks-bedrock-agent` → Test agent (com a alias ativa)

**Prompt de teste:**
```
Delete access entry for role arn:aws:iam::115476679712:role/eks-pod-test-role in cluster jam-eks-cluster
```

**Respostas esperadas:**
- **200 OK** com mensagem tipo "Successfully deleted the access entry" (é o texto que o Lambda retorna hoje)
- Se o entry já tiver sido removido, você pode ver um erro do EKS informando que não foi encontrado — nesse caso, recrie com o prompt da Task 1 e tente deletar novamente

### 6. Verificação por CLI (Opcional)

```bash
# Deve não encontrar (ou retornar erro de not found) após o delete:
aws eks describe-access-entry \
  --cluster-name jam-eks-cluster \
  --principal-arn arn:aws:iam::115476679712:role/eks-pod-test-role
```

## 🔧 Troubleshooting Rápido

| Problema | Solução |
|----------|---------|
| **"The agent is not found"** | Confira região e se você Prepare/Deploy a versão nova na alias |
| **AccessDenied ao invocar Lambda** | Garanta que a Lambda tem a resource-policy permitindo `bedrock.amazonaws.com` invocar (o add-permission da Task 1) |
| **Schema error** | Valide indentação, tipos (`type: object`, `properties:`) e `requestBody.required: true` |

## ✅ Resultado

O Bedrock Agent agora pode deletar EKS Access Entries através de comandos em linguagem natural, completando a funcionalidade de gerenciamento automatizado de acessos ao cluster EKS.