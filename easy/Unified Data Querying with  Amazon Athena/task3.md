# Task 3 – DynamoDB Federated Query with Amazon Athena

## 🎯 Objetivo
Utilizar **Amazon Athena Federated Query** para consultar dados do **DynamoDB** e descobrir o nome do campeão (`ChampName`) cujo `ChampId` é **40**.

## 📋 Contexto do Ambiente

### Configuração Prévia:
- **Data Source:** `dynamo_dc` (conector DynamoDB)
- **Database/Schema:** `default`
- **Tabela DynamoDB:** `labstack-prewarm-006648d6-ba12-45fe-ad1c-3d7720bee0ee-cjxauxtxnequokhmgg6w4c-1-dynamodbtable-htuvkwbqig97`
- **Query Result Location:** Configurado (bucket S3)

### Estrutura dos Dados:
- **ChampId:** Identificador único do campeão
- **ChampName:** Nome do campeão (resposta desejada)

## 🔧 Implementação da Solução

### 1️⃣ Configuração do Ambiente Athena
**Localização:** AWS Console → Amazon Athena → Query Editor

**Passos:**
1. **Acesse o Athena Console**
   - Navegue para Amazon Athena
   - Clique em "Query editor"

2. **Selecione Data Source**
   - No painel esquerdo "Data"
   - Dropdown "Data source": selecione `dynamo_dc`
   - (Padrão estava como `AwsDataCatalog`)

3. **Selecione Database**
   - Dropdown "Database": selecione `default`

### 2️⃣ Identificação da Tabela
**Localização:** Painel "Tables and views"

**Ação:**
- Se a tabela não aparecer automaticamente:
  - Clique no ícone de **refresh** (setinhas circulares) ao lado de "Data"
- Confirme a tabela listada:
  ```
  labstack-prewarm-006648d6-ba12-45fe-ad1c-3d7720bee0ee-cjxauxtxnequokhmgg6w4c-1-dynamodbtable-htuvkwbqig97
  ```

### 3️⃣ Execução da Query Principal
**Objetivo:** Buscar ChampName onde ChampId = 40

#### Query SQL (Tipo Integer):
```sql
SELECT champname
FROM default."labstack-prewarm-006648d6-ba12-45fe-ad1c-3d7720bee0ee-cjxauxtxnequokhmgg6w4c-1-dynamodbtable-htuvkwbqig97"
WHERE CAST(champid AS INTEGER) = 40;
```

#### Query SQL (Tipo String):
```sql
SELECT champname
FROM default."labstack-prewarm-006648d6-ba12-45fe-ad1c-3d7720bee0ee-cjxauxtxnequokhmgg6w4c-1-dynamodbtable-htuvkwbqig97"
WHERE champid = '40';
```

**⚠️ Importante:** Nome da tabela entre **aspas duplas** devido aos hífens.

### 4️⃣ Validação e Submissão
**Passos:**
1. **Execute a query** no editor central
2. **Aguarde o resultado** (pode levar alguns segundos)
3. **Copie o valor** da coluna `champname`
4. **Cole no campo** "Enter answer here" do lab
5. **Clique em Submit**

## ✅ Critérios de Sucesso

- [ ] **Data source** `dynamo_dc` selecionado
- [ ] **Database** `default` configurado
- [ ] **Tabela identificada** e nomeada corretamente
- [ ] **Query executada** sem erros de sintaxe
- [ ] **Resultado obtido** com nome do campeão
- [ ] **Resposta submetida** no lab

## 📊 Análise da Query

### Explicação Técnica:
- **SELECT champname:** Retorna apenas o nome do campeão
- **FROM default."tabela":** Especifica schema e tabela com aspas
- **WHERE CAST(champid AS INTEGER) = 40:** Converte e filtra por ID
- **WHERE champid = '40':** Alternativa para tipo string

### Interpretação do Resultado:
- **Uma linha retornada** com o nome do campeão
- **ChampName** é a resposta final para o lab
- **Apenas o nome** deve ser submetido (sem formatação)

## 🚨 Troubleshooting

### Problemas Comuns:

#### Erro: "no viable alternative at input 'SHOW CATALOGS'"
- **Causa:** Comando usado no contexto errado (dynamo_dc vs AwsDataCatalog)
- **Solução:** Use `SHOW SCHEMAS;` e `SHOW TABLES IN default;`

#### Erro: "Table not found"
- **Causa:** Nome da tabela incorreto ou não encontrado
- **Solução:** 
  - Clique em refresh no painel Data
  - Use aspas duplas no nome da tabela
  - Verifique se está no data source correto

#### Zero resultados retornados
- **Causa:** Tipo de dados incorreto para ChampId
- **Solução:** Teste ambas as abordagens:
  - `CAST(champid AS INTEGER) = 40` (para integer)
  - `champid = '40'` (para string)

#### Data source não aparece
- **Causa:** Conector DynamoDB não configurado ou região incorreta
- **Solução:** 
  - Settings → Manage data sources
  - Verificar se conector está ativo na mesma região

### Queries Auxiliares para Navegação:
```sql
-- Listar schemas disponíveis
SHOW SCHEMAS;

-- Listar tabelas no schema default
SHOW TABLES IN default;

-- Descrever estrutura da tabela
DESCRIBE default."nome-da-tabela";
```

## 📝 Instruções de Submissão

### Como Submeter a Resposta:
1. **Execute a query** no Amazon Athena
2. **Copie o valor** da coluna `champname`
3. **Cole no campo** "Enter answer here" do lab
4. **Clique em Submit** para finalizar

### ⚠️ Importante:
- **Use apenas o nome** do campeão (sem aspas ou formatação)
- **Não inclua** texto adicional ou explicações
- **Submeta exatamente** o valor retornado pela query

## 🎓 Conceitos Aprendidos

### 🔗 Athena Federated Query:
- **Consulta federada** permite acessar múltiplas fontes de dados
- **DynamoDB connector** integra dados NoSQL com SQL
- **Data sources** diferentes para diferentes tipos de dados
- **Schema mapping** entre DynamoDB e SQL

### 📊 Consultas SQL:
- **CAST()** para conversão de tipos de dados
- **Aspas duplas** para nomes com caracteres especiais
- **WHERE** para filtragem específica
- **SELECT** para retorno de colunas específicas

### 🔧 Troubleshooting:
- **Identificação de tipos** de dados (string vs integer)
- **Navegação entre data sources** diferentes
- **Refresh de metadados** quando tabelas não aparecem
- **Validação de resultados** antes da submissão

## 🏆 Resultado Final

- ✅ **Federated Query** executada com sucesso
- ✅ **Nome do campeão** identificado para ChampId = 40
- ✅ **Resposta submetida** no lab
- ✅ **Task 3 concluída** com sucesso

---

**💡 Reflexão:** Esta task demonstra o poder das consultas federadas do Amazon Athena, permitindo acessar dados NoSQL do DynamoDB usando SQL familiar, expandindo as possibilidades de análise de dados em diferentes formatos e fontes.