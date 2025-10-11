# Task 2: Ingest Streaming Data into Amazon Redshift 📥

**Pontos Possíveis:** 45  
**Penalidade de Dica:** 0  
**Pontos Disponíveis:** 45  
**Check my progress:** Disponível

---

## 📖 Background

Nesta tarefa, você irá criar SQLs simples para **ingerir dados de streaming** do Kinesis Data Streams para o Redshift. Em seguida, você irá **unnest** (desmontar) os dados de streaming aplicando um schema dinamicamente.

Um cluster Redshift (**gamesds**) foi pré-criado para você na conta.

## 🎯 Sua Tarefa

1. Conectar ao cluster Redshift **gamesds**
2. Criar **External Schema** apontando para Kinesis
3. Criar **Materialized View** para coletar dados de streaming
4. Criar **View** para aplicar schema nos dados semi-estruturados
5. Identificar o tipo de dados do campo `payload`

---

## 📚 Passo a Passo Completo

### Step 1: Conectar ao Redshift Query Editor V2

**Navegação:**
1. AWS Console → **Amazon Redshift**
2. Expanda o painel de navegação esquerdo
3. Clique em **Query Editor V2**

**Conectar ao Games Data Store:**
1. Click em **Add connection** (ou selecione conexão existente)
2. **Connection type:** Temporary credentials
3. **Authentication:** Database user name
4. **Cluster:** Selecione **gamesds**
5. **Database:** `dev`
6. **Database user:** `awsuser`
7. Click **Connect**

> ⚠️ **Importante:** Verifique se está conectado ao cluster **gamesds** (não playersds)

---

### Step 2: Criar External Schema para Kinesis

**O que é:**
External Schema permite que o Redshift acesse dados de fontes externas (Kinesis, S3, etc.) sem copiá-los primeiro.

**SQL a executar:**

```sql
CREATE EXTERNAL SCHEMA lol_game_session
FROM KINESIS
IAM_ROLE '<ARN_DO_ROLE>';
```

**Onde encontrar o ARN do Role:**
1. **Opção A:** Output Properties do desafio
   - Propriedade: **RedshiftGameRoleArn**
   - Copie o ARN completo

2. **Opção B:** Console IAM
   - AWS Console → IAM → Roles
   - Procure por: `Redshiftgamesrole`
   - Copie o ARN da role

**Formato do ARN:**
```
arn:aws:iam::ACCOUNT_ID:role/Redshiftgamesrole
```

**SQL completo (exemplo):**
```sql
CREATE EXTERNAL SCHEMA lol_game_session
FROM KINESIS
IAM_ROLE 'arn:aws:iam::123456789012:role/Redshiftgamesrole';
```

**Resultado esperado:**
```
CREATE SCHEMA
```

---

### Step 3: Criar Materialized View para Streaming

**O que é:**
Materialized View que se atualiza automaticamente com novos dados do Kinesis a cada ~10 segundos.

**SQL a executar:**

```sql
CREATE MATERIALIZED VIEW mv_lol_game_session 
SORTKEY(refresh_time) 
DISTKEY(sequence_number) 
AUTO REFRESH YES AS
SELECT
  approximate_arrival_timestamp,
  refresh_time,
  partition_key,
  shard_id,
  sequence_number,
  json_parse(kinesis_data) AS payload
FROM lol_game_session.<STREAM_NAME>;
```

**Substituir `<STREAM_NAME>`:**
- Use o nome do stream da Task 1
- Exemplo: `GameSessionStream-XXXXXXXXXX`

**SQL completo (exemplo):**
```sql
CREATE MATERIALIZED VIEW mv_lol_game_session 
SORTKEY(refresh_time) 
DISTKEY(sequence_number) 
AUTO REFRESH YES AS
SELECT
  approximate_arrival_timestamp,
  refresh_time,
  partition_key,
  shard_id,
  sequence_number,
  json_parse(kinesis_data) AS payload
FROM lol_game_session.GameSessionStream-ABC123;
```

**Resultado esperado:**
```
CREATE MATERIALIZED VIEW
```

**Componentes importantes:**
- **`json_parse(kinesis_data)`:** Converte JSON string para tipo **SUPER**
- **`AS payload`:** Nome do campo resultado
- **`AUTO REFRESH YES`:** Atualização automática

---

### Step 4: Verificar Dados Ingeridos

**Aguarde 10-20 segundos** para a primeira atualização da Materialized View.

#### Query 1: Ver contagem por refresh

```sql
SELECT 
  COUNT(*) AS record_count,
  refresh_time
FROM mv_lol_game_session
GROUP BY refresh_time
ORDER BY refresh_time DESC;
```

**Resultado esperado:**
```
record_count | refresh_time
-------------|-------------------------
150          | 2024-01-15 14:32:15
100          | 2024-01-15 14:32:05
50           | 2024-01-15 14:31:55
```

#### Query 2: Ver dados de amostra

```sql
SELECT * 
FROM mv_lol_game_session 
LIMIT 5;
```

**Resultado esperado:**
```
approximate_arrival_timestamp | refresh_time        | partition_key | shard_id      | sequence_number              | payload
------------------------------|---------------------|---------------|---------------|------------------------------|----------
2024-01-15 14:32:10          | 2024-01-15 14:32:15 | 123456        | shardId-00001 | 495...                       | {...}
```

> 💡 **Nota:** O campo `payload` contém todo o JSON como tipo **SUPER**

---

### Step 5: Aplicar Schema nos Dados RAW

**O que faz:**
Cria uma view que "desmonta" (unnests) o JSON da coluna `payload` em colunas individuais tipadas.

#### Habilitar Case Sensitivity

**Por que necessário:**
Os campos JSON têm nomes em CamelCase (ex: `gameId`, `creationTime`), então precisamos habilitar case-sensitivity.

```sql
SET enable_case_sensitive_identifier TO true;
```

#### Criar View com Schema

**SQL completo:**

```sql
CREATE VIEW public.vw_lol_game_session AS
SELECT 
  (payload."gameId")::varchar(10) AS game_id,
  timestamp 'epoch' + ((payload."creationTime")::numeric/1000) * interval '1 second' AS creation_time,
  (payload."gameDuration")::int AS game_duration,
  REPLACE((payload."seasonId")::varchar(100), '"', '')::int AS season_id,
  REPLACE((payload."winner")::varchar(100), '"', '')::int AS winner,
  REPLACE((payload."firstBlood")::varchar(100), '"', '')::int AS first_blood,
  REPLACE((payload."firstTower")::varchar(100), '"', '')::int AS first_tower,
  REPLACE((payload."firstInhibitor")::varchar(100), '"', '')::int AS first_inhibitor,
  REPLACE((payload."firstBaron")::varchar(100), '"', '')::int AS first_baron,
  REPLACE((payload."firstDragon")::varchar(100), '"', '')::int AS first_dragon,
  REPLACE((payload."firstRiftHerald")::varchar(100), '"', '')::int AS first_rift_herald,
  -- Time 1 Champions
  (payload."t1_champ1id")::int AS t1_champ1id,
  (payload."t1_champ1_sum1")::int AS t1_champ1_sum1,
  (payload."t1_champ1_sum2")::int AS t1_champ1_sum2,
  (payload."t1_champ2id")::int AS t1_champ2id,
  (payload."t1_champ2_sum1")::int AS t1_champ2_sum1,
  (payload."t1_champ2_sum2")::int AS t1_champ2_sum2,
  (payload."t1_champ3id")::int AS t1_champ3id,
  (payload."t1_champ3_sum1")::int AS t1_champ3_sum1,
  (payload."t1_champ3_sum2")::int AS t1_champ3_sum2,
  (payload."t1_champ4id")::int AS t1_champ4id,
  (payload."t1_champ4_sum1")::int AS t1_champ4_sum1,
  (payload."t1_champ4_sum2")::int AS t1_champ4_sum2,
  (payload."t1_champ5id")::int AS t1_champ5id,
  (payload."t1_champ5_sum1")::int AS t1_champ5_sum1,
  (payload."t1_champ5_sum2")::int AS t1_champ5_sum2,
  -- Time 1 Stats
  (payload."t1_towerKills")::int AS t1_tower_kills,
  (payload."t1_inhibitorKills")::int AS t1_inhibitor_kills,
  (payload."t1_baronKills")::int AS t1_baron_kills,
  (payload."t1_dragonKills")::int AS t1_dragon_kills,
  (payload."t1_riftHeraldKills")::int AS t1_rift_herald_kills,
  (payload."t1_ban1")::int AS t1_ban1,
  (payload."t1_ban2")::int AS t1_ban2,
  (payload."t1_ban3")::int AS t1_ban3,
  (payload."t1_ban4")::int AS t1_ban4,
  (payload."t1_ban5")::int AS t1_ban5,
  -- Time 2 Champions
  (payload."t2_champ1id")::int AS t2_champ1id,
  (payload."t2_champ1_sum1")::int AS t2_champ1_sum1,
  (payload."t2_champ1_sum2")::int AS t2_champ1_sum2,
  (payload."t2_champ2id")::int AS t2_champ2id,
  (payload."t2_champ2_sum1")::int AS t2_champ2_sum1,
  (payload."t2_champ2_sum2")::int AS t2_champ2_sum2,
  (payload."t2_champ3id")::int AS t2_champ3id,
  (payload."t2_champ3_sum1")::int AS t2_champ3_sum1,
  (payload."t2_champ3_sum2")::int AS t2_champ3_sum2,
  (payload."t2_champ4id")::int AS t2_champ4id,
  (payload."t2_champ4_sum1")::int AS t2_champ4_sum1,
  (payload."t2_champ4_sum2")::int AS t2_champ4_sum2,
  (payload."t2_champ5id")::int AS t2_champ5id,
  (payload."t2_champ5_sum1")::int AS t2_champ5_sum1,
  (payload."t2_champ5_sum2")::int AS t2_champ5_sum2,
  -- Time 2 Stats
  (payload."t2_towerKills")::int AS t2_tower_kills,
  (payload."t2_inhibitorKills")::int AS t2_inhibitor_kills,
  (payload."t2_baronKills")::int AS t2_baron_kills,
  (payload."t2_dragonKills")::int AS t2_dragon_kills,
  (payload."t2_riftHeraldKills")::int AS t2_rift_herald_kills,
  (payload."t2_ban1")::int AS t2_ban1,
  (payload."t2_ban2")::int AS t2_ban2,
  (payload."t2_ban3")::int AS t2_ban3,
  (payload."t2_ban4")::int AS t2_ban4,
  (payload."t2_ban5")::int AS t2_ban5
FROM public.mv_lol_game_session;
```

**Resultado esperado:**
```
CREATE VIEW
```

#### Ver Dados Parsed

```sql
SELECT * 
FROM public.vw_lol_game_session 
LIMIT 5;
```

**Resultado esperado:**
```
game_id | creation_time       | game_duration | season_id | winner | first_blood | t1_champ1id | ...
--------|---------------------|---------------|-----------|--------|-------------|-------------|----
123456  | 2024-01-15 14:30:00 | 2156          | 9         | 1      | 1           | 42          | ...
```

---

## ✅ Validação da Tarefa

**Challenge Question:**
```
What is the data type of payload field in materialized view mv_lol_game_session?
```

**Análise:**

No SQL da Materialized View:
```sql
json_parse(kinesis_data) AS payload
```

**Processo:**
1. `kinesis_data` vem do Kinesis como **VARCHAR** (texto)
2. `json_parse()` converte para tipo **SUPER**
3. `payload` tem tipo de dados **SUPER**

**Resposta:**
```
SUPER
```

> 💡 **SUPER** é o tipo de dados do Redshift que permite armazenar e consultar dados semiestruturados (JSON, Parquet, Avro) de forma eficiente.

---

## 🔍 Entendendo o Tipo SUPER

### O que é SUPER?

**Definição:**
Tipo de dados que suporta persistência de dados semiestruturados em forma schema-less.

**Características:**
- Armazena objetos JSON complexos
- Permite consultas PartiQL
- Schema-on-read (aplica schema na leitura)
- Suporta dados aninhados
- Indexável e otimizado

**Exemplo:**
```sql
CREATE TABLE exemplo (
  id INT,
  data SUPER  -- Pode conter qualquer estrutura JSON
);

INSERT INTO exemplo VALUES (
  1, 
  JSON_PARSE('{"name":"John","age":30,"address":{"city":"NYC"}}')
);

-- Acessar campos
SELECT 
  id,
  data.name::varchar,
  data.age::int,
  data.address.city::varchar
FROM exemplo;
```

### Funções SUPER

**json_parse():**
```sql
json_parse('{"key":"value"}')  -- String → SUPER
```

**json_serialize():**
```sql
json_serialize(super_column)  -- SUPER → String
```

**Navegação:**
```sql
super_column.field              -- Dot notation
super_column["field"]           -- Bracket notation
super_column[0]                 -- Array access
```

**Casting:**
```sql
super_column::varchar          -- Convert to string
super_column::int              -- Convert to integer
```

---

## 🚨 Troubleshooting

### Problema: External Schema não cria

**Erro:**
```
Could not create external schema lol_game_session
```

**Causas possíveis:**
- IAM Role ARN incorreto
- Role não tem permissões para Kinesis
- Schema já existe

**Solução:**
```sql
-- Verificar se já existe
SELECT * FROM svv_external_schemas 
WHERE schemaname = 'lol_game_session';

-- Se existir, pode dropar e recriar
DROP SCHEMA IF EXISTS lol_game_session;

-- Recriar com ARN correto
CREATE EXTERNAL SCHEMA lol_game_session
FROM KINESIS
IAM_ROLE 'arn:aws:iam::123456789012:role/Redshiftgamesrole';
```

### Problema: Materialized View vazia

**Sintomas:**
```sql
SELECT COUNT(*) FROM mv_lol_game_session;
-- Retorna 0
```

**Causas possíveis:**
- Streaming não está ativo (Task 1)
- Aguardou menos de 10-20 segundos
- Nome do stream incorreto

**Solução:**
1. Verifique Task 1: Data Generator deve estar enviando dados
2. Aguarde 10-20 segundos
3. Execute query novamente

```sql
-- Ver último refresh
SELECT MAX(refresh_time) FROM mv_lol_game_session;

-- Forçar refresh (se necessário)
REFRESH MATERIALIZED VIEW mv_lol_game_session;
```

### Problema: Erro de case sensitivity

**Erro:**
```
column "gameid" does not exist
```

**Causa:**
- `enable_case_sensitive_identifier` não foi setado para true
- Campo JSON usa CamelCase mas query usa lowercase

**Solução:**
```sql
-- Habilitar case sensitivity
SET enable_case_sensitive_identifier TO true;

-- Usar aspas duplas nos campos JSON
SELECT (payload."gameId")::varchar  -- ✅ Correto
-- NÃO: SELECT payload.gameid       -- ❌ Errado
```

### Problema: Tipo SUPER não reconhecido

**Erro:**
```
type "super" does not exist
```

**Causa:**
- Redshift versão muito antiga (não é o caso no lab)

**Solução:**
- Verifique se executou `json_parse()` corretamente
- SUPER é criado implicitamente ao usar json_parse()

---

## 💡 Dicas Importantes

### 1. Nomenclatura Consistente
- Use mesmo nome para external schema e materialized view prefix
- Facilita identificação e manutenção

### 2. SORTKEY e DISTKEY
```sql
SORTKEY(refresh_time)      -- Otimiza queries por tempo
DISTKEY(sequence_number)   -- Distribui dados uniformemente
```

### 3. Auto Refresh
- Atualiza automaticamente a cada ~10 segundos
- Não precisa fazer REFRESH MATERIALIZED VIEW manualmente
- Pode desabilitar se quiser controle manual:
  ```sql
  AUTO REFRESH NO
  ```

### 4. Monitoramento
```sql
-- Ver histórico de refreshes
SELECT 
  DISTINCT refresh_time,
  COUNT(*) AS records
FROM mv_lol_game_session
GROUP BY refresh_time
ORDER BY refresh_time DESC;

-- Ver estatísticas de refresh
SELECT * FROM svl_mv_refresh_status
WHERE mv_name = 'mv_lol_game_session'
ORDER BY refresh_end DESC
LIMIT 10;
```

### 5. Performance
- Materialized Views são pré-computadas
- Queries na MV são muito mais rápidas que na fonte
- Use views (não MVs) para transformações leves

---

## 🎓 Conceitos Aprendidos

### 1. External Schemas
Permitem acessar dados de fontes externas sem ETL prévio.

**Fontes suportadas:**
- Amazon Kinesis Data Streams
- Amazon S3 (via Spectrum)
- AWS Glue Data Catalog
- Apache Hive Metastore

### 2. Materialized Views
Views cujos resultados são armazenados fisicamente.

**Benefícios:**
- Performance muito melhor
- Auto-refresh para dados em tempo real
- Reduz carga na fonte

### 3. Schema-on-Read
Aplica schema na hora da leitura, não da escrita.

**Vantagens:**
- Flexibilidade para múltiplos schemas
- Evolução de schema mais fácil
- Armazena dados "crus" primeiro

### 4. Type Casting em SQL
```sql
(campo)::tipo           -- PostgreSQL/Redshift style
CAST(campo AS tipo)     -- ANSI SQL style
```

### 5. REPLACE Function
```sql
REPLACE(string, from, to)
-- Remove aspas: REPLACE('"value"', '"', '')
```

---

## 🎯 Checklist de Conclusão

- [ ] Conectado ao cluster gamesds
- [ ] Database dev selecionado
- [ ] External Schema lol_game_session criado
- [ ] IAM Role ARN correto usado
- [ ] Materialized View mv_lol_game_session criada
- [ ] Stream name correto referenciado
- [ ] Aguardados 10-20 segundos para dados
- [ ] Dados visíveis na Materialized View
- [ ] enable_case_sensitive_identifier configurado
- [ ] View vw_lol_game_session criada
- [ ] Dados unnested visíveis
- [ ] Tipo de dados SUPER identificado
- [ ] Resposta "SUPER" submetida
- [ ] Task 2 validada com sucesso

---

**✅ Próxima etapa:** Task 3 - Carregar dados de referência de jogadores do S3!

> **💡 Conceito-chave aprendido:** O tipo **SUPER** permite trabalhar com dados semiestruturados (JSON) de forma eficiente no Redshift, aplicando schema dinamicamente nas queries.
