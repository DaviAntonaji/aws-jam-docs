# Task 1 – Automating EKS Access Entry with Bedrock Agent

## 🎯 Objetivo

Automatizar a criação de EKS Access Entries usando um Amazon Bedrock Agent com Action Group e Lambda, eliminando a necessidade de configurar manualmente acessos aos clusters.

## 🔑 Pré-requisitos

- Account ID e Region fornecidos pelo AWS JAM
- Modelo Amazon Nova Lite habilitado no Bedrock Console
- Instância EC2 (TestInstance) acessível via Session Manager
- Credenciais temporárias (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN) obtidas no botão `>_ AWS CLI` do JAM Console

## 📝 Passos Executados

### 1. Configuração Inicial

```bash
# No EC2 via Session Manager
export AWS_ACCESS_KEY_ID=...
export AWS_SECRET_ACCESS_KEY=...
export AWS_SESSION_TOKEN=...
export AWS_DEFAULT_REGION=us-east-1
export AWS_EC2_METADATA_DISABLED=true

aws sts get-caller-identity
```

### 2. Download do Schema

```bash
aws s3 cp s3://aws-jam-challenge-resources-us-east-1/eks-access-controls-bedrock/openapi-schema.yaml .
```

### 3. Configuração do Bedrock Agent

**Navegação no Console:**
- Console → Bedrock → Agents → `eks-bedrock-agent`

**Criar Action Group:**
- **Type:** Define with API schemas
- **Schema:** Colar o conteúdo do `openapi-schema.yaml`
- **Invocation:** Lambda existente `bedrock-agent-eks-access-control`
- **Deploy:** Salvar → Prepare → Create Alias → Deploy

### 4. Implementação no Lambda

#### Imports Necessários

```javascript
import {
  EKSClient,
  CreateAccessEntryCommand,
  DeleteAccessEntryCommand,
  ListAssociatedAccessPoliciesCommand,
} from "@aws-sdk/client-eks";
```

#### Implementação do Endpoint `/createAccessEntry`

```javascript
if (api_path == '/createAccessEntry') {
  try {
    var array = event['requestBody']['content']['application/json']['properties'];
    array.forEach((element) => {
      if (element['name'] == 'clusterName')
        clusterName = element['value'];
      else if (element['name'] == 'principalArn')
        principalArn = element['value'];
    });

    const input = { clusterName, principalArn };
    command = new CreateAccessEntryCommand(input);
    res = await client.send(command);

    const accessEntry = res?.accessEntry || {};
    body = {
      message: "Access entry created",
      accessEntryArn: accessEntry.accessEntryArn,
      accessEntry
    };
    response_code = 200;
    response_body = { "application/json": { "body": JSON.stringify(body) } };
  } catch (error) {
    const reason = error instanceof Error
      ? error.message + ` API Call - ${api_path}`
      : `error occurred in API call ${api_path}`;
    body = { error: reason };
    response_code = 400;
    response_body = { "application/json": { "body": JSON.stringify(body) } };
  }
}
```

### 5. Configuração de Permissões IAM

#### Role do Lambda

```json
{
  "Effect": "Allow",
  "Action": [
    "eks:CreateAccessEntry",
    "eks:DescribeAccessEntry",
    "eks:ListAccessEntries"
  ],
  "Resource": "*"
}
```

### 6. Validação

**Prompt no Test Agent:**

```
Create access entry for role arn:aws:iam::115476679712:role/eks-pod-test-role in cluster jam-eks-cluster
```

## ✅ Resultado

O Bedrock Agent agora pode automatizar a criação de EKS Access Entries através de comandos em linguagem natural, eliminando a necessidade de configuração manual via AWS CLI ou Console.