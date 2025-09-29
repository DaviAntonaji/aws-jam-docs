# Jam Challenge - Not Finding My Favourite Car. Help Me

## 🚗 Visão Geral

Você trabalha para uma empresa automotiva XYZ e foi solicitado a gerenciar um site que exibirá diferentes modelos de carros oferecidos pela sua empresa. A aplicação é construída usando arquitetura serverless, com Amazon API Gateway, AWS Lambda e backend como banco de dados Amazon DynamoDB.

Houve um rollout de produção recente que impactou a funcionalidade de busca da sua aplicação, causando problemas para os usuários que não conseguem buscar e encontrar detalhes do seu carro favorito. É muito crítico para sua empresa corrigir este problema o mais rápido possível, pois tem um grande impacto nos negócios.

## 🎯 Objetivo

Como desenvolvedor, você precisa investigar por que alguns carros não estão aparecendo nos resultados da busca, mesmo atendendo aos critérios de busca.

## 📋 Contexto do Problema

### Cenário
- **Empresa:** Automobile Company XYZ
- **Problema:** Funcionalidade de busca quebrada após rollout de produção
- **Impacto:** Usuários não conseguem encontrar carros específicos
- **Urgência:** Alto impacto nos negócios

### Arquitetura
- **Frontend:** Website
- **API:** Amazon API Gateway
- **Backend:** AWS Lambda
- **Database:** Amazon DynamoDB

## 🔍 Problema Específico

### Nova Modelo Adicionado
- **Modelo:** Audi "e-tron GT"
- **Estilo de Carroceria:** "Sedan"
- **Total de modelos Audi:** 36 carros

### Comportamento Esperado vs Atual
- **Esperado:** Buscar "Audi" + "Sedan" deve retornar todos os modelos incluindo "e-tron GT"
- **Atual:** O modelo "e-tron GT" não aparece nos resultados de busca

## 🛠️ Recursos Disponíveis

### Inventário
- **API Gateway:** Endpoint configurado
- **Lambda Function:** `jamDynamoDbLimitFunction` (consulta DynamoDB para carros Audi "Sedan")
- **DynamoDB Table:** `cars`
  - **Partition Key:** `make` ("Audi" etc.)
  - **Sort Key:** `model` ("e-tron GT" etc.)
  - **Attributes:** `body_styles` ("Sedan" etc.)

### Como Acessar
1. Navegue para o menu "Output Properties" do jam challenge
2. Obtenha a URL do website da propriedade `ReadFromDynamoDbCarsApiUrl`
3. Acesse o website para ver o problema

## 🔧 Análise Técnica

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
  // ... resto do código
};
```

### Problema Identificado
O parâmetro `Limit` está limitando o número de resultados retornados pela query. Com 36 modelos Audi e um limite baixo (provavelmente 14), o novo modelo "e-tron GT" não está sendo incluído nos resultados.

## 💡 Soluções

### Solução 1: Ajustar Environment Variable (Recomendada)
1. **Acesse AWS Lambda Console**
2. **Vá para:** Lambda Function → `jamDynamoDbLimitFunction`
3. **Navegue para:** Configuration → Environment variables
4. **Modifique:** `DynamoDbQueryLimit` de `14` para `1000`
5. **Salve** as alterações

### Solução 2: Remover Limit (Ideal, mas pode não ser possível)
Se tiver permissões para modificar o código:
```javascript
const paramsGetFilter = {
  TableName: 'cars',
  KeyConditionExpression: 'make = :make',
  FilterExpression: 'body_styles = :body_styles',
  ExpressionAttributeValues: {
    ':make': 'Audi',
    ':body_styles': 'Sedan',
  },
  // Limit: dynamoDbQueryLimit, // Remover esta linha
};
```

## 📊 Limitações do DynamoDB

### Query Limit
- **Limite máximo:** 1000 itens por query
- **Limite padrão:** Sem limite (retorna todos os itens)
- **Paginação:** Use `ExclusiveStartKey` para resultados maiores

### Considerações de Performance
- Limites ajudam a controlar latência
- Para datasets grandes, implemente paginação
- Monitor custos de leitura (RCU)

## ✅ Validação

### Critério de Sucesso
- ✅ Audi "e-tron GT" aparece nos resultados da busca
- ✅ Todos os 36 modelos Audi "Sedan" são retornados
- ✅ Website funciona corretamente

### Como Testar
1. Acesse a URL do website
2. Execute busca por "Audi" + "Sedan"
3. Verifique se "e-tron GT" está na lista
4. Confirme que todos os modelos aparecem

## 🔍 Conceitos Aprendidos

### DynamoDB Query Operations
- **KeyConditionExpression:** Para partition key e sort key
- **FilterExpression:** Para filtrar após a query
- **Limit:** Controla número máximo de itens retornados
- **ExpressionAttributeValues:** Parâmetros seguros para query

### Troubleshooting Serverless
- Verificar environment variables
- Analisar logs do Lambda
- Validar configurações do DynamoDB
- Testar queries diretamente

### Boas Práticas
- **Sempre teste** após mudanças de configuração
- **Monitore performance** ao ajustar limites
- **Documente** environment variables importantes
- **Implemente paginação** para datasets grandes

## 🎓 Lições Importantes

1. **Environment Variables:** Podem impactar comportamento da aplicação
2. **Query Limits:** Podem excluir dados válidos dos resultados
3. **Troubleshooting:** Comece verificando configurações antes de código
4. **DynamoDB:** Entenda limitações de query para evitar problemas

## 🚀 Próximos Passos

Após resolver este problema:
- Implemente monitoramento para detectar problemas similares
- Considere implementar paginação para melhor UX
- Documente todas as environment variables críticas
- Configure alertas para mudanças não autorizadas

---

**🎯 Objetivo:** Garantir que todos os modelos de carros sejam encontrados na busca, mantendo a funcionalidade completa do site da empresa automotiva.
