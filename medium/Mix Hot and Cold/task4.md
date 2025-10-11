# Task 4: Share Data Between Clusters 🔗

**Pontos Possíveis:** 45  
**Penalidade de Dica:** 0  
**Pontos Disponíveis:** 45  
**Check my progress:** Disponível

---

## ⚠️ AVISO - PROBLEMA DE PERMISSÕES

> **❌ ESTA TASK TEM LIMITAÇÕES DE PERMISSÕES**
> 
> **Problema:** O usuário do laboratório não possui permissões adequadas para criar **Datashares** no Redshift.
>
> **Erro típico:**
> ```
> Permission denied for CREATE DATASHARE
> ```
> ou
> ```
> User does not have permissions to create datashare
> ```
>
> **Status:**  
> - Conceitos podem ser aprendidos ✅  
> - Execução prática bloqueada ❌
>
> **Recomendação:** Use esta documentação para aprendizado teórico. Em ambiente próprio, você poderá executar completamente.

---

## 📖 Background

Nesta tarefa, você irá criar um **Data Share** para compartilhar dados de jogadores do cluster **playersds** (produtor) para o cluster **gamesds** (consumidor).

Data Sharing permite que múltiplos clusters Redshift acessem os mesmos dados em **tempo real** sem necessidade de copiar ou mover os dados, ideal para:
- Isolamento de workloads (produção vs análise)
- Compartilhamento entre times
- Governança centralizada de dados

---

## 🎯 Sua Tarefa (Teórica)

1. Criar um datashare em **playersds** (produtor)
2. Adicionar tabela `lol_players` ao datashare
3. Conceder acesso ao cluster **gamesds** (consumidor)
4. Conectar a **gamesds** e criar database local a partir do datashare
5. Executar queries combinando dados compartilhados com dados locais

---

## 📚 Procedimento Teórico

### STEP 1: Criar Datashare no Cluster Produtor (playersds)

**Conectar ao playersds:**
1. Redshift Query Editor V2
2. Cluster: **playersds**
3. Database: **dev**
4. User: **awsuser**

**Criar o Datashare:**

```sql
-- 1. Criar datashare
CREATE DATASHARE player_datashare;
```

**Adicionar schema ao datashare:**

```sql
-- 2. Adicionar schema public ao datashare
ALTER DATASHARE player_datashare 
ADD SCHEMA public;
```

**Adicionar tabela ao datashare:**

```sql
-- 3. Adicionar tabela lol_players ao datashare
ALTER DATASHARE player_datashare 
ADD TABLE public.lol_players;
```

**Verificar o que foi adicionado:**

```sql
-- Ver conteúdo do datashare
SELECT * FROM svv_datashares 
WHERE share_name = 'player_datashare';

-- Ver objetos no datashare
SELECT * FROM svv_datashare_objects 
WHERE share_name = 'player_datashare';
```

**Obter namespace do cluster gamesds:**

Para conceder acesso, você precisa do **namespace** (um GUID único) do cluster consumidor.

```sql
-- No cluster gamesds, execute:
SELECT current_namespace;
-- Resultado: algo como 'a1b2c3d4-e5f6-7890-1234-567890abcdef'
```

**Conceder acesso ao cluster gamesds:**

```sql
-- Volte ao cluster playersds e execute:
GRANT USAGE ON DATASHARE player_datashare 
TO NAMESPACE 'a1b2c3d4-e5f6-7890-1234-567890abcdef';  -- namespace do gamesds
```

**Resultado esperado:**
```
GRANT
```

---

### STEP 2: Consumir Datashare no Cluster Consumidor (gamesds)

**Conectar ao gamesds:**
1. Redshift Query Editor V2 (nova aba/conexão)
2. Cluster: **gamesds**
3. Database: **dev**
4. User: **awsuser**

**Listar datashares disponíveis:**

```sql
-- Ver datashares compartilhados para este cluster
SELECT * FROM svv_datashares 
WHERE share_type = 'INBOUND';
```

**Criar database local a partir do datashare:**

```sql
-- Criar database local que aponta para o datashare
CREATE DATABASE shared_players_db 
FROM DATASHARE player_datashare 
OF NAMESPACE 'namespace-do-playersds';
```

> **💡 Nota:** Você precisa do namespace do cluster **playersds** (produtor) para este comando.

**Obter namespace do playersds:**

```sql
-- No cluster playersds, execute:
SELECT current_namespace;
```

**SQL completo (exemplo):**

```sql
CREATE DATABASE shared_players_db 
FROM DATASHARE player_datashare 
OF NAMESPACE 'z9y8x7w6-v5u4-3210-9876-543210fedcba';
```

**Verificar database criado:**

```sql
-- Ver databases
SELECT * FROM pg_database 
WHERE datname = 'shared_players_db';
```

---

### STEP 3: Executar Queries Cross-Cluster

**Query combinando dados locais e compartilhados:**

Agora no **gamesds**, você pode fazer queries que combinam:
- Dados locais (streaming de jogos)
- Dados compartilhados (jogadores)

**Exemplo 1: Jogos com detalhes dos jogadores**

```sql
-- Substituir <shared_db> pelo nome do database criado
SELECT
  s.season_id,
  s.game_id,
  s.game_duration,
  p.name,
  p.title
FROM 
	public.vw_lol_game_session s,
  shared_players_db.public.lol_players p
WHERE
  s.t1_champ1id = p.id
ORDER BY s.season_id
LIMIT 100;
```

**Campos retornados:**
```
season_id | game_id | game_duration | name       | title
----------|---------|---------------|------------|-------------------
9         | 123456  | 2156          | Ahri       | the Nine-Tailed Fox
9         | 123457  | 1987          | Zed        | the Master of Shadows
```

**Exemplo 2: Estatísticas agregadas**

```sql
SELECT 
  p.name,
  COUNT(DISTINCT s.game_id) AS games_played,
  AVG(s.game_duration) AS avg_duration,
  SUM(CASE WHEN s.winner = 1 THEN 1 ELSE 0 END) AS team1_wins
FROM 
  public.vw_lol_game_session s,
  shared_players_db.public.lol_players p
WHERE
  s.t1_champ1id = p.id OR s.t2_champ1id = p.id
GROUP BY p.name
ORDER BY games_played DESC
LIMIT 20;
```

---

## ✅ Validação da Tarefa (Teórica)

**Challenge:**
```
Find the total count of players running below SQL from gamesds. 
You need to replace "<>" with local database name created in STEP2.
```

**SQL:**

```sql
SELECT COUNT(*) 
FROM shared_players_db.public.lol_players;
```

**Resposta esperada:**
Número total de jogadores na tabela compartilhada (mesmo valor da Task 3).

---

## 🚨 Problema de Permissões - Análise Detalhada

### Erro Encontrado

**Ao tentar criar datashare:**

```sql
CREATE DATASHARE player_datashare;
```

**Erro retornado:**
```
ERROR: permission denied to create datashare
```

ou

```
ERROR: User "awsuser" does not have CREATE DATASHARE privilege
```

### Causa Raiz

**Permissões IAM faltantes:**

O usuário `awsuser` do laboratório não possui as seguintes permissões necessárias:

```sql
-- Permissões necessárias (mas não concedidas):
GRANT CREATE DATASHARE ON DATABASE dev TO awsuser;
GRANT ALTER DATASHARE ON DATASHARE player_datashare TO awsuser;
GRANT GRANT DATASHARE ON DATASHARE player_datashare TO awsuser;
```

**Verificação:**

```sql
-- Ver privilégios do usuário atual
SELECT * FROM pg_user WHERE usename = 'awsuser';

-- Ver datashares existentes (se houver)
SELECT * FROM svv_datashares;
```

### Impacto

**Não é possível:**
- ✅ Ver conceito de Data Sharing
- ✅ Entender sintaxe SQL
- ✅ Compreender benefícios
- ❌ **Criar datashare** (bloqueado)
- ❌ **Adicionar objetos ao datashare** (bloqueado)
- ❌ **Conceder acesso** (bloqueado)
- ❌ **Testar queries cross-cluster** (bloqueado)
- ❌ **Validar a task** (bloqueado)

**Consequência:**
- Task 4 não pode ser completada no ambiente do lab
- 45 pontos não podem ser obtidos
- Conceitos ainda podem ser aprendidos teoricamente

---

## 💡 Soluções Alternativas

### Opção 1: Reportar ao Suporte

**Ações:**
1. Abrir ticket com suporte do AWS Jam
2. Informar o problema de permissões
3. Fornecer detalhes:
   - Lab: "Mix Hot and Cold"
   - Task: Task 4
   - Erro: Permission denied to create datashare
4. Solicitar correção das permissões

### Opção 2: Ambiente Próprio

Se você tem conta AWS própria, pode recriar o cenário:

**Recursos necessários:**
```
1. Dois clusters Redshift (producer e consumer)
2. Tabelas com dados no producer
3. Usuários com permissões adequadas:
   - CREATE DATASHARE
   - ALTER DATASHARE
   - GRANT DATASHARE
4. Conectividade entre clusters (mesma região ou cross-region)
```

**Permissões necessárias:**

```sql
-- No cluster producer
GRANT CREATE DATASHARE ON DATABASE dev TO username;

-- Após criar datashare
GRANT ALTER ON DATASHARE datashare_name TO username;
GRANT SHARE ON DATASHARE datashare_name TO username;
```

### Opção 3: Uso Educacional

**Aproveite para aprender:**
- ✅ Sintaxe de Data Sharing
- ✅ Arquitetura de data sharing
- ✅ Casos de uso reais
- ✅ Benefícios vs alternativas (COPY, Federated Query, etc.)

---

## 📚 Recursos Úteis

### Documentação AWS

- [Redshift Data Sharing Overview](https://docs.aws.amazon.com/redshift/latest/dg/datashare-overview.html)
- [Creating Datashares](https://docs.aws.amazon.com/redshift/latest/dg/create-datashare-console.html)
- [Consuming Datashares](https://docs.aws.amazon.com/redshift/latest/dg/consume-datashare.html)
- [Managing Datashare Permissions](https://docs.aws.amazon.com/redshift/latest/dg/datashare-permissions.html)

### Blogs AWS

- [Sharing Redshift Data Securely](https://aws.amazon.com/blogs/big-data/sharing-amazon-redshift-data-securely-across-amazon-redshift-clusters-for-workload-isolation/)
  - **Referência principal** sugerida no lab
  - Seções importantes:
    - "Sharing data across Amazon Redshift clusters"
    - "Consuming the data share from the consumer BI Amazon Redshift cluster"

- [Cross-Account Data Sharing](https://aws.amazon.com/blogs/big-data/securely-share-your-data-across-aws-accounts-using-amazon-redshift-data-sharing/)

### Vídeos e Tutoriais

- [AWS re:Invent - Redshift Data Sharing](https://www.youtube.com/results?search_query=redshift+data+sharing)
- [AWS Workshops - Data Sharing](https://catalog.workshops.aws/)

---

## 🎓 Conceitos Importantes (Mesmo Sem Executar)

### 1. Data Sharing vs Alternativas

**Comparação:**

| Método | Latência | Custo Storage | Complexidade | Isolamento |
|--------|----------|---------------|--------------|------------|
| **Data Sharing** | Real-time | Único | Baixa | Alto |
| COPY | Minutos/Horas | Duplicado | Média | Médio |
| Federated Query | Segundos | Único | Alta | Médio |
| ETL | Horas | Duplicado | Alta | Alto |

**Quando usar Data Sharing:**
- ✅ Múltiplos times precisam dos mesmos dados
- ✅ Dados atualizados em tempo real
- ✅ Isolamento de workloads (prod vs analytics)
- ✅ Redução de custos de storage
- ✅ Governança centralizada

### 2. Arquitetura de Data Sharing

```
┌─────────────────────────────────────────────────────────┐
│                  Producer Cluster                       │
│                  (playersds)                            │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Database: dev                                          │
│    Schema: public                                       │
│      Table: lol_players                                 │
│                                                         │
│  ┌─────────────────────────────────┐                   │
│  │  Datashare: player_datashare    │                   │
│  │    - ADD SCHEMA public          │                   │
│  │    - ADD TABLE lol_players      │                   │
│  │    - GRANT TO namespace-ABC     │                   │
│  └───────────────┬─────────────────┘                   │
└──────────────────┼─────────────────────────────────────┘
                   │
                   │ Network (zero data movement)
                   │
┌──────────────────▼─────────────────────────────────────┐
│               Consumer Cluster                          │
│                (gamesds)                                │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Database: shared_players_db (FROM DATASHARE)          │
│    ↓ (aponta para producer)                            │
│    Schema: public                                       │
│      Table: lol_players (read-only)                    │
│                                                         │
│  Database: dev (local)                                  │
│    Schema: public                                       │
│      Table: vw_lol_game_session                        │
│                                                         │
│  Query: JOIN local + shared data ✅                     │
└─────────────────────────────────────────────────────────┘
```

### 3. Tipos de Datashare

**Within AWS Account:**
- Mesmo account, clusters diferentes
- Configuração mais simples
- Usado neste lab (se funcionasse)

**Cross-Account:**
- Contas AWS diferentes
- Requer aprovação no console
- Casos de uso entre organizações

**Cross-Region:**
- Regiões AWS diferentes
- Latência adicional
- Custos de transferência inter-region

### 4. Permissões Granulares

**O que pode ser compartilhado:**

```sql
-- Schema inteiro
ALTER DATASHARE ds ADD SCHEMA schema_name;

-- Tabela específica
ALTER DATASHARE ds ADD TABLE schema.table_name;

-- View
ALTER DATASHARE ds ADD VIEW schema.view_name;

-- Materialized View
ALTER DATASHARE ds ADD MATERIALIZED VIEW schema.mv_name;

-- User-defined function
ALTER DATASHARE ds ADD FUNCTION schema.function_name();
```

**O que NÃO pode ser compartilhado:**
- ❌ Stored procedures
- ❌ Late binding views
- ❌ External tables (Spectrum)
- ❌ System tables
- ❌ Temporary tables

### 5. Governança e Auditoria

**Monitoramento:**

```sql
-- Ver todos datashares
SELECT * FROM svv_datashares;

-- Ver objetos compartilhados
SELECT * FROM svv_datashare_objects;

-- Ver consumidores
SELECT * FROM svv_datashare_consumers;

-- Logs de acesso
-- Use CloudTrail e Redshift audit logs
```

**Revogação de acesso:**

```sql
-- Revogar acesso de um consumer
REVOKE USAGE ON DATASHARE player_datashare 
FROM NAMESPACE 'consumer-namespace';

-- Remover objeto do datashare
ALTER DATASHARE player_datashare 
REMOVE TABLE public.lol_players;

-- Deletar datashare
DROP DATASHARE player_datashare;
```

---

## 🎯 Checklist de Compreensão Teórica

Mesmo sem poder executar, você deve entender:

- [ ] Conceito de Data Sharing no Redshift
- [ ] Diferença entre producer e consumer
- [ ] Como criar datashare (`CREATE DATASHARE`)
- [ ] Como adicionar objetos (`ALTER DATASHARE ADD`)
- [ ] Como conceder acesso (`GRANT USAGE ON DATASHARE`)
- [ ] Como obter namespace (`SELECT current_namespace`)
- [ ] Como criar database a partir de datashare
- [ ] Como fazer queries cross-cluster
- [ ] Benefícios vs alternativas
- [ ] Limitações e restrições
- [ ] Casos de uso reais
- [ ] Impacto de permissões faltantes

---

## 📝 Conclusão

### Status Final

| Aspecto | Status | Detalhes |
|---------|--------|----------|
| Conceitos teóricos | ✅ Aprendidos | Documentação completa |
| Sintaxe SQL | ✅ Documentada | Exemplos fornecidos |
| Arquitetura | ✅ Entendida | Diagramas e explicações |
| **Execução prática** | ❌ **Bloqueada** | **Permissões faltantes** |
| Task completável | 🔴 **NÃO** | Requer correção do lab |

### Lições Aprendidas

1. **Data Sharing é poderoso:**
   - Compartilhamento em tempo real
   - Zero data movement
   - Isolamento de workloads

2. **Permissões são críticas:**
   - CREATE DATASHARE necessário
   - Sem isso, toda funcionalidade bloqueada
   - IAM e Redshift permissions devem estar alinhadas

3. **Alternativas existem:**
   - COPY para duplicar dados
   - Federated Query para acesso remoto
   - ETL tradicional para transformações

4. **Conceito vale a pena aprender:**
   - Usado em ambientes enterprise
   - Padrão moderno de arquitetura
   - Reduz custos e complexidade

---

**⚠️ Esta task não pode ser completada até que as permissões de Data Sharing sejam corrigidas no laboratório.**

**✅ Para praticar:** Recrie o cenário em conta AWS própria onde você tem controle total de permissões.

> **💭 Reflexão:** Data Sharing é uma feature moderna e poderosa do Redshift que permite arquiteturas de dados mais eficientes e governadas. Mesmo sem poder executar no lab, entender o conceito é valioso para ambientes de produção reais.
