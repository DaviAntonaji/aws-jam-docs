# Task 1: Find the best place to review RDS Audit logs

**Pontos Possíveis:** 40  
**Penalidade por Dica:** 0  
**Pontos Disponíveis:** 40

## 🎯 Background

Sua instância Amazon RDS MySQL não tem Audit logging (option group) habilitado e sem ele é difícil investigar mais a fundo.

## 📋 Your Task

Sua tarefa aqui é simples. Apenas habilite e envie os Audit logs da instância de banco de dados RDS MySQL para o CloudWatch.

## 🚀 Getting Started

Você pode realizar isso usando o console AWS indo até o serviço RDS.

## 📦 Inventory

Este desafio já vem provisionado com os seguintes recursos. Use o AWS Management Console para navegar pelos vários serviços e recursos.

- **Amazon RDS MySQL instance:** `challenge-node-777`
- **Amazon CloudWatch**

## 🛠️ Services You Should Use

- Amazon RDS MySQL
- Amazon CloudWatch

## ✅ Task Validation

Você será bem-sucedido nesta tarefa assim que exportar seus Audit logs para o CloudWatch.

---

## 🔍 Resolução Detalhada

### 🎯 Objetivo

Ativar o MySQL Audit Log no RDS (usando o MariaDB Audit Plugin dentro de um Option Group) e configurar o envio dos logs para o CloudWatch Logs.

### 📊 Informações da Instância

| Item | Valor |
|------|-------|
| **Nome da instância** | `challenge-node-777` |
| **Endpoint** | `challenge-node-777.cmqbsuenxuki.us-east-1.rds.amazonaws.com` |
| **Engine** | MySQL |
| **Região** | us-east-1 |

### 🪜 Passo a Passo Completo

#### 1️⃣ Acessar o Console do RDS

1. Vá em **Amazon RDS** → **Databases** (Bancos de Dados)
2. Localize sua instância: `challenge-node-777`
3. Clique na instância para ver os detalhes

#### 2️⃣ Confirmar a Versão do MySQL

1. Na página de detalhes da instância, verifique:
   - **Engine:** MySQL (não Aurora)
   - **Engine version:** Exemplo: `8.0.x`
2. **Anote a versão** - você precisará dela ao criar o Option Group

#### 3️⃣ Criar um Novo Option Group

1. No menu lateral esquerdo, clique em **Option groups**
2. Clique em **Create group**
3. Preencha os campos:

| Campo | Valor | Descrição |
|-------|-------|-----------|
| **Name** | `mysql-audit-logs` | Nome descritivo |
| **Engine** | `mysql` | Motor do banco |
| **Major engine version** | Selecione a mesma da sua instância (ex: `8.0`) | ⚠️ Deve ser compatível! |
| **Description** | `Habilitar MariaDB Audit Plugin` | Descrição do grupo |

4. Clique em **Create**

#### 4️⃣ Adicionar o Plugin de Auditoria (MariaDB Audit Plugin)

1. Na lista de Option Groups, selecione o grupo recém-criado (`mysql-audit-logs`)
2. Clique em **Add option**
3. Configure assim:

**Configurações Principais:**

| Campo | Valor | Descrição |
|-------|-------|-----------|
| **Option name** | `MARIADB_AUDIT_PLUGIN` | Plugin de auditoria |
| **Version** | Selecione a mais recente | - |
| **Apply immediately** | ✅ Marcar | Aplica sem aguardar janela de manutenção |

**Option Settings:**

Configure os seguintes parâmetros:

```
SERVER_AUDIT_EVENTS = CONNECT,QUERY
SERVER_AUDIT_FILE_ROTATIONS = 10
SERVER_AUDIT_FILE_ROTATE_SIZE = 1000000
SERVER_AUDIT_LOG_STREAM = ON
```

**Detalhamento dos parâmetros:**

| Parâmetro | Valor | Descrição |
|-----------|-------|-----------|
| `SERVER_AUDIT_EVENTS` | `CONNECT,QUERY` | Captura conexões e queries |
| `SERVER_AUDIT_FILE_ROTATIONS` | `10` | Quantidade de arquivos de rotação |
| `SERVER_AUDIT_FILE_ROTATE_SIZE` | `1000000` | Tamanho do arquivo antes de rotacionar (bytes) |
| `SERVER_AUDIT_LOG_STREAM` | `ON` | ⭐ **Crucial!** Envia logs para CloudWatch |

⚠️ **Importante:** A última linha (`SERVER_AUDIT_LOG_STREAM = ON`) é o que envia os logs para o CloudWatch!

4. Clique em **Add option**

#### 5️⃣ Vincular o Option Group à Instância RDS

1. Vá em **Databases** → `challenge-node-777`
2. Clique em **Modify**
3. Role até a seção **Database options**
4. Encontre **Option group**
5. Selecione o grupo que você acabou de criar: `mysql-audit-logs`
6. Role até o fim da página
7. Marque **Apply immediately** ✅
8. Clique em **Continue**
9. Revise as mudanças
10. Clique em **Modify DB Instance**

⏱️ **Aguarde:** A instância entrará em estado "modifying" e pode levar alguns minutos.

#### 6️⃣ Habilitar Exportação dos Audit Logs para o CloudWatch

Durante a configuração do plugin de auditoria, é necessário também habilitar a exportação explícita dos logs para o CloudWatch.

1. Se ainda não estiver na tela de Modify, vá em **Databases** → `challenge-node-777` → **Modify**
2. Role até a seção **Log exports**
3. Marque as seguintes opções:

| Log | Obrigatório | Descrição |
|-----|-------------|-----------|
| ☑ **Audit log** | ✅ **SIM** | Logs de auditoria |
| ☑ Error log | Opcional | Erros do MySQL |
| ☑ General log | Opcional | Log geral de queries |
| ☑ Slow query log | Opcional | Queries lentas |

4. Selecione **Apply immediately** ✅
5. **Continue** → **Modify DB Instance**

#### 7️⃣ Validar no CloudWatch Logs

Após a aplicação das mudanças:

1. Vá para **Amazon CloudWatch**
2. No menu lateral, clique em **Log groups**
3. Procure pelo grupo de logs:
   ```
   /aws/rds/instance/challenge-node-777/audit
   ```
4. Clique no log group
5. Você deve ver **log streams** sendo criados
6. Clique em um log stream para ver os eventos de auditoria

**Exemplo de log de auditoria:**
```
20231215 12:34:56,rdsadmin,localhost,1,2,QUERY,mysql,'SELECT 1'
20231215 12:35:01,jamrdsuser,10.0.1.50,2,3,CONNECT,audit,''
```

### ✅ Validação

Após completar todos os passos:

| Verificação | Status |
|-------------|--------|
| Option Group criado | ✅ |
| MariaDB Audit Plugin adicionado | ✅ |
| SERVER_AUDIT_LOG_STREAM = ON | ✅ |
| Option Group vinculado à instância | ✅ |
| Log exports → Audit log habilitado | ✅ |
| Log group criado no CloudWatch | ✅ |
| Log streams aparecendo | ✅ |
| Task "Check my progress" | ✅ **40 pontos** |

## 🏁 Conclusão

✅ **Task 1 completada com sucesso!**

Os logs de auditoria do RDS MySQL agora estão sendo enviados para o CloudWatch Logs e podem ser analisados para investigação de atividades suspeitas.

---

## 🔧 Troubleshooting

### Problema: Logs não aparecem no CloudWatch

**Possíveis causas:**
1. `SERVER_AUDIT_LOG_STREAM` não foi configurado como `ON`
2. Log exports → Audit log não foi marcado
3. Instância ainda está sendo modificada (aguarde)
4. Permissões IAM da instância RDS

**Soluções:**
```bash
# Verificar via AWS CLI se log exports está habilitado
aws rds describe-db-instances \
  --db-instance-identifier challenge-node-777 \
  --query 'DBInstances[0].EnabledCloudwatchLogsExports'

# Resultado esperado:
# [
#     "audit"
# ]
```

### Problema: Option Group não pode ser vinculado

**Erro comum:**
```
Option group 'mysql-audit-logs' cannot be associated with the DB instance.
```

**Causas possíveis:**
- Versão do engine não é compatível
- Option Group é para engine diferente
- Instância em estado não modificável

**Solução:**
1. Verifique que a versão do Option Group corresponde exatamente à versão da instância
2. Confirme que o engine é `mysql` (não `aurora-mysql`)
3. Aguarde se a instância estiver em modificação

### Problema: "Apply immediately" não funciona

**Nota:** Algumas mudanças em Option Groups requerem reinicialização da instância.

**Solução:**
- Aguarde a janela de manutenção automática, OU
- Force reinicialização manual:
  ```
  RDS → challenge-node-777 → Actions → Reboot
  ```

### Problema: Task não valida automaticamente

**Checklist:**
- [ ] Option Group contém MARIADB_AUDIT_PLUGIN
- [ ] SERVER_AUDIT_LOG_STREAM = ON está configurado
- [ ] Log exports → Audit log está marcado
- [ ] Log group `/aws/rds/instance/challenge-node-777/audit` existe
- [ ] Log streams estão aparecendo no CloudWatch
- [ ] Aguardou 5-10 minutos para propagação

## 📚 Conceitos Aprendidos

### **RDS Option Groups**
- Mecanismo para habilitar recursos adicionais no RDS
- Vinculados a versões específicas do engine
- Podem requerer reinicialização da instância

### **MariaDB Audit Plugin**
- Plugin de auditoria compatível com MySQL no RDS
- Alternativa ao Enterprise Audit Plugin (não disponível no RDS)
- Captura eventos de conexão e queries

### **CloudWatch Logs Integration**
- `SERVER_AUDIT_LOG_STREAM = ON` ativa streaming
- Log exports devem ser habilitados separadamente
- Logs aparecem em `/aws/rds/instance/<instance-name>/audit`

### **Eventos de Auditoria**
- **CONNECT:** Conexões e desconexões
- **QUERY:** Todas as queries executadas
- **TABLE:** Operações em tabelas específicas

## 🎯 Próximo Nível

Após completar esta task:
- Configure alertas no CloudWatch para atividades suspeitas
- Use CloudWatch Logs Insights para análise avançada
- Implemente retention policies para gerenciar custos
- Configure filtros para focar em eventos críticos

## 📖 Recursos Adicionais

- [RDS MySQL Audit Plugin](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MySQL.Options.AuditPlugin.html)
- [RDS Option Groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithOptionGroups.html)
- [Publishing Logs to CloudWatch](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.Concepts.MySQL.html)
