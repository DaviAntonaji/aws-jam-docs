# Task 1: CONFIGURE MY BUS (EVENT RULES)

## 📊 Informações da Tarefa
- **Pontos Possíveis:** 60
- **Penalidade por Dica:** 0
- **Pontos Disponíveis:** 60

## 🎯 Objetivo

Configurar regras de eventos no Amazon EventBridge para automatizar o redirecionamento de pedidos usando funções AWS Lambda.

## 📋 Contexto

Você lembrou do requisito de automatizar o redirecionamento manual de pedidos usando funções AWS Lambda. Descobriu que deve usar regras de eventos do Amazon EventBridge para acionar essas funções Lambda.

### ⚠️ Informações Importantes

- **Amazon EventBridge custom event bus** já foi criado com o nome `OrderEventBus`
- **Duas funções AWS Lambda** foram criadas:
  - Uma para pedidos de **Food** (nome contém `FoodOrdersLambdaFunction`)
  - Uma para pedidos de **Beverage** (nome contém `BeverageOrdersLambdaFunction`)

## 🎯 Sua Tarefa

Seu Amazon EventBridge não está configurado com regras de eventos para processar pedidos de Food e Beverage. Você precisa:

1. **Criar regras de eventos** no `OrderEventBus`
2. **Configurar suas respectivas funções AWS Lambda**

> **⚠️ IMPORTANTE:** Crie as regras de eventos no `OrderEventBus`, não no event bus padrão.

## 🔧 Como Começar

1. Navegue até o serviço **Amazon EventBridge** no AWS Management Console
2. Encontre o event bus com o nome `OrderEventBus` (criado sem regras de eventos)
3. Descubra como criar regras de eventos e configurar suas funções Lambda

## 📦 Inventário

- Amazon EventBridge event bus
- Verifique o arquivo de propriedades de saída para valores apropriados

## 🛠️ Serviços a Utilizar

- **Amazon EventBridge**

## ✅ Validação da Tarefa

Clique no botão "Check my progress" - um script automatizado validará se o desafio está completo verificando se suas regras de eventos do Amazon EventBridge foram criadas.

---

## 🧭 Passo a Passo Detalhado

### 1️⃣ Acessar o EventBridge

1. Entre no **AWS Console** → procure **EventBridge**
2. No menu lateral, clique em **Event buses**
3. Você verá um custom event bus chamado `OrderEventBus`

> **⚠️ CRÍTICO:** Não use o default bus! É crucial usar o `OrderEventBus`.

### 2️⃣ Criar Regra para Food Orders

1. Clique em **Rules** no menu lateral
2. Clique em **Create rule**
3. **Nome da regra:** `FoodOrdersRule`
4. **Event bus:** Selecione `OrderEventBus`
5. **Creation method:** Selecione `Custom pattern`
6. **Event pattern:** Clique em `Edit pattern` e cole:

```json
{
  "detail": {
    "OrderType": ["Food"]
  }
}
```

7. Clique em **Next**

### 3️⃣ Vincular a Função Lambda Correta

1. **Select target:** Selecione `Lambda function`
2. **Function:** Procure por uma função que contenha `FoodOrdersLambdaFunction` no nome
3. Selecione essa função
4. Clique em **Next** → **Next** → **Create rule**

### 4️⃣ Criar Regra para Beverage Orders

Repita o mesmo processo com:

- **Nome:** `BeverageOrdersRule`
- **Event bus:** `OrderEventBus`
- **Event pattern:**
```json
{
  "detail": {
    "OrderType": ["Beverage"]
  }
}
```
- **Target:** Função Lambda que contém `BeverageOrdersLambdaFunction`

### 5️⃣ Validar Configuração

Após criar as duas regras:

1. Vá em **EventBridge** → **Rules** → **OrderEventBus**
2. Confirme que existem duas regras ativas:
   - `FoodOrdersRule` → target: `FoodOrdersLambdaFunction`
   - `BeverageOrdersRule` → target: `BeverageOrdersLambdaFunction`
3. Ambas devem estar **Enabled**

### 6️⃣ Testar (Opcional)

Você pode testar manualmente:

1. Vá até **Event buses** → `OrderEventBus` → **Send events**
2. Cole no campo JSON:
```json
{
  "detail": {
    "OrderType": "Food"
  }
}
```
3. Clique em **Send**
4. A Lambda de Food deve ser acionada (confirme nos logs do CloudWatch)

---

## ✅ Checklist para Validação

O script do lab verificará:

- [ ] Se existem duas regras no `OrderEventBus`
- [ ] Se os padrões JSON estão corretos
- [ ] Se cada regra aponta para o Lambda correto
- [ ] Se as regras estão habilitadas

---

## 💡 Dicas Importantes

### 🎯 Event Pattern Correto
- Use exatamente: `{ "detail": { "OrderType": ["Food"] } }`
- Use exatamente: `{ "detail": { "OrderType": ["Beverage"] } }`
- **Creation method** deve ser `Custom pattern`, não `Use schema` ou `Use pattern form`

### 🔧 Configuração de Target
- **Target type:** AWS service
- **Select a target:** Lambda function
- **Function:** Selecione a função correta baseada no nome

### ⚠️ Armadilhas Comuns
- **NÃO use o default event bus** - sempre use `OrderEventBus`
- **NÃO use "Use schema"** - sempre use "Custom pattern"
- **Verifique os nomes das funções Lambda** - eles contêm `FoodOrdersLambdaFunction` e `BeverageOrdersLambdaFunction`

---

## 🚀 Comandos AWS CLI (Alternativa)

Se preferir usar CLI em vez do console:

```bash
# Criar regra para Food Orders
aws events put-rule \
  --name FoodOrdersRule \
  --event-bus-name OrderEventBus \
  --event-pattern '{"detail":{"OrderType":["Food"]}}' \
  --state ENABLED

# Adicionar target Lambda para Food
aws events put-targets \
  --rule FoodOrdersRule \
  --event-bus-name OrderEventBus \
  --targets Id=1,Arn=arn:aws:lambda:REGION:ACCOUNT:function:FoodOrdersLambdaFunction

# Criar regra para Beverage Orders
aws events put-rule \
  --name BeverageOrdersRule \
  --event-bus-name OrderEventBus \
  --event-pattern '{"detail":{"OrderType":["Beverage"]}}' \
  --state ENABLED

# Adicionar target Lambda para Beverage
aws events put-targets \
  --rule BeverageOrdersRule \
  --event-bus-name OrderEventBus \
  --targets Id=1,Arn=arn:aws:lambda:REGION:ACCOUNT:function:BeverageOrdersLambdaFunction
```

> **Nota:** Substitua `REGION` e `ACCOUNT` pelos valores corretos do seu ambiente.

---

## 🎉 Próximos Passos

Após completar esta tarefa, você estará pronto para a **Task 2: ADDRESS MY CONFIGURATIONS**, onde configurará as variáveis de ambiente necessárias nas funções Lambda.