# Task 2: ADDRESS MY CONFIGURATIONS

## 📊 Informações da Tarefa
- **Pontos Possíveis:** 45
- **Penalidade por Dica:** 0
- **Pontos Disponíveis:** 45

## 🎯 Objetivo

Configurar as variáveis de ambiente necessárias nas funções AWS Lambda para integração com Amazon EventBridge e DynamoDB.

## 📋 Contexto

A configuração das suas funções AWS Lambda precisa ser atualizada conforme os novos serviços Amazon EventBridge e AWS Lambda introduzidos.

## 🎯 Sua Tarefa

Encontre as funções AWS Lambda criadas para este desafio e configure suas **Environment Variables** necessárias, analisando o código de cada função Lambda.

## 🔧 Como Começar

1. Navegue até o serviço **AWS Lambda** no AWS Management Console
2. As funções Lambda criadas contêm os nomes:
   - `OrdersLambdaFunction`
   - `FoodOrdersLambdaFunction`
   - `BeverageOrdersLambdaFunction`

## 📦 Inventário

- AWS Lambda functions
- Verifique o arquivo de propriedades de saída para valores apropriados

## 🛠️ Serviços a Utilizar

- **AWS Lambda**

## ✅ Validação da Tarefa

Clique no botão "Check my progress" - um script automatizado validará se o desafio está completo verificando se suas funções AWS Lambda estão configuradas corretamente.

---

## 🧭 Passo a Passo Detalhado

### 1️⃣ Abrir Cada Função Lambda

1. **AWS Console** → **Lambda**
2. Abra cada uma das funções:
   - `OrdersLambdaFunction`
   - `FoodOrdersLambdaFunction`
   - `BeverageOrdersLambdaFunction`

### 2️⃣ Descobrir os Nomes das Variáveis

Para cada função Lambda:

1. Vá na aba **Code**
2. Abra o arquivo principal (geralmente `index.js`, `app.js`, `lambda_function.py`)
3. Procure por referências a variáveis de ambiente:

**Node.js:**
```javascript
process.env.VARIABLE_NAME
```

**Python:**
```python
os.environ["VARIABLE_NAME"]
# ou
os.getenv("VARIABLE_NAME")
```

4. **Anote exatamente** os nomes esperados (case-sensitive) e para que servem

### 3️⃣ Obter os Valores Corretos

1. No painel do JAM/lab, abra o **output properties file**
2. Mapeie cada nome → valor

**Exemplos comuns neste desafio:**
- `EVENT_BUS_NAME` → `OrderEventBus` (comum no OrdersLambdaFunction)
- `EVENT_SOURCE` → `restaurant.orders`
- `DETAIL_TYPE_FOOD` → `Food`
- `DETAIL_TYPE_BEVERAGE` → `Beverage`
- `TABLE_NAME` → Nome da tabela DynamoDB

> **⚠️ IMPORTANTE:** Não adivinhe nomes. Use exatamente os nomes que aparecem no código de cada função e os valores do output properties file. O validador é rígido.

### 4️⃣ Configurar as Variáveis na Lambda

Para cada função Lambda:

1. Aba **Configuration** → **Environment variables** → **Edit**
2. **Add environment variable**
3. Adicione todos os pares **Name / Value** requeridos por aquela função
4. **Save**

Repita para as três funções.

### 5️⃣ Teste Rápido (Opcional)

**Se o OrdersLambdaFunction publica no EventBridge:**
1. Use **Test** na própria Lambda com um payload de exemplo
2. Ou rode a Lambda sem payload (se o código não exigir)

**Para testar o fluxo completo:**
1. **EventBridge** → **Event buses** → `OrderEventBus` → **Send events**
2. Use:
```json
{
  "detail": {
    "OrderType": "Food"
  }
}
```
3. Depois teste com `"Beverage"`
4. Verifique os disparos das Lambdas alvo nos **CloudWatch Logs**

### 6️⃣ Executar Validação

Clique em **Check my progress** no lab.

---

## 📋 Configurações Específicas por Função

### 🔧 OrdersLambdaFunction
**Variável necessária:**
- **Name:** `EventBusArn`
- **Value:** `arn:aws:events:us-east-1:948478956855:event-bus/OrderEventBus`

> **Função:** Esta Lambda publica eventos no EventBridge, então precisa do ARN do event bus.

### 🍔 FoodOrdersLambdaFunction
**Variável necessária:**
- **Name:** `FoodOrdersTableName`
- **Value:** `LabStack-prewarm-b8f37d69-4baf-44ee-8399-243b15043a84-sdVDHfMNzMg2QhoZidNfKD-2-FoodOrders-S3JQVXHFHOXD`

> **Função:** Esta Lambda salva pedidos de comida na tabela DynamoDB específica.

### 🥤 BeverageOrdersLambdaFunction
**Variável necessária:**
- **Name:** `BeverageOrdersTableName`
- **Value:** `LabStack-prewarm-b8f37d69-4baf-44ee-8399-243b15043a84-sdVDHfMNzMg2QhoZidNfKD-2-BeverageOrders-18159W9QHFNZW`

> **Função:** Esta Lambda salva pedidos de bebida na tabela DynamoDB específica.

---

## ✅ Checklist de Validação

- [ ] **OrdersLambdaFunction** tem `EventBusArn` configurado
- [ ] **FoodOrdersLambdaFunction** tem `FoodOrdersTableName` configurado
- [ ] **BeverageOrdersLambdaFunction** tem `BeverageOrdersTableName` configurado
- [ ] Todos os valores são exatos (case-sensitive)
- [ ] Todas as variáveis foram salvas corretamente

---

## 💡 Dicas Práticas

### 🔍 Identificação de Variáveis
- **OrdersLambdaFunction** costuma precisar do nome do Event Bus para fazer `PutEvents`
- **FoodOrdersLambdaFunction** e **BeverageOrdersLambdaFunction** geralmente não precisam do bus, mas têm variáveis como `TABLE_NAME`, etc.
- **Confirme no código** - não assuma nada

### ⚠️ Troubleshooting
- Se o código usar `process.env/os.environ` e você não definiu a variável, a execução costuma falhar com erro de variável ausente
- **Bom para detectar** o que falta
- **Não altere** nomes, capitalização ou chaves
- **Siga 1:1** o que o código pede

### 🎯 Valores do Output Properties

**Valores específicos para este lab:**
```
AuthorizerLambdaFunction: OrdersAuthorizer
AuthorizerLambdaFunctionArn: arn:aws:lambda:us-east-1:948478956855:function:OrdersAuthorizer
BeverageOrdersLambdaFunction: LabStack-prewarm-b8f37d69-BeverageOrdersLambdaFunc-GQ73t5zdpvDy
BeverageOrdersLambdaFunctionArn: arn:aws:lambda:us-east-1:948478956855:function:LabStack-prewarm-b8f37d69-BeverageOrdersLambdaFunc-GQ73t5zdpvDy
BeverageOrdersTableName: LabStack-prewarm-b8f37d69-4baf-44ee-8399-243b15043a84-sdVDHfMNzMg2QhoZidNfKD-2-BeverageOrders-18159W9QHFNZW
EventBusArn: arn:aws:events:us-east-1:948478956855:event-bus/OrderEventBus
FoodOrdersLambdaFunction: LabStack-prewarm-b8f37d69-FoodOrdersLambdaFunction-ogrShYWyWhn0
FoodOrdersLambdaFunctionArn: arn:aws:lambda:us-east-1:948478956855:function:LabStack-prewarm-b8f37d69-FoodOrdersLambdaFunction-ogrShYWyWhn0
FoodOrdersTableName: LabStack-prewarm-b8f37d69-4baf-44ee-8399-243b15043a84-sdVDHfMNzMg2QhoZidNfKD-2-FoodOrders-S3JQVXHFHOXD
```

---

## 🚀 Comandos AWS CLI (Alternativa)

Se preferir usar CLI em vez do console:

```bash
# Configurar OrdersLambdaFunction
aws lambda update-function-configuration \
  --function-name OrdersLambdaFunction \
  --environment Variables='{EventBusArn=arn:aws:events:us-east-1:948478956855:event-bus/OrderEventBus}'

# Configurar FoodOrdersLambdaFunction
aws lambda update-function-configuration \
  --function-name FoodOrdersLambdaFunction \
  --environment Variables='{FoodOrdersTableName=LabStack-prewarm-b8f37d69-4baf-44ee-8399-243b15043a84-sdVDHfMNzMg2QhoZidNfKD-2-FoodOrders-S3JQVXHFHOXD}'

# Configurar BeverageOrdersLambdaFunction
aws lambda update-function-configuration \
  --function-name BeverageOrdersLambdaFunction \
  --environment Variables='{BeverageOrdersTableName=LabStack-prewarm-b8f37d69-4baf-44ee-8399-243b15043a84-sdVDHfMNzMg2QhoZidNfKD-2-BeverageOrders-18159W9QHFNZW}'
```

---

## 🎉 Próximos Passos

Após completar esta tarefa, você terá configurado todas as variáveis de ambiente necessárias para o funcionamento completo do sistema de processamento de pedidos.

**Status do desafio:**
- ✅ **Task 1:** Event Rules configuradas
- ✅ **Task 2:** Environment Variables configuradas
- ⚠️ **Task 3:** Em desenvolvimento futuro