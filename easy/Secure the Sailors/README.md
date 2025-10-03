# ⚓ Secure the Sailors

## 📋 Visão Geral

Você foi contratado como desenvolvedor de jogos para "Sail to the Unknown". Uma das funcionalidades é proteger os dados dos marinheiros (sailors), garantindo que o acesso seja baseado no princípio de "need to know" - usuários devem ter acesso apenas às informações que sua função de trabalho exige.

Este desafio ensina conceitos avançados de segurança em bancos de dados usando **Amazon Redshift Serverless**, incluindo **Row-Level Security (RLS)** e **Column-Level Security (CLS)** para implementar controles granulares de acesso a dados.

## 🎯 Objetivos de Aprendizado

- ✅ Configurar Amazon Redshift Serverless e carregar dados
- ✅ Implementar Column-Level Security (CLS) para controle de acesso por coluna
- ✅ Implementar Row-Level Security (RLS) para controle de acesso por linha
- ✅ Criar usuários e roles com permissões específicas
- ✅ Aplicar princípios de least privilege em bancos de dados
- ✅ Validar políticas de segurança através de testes práticos
- ✅ Entender o comportamento de RLS quando usuários não têm políticas anexadas

## 🏗️ Arquitetura

```
Amazon Redshift Serverless
├── Workgroup: seabird-wg
├── Namespace: seabird-nm
├── Database: dev
├── Tabela: sailors
│   ├── Column-Level Security (CLS)
│   └── Row-Level Security (RLS)
├── Roles: captain, crew, finance
└── Users: cook, cuddy, cashking, pirate
```

## 🛠️ Serviços Utilizados

- **Amazon Redshift Serverless** - Data warehouse para análise de dados
- **AWS Secrets Manager** - Armazenamento seguro de credenciais
- **Amazon S3** - Fonte de dados para carregamento
- **IAM** - Roles para acesso ao S3

## 📚 Conceitos Principais

### 1. **Column-Level Security (CLS)**
- Controle de acesso baseado em colunas específicas
- Usuários veem apenas colunas autorizadas
- Implementado via GRANT SELECT em colunas específicas

### 2. **Row-Level Security (RLS)**
- Controle de acesso baseado em linhas/filtros
- Políticas que determinam quais linhas são visíveis
- Usuários sem políticas anexadas veem zero linhas

### 3. **Princípio de Need-to-Know**
- Acesso baseado em função de trabalho
- Diferentes níveis de acesso por role
- Proteção de dados sensíveis (PII)

## 🚀 Passo a Passo Detalhado

### **Task 1: All Aboard - Configuração Inicial**

#### 1. **Conectar ao Redshift Serverless**

1. Navegue para **Redshift** → **Query Editor V2**
2. Conecte ao workgroup `seabird-wg`
3. **Autenticação:** Database user name and password
   - **Username:** `awsuser`
   - **Password:** Recupere de `RedshiftServerlessSecret-*` no Secrets Manager
   - **Database:** `dev`

#### 2. **Criar Tabela Sailors**

```sql
CREATE TABLE IF NOT EXISTS public.sailors (
  s_id               BIGINT,
  s_name             VARCHAR(25),
  s_address          VARCHAR(40),
  s_phone            VARCHAR(15),
  s_acctbal          NUMERIC(12,2),
  s_segment          VARCHAR(10),
  s_dietrestrictions VARCHAR(20),
  s_onboard          BOOLEAN
);
```

#### 3. **Carregar Dados do S3**

```sql
COPY public.sailors (
  s_id, s_name, s_address, s_phone, s_acctbal,
  s_segment, s_dietrestrictions, s_onboard
)
FROM 's3://redshift-demos/data/gamejam/sailors'
IAM_ROLE 'arn:aws:iam::370381165256:role/Redshiftgamesrole';
```

#### 4. **Criar Usuários e Roles**

```sql
-- Criar roles
CREATE ROLE captain;
CREATE ROLE crew;
CREATE ROLE finance;

-- Criar usuários
CREATE USER cook     PASSWORD 'Cook_P@ssw0rd!';
CREATE USER cuddy    PASSWORD 'Cuddy_P@ssw0rd!';
CREATE USER cashking PASSWORD 'Cash_P@ssw0rd!';

-- Atribuir roles aos usuários
GRANT ROLE captain TO USER cook;
GRANT ROLE crew    TO USER cuddy;
GRANT ROLE finance TO USER cashking;
```

#### 5. **Responder Pergunta de Negócio**

```sql
SELECT COUNT(*) AS diamond_onboard
FROM public.sailors
WHERE s_onboard = TRUE
  AND LOWER(TRIM(s_segment)) = 'diamond';
```

### **Task 2: Secure Sailors - Implementar Segurança**

#### 1. **Remover Permissões Públicas**

```sql
REVOKE ALL ON TABLE public.sailors FROM PUBLIC;
```

#### 2. **Implementar Column-Level Security**

```sql
-- Captain: acesso a todas as colunas
GRANT SELECT ON TABLE public.sailors TO ROLE captain;

-- Crew: apenas nome, segmento e dieta
GRANT SELECT (s_name, s_segment, s_dietrestrictions)
ON TABLE public.sailors TO ROLE crew;

-- Finance: apenas nome, endereço e saldo
GRANT SELECT (s_name, s_address, s_acctbal)
ON TABLE public.sailors TO ROLE finance;
```

#### 3. **Implementar Row-Level Security**

```sql
-- Política para todas as linhas (captain e finance)
CREATE RLS POLICY rls_all_rows
WITH (s_onboard BOOLEAN) AS s
USING (TRUE);

-- Política apenas para onboard (crew)
CREATE RLS POLICY rls_only_onboard
WITH (s_onboard BOOLEAN) AS s
USING (s.s_onboard = TRUE);

-- Anexar políticas às roles
ATTACH RLS POLICY rls_all_rows     ON TABLE public.sailors TO ROLE captain;
ATTACH RLS POLICY rls_all_rows     ON TABLE public.sailors TO ROLE finance;
ATTACH RLS POLICY rls_only_onboard ON TABLE public.sailors TO ROLE crew;

-- Habilitar RLS na tabela
ALTER TABLE public.sailors ENABLE ROW LEVEL SECURITY;
```

#### 4. **Validar Implementação**

```sql
-- Verificar quantas linhas cada role vê
SELECT
  COUNT(*) AS total_rows,
  COUNT(CASE WHEN s_onboard THEN 1 END) AS total_onboard
FROM public.sailors;
```

### **Task 3: Watch for Pirates - Testar Segurança**

#### 1. **Criar Usuário Pirate**

```sql
-- Criar usuário pirate
CREATE USER pirate PASSWORD 'Pirate_P@ssw0rd!';

-- Conceder permissões totais
GRANT USAGE ON SCHEMA public TO pirate;
GRANT ALL ON TABLE public.sailors TO pirate;
```

#### 2. **Testar Acesso do Pirate**

```sql
-- Fazer login como pirate
SET SESSION AUTHORIZATION 'pirate';

-- Tentar consultar a tabela
SELECT COUNT(*) FROM public.sailors;
```

#### 3. **Monitorar Políticas de Segurança**

```sql
-- Ver tabelas protegidas por RLS
SELECT * FROM SVV_RLS_RELATION;

-- Ver políticas de RLS criadas
SELECT * FROM SVV_RLS_POLICY;

-- Ver políticas anexadas
SELECT * FROM SVV_RLS_ATTACHED_POLICY;

-- Ver aplicação de políticas
SELECT * FROM SVV_RLS_APPLIED_POLICY;
```

## 🔍 Validação

### **Task 1 - Critérios de Sucesso**
- [ ] Tabela sailors criada com estrutura correta
- [ ] Dados carregados do S3 com sucesso
- [ ] Usuários e roles criados
- [ ] Roles atribuídos aos usuários
- [ ] Pergunta sobre sailors Diamond respondida

### **Task 2 - Critérios de Sucesso**
- [ ] Permissões públicas revogadas
- [ ] Column-Level Security implementada
- [ ] Row-Level Security implementada
- [ ] Políticas anexadas às roles corretas
- [ ] RLS habilitado na tabela
- [ ] Usuário cuddy vê apenas sailors onboard

### **Task 3 - Critérios de Sucesso**
- [ ] Usuário pirate criado
- [ ] Permissões totais concedidas
- [ ] Pirate vê 0 linhas (sem políticas RLS)
- [ ] Comportamento de segurança validado

## 🎓 Conceitos Aprendidos

### **Amazon Redshift Serverless**
- **Configuração** de workgroups e namespaces
- **Carregamento** de dados via COPY do S3
- **Autenticação** via Secrets Manager
- **Query Editor V2** para execução de comandos

### **Segurança em Bancos de Dados**
- **Column-Level Security** para controle granular de colunas
- **Row-Level Security** para filtros baseados em dados
- **Princípio de least privilege** aplicado a dados
- **Políticas de acesso** baseadas em roles

### **Controle de Acesso Baseado em Função**
- **Captain:** Acesso total a todos os dados
- **Crew:** Apenas dados de sailors onboard + colunas específicas
- **Finance:** Dados financeiros de todos os sailors
- **Pirate:** Demonstra que permissões sem políticas RLS = 0 linhas

## ⚠️ Pontos de Atenção

### **Configuração de RLS**
- **RLS habilitado** significa que usuários sem políticas veem 0 linhas
- **Políticas devem ser anexadas** às roles, não aos usuários
- **Ordem de execução** importa: criar políticas antes de anexar

### **Permissões de Coluna**
- **GRANT SELECT** em colunas específicas limita visibilidade
- **Usuários sem permissão** em colunas recebem erro de acesso
- **Combinação** de CLS + RLS oferece controle total

### **Ambiente de Teste**
- **SET SESSION AUTHORIZATION** simula login de outros usuários
- **Validação** pode ser feita com awsuser consultando contadores
- **Sistema tables** (SVV_*) mostram configurações de segurança

## 🔧 Troubleshooting Comum

### **Erro de COPY do S3**
- Verifique se a IAM role tem permissões no bucket
- Confirme o caminho do S3 está correto
- Teste com formato específico se necessário

### **RLS não funciona**
- Verifique se RLS está habilitado na tabela
- Confirme se políticas estão anexadas às roles
- Teste com usuário que tem política anexada

### **Usuário vê 0 linhas**
- Verifique se usuário tem role com política RLS
- Confirme se política está corretamente anexada
- Teste com awsuser para validar dados existem

## 📖 Recursos Adicionais

### **Documentação AWS**
- [Redshift Serverless](https://docs.aws.amazon.com/redshift/latest/mgmt/serverless-overview.html)
- [Row-Level Security](https://docs.aws.amazon.com/redshift/latest/dg/t_rls.html)
- [Column-Level Security](https://docs.aws.amazon.com/redshift/latest/dg/t_column_level_security.html)
- [Query Editor V2](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2.html)

### **Boas Práticas de Segurança**
- **Princípio de least privilege** em todos os acessos
- **Separação de responsabilidades** por roles
- **Auditoria regular** de permissões
- **Testes de segurança** com usuários não autorizados

### **Próximos Passos**
- **Implementar** RLS em outras tabelas sensíveis
- **Configurar** alertas para tentativas de acesso não autorizado
- **Integrar** com sistemas de auditoria
- **Automatizar** provisionamento de usuários e roles

## 🏆 Critérios de Sucesso

- [ ] **Compreensão:** Entender conceitos de RLS e CLS
- [ ] **Implementação:** Configurar segurança corretamente
- [ ] **Validação:** Testar diferentes níveis de acesso
- [ ] **Troubleshooting:** Resolver problemas de permissão
- [ ] **Aplicação:** Transferir conhecimento para cenários reais

## 🎯 Cenários de Aplicação

### **Ambiente Corporativo**
- **Controle de acesso** a dados financeiros
- **Separação** entre dados de produção e desenvolvimento
- **Compliance** com regulamentações de privacidade
- **Auditoria** de acessos a dados sensíveis

### **Multi-tenant Applications**
- **Isolamento** de dados entre clientes
- **Controle granular** de acesso por tenant
- **Segurança** em aplicações SaaS
- **Escalabilidade** de políticas de segurança

---

**🎉 Parabéns!** Você implementou com sucesso controles avançados de segurança em Amazon Redshift Serverless, incluindo Row-Level Security e Column-Level Security. Estes conceitos são fundamentais para proteger dados sensíveis em ambientes de data warehouse.

> **💡 Dica:** RLS e CLS são ferramentas poderosas para implementar segurança em profundidade. Use-as sempre que precisar de controle granular de acesso a dados, especialmente em ambientes com múltiplos usuários e dados sensíveis.
