# 🔍 Who messed up the data in my DB Cluster?

## ⚠️ AVISO IMPORTANTE - PROBLEMA NA TASK 2

> **🚨 DADOS AUSENTES NO AMBIENTE:**  
> A **Task 2 deste desafio não pode ser completada** porque o evento esperado **não existe nos logs**. Os logs de auditoria estão funcionando corretamente e a query oficial das dicas executa sem erros, **MAS** apenas aparecem logs do usuário do sistema `rdsadmin` (operações de manutenção). O validador **rejeita `rdsadmin` como resposta**. O evento de UPDATE malicioso na tabela `AUDIT.REVENUE` que deveria existir para investigação forense **nunca foi gerado** no ambiente do lab. A Task 1 funciona perfeitamente (40 pts), mas a Task 2 **não pode ser validada** devido a dados ausentes no ambiente.

## 📋 Visão Geral

Você é um DBA na organização Cappix. Seu chefe de unidade de negócios pediu para você descobrir quem bagunçou os dados no relatório trimestral mais recente. Você tem acesso total ao console RDS e precisa auditar mudanças de dados em uma instância Amazon RDS MySQL onde os relatórios estão armazenados para identificar o culpado.

Este desafio ensina como configurar e usar **Audit Logs no RDS MySQL** usando o **MariaDB Audit Plugin** e enviar os logs para o Amazon CloudWatch para análise forense.

## 🎯 Objetivos de Aprendizado

- ✅ Entender o funcionamento de Audit Logs no Amazon RDS MySQL
- ✅ Configurar o MariaDB Audit Plugin via Option Groups
- ✅ Habilitar exportação de logs para CloudWatch Logs
- ✅ Usar CloudWatch Logs Insights para análise de logs
- ✅ Identificar atividades DML suspeitas em bancos de dados
- ✅ Aplicar técnicas de auditoria e forense em ambientes RDS

## 🏗️ Arquitetura

```
Amazon RDS MySQL (challenge-node-777)
├── Option Group (mysql-audit-logs)
│   └── MariaDB Audit Plugin
│       ├── SERVER_AUDIT_EVENTS: CONNECT, QUERY
│       └── SERVER_AUDIT_LOG_STREAM: ON
├── Log Exports
│   ├── Audit log ✅
│   ├── Error log
│   ├── General log
│   └── Slow query log
└── CloudWatch Logs
    └── /aws/rds/instance/challenge-node-777/audit
        └── CloudWatch Logs Insights
```

## 🛠️ Serviços Utilizados

- **Amazon RDS MySQL** - Banco de dados relacional gerenciado
- **Amazon CloudWatch Logs** - Armazenamento e análise de logs
- **CloudWatch Logs Insights** - Query de logs com linguagem específica
- **MariaDB Audit Plugin** - Plugin de auditoria para MySQL

## 📚 Conceitos Principais

### 1. **MariaDB Audit Plugin**
- Plugin de auditoria compatível com RDS MySQL
- Captura eventos de CONNECT, QUERY, TABLE
- Configurável via Option Groups no RDS

### 2. **Option Groups no RDS**
- Grupos de opções para habilitar recursos adicionais
- Vinculados a instâncias RDS
- Requerem reinicialização da instância

### 3. **CloudWatch Logs Insights**
- Linguagem de query para análise de logs
- Filtros, agregações e visualizações
- Análise em tempo real de logs

### 4. **Auditoria de Banco de Dados**
- Registro de atividades de usuários
- Forense e compliance
- Identificação de atividades suspeitas

## 🚀 Passo a Passo Detalhado

### **Task 1: Find the best place to review RDS Audit logs** (40 pontos)

#### Objetivo
Habilitar o MySQL Audit Log no RDS e configurar o envio dos logs para o CloudWatch Logs.

#### 1. Acessar o Console RDS

1. Vá em **Amazon RDS** → **Databases**
2. Localize sua instância: `challenge-node-777`
3. Anote a versão do MySQL (exemplo: 8.0.x)

#### 2. Criar um Option Group

1. Menu lateral → **Option groups** → **Create group**
2. Configure:
   - **Name:** `mysql-audit-logs`
   - **Engine:** `mysql`
   - **Major engine version:** Selecione a mesma da sua instância
   - **Description:** Habilitar MariaDB Audit Plugin
3. **Create**

#### 3. Adicionar o MariaDB Audit Plugin

1. Selecione o grupo recém-criado → **Add option**
2. Configure:

| Campo | Valor | Descrição |
|-------|-------|-----------|
| **Option name** | `MARIADB_AUDIT_PLUGIN` | Plugin de auditoria |
| **Version** | Mais recente | - |
| **Apply immediately** | ✅ | Aplicar sem aguardar janela de manutenção |

3. **Option settings:**
```
SERVER_AUDIT_EVENTS = CONNECT,QUERY
SERVER_AUDIT_FILE_ROTATIONS = 10
SERVER_AUDIT_FILE_ROTATE_SIZE = 1000000
SERVER_AUDIT_LOG_STREAM = ON
```

⚠️ **Importante:** `SERVER_AUDIT_LOG_STREAM = ON` é o que envia os logs para o CloudWatch!

4. **Add option**

#### 4. Vincular Option Group à Instância

1. **Databases** → `challenge-node-777` → **Modify**
2. Seção **Database options** → **Option group**
3. Selecione: `mysql-audit-logs`
4. Role até o fim → marque **Apply immediately**
5. **Continue** → **Modify DB Instance**

#### 5. Habilitar Exportação de Logs para CloudWatch

1. Ainda na tela de **Modify**
2. Seção **Log exports** → marque:
   - ☑ **Audit log** (obrigatório)
   - ☑ Error log (opcional)
   - ☑ General log (opcional)
   - ☑ Slow query log (opcional)
3. **Apply immediately** → **Continue** → **Modify DB Instance**

#### 6. Validar no CloudWatch

1. Vá para **CloudWatch** → **Log groups**
2. Procure por: `/aws/rds/instance/challenge-node-777/audit`
3. Clique no log group → verifique se há log streams
4. Os eventos de auditoria devem começar a aparecer

✅ **Task 1 completada com sucesso!**

---

### **Task 2: AUDIT USER ACTIVITY** (40 pontos) ⚠️

#### ⛔ DADOS AUSENTES NO AMBIENTE

> **🚨 PROBLEMA IDENTIFICADO:**  
> Esta task **NÃO PODE SER COMPLETADA** porque os dados esperados não existem:
> 
> 1. **Query oficial das dicas:** Executa corretamente ✅
> 2. **Resultado obtido:** Apenas usuário `rdsadmin` (sistema)
> 3. **Validador:** Rejeita `rdsadmin` como resposta ❌
> 4. **Evento esperado:** UPDATE em `AUDIT.REVENUE` não existe nos logs
>
> **Consequência:** O evento de modificação maliciosa que deveria existir para análise forense **nunca foi gerado** no ambiente do lab. Os logs de auditoria estão funcionando perfeitamente, mas não há o evento suspeito para investigar.

#### Objetivo (Teórico)

Usar CloudWatch Logs Insights para identificar qual usuário executou comandos DML (UPDATE) na tabela `AUDIT.REVENUE`.

#### Ambiente Fornecido

| Item | Valor |
|------|-------|
| Instância RDS | `challenge-node-777.cmqbsuenxuki.us-east-1.rds.amazonaws.com` |
| Banco principal | `audit` |
| Usuário de aplicação | `jamrdsuser` |
| Senha | `+o5%.X,I0!=k<gx\` |
| CloudWatch Log Group | `/aws/rds/instance/challenge-node-777/audit` |

#### Query CloudWatch Logs Insights (Oficial das Dicas)

**Query fornecida nas dicas oficiais:**

```sql
filter @message like /update/ 
| parse @message "ip*,*,*" as IP, USER 
| stats count(*) by USER
```

**Passo a passo:**
1. CloudWatch → Log Insights
2. Selecione o log group: `/aws/rds/instance/challenge-node-777/audit`
3. Execute a query acima
4. Submeta o username obtido

#### Resultado Obtido

**Query executada com sucesso:**
```
Field: USER
Value: rdsadmin
count(*): 5
```

**Status:** ❌ **`rdsadmin` não é aceito pelo validador**

#### O Que Foi Encontrado

1. ✅ **Configuração de Audit Plugin:** Completa e funcional
2. ✅ **Logs no CloudWatch:** Funcionando e recebendo eventos
3. ✅ **Query das dicas:** Executa corretamente
4. ⚠️ **Resultado:** Apenas `rdsadmin` (usuário do sistema)
5. ❌ **Validação:** `rdsadmin` rejeitado como resposta
6. ❌ **Evento esperado:** UPDATE em `AUDIT.REVENUE` não existe

#### O Que os Logs Mostram

```
Apenas logs do sistema são visíveis:
- rdsadmin executando rds_heartbeat2
- Operações internas de manutenção do RDS
- Nenhum log de usuário de aplicação (jamrdsuser)
- Nenhum UPDATE em AUDIT.REVENUE

Conclusão: O evento malicioso que a task pede para investigar
           nunca foi gerado no ambiente do lab.
```

## 🔍 Validação

### Task 1 - Critérios de Sucesso
- [x] Option Group criado com MariaDB Audit Plugin
- [x] Plugin configurado com eventos CONNECT e QUERY
- [x] Option Group vinculado à instância
- [x] Log exports habilitados para Audit log
- [x] Logs aparecendo no CloudWatch Logs
- [x] Task validada automaticamente (40 pontos)

### Task 2 - Status
- [x] CloudWatch Logs Insights acessível
- [x] Queries funcionando corretamente
- [ ] ⚠️ **Evento UPDATE não existe** (ambiente sem acesso SQL)
- [ ] ⚠️ **Validação automática impossível**

## 🎓 Conceitos Aprendidos

### **RDS Audit Logs**
- **Option Groups:** Mecanismo para habilitar recursos
- **MariaDB Audit Plugin:** Compatível com RDS MySQL
- **Log Streaming:** Envio direto para CloudWatch
- **Exportação de Logs:** Configuração em nível de instância

### **CloudWatch Logs Insights**
- **Query Language:** Sintaxe específica para análise
- **Filtros e Parse:** Extração de campos estruturados
- **Agregações:** Stats e contadores
- **Visualização:** Análise temporal de eventos

### **Auditoria de Bancos de Dados**
- **Eventos auditáveis:** CONNECT, QUERY, TABLE
- **Forense:** Identificação de atividades suspeitas
- **Compliance:** Requisitos regulatórios (SOX, GDPR, HIPAA)
- **Performance:** Impacto mínimo com configuração adequada

## ⚠️ Pontos de Atenção

### **Option Groups**
- Requerem versão exata do engine
- Mudanças podem necessitar reinicialização
- Apply immediately força aplicação imediata

### **Audit Plugin Performance**
- Captura de QUERY pode gerar volume alto de logs
- Configure eventos específicos conforme necessidade
- Monitore custos do CloudWatch Logs

### **Limitações do Ambiente Jam**
- ⚠️ Nem todos os recursos AWS estão disponíveis
- ⚠️ Query Editor pode estar bloqueado
- ⚠️ CloudShell pode estar desabilitado
- ⚠️ Conexões externas podem estar bloqueadas

## 🔧 Troubleshooting

### Problema: Logs não aparecem no CloudWatch

**Soluções:**
1. Verifique se `SERVER_AUDIT_LOG_STREAM = ON`
2. Confirme que Log exports → Audit log está marcado
3. Aguarde 5-10 minutos para propagação
4. Verifique se a instância foi reiniciada (se necessário)

### Problema: Option Group não pode ser vinculado

**Causas possíveis:**
- Versão do engine não compatível
- Instância em estado modificando
- Option Group em uso por outra instância

### Problema: Query Editor não funciona

**Erro comum:**
```
Your account doesn't have access to AWS Secrets Manager
```

**Motivo:** Limitação do ambiente Jam

**Alternativas:**
- Tente AWS CloudShell (se disponível)
- Tente conexão externa via MySQL client
- Reporte ao instrutor se for ambiente de treinamento

### Problema: Conexão MySQL externa bloqueada

**Erro:**
```
ERROR 2003 (HY000): Can't connect to MySQL server
```

**Causas:**
- Security Group não permite porta 3306
- VPC/Subnet sem acesso público
- Network ACL bloqueando tráfego

## 📖 Recursos Adicionais

### **Documentação AWS**
- [RDS MySQL Audit Log](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MySQL.Options.AuditPlugin.html)
- [CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html)
- [RDS Option Groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithOptionGroups.html)

### **Boas Práticas**
- Configure audit apenas para eventos necessários
- Use CloudWatch Logs Retention para controlar custos
- Implemente alertas para atividades suspeitas
- Documente usuários e propósitos de acesso

### **Queries CloudWatch Insights Úteis**

#### Listar todos os usuários conectados:
```sql
fields @message
| filter @message like /CONNECT/
| parse @message /.*,(?<username>[^,]+),(?<host>[^,]+),CONNECT.*/ 
| stats count() by username, host
```

#### Buscar comandos UPDATE:
```sql
fields @message
| filter @message like /(?i)update/
| filter @message like /QUERY/
| limit 100
```

#### Análise temporal de queries:
```sql
fields @timestamp, @message
| filter @message like /QUERY/
| stats count() by bin(5m)
```

## 🏆 Critérios de Sucesso

- [ ] **Task 1 (40 pts):** Audit logs configurados e visíveis no CloudWatch ✅
- [ ] **Task 2 (40 pts):** Username identificado via Logs Insights ⚠️ **Bloqueado**
- [ ] **Total possível:** 40 de 80 pontos (devido a limitação de ambiente)

## 📊 Sumário de Pontuação

| Task | Pontos | Status | Observação |
|------|--------|--------|------------|
| Task 1 | 40 | ✅ Completável | Funciona perfeitamente |
| Task 2 | 40 | ⚠️ Bloqueado | Limitação de ambiente |
| **Total** | **80** | **50% atingível** | 40 pontos máximo possível |

---

**🎯 Conclusão:** Este desafio ensina conceitos valiosos de auditoria no RDS MySQL, mas apresenta uma limitação de infraestrutura no ambiente Jam que impede a conclusão da Task 2. A configuração técnica está correta e funcional.

> **💡 Recomendação:** Use este desafio para aprender a configurar Audit Logs (Task 1), mas esteja ciente que a Task 2 não poderá ser validada devido às restrições do ambiente.