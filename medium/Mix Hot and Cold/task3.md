# Task 3: Load Player Reference Data 👥

**Pontos Possíveis:** 45  
**Penalidade de Dica:** 0  
**Pontos Disponíveis:** 45

---

## 📖 Background

Nesta seção, você irá carregar dados de jogadores com **diferentes schemas** em uma única tabela no Redshift. O tipo de dados **SUPER** do Redshift suporta a persistência de dados semiestruturados em forma schema-less. Você então usará **PartiQL** para consultar os dados semiestruturados com tipagem dinâmica.

Um cluster Redshift (**playersds**) foi pré-criado para você na conta.

## 🎯 Sua Tarefa

1. Conectar ao cluster Redshift **playersds**
2. Criar tabela **staging** com coluna tipo **SUPER**
3. Carregar múltiplos arquivos JSON do S3 (cada um com schema diferente)
4. **Unnest** e **unpivot** os dados para tabela final
5. Contar total de jogadores registrados

---

## 📚 Passo a Passo Completo

### STEP 1: Abrir Nova Aba do Query Editor

**Por quê:**
- Você já tem uma aba conectada ao **gamesds** (Task 2)
- Precisa de outra aba para **playersds**
- Ter ambas abertas facilitará a Task 4

**Ações:**
1. **Opção A:** Duplicar aba atual do browser (Ctrl+Shift+K ou Cmd+T)
2. **Opção B:** Abrir nova janela do Query Editor V2

---

### STEP 2: Conectar ao Players Data Store

**Navegação:**
1. Redshift Query Editor V2
2. **Add connection** ou selecione conexão existente

**Configuração:**
- **Connection type:** Temporary credentials
- **Authentication:** Database user name
- **Cluster:** **playersds** ⚠️ (não gamesds!)
- **Database:** `dev`
- **Database user:** `awsuser`
- Click **Connect**

> ⚠️ **IMPORTANTE:** Verifique o dropdown do cluster. Deve estar em **playersds**!

---

### STEP 3: Habilitar Case Sensitivity

**Por quê necessário:**
Os campos JSON podem ter nomes em upper case ou mixed case. Precisamos configurar o Redshift para reconhecer esses nomes.

```sql
SET enable_case_sensitive_identifier TO true;
```

**Resultado esperado:**
```
SET
```

> 💡 **Nota:** Quando os campos JSON estão em upper/mixed case, você DEVE:
> 1. Configurar `enable_case_sensitive_identifier` = TRUE
> 2. Envolver campos com aspas duplas: `"FieldName"`

---

### STEP 4: Criar Tabela Staging

**O que é staging:**
Tabela temporária que recebe dados "crus" antes de serem transformados.

**SQL:**

```sql
DROP TABLE IF EXISTS lol_player_stg;

CREATE TABLE lol_player_stg (
  type    VARCHAR,
  version VARCHAR,
  data    SUPER     -- ⭐ Coluna que armazena JSON de qualquer schema
);
```

**Resultado esperado:**
```
CREATE TABLE
```

**Estrutura:**
- `type` e `version`: Metadados do arquivo JSON
- `data`: Coluna **SUPER** que pode conter qualquer estrutura JSON

---

### STEP 5: Carregar Dados do S3

**Onde encontrar IAM Role ARN:**
- **Output Properties** → **RedshiftGameRoleArn**
- Ou IAM Console → Roles → `Redshiftgamesrole`

**Formato do ARN:**
```
arn:aws:iam::ACCOUNT_ID:role/Redshiftgamesrole
```

#### COPY 1: Champion Info (primeira versão)

```sql
COPY lol_player_stg 
FROM 's3://redshift-demos/data/players/champion_info.json'
REGION 'us-east-1'
IAM_ROLE 'arn:aws:iam::123456789012:role/Redshiftgamesrole'  -- ⚠️ Substitua
FORMAT JSON 'auto';
```

**Resultado esperado:**
```
INFO: Load into table 'lol_player_stg' completed, N rows loaded successfully
```

#### COPY 2: Champion Info (segunda versão)

```sql
COPY lol_player_stg 
FROM 's3://redshift-demos/data/players/champion_info_2.json'
REGION 'us-east-1'
IAM_ROLE 'arn:aws:iam::123456789012:role/Redshiftgamesrole'  -- ⚠️ Substitua
FORMAT JSON 'auto';
```

#### COPY 3: Summoner Spell Info

```sql
COPY lol_player_stg 
FROM 's3://redshift-demos/data/players/summoner_spell_info.json'
REGION 'us-east-1'
IAM_ROLE 'arn:aws:iam::123456789012:role/Redshiftgamesrole'  -- ⚠️ Substitua
FORMAT JSON 'auto';
```

**Verificar dados carregados:**

```sql
SELECT 
  type,
  version,
  COUNT(*) AS record_count
FROM lol_player_stg
GROUP BY type, version;
```

**Resultado esperado:**
```
type     | version | record_count
---------|---------|-------------
champion | 9.3.1   | 143
champion | 10.5.1  | 148
summoner | 9.3.1   | 14
```

**Ver estrutura dos dados:**

```sql
SELECT type, version, data 
FROM lol_player_stg 
LIMIT 3;
```

---

### STEP 6: Unnest e Criar Tabela Final

**O que este SQL faz:**
1. **Unnest:** Expande o objeto JSON da coluna `data`
2. **Unpivot:** Transforma chaves do JSON em linhas
3. **Cast:** Converte campos SUPER para tipos tradicionais (INT, VARCHAR)
4. **Create + Insert:** Cria tabela final e já popula com dados transformados

**SQL completo:**

```sql
CREATE TABLE lol_players
DISTKEY (id)
SORTKEY AUTO
AS
SELECT
  type,
  version,
  value.id::int                   AS id,
  value.title::varchar            AS title,
  value.name::varchar             AS name,
  value.key::varchar              AS key,
  value.description::varchar      AS description,
  value.summonerLevel::int        AS summoner_level,
  value.tags                      AS tags    -- Mantém como SUPER
FROM 
  lol_player_stg c,
  UNPIVOT c.data AS value AT key;
```

**Resultado esperado:**
```
SELECT INTO
```

**Explicação linha por linha:**

| Elemento | Função |
|----------|---------|
| `CREATE TABLE ... AS` | Cria tabela e popula em uma operação |
| `DISTKEY (id)` | Distribui dados por ID entre nodes |
| `SORTKEY AUTO` | Redshift escolhe melhor sort key automaticamente |
| `FROM lol_player_stg c` | Tabela staging como fonte |
| `UNPIVOT c.data AS value AT key` | Transforma objeto JSON em linhas |
| `value.id::int` | Extrai campo `id` e converte para INT |
| `value.title::varchar` | Extrai campo `title` como VARCHAR |
| `value.tags` | Mantém campo `tags` como SUPER (array) |

**UNPIVOT visual:**

```
Antes (1 linha):
{
  "Ahri": {"id": 103, "name": "Ahri", "title": "the Nine-Tailed Fox"},
  "Zed": {"id": 238, "name": "Zed", "title": "the Master of Shadows"}
}

Depois (2 linhas):
key   | value
------|----------------------------------------
Ahri  | {"id": 103, "name": "Ahri", ...}
Zed   | {"id": 238, "name": "Zed", ...}
```

---

### STEP 7: Consultar Dados Parseados

**Ver primeiras linhas:**

```sql
SELECT * 
FROM lol_players 
ORDER BY type, id 
LIMIT 20;
```

**Resultado esperado:**
```
type     | version | id  | title               | name    | key  | description
---------|---------|-----|---------------------|---------|------|-------------
champion | 9.3.1   | 1   | the Dark Child      | Annie   | 1    | Wielding...
champion | 9.3.1   | 2   | the Berserker       | Olaf    | 2    | Olaf is...
champion | 9.3.1   | 3   | the Twisted Fate    | Twisted | 4    | Twisted...
```

**Contagem total de registros:**

```sql
SELECT COUNT(*) AS total_rows 
FROM lol_players;
```

**Contagem por tipo:**

```sql
SELECT 
  type,
  COUNT(*) AS count
FROM lol_players
GROUP BY type;
```

---

## ✅ Validação da Tarefa

**Challenge Question:**
```
What is the total count of players registered to the game?
```

**SQL para obter a resposta:**

```sql
SELECT COUNT(DISTINCT id) AS total_players
FROM lol_players
WHERE id IS NOT NULL;
```

**Por que usar DISTINCT id?**

O desafio pergunta por "players registered", não por "linhas na tabela". Como você carregou múltiplas versões de dados do mesmo jogo, alguns IDs podem aparecer em diferentes versões.

**Contagem correta:**
- Usa `COUNT(DISTINCT id)` para contar IDs únicos
- Filtra `id IS NOT NULL` para excluir possíveis nulos

**Resultado esperado:**
```
total_players
-------------
XXX
```

> **📝 Este número é a resposta que você deve submeter**

---

## 🔍 Troubleshooting

### Problema: COPY falha com erro de permissão

**Erro:**
```
ERROR: S3ServiceException: Access Denied
```

**Causas possíveis:**
- IAM Role ARN incorreto
- Role não tem permissões S3
- Bucket ou caminho incorreto

**Solução:**

```sql
-- Verificar ARN exato nas Output Properties
-- O ARN deve estar completo:
'arn:aws:iam::123456789012:role/Redshiftgamesrole'

-- Verificar se bucket existe (use exatamente este caminho):
's3://redshift-demos/data/players/champion_info.json'
```

### Problema: UNPIVOT não funciona

**Erro:**
```
ERROR: syntax error at or near "UNPIVOT"
```

**Causa:**
- Redshift versão muito antiga (não é o caso no lab)
- Syntax error no SQL

**Solução:**

```sql
-- Sintaxe correta do UNPIVOT:
FROM table_name,
UNPIVOT column_name AS value_alias AT key_alias
```

### Problema: Contagem retorna valor errado

**Sintomas:**
- Contagem muito alta (conta versões duplicadas)

**Solução:**

```sql
-- ❌ Errado:
SELECT COUNT(*) FROM lol_players;  -- Conta todas as linhas

-- ✅ Correto:
SELECT COUNT(DISTINCT id) FROM lol_players;  -- Conta IDs únicos
```

### Problema: Conectado ao cluster errado

**Sintomas:**
- Tabelas não aparecem
- Erro "table does not exist"

**Solução:**
1. Verifique dropdown do cluster no Query Editor
2. Deve estar em **playersds** (não gamesds)
3. Se estiver errado, reconecte ao cluster correto

---

## 💡 Dicas Importantes

### 1. Diferenças entre Clusters

**gamesds:**
- Dados de streaming (hot data)
- Materialized Views
- Dados de sessões de jogos

**playersds:**
- Dados de referência (cold data)
- Carregados do S3
- Dados de jogadores

### 2. SUPER vs Tipos Tradicionais

**Quando usar SUPER:**
- Schema varia entre registros
- Dados aninhados complexos
- Precisa armazenar JSON "as is"

**Quando converter para tipos tradicionais:**
- Queries mais frequentes
- Performance crítica
- Schema estável

### 3. FORMAT JSON 'auto'

**O que faz:**
- Detecta schema automaticamente
- Mapeia campos JSON para colunas
- Se não houver colunas correspondentes, usa SUPER

**Alternativas:**
```sql
FORMAT JSON 's3://bucket/jsonpaths.json'  -- Schema explícito
FORMAT JSON 'auto ignorecase'             -- Ignora case nos nomes
```

### 4. DISTKEY e SORTKEY

**DISTKEY:**
- Distribui dados entre nodes do cluster
- Use em colunas de JOIN frequentes

**SORTKEY AUTO:**
- Redshift escolhe automaticamente
- Baseado em padrões de query

### 5. Monitore Carga

```sql
-- Ver últimas cargas
SELECT * FROM stl_load_errors 
ORDER BY starttime DESC 
LIMIT 10;

-- Ver estatísticas de tabela
SELECT 
  "table",
  size,
  tbl_rows
FROM svv_table_info
WHERE "table" = 'lol_players';
```

---

## 🎓 Conceitos Aprendidos

### 1. Staging Tables

**Padrão:**
```
RAW (S3) → STAGING (Redshift SUPER) → FINAL (Redshift typed)
```

**Benefícios:**
- Valida dados antes de processar
- Permite reprocessamento
- Separa ingestão de transformação

### 2. SUPER Data Type

**Capacidades:**
- Armazena JSON, array, struct
- Schema flexível
- Suporta PartiQL
- Indexável

**Limites:**
- Max 16 MB por valor
- Performance menor que colunas tipadas para queries frequentes

### 3. UNPIVOT

**Transforma:**
```sql
-- De: colunas → linhas
SELECT col1, col2, col3 FROM table;

-- Para: key-value pairs
SELECT key, value FROM table UNPIVOT ...;
```

**Casos de uso:**
- JSON com chaves dinâmicas
- Normalização de dados wide
- Transformação de formato

### 4. PartiQL

**SQL + JSON:**
```sql
-- Dot notation
SELECT data.field FROM table;

-- Array access
SELECT data[0] FROM table;

-- Nested access
SELECT data.nested.field FROM table;
```

### 5. COPY Command

**Performance:**
- Paralelo e otimizado
- Compressão automática
- Carrega de múltiplos arquivos

**Opções importantes:**
```sql
COPY table FROM 's3://...'
IAM_ROLE '...'
REGION '...'
FORMAT JSON 'auto'
COMPUPDATE ON         -- Atualiza colunas de compressão
STATUPDATE ON         -- Atualiza estatísticas
MAXERROR 10;          -- Permite até 10 erros
```

---

## 🎯 Checklist de Conclusão

- [ ] Nova aba do Query Editor aberta
- [ ] Conectado ao cluster playersds
- [ ] Database dev selecionado
- [ ] Case sensitivity habilitado
- [ ] Tabela staging lol_player_stg criada
- [ ] IAM Role ARN obtido
- [ ] Três arquivos JSON carregados via COPY
- [ ] Dados visíveis na staging table
- [ ] Tabela final lol_players criada com UNPIVOT
- [ ] Dados parsed visíveis
- [ ] COUNT(DISTINCT id) executado
- [ ] Total de players identificado
- [ ] Resposta submetida
- [ ] Task 3 validada com sucesso

---

**✅ Próxima etapa:** Task 4 - Compartilhar dados entre clusters (⚠️ problema de permissões)

> **💡 Conceito-chave aprendido:** O tipo **SUPER** permite carregar múltiplos schemas JSON em uma única tabela, que podem então ser unnested e convertidos para tipos tradicionais conforme necessário. Isso oferece flexibilidade máxima para dados semiestruturados.
