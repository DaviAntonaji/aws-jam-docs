# Jam Challenge - Task 1: DynamoDB Limit Condition

## 🎯 Objetivo

**Task 1:** Uso da condição "Limit" do Amazon DynamoDB  
**Pontos Possíveis:** 80  
**Penalidade de Pista:** 0  
**Pontos Disponíveis:** 80

## 📋 Contexto

### Problema
Sua empresa lançou recentemente um novo modelo Audi "e-tron GT" com estilo de carroceria "Sedan". Existem 36 modelos de carros Audi lançados pela sua empresa, e os detalhes dos carros (marca, modelo e estilo de carroceria) são armazenados na tabela Amazon DynamoDB `cars`.

Quando os usuários fazem busca no site da empresa, o endpoint API Gateway invoca a função AWS Lambda, que consulta os dados da tabela DynamoDB `cars` com os critérios de busca especificados para exibir os resultados.

**Problema:** Devido ao rollout de produção recente, quando os usuários buscam carros "Audi" com estilo de carroceria "Sedan", não conseguem encontrar o modelo Audi "e-tron GT" recentemente lançado nos resultados da busca.

## 🔍 Sua Tarefa

Determine o motivo pelo qual o modelo Audi "e-tron GT" não está aparecendo nos resultados da busca e corrija o problema.

## 🚀 Primeiros Passos

1. **Navegue para:** Output Properties menu do jam challenge
2. **Obtenha:** URL do website da propriedade `ReadFromDynamoDbCarsApiUrl`
3. **Acesse:** O website para confirmar que Audi "e-tron GT" não aparece na lista

## 🛠️ Inventário de Recursos

### Serviços Configurados
- **API Gateway:** Endpoint configurado
- **Lambda Function:** `jamDynamoDbLimitFunction` (consulta DynamoDB para carros Audi "Sedan")
- **DynamoDB Table:** `cars`
  - **Partition Key:** `make` ("Audi" etc.)
  - **Sort Key:** `model` ("e-tron GT" etc.)
  - **Attributes:** `body_styles` ("Sedan" etc.)

## 🔧 Análise e Solução

### Código Lambda Original (Problemático)
```javascript
exports.handler = async (event) => {
  const AWS = require('aws-sdk');
  const dynamoDbQueryLimit = process.env.DynamoDbQueryLimit;
  const dynamoGetFilter = new AWS.DynamoDB.DocumentClient();
  
  const paramsGetFilter = {
    TableName: 'cars',
    KeyConditionExpression: 'make = :make',
    FilterExpression: 'body_styles = :body_styles',
    ExpressionAttributeValues: {
      ':make': 'Audi',
      ':body_styles': 'Sedan',
    },
    Limit: dynamoDbQueryLimit, // ⚠️ PROBLEMA AQUI
  };
  
  const dataFilter = await dynamoGetFilter.query(paramsGetFilter).promise();
  
  let result = '';
  result = result + 'The following are the list of cars based on search criteria: ';
  
  for (let i = 0; i < dataFilter.Count; i++) {
    result = result + (i+1) + ') Make - ' + dataFilter.Items[i]["make"] + 
             ', Model - ' + dataFilter.Items[i]["model"] + 
             ', Body Style - ' + dataFilter.Items[i]["body_styles"] + ' ';
  }
  
  const response = { statusCode: 200, body: result};
  return response;
};
```

### Problema Identificado
O parâmetro `Limit` está limitando o número de resultados retornados pela query DynamoDB. Com 36 modelos Audi e um limite baixo (provavelmente 14), o novo modelo "e-tron GT" não está sendo incluído nos resultados.

## ✅ Solução Implementada

### Tentativa 1: Modificar Código (Sem Sucesso)
- **Ação:** Tentativa de remover a linha `Limit: dynamoDbQueryLimit`
- **Resultado:** Sem permissão para modificar o código Lambda

### Tentativa 2: Ajustar Environment Variable (Sucesso)
- **Ação:** Modificar `DynamoDbQueryLimit` de `14` para `1000`
- **Local:** Lambda → Configuration → Environment variables
- **Resultado:** ✅ Problema resolvido

### Limitações Descobertas
- **Limite máximo DynamoDB:** 1000 itens por query
- **Valor inicial:** 14 (muito baixo para 36 modelos)
- **Valor final:** 1000 (acomoda todos os modelos)

## 🎯 Validação

### Critério de Sucesso
- ✅ Audi "e-tron GT" aparece nos resultados da busca
- ✅ Todos os modelos Audi "Sedan" são retornados
- ✅ Website funciona corretamente

## 📚 Conceitos Aprendidos

### DynamoDB Query Limits
- **Propósito:** Controlar latência e custos
- **Comportamento:** Retorna apenas N primeiros itens
- **Impacto:** Pode excluir dados válidos se limite for baixo

### Environment Variables
- **Uso:** Configuração dinâmica sem alterar código
- **Vantagem:** Permite ajustes sem deploy
- **Limitação:** Respeita limites do serviço

### Troubleshooting Serverless
1. **Verificar configurações** antes de código
2. **Analisar environment variables**
3. **Entender limitações dos serviços**
4. **Testar incrementalmente**

## 🎓 Lições Importantes

1. **Environment Variables** podem resolver problemas sem alterar código
2. **Query Limits** no DynamoDB podem excluir dados válidos
3. **Troubleshooting** deve começar pelas configurações
4. **Limitações de serviços** devem ser consideradas no design

## 🔍 Passo a Passo da Solução

1. **Identificar o problema:** Audi "e-tron GT" não aparece na busca
2. **Analisar o código:** Verificar função Lambda `jamDynamoDbLimitFunction`
3. **Localizar a causa:** Parâmetro `Limit` muito baixo
4. **Tentar solução 1:** Modificar código (sem permissão)
5. **Implementar solução 2:** Ajustar environment variable
6. **Validar resultado:** Confirmar que todos os modelos aparecem

---

**🎯 Resultado:** Audi "e-tron GT" agora aparece corretamente nos resultados da busca, resolvendo o problema de negócios crítico.