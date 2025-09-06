# Task 3 – Trace with AWS Lambda Powertools

## 🎯 Objetivo

Instrumentar a função Lambda `GetUser` com AWS Lambda Powertools para criar traces detalhados no X-Ray, incluindo subsegmentos para operações DynamoDB e código customizado.

## 📋 Pré-requisitos

- ✅ **Task 2 concluída**: Active tracing (X-Ray) ligado em Configuration → Monitoring and operations tools → Lambda service traces = ON
- ✅ **Função GetUser** acessível no console
- ✅ **Permissões** para modificar código e configurações da Lambda

## 🚀 Passo a Passo (Mínimo Esforço)

### 1. Adicionar o Layer do AWS Lambda Powertools

Na função **GetUser**:

1. Aba **Code** → botão **Layers** → **Add a layer**
2. **AWS layers** (ou **Specify an ARN**, se preferir)
3. Selecione o layer:
   - **Python**: `AWSLambdaPowertoolsPythonV2` (compatível com Python 3.11/3.12)
   - **Node.js/TypeScript**: `AWSLambdaPowertoolsTypeScript`
4. **Salve**

> **Dica:** Se usar "Specify an ARN", escolha a versão/ARN correspondente à sua região.

### 2. Definir o Service Name Exigido

Em **Configuration** → **Environment variables** adicione:

```
POWERTOOLS_SERVICE_NAME=jam
```

**Variáveis opcionais úteis:**
```
POWERTOOLS_LOG_LEVEL=INFO
POWERTOOLS_TRACER_CAPTURE_RESPONSE=false
```

### 3. Instrumentar o Handler e o DynamoDB

#### Para Lambda Python (boto3)

```python
# handler.py (exemplo)
import os
import boto3
from aws_lambda_powertools import Tracer
from aws_xray_sdk.core import patch_all

# Cria subsegments automáticos para boto3/requests/etc
patch_all()

# service name virá de POWERTOOLS_SERVICE_NAME=jam
tracer = Tracer()

dynamodb = boto3.client("dynamodb")
TABLE = os.environ.get("USERS_TABLE", "Users")

@tracer.capture_lambda_handler
def handler(event, context):
    user_id = (event or {}).get("userId", "1")

    # Subsegment explícito do seu código (opcional, mas bom para evidência)
    with tracer.provider.in_subsegment("GetUserById"):
        resp = dynamodb.get_item(
            TableName=TABLE,
            Key={"id": {"S": user_id}},
            ConsistentRead=True,
        )

    item = resp.get("Item")
    return {"statusCode": 200, "body": item}
```

**O que isso faz:**
- ✅ `@tracer.capture_lambda_handler` cria o segmento do Handler no X-Ray
- ✅ `patch_all()` ativa auto-instrumentation do boto3 → verá `AWS::DynamoDB::GetItem` como subsegmento
- ✅ `in_subsegment("GetUserById")` evidencia a atividade do seu código (boa para a checagem da task)

#### Para Lambda Node.js (AWS SDK v3)

```javascript
// index.js (exemplo)
const { Tracer } = require('@aws-lambda-powertools/tracer');
const { DynamoDBClient, GetItemCommand } = require('@aws-sdk/client-dynamodb');
const { captureAWSv3Client } = require('aws-xray-sdk-core');

const tracer = new Tracer(); // serviceName vem de POWERTOOLS_SERVICE_NAME=jam

// Instrumenta o client do SDK v3 para X-Ray
const ddb = captureAWSv3Client(new DynamoDBClient({}));
const TABLE = process.env.USERS_TABLE || 'Users';

exports.handler = tracer.captureLambdaHandler(async (event, context) => {
  const userId = (event && event.userId) || '1';

  // Subsegment explícito do seu código
  const sub = tracer.getSegment().addNewSubsegment('GetUserById');
  try {
    const res = await ddb.send(new GetItemCommand({
      TableName: TABLE,
      Key: { id: { S: userId } },
      ConsistentRead: true,
    }));
    sub.close(); // fecha subsegment
    return { statusCode: 200, body: res.Item };
  } catch (err) {
    sub.addError(err);
    sub.close();
    throw err;
  }
});
```

**O que isso faz:**
- ✅ `tracer.captureLambdaHandler(...)` cria o segmento do Handler
- ✅ `captureAWSv3Client(...)` habilita subsegmentos `AWS::DynamoDB::GetItem` automaticamente
- ✅ Subsegmento manual `GetUserById` mostra claramente a atividade do seu código

### 4. Salvar/Deploy e Testar

1. Clique **Deploy** (se necessário)
2. Use o mesmo evento de teste da Task 2 (ex.: `{}`) → **Test**

### 5. Capturar o X-Ray Trace ID para Validação

1. No **Execution results**, copie o **Trace ID** (formato: `1-xxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx`)
2. **Alternativo:** Clique no link **View X-Ray traces** e copie de lá

## ✅ Checklist de Validação

**O que o avaliador vai ver no X-Ray:**

- ✅ **Service name = jam** (vem do `POWERTOOLS_SERVICE_NAME`)
- ✅ **Trace inclui Lambda Handler** (segmento criado pelo Powertools)
- ✅ **Trace inclui DynamoDB API call** (subsegmento `AWS::DynamoDB::GetItem`)
- ✅ **Subsegmento do seu código** (ex.: `GetUserById`) - opcional, mas recomendado

## 🎯 Resultado Esperado

- ✅ AWS Lambda Powertools layer adicionado
- ✅ Service name configurado como "jam"
- ✅ Código instrumentado com traces detalhados
- ✅ Trace ID capturado com subsegmentos visíveis
- ✅ Task 3 validada com o Trace ID correto

## 🔍 Troubleshooting

| Problema | Solução |
|----------|---------|
| **Layer não encontrado** | Verificar região e versão do runtime |
| **Erro de import** | Verificar se o layer foi adicionado corretamente |
| **Service name não aparece** | Verificar variável de ambiente `POWERTOOLS_SERVICE_NAME` |
| **Subsegmentos não aparecem** | Verificar se `patch_all()` ou `captureAWSv3Client()` foi chamado |
| **Trace ID não muda** | Aguardar alguns segundos e executar novo teste |

## 💡 Dica Extra

Se quiser, me diga qual runtime (Python/Node) você está usando e eu ajusto o snippet exatamente ao seu código atual (nomes de arquivo, handler, tabela, etc.).