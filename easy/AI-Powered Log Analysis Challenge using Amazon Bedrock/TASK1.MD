# Task 1: Enabling Amazon Nova Model Access in Bedrock

## 🎯 Objetivo

Resolver o erro `AccessDeniedException` ao tentar usar o modelo Amazon Nova Lite no Bedrock, habilitando o acesso ao modelo para que a função Lambda `bedrock-api-function` possa processar logs automaticamente.

## 📊 Cenário

### Situação Inicial
- ✅ **Lambda function** `bedrock-api-function` criada e configurada
- ✅ **IAM roles** básicos configurados
- ❌ **Modelo Amazon Nova Lite** não acessível
- ❌ **Função falhando** com `AccessDeniedException`

### Problema Identificado
```
AccessDeniedException: Could not access the model amazon.nova-lite-v1:0.
Make sure this model is available in your region and you have access to it.
```

## 🔍 Diagnóstico

### Análise dos Logs
1. **Acessar CloudWatch Logs** da função `bedrock-api-function`
2. **Identificar erro** de acesso ao modelo
3. **Confirmar** que o modelo não está habilitado

### Error Pattern Típico
```json
{
  "errorMessage": "AccessDeniedException",
  "errorType": "ClientError", 
  "stackTrace": [
    "botocore.exceptions.ClientError: An error occurred (AccessDeniedException) when calling the InvokeModel operation: Could not access the model amazon.nova-lite-v1:0. Make sure this model is available in your region and you have access to it."
  ]
}
```

## 🔧 Resolução

### Passo a Passo Detalhado

#### 1. Acessar Amazon Bedrock Console
1. **Abrir AWS Console**
2. **Navegar para Amazon Bedrock**
3. **Verificar região** (deve estar na mesma região da Lambda)

#### 2. Configurar Model Access
1. **No menu lateral**, clicar em **"Model access"**
2. **Localizar "Amazon Nova Lite"** na lista de modelos
3. **Verificar status** atual (provavelmente "Not available")
4. **Clicar em "Manage model access"**

#### 3. Habilitar Amazon Nova Lite
1. **Na página de model access**, localizar **"Amazon Nova Lite"**
2. **Marcar a checkbox** ao lado do modelo
3. **Revisar termos** de uso se solicitado
4. **Clicar em "Request model access"**
5. **Aguardar aprovação** (geralmente instantânea em labs)

#### 4. Verificar Ativação
1. **Aguardar status** mudar para "Available" ou "Access granted"
2. **Confirmar modelo** está listado como acessível
3. **Anotar model ID**: `amazon.nova-lite-v1:0`

### Configuração Visual
```
Amazon Bedrock Console
    ↓
Model Access
    ↓
Amazon Nova Lite: ❌ Not available
    ↓ (Request Access)
Amazon Nova Lite: ✅ Available
```

## ✅ Validação

### Teste da Função Lambda
1. **Acessar Lambda Console** → `bedrock-api-function`
2. **Clicar em "Test"** para executar função
3. **Verificar saída** sem erros de acesso
4. **Confirmar** processamento de logs

### Comandos de Teste
```bash
# Testar função Lambda
aws lambda invoke \
  --function-name bedrock-api-function \
  --payload '{}' \
  response.json

# Verificar resposta
cat response.json

# Verificar logs
aws logs describe-log-streams \
  --log-group-name /aws/lambda/bedrock-api-function \
  --order-by LastEventTime \
  --descending
```

### Saída Esperada
```json
{
  "statusCode": 200,
  "body": "Log analysis completed successfully",
  "logs_processed": 0,
  "analysis_summary": "No logs found in specified time range"
}
```

## 🔍 Detalhes Técnicos

### Amazon Nova Models Disponíveis
| Modelo | Model ID | Capacidades |
|--------|----------|-------------|
| **Nova Lite** | `amazon.nova-lite-v1:0` | Text generation, analysis |
| **Nova Micro** | `amazon.nova-micro-v1:0` | Lightweight text tasks |
| **Nova Pro** | `amazon.nova-pro-v1:0` | Advanced text generation |

### Model Access Status
```bash
# Verificar modelos disponíveis via CLI
aws bedrock list-foundation-models \
  --region us-east-1 \
  --query 'modelSummaries[?contains(modelId, `nova`)]'

# Verificar acesso específico ao Nova Lite
aws bedrock invoke-model \
  --region us-east-1 \
  --model-id amazon.nova-lite-v1:0 \
  --body '{"inputText":"Test","textGenerationConfig":{"maxTokenCount":50}}' \
  --content-type application/json \
  response.json
```

### IAM Permissions Necessárias
A função Lambda precisa das seguintes permissões:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream"
      ],
      "Resource": "arn:aws:bedrock:*::foundation-model/amazon.nova-lite-v1:0"
    }
  ]
}
```

## 🚨 Troubleshooting

### Problemas Comuns

#### Modelo ainda não disponível após request
- **Aguardar propagação** (pode levar 2-5 minutos)
- **Verificar região** (modelo deve estar na mesma região da Lambda)
- **Tentar refresh** da página do console
- **Verificar quotas** da conta AWS

#### AccessDeniedException persiste
- **Confirmar IAM permissions** da função Lambda
- **Verificar resource-based policies**
- **Checar se modelo está realmente "Available"**
- **Tentar outro modelo** (Nova Micro) para teste

#### Throttling errors
- **Aguardar entre tentativas** (rate limiting em labs)
- **Verificar quotas** de requests per minute
- **Implementar retry logic** com backoff

### Comandos de Diagnóstico
```bash
# Verificar status dos modelos
aws bedrock list-foundation-models \
  --query 'modelSummaries[?contains(modelId, `amazon.nova`)].[modelId,modelLifecycle.status]' \
  --output table

# Testar acesso direto ao modelo
aws bedrock invoke-model \
  --model-id amazon.nova-lite-v1:0 \
  --body '{"inputText":"Hello","textGenerationConfig":{"maxTokenCount":10}}' \
  --content-type application/json \
  test-response.json

# Verificar IAM permissions da função
aws lambda get-function --function-name bedrock-api-function \
  --query 'Configuration.Role'
```

## 💡 Considerações Importantes

### Custos
- **Amazon Nova Lite** tem custo por token processado
- **Ambiente de lab** pode ter quotas limitadas
- **Monitorar uso** para evitar custos inesperados

### Quotas e Limites
```
Requests per Minute (RPM): 100-1000 (varia por região)
Tokens per Minute (TPM): 10,000-100,000
Tokens per Day (TPD): 1,000,000
```

### Regiões Disponíveis
- **us-east-1** (N. Virginia) - Disponibilidade completa
- **us-west-2** (Oregon) - Disponibilidade completa  
- **eu-west-1** (Ireland) - Limitada
- **Verificar documentação** para updates de disponibilidade

## 📊 Validação Final

### Checklist de Verificação
- [ ] Modelo Amazon Nova Lite está "Available" no Bedrock Console
- [ ] Função Lambda executa sem `AccessDeniedException`
- [ ] CloudWatch Logs mostram execução bem-sucedida
- [ ] Response da função retorna status 200
- [ ] Task 1 marcada como "Completed" no Jam

### Métricas de Sucesso
- **Error Rate:** 0% para AccessDeniedException
- **Success Rate:** 100% para invocações de modelo
- **Latency:** < 5 segundos para análise básica
- **Cost:** Dentro dos limites de quota do lab

## 🎓 Lições Aprendidas

### Amazon Bedrock
- **Model Access** é um pré-requisito obrigatório
- **Regional availability** varia por modelo
- **Quotas** são importantes em ambiente de produção
- **Cost management** deve ser considerado desde o início

### Troubleshooting
- **Error messages** são geralmente precisos e informativos
- **Console UI** é a forma mais simples de configurar acesso
- **CLI commands** são úteis para automação e verificação
- **Propagation time** deve ser considerado

### Integração Lambda + Bedrock
- **IAM permissions** devem ser específicas por modelo
- **Error handling** é crucial para resiliência
- **Retry logic** ajuda com throttling temporário
- **Monitoring** é essencial para produção

---

**🎉 Task 1 Concluída!**

> **💭 Reflexão:** A habilitação de acesso a modelos de IA no Bedrock é um passo fundamental que demonstra como a AWS gerencia o acesso a recursos de IA de forma granular. Este controle permite tanto segurança quanto gestão de custos, essenciais em ambientes de produção.
