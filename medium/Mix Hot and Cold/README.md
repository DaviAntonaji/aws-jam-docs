# 🎮 Mix Hot and Cold - Redshift Streaming & Data Sharing

## 📋 Visão Geral

Este desafio aborda **streaming de dados em tempo real** com Amazon Kinesis Data Streams, **ingestão para Amazon Redshift**, processamento de **dados semiestruturados** com tipo SUPER, e **compartilhamento de dados** entre clusters Redshift usando o recurso de **Data Sharing**.

### 🎯 Cenário

Você trabalhará com dados de **sessões de jogos** (gaming) transmitidos em tempo real via Kinesis Data Streams para um Data Warehouse Redshift. Você também juntará esses dados com dados de referência de jogadores usando o recurso de **Redshift Data Sharing**, permitindo consultas analíticas combinando dados "quentes" (streaming) e "frios" (referência).

> **💡 Nome do Desafio:** "Mix Hot and Cold" refere-se à mistura de dados **quentes** (hot = streaming em tempo real) com dados **frios** (cold = dados de referência/históricos)

---

## ⚠️ Aviso Importante - Problema na Task 4

> **❌ TASK 4 TEM PROBLEMA DE PERMISSÕES**
> 
> **Problema:** A Task 4 requer criação de Datashare no Redshift, mas o usuário do lab não possui permissões adequadas para criar datashares entre clusters.
>
> **Status:** 
> - Tasks 1-3: ✅ Funcionam normalmente
> - Task 4: ⚠️ Parcialmente bloqueada (conceitos podem ser aprendidos, mas não executados)
>
> **Recomendação:** Complete Tasks 1-3 normalmente. Use Task 4 para aprendizado teórico de Data Sharing.

---

## 🎓 O Que Você Vai Aprender

- ✅ Gerar dados de streaming com **Kinesis Data Generator**
- ✅ Criar e gerenciar **Kinesis Data Streams**
- ✅ Ingestão de streaming em tempo real para **Amazon Redshift**
- ✅ Trabalhar com **External Schemas** (Kinesis no Redshift)
- ✅ Criar e usar **Materialized Views** com auto-refresh
- ✅ Processar dados semiestruturados com tipo **SUPER**
- ✅ Usar **PartiQL** para consultar dados JSON
- ✅ Técnicas de **UNNEST** e **UNPIVOT**
- ✅ Carregar dados do S3 para Redshift com COPY
- ✅ **Redshift Data Sharing** (teórico, devido ao problema)
- ✅ Consultas analíticas combinando múltiplas fontes

## 🛠️ Serviços AWS Utilizados

- **Amazon Kinesis Data Streams:** Streaming de dados em tempo real
- **Kinesis Data Generator:** Geração de dados de teste
- **Amazon Redshift:** Data Warehouse
  - **gamesds cluster:** Para dados de jogos (streaming)
  - **playersds cluster:** Para dados de jogadores (referência)
- **Amazon S3:** Armazenamento de dados de referência
- **Redshift Query Editor V2:** Interface SQL
- **IAM Roles:** Permissões para Redshift acessar Kinesis e S3

## 📦 Inventário

- ✅ **Kinesis Data Stream** (pré-criado) para receber dados de jogos
- ✅ **Kinesis Data Generator** (URL fornecida) para simular streaming
- ✅ **Redshift Cluster "gamesds"** para dados de sessões de jogos
- ✅ **Redshift Cluster "playersds"** para dados de jogadores
- ✅ **IAM Role "Redshiftgamesrole"** com permissões adequadas
- ✅ **Dados de jogadores no S3** (champion_info.json, etc.)
- ✅ **Credenciais:** awsuser / Awsuser123

## 🎯 Estrutura de Tarefas

### Task 1: Turn on the Game (15 pontos) 🎮

**Objetivo:** Gerar dados de sessão de jogos e transmitir para Kinesis Data Streams

**Ações:**
- Usar Kinesis Data Generator para simular dados de jogos
- Configurar template JSON
- Iniciar streaming para KDS

**Resultado:** Nome do Kinesis Data Stream

---

### Task 2: Ingest Streaming Data (45 pontos) 📥

**Objetivo:** Ingerir dados de streaming do KDS para Redshift e aplicar schema dinamicamente

**Ações:**
- Criar External Schema apontando para Kinesis
- Criar Materialized View com auto-refresh
- Criar View para unnest dados semiestruturados (tipo SUPER)

**Resultado:** Tipo de dados do campo `payload` (SUPER)

---

### Task 3: Load Player Reference Data (45 pontos) 👥

**Objetivo:** Carregar dados de jogadores de diferentes esquemas JSON em uma única tabela

**Ações:**
- Criar tabela staging com tipo SUPER
- Carregar JSONs do S3 usando COPY
- Unnest e unpivot dados para tabela final

**Resultado:** Contagem total de jogadores registrados

---

### ⚠️ Task 4: Share Data Between Clusters (45 pontos) 🔗

**Objetivo:** Compartilhar dados de jogadores entre clusters usando Data Sharing

**🔴 PROBLEMA IDENTIFICADO:**
- Requer permissões para criar Datashare
- Usuário do lab não tem essas permissões
- Conceitos podem ser aprendidos, mas não executados

**Ações (teóricas):**
- Criar datashare em playersds
- Adicionar tabela lol_players ao datashare
- Conceder acesso ao cluster gamesds
- Criar database local a partir do datashare
- Executar queries combinando dados compartilhados

**Resultado esperado:** Contagem de jogadores via datashare

---

## 📊 Arquitetura do Desafio

```
┌─────────────────────────────────────────────────────────────┐
│                    Fluxo de Dados                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. Kinesis Data Generator                                 │
│      │                                                      │
│      ├─► Gera JSON de sessões de jogos                     │
│      │                                                      │
│      ▼                                                      │
│  2. Kinesis Data Stream (Hot Data - Streaming)             │
│      │                                                      │
│      ├─► Real-time streaming                               │
│      │                                                      │
│      ▼                                                      │
│  3. Redshift "gamesds" Cluster                             │
│      │                                                      │
│      ├─► External Schema (Kinesis)                         │
│      ├─► Materialized View (auto-refresh)                  │
│      ├─► View (unnested data) - tipo SUPER                 │
│      │                                                      │
│      │  ┌────────────────────────────────────┐             │
│      │  │  4. S3 (Cold Data - Reference)     │             │
│      │  │     │                               │             │
│      │  │     ├─► champion_info.json         │             │
│      │  │     ├─► champion_info_2.json       │             │
│      │  │     └─► summoner_spell_info.json   │             │
│      │  │                                     │             │
│      │  │  ▼                                  │             │
│      │  │  5. Redshift "playersds" Cluster   │             │
│      │  │     │                               │             │
│      │  │     ├─► COPY from S3               │             │
│      │  │     ├─► Staging table (SUPER)      │             │
│      │  │     ├─► UNNEST / UNPIVOT           │             │
│      │  │     └─► lol_players table          │             │
│      │  └────────────┬─────────────────────────             │
│      │               │                                      │
│      │               │  6. Data Sharing                     │
│      │               │     (⚠️ PROBLEMA AQUI)               │
│      │               │                                      │
│      └───────────────┴──────► 7. Analytic Queries          │
│                               Combining Hot + Cold          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔑 Conceitos-Chave

### 1. Tipo SUPER no Redshift

**O que é:**
Tipo de dados que suporta armazenamento e consulta de dados **semiestruturados** (JSON, Parquet, Avro) sem necessidade de schema fixo.

**Benefícios:**
- Schema-on-read (aplica schema na leitura, não na escrita)
- Suporta dados aninhados
- Permite consultas PartiQL
- Flexível para múltiplos schemas

**Exemplo:**
```sql
CREATE TABLE staging (
  id INT,
  data SUPER  -- Pode conter qualquer estrutura JSON
);
```

### 2. Streaming Ingestion no Redshift

**External Schema para Kinesis:**
```sql
CREATE EXTERNAL SCHEMA kinesis_schema
FROM KINESIS
IAM_ROLE 'arn:aws:iam::...';
```

**Materialized View com Auto-Refresh:**
```sql
CREATE MATERIALIZED VIEW mv_streaming
  sortkey(refresh_time)
  distkey(sequence_number)
  auto refresh yes AS
SELECT
  approximate_arrival_timestamp,
  json_parse(kinesis_data) as payload  -- Tipo SUPER
FROM kinesis_schema.stream_name;
```

**Características:**
- Auto-refresh a cada ~10 segundos
- Dados chegam quase em tempo real
- Usa `json_parse()` para converter para SUPER

### 3. UNNEST e UNPIVOT

**UNNEST:**
Expande arrays em linhas individuais.

**UNPIVOT:**
Transforma colunas em linhas, especialmente útil para JSON dinâmico.

**Exemplo:**
```sql
SELECT
  value.id::int,
  value.name::varchar
FROM staging_table,
UNPIVOT data AS value AT key;
```

### 4. Redshift Data Sharing

**O que é:**
Permite compartilhar dados em **tempo real** entre clusters Redshift sem copiar ou mover dados.

**Benefícios:**
- Isolamento de workloads (produção vs análise)
- Sem duplicação de dados
- Acesso instantâneo
- Controle granular de permissões

**Processo (teórico):**
```sql
-- No cluster produtor (playersds):
CREATE DATASHARE player_share;
ALTER DATASHARE player_share ADD SCHEMA public;
ALTER DATASHARE player_share ADD TABLE public.lol_players;
GRANT USAGE ON DATASHARE player_share TO NAMESPACE 'consumer-namespace';

-- No cluster consumidor (gamesds):
CREATE DATABASE shared_db FROM DATASHARE player_share OF NAMESPACE 'producer-namespace';
SELECT * FROM shared_db.public.lol_players;
```

### 5. Case Sensitivity no Redshift

**Por que é necessário:**
JSON frequentemente tem campos em CamelCase ou UPPERCASE.

**Como configurar:**
```sql
SET enable_case_sensitive_identifier TO true;
```

**Uso:**
```sql
SELECT
  (payload."gameId")::varchar,  -- Aspas duplas para case-sensitive
  (payload."creationTime")::numeric
FROM mv_streaming;
```

---

## 🏆 Critérios de Sucesso

### Tasks 1-3 (Funcionam):
- [ ] Geração de dados de streaming funcionando
- [ ] Kinesis Data Stream recebendo dados
- [ ] External Schema criado no Redshift
- [ ] Materialized View ingesting dados
- [ ] Tipo SUPER identificado e usado corretamente
- [ ] Dados unnested e parsed
- [ ] Dados de jogadores carregados do S3
- [ ] UNPIVOT aplicado corretamente
- [ ] Contagem de jogadores obtida

### Task 4 (Problema):
- [ ] Compreensão teórica de Data Sharing
- [ ] Entendimento de quando usar Data Sharing
- [ ] Conhecimento da sintaxe SQL de datashares
- ⚠️ Criação de datashare (bloqueada por permissões)
- ⚠️ Queries cross-cluster (não pode ser testado)

---

## 📚 Recursos Úteis

### Documentação AWS
- [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/)
- [Streaming Ingestion in Redshift](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-streaming-ingestion.html)
- [Redshift SUPER Data Type](https://docs.aws.amazon.com/redshift/latest/dg/r_SUPER_type.html)
- [Redshift Data Sharing](https://docs.aws.amazon.com/redshift/latest/dg/datashare-overview.html)
- [PartiQL in Redshift](https://docs.aws.amazon.com/redshift/latest/dg/query-super.html)

### Blogs e Artigos
- [Sharing Redshift Data Securely](https://aws.amazon.com/blogs/big-data/sharing-amazon-redshift-data-securely-across-amazon-redshift-clusters-for-workload-isolation/)
- [SUPER Data Type Deep Dive](https://aws.amazon.com/blogs/big-data/query-and-visualize-nested-data-in-amazon-redshift-using-the-super-data-type/)
- [Streaming Ingestion Best Practices](https://aws.amazon.com/blogs/big-data/stream-data-into-amazon-redshift-for-near-real-time-analytics/)

### Ferramentas
- [Kinesis Data Generator](https://awslabs.github.io/amazon-kinesis-data-generator/)

---

## 🎯 Pontuação Total

| Task | Pontos | Status |
|------|--------|--------|
| Task 1: Turn on the Game | 15 | ✅ Funciona |
| Task 2: Ingest Streaming Data | 45 | ✅ Funciona |
| Task 3: Load Player Data | 45 | ✅ Funciona |
| Task 4: Data Sharing | 45 | ⚠️ Problema de permissões |
| **TOTAL** | **150** | **105 possíveis** |

---

## ⏱️ Tempo Estimado

- **Task 1:** 10-15 minutos
- **Task 2:** 20-30 minutos (aguardar refresh de MV)
- **Task 3:** 20-30 minutos
- **Task 4:** 15-20 minutos (se funcionasse)
- **Total:** 65-95 minutos

---

## 🎯 Dificuldade

**⭐⭐⭐☆☆ Medium**

Requer conhecimento de:
- SQL intermediário/avançado
- Conceitos de streaming de dados
- Tipos de dados semiestruturados
- Redshift-specific features

---

## 💡 Dicas Importantes

### Geral
1. ✅ **Mantenha duas abas** do Query Editor abertas (uma para cada cluster)
2. ✅ **Verifique o cluster selecionado** antes de executar queries
3. ✅ **Use DISTINCT id** ao contar jogadores (não apenas COUNT(*))
4. ✅ **Aguarde ~10-20 segundos** para Materialized View atualizar

### Task 1
- Stream name aparece automaticamente no Data Generator
- Use partition key: `gameId` ou `{{random.number()}}`
- Records per second: 5-50 é suficiente

### Task 2
- Execute `SET enable_case_sensitive_identifier TO true;` antes de criar views
- Use aspas duplas em campos JSON com maiúsculas
- Aguarde alguns segundos após iniciar streaming para ver dados

### Task 3
- Confirme que está conectado ao cluster **playersds**
- Execute os 3 COPYs sequencialmente
- Use `COUNT(DISTINCT id)` para contar jogadores únicos

### Task 4
- ⚠️ Se encontrar erro de permissões, é esperado
- Estude a sintaxe de Data Sharing para uso futuro
- Conceito é importante mesmo sem poder executar

---

## 🚨 Troubleshooting

### Problema: Não vejo dados na Materialized View

**Causas possíveis:**
- Streaming não foi iniciado no Data Generator
- Aguardou menos de 10 segundos
- External Schema aponta para stream incorreto

**Solução:**
```sql
-- Verificar se há dados
SELECT COUNT(*) FROM mv_lol_game_session;

-- Ver refresh times
SELECT DISTINCT refresh_time 
FROM mv_lol_game_session 
ORDER BY refresh_time DESC;
```

### Problema: Erro ao fazer COPY do S3

**Causas possíveis:**
- IAM Role ARN incorreto
- Conectado ao cluster errado
- Bucket/arquivo não existe

**Solução:**
- Copie ARN exato das Output Properties
- Verifique dropdown do cluster
- Use exatamente: `s3://redshift-demos/data/players/`

### Problema: SUPER data type não reconhecido

**Causas possíveis:**
- Versão antiga do Redshift (não é o caso no lab)
- Syntax error no SQL

**Solução:**
```sql
-- Testar SUPER
CREATE TABLE test_super (id INT, data SUPER);
INSERT INTO test_super VALUES (1, JSON_PARSE('{"key":"value"}'));
SELECT * FROM test_super;
```

### Problema: Task 4 - Erro ao criar Datashare

**Causa:**
- Permissões IAM faltantes no usuário do lab

**Solução:**
- ❌ Não há workaround no lab atual
- ✅ Estude a documentação de Data Sharing
- ✅ Use em conta própria para praticar

---

## 🏭 Aplicação em Produção

### Melhorias para Ambiente Real

**1. Alta Disponibilidade:**
- Múltiplos shards no Kinesis
- Redshift cluster multi-node
- Backup e disaster recovery

**2. Monitoramento:**
- CloudWatch metrics para Kinesis
- Redshift query monitoring
- Alerts para latência de streaming

**3. Otimização:**
- Tuning de distribution e sort keys
- Ajuste de intervalo de auto-refresh
- Particionamento de dados históricos

**4. Segurança:**
- Encryption at rest (S3, Redshift)
- Encryption in transit (Kinesis, Redshift)
- VPC Endpoints para tráfego privado
- Fine-grained access control

**5. Custo:**
- Right-sizing de clusters Redshift
- Kinesis on-demand vs provisioned
- S3 lifecycle policies
- Pause de clusters quando não usados

---

## 🎓 Próximos Passos

Após completar este desafio:
1. **Pratique em conta própria** para experiência completa com Data Sharing
2. **Explore** outras fontes de streaming (DynamoDB Streams, MSK)
3. **Aprenda** Redshift Spectrum para consultas diretas ao S3
4. **Estude** RA3 nodes e managed storage no Redshift
5. **Implemente** pipelines de dados end-to-end

---

**🎉 Boa sorte com o desafio!**

> **💭 Reflexão:** Este desafio demonstra como combinar dados em tempo real (hot) com dados de referência (cold) em um Data Warehouse moderno, uma arquitetura comum em cenários de analytics de IoT, gaming, e e-commerce.
