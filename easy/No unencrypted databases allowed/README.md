# No unencrypted databases allowed

## 📋 Visão Geral

Este desafio foca na **migração de criptografia** de bancos de dados RDS, abordando um cenário comum em ambientes de produção onde bancos existentes precisam ser criptografados para atender requisitos de segurança e compliance. O objetivo é migrar um banco MySQL não criptografado para uma versão criptografada sem perda de dados.

## 🎯 Objetivo

Migrar um banco de dados MySQL RDS **não criptografado** para uma versão **criptografada**, mantendo todos os dados e configurações, sem custos adicionais e seguindo as melhores práticas de segurança AWS.

## 🔧 Conceitos Principais

- **RDS Encryption** - Criptografia de dados em repouso e em trânsito
- **Database Snapshots** - Criação e gerenciamento de snapshots RDS
- **KMS Integration** - Integração com AWS Key Management Service
- **Migration Strategy** - Estratégia de migração via snapshots
- **Cost Optimization** - Manutenção de custos durante migração
- **Data Security** - Implementação de segurança em camadas

## 🏗️ Arquitetura

### Situação Inicial (Não Criptografada)
```
Application
    ↓
RDS MySQL Instance (db.t3.micro)
    ↓
Storage (Não Criptografado)
```

### Situação Final (Criptografada)
```
Application
    ↓
RDS MySQL Instance (db.t3.micro)
    ↓
Storage (Criptografado com KMS)
```

### Fluxo de Migração
```
Banco Original (Não Criptografado)
    ↓ (Snapshot)
Snapshot Não Criptografado
    ↓ (Copy com Encryption)
Snapshot Criptografado
    ↓ (Restore)
Nova Instância (Criptografada)
```

## 📚 Tarefas

### [Task 1: Database Encryption Migration](./task1.md)

**Objetivo:** Migrar banco MySQL não criptografado para versão criptografada

**Problema identificado:**
- Banco de dados MySQL RDS sem criptografia
- Necessidade de atender requisitos de segurança
- Impossibilidade de ativar criptografia em banco existente

**Conceitos abordados:**
- Criação e gerenciamento de snapshots RDS
- Cópia de snapshots com criptografia habilitada
- Restauração de instâncias a partir de snapshots criptografados
- Configuração de KMS keys para RDS
- Validação de criptografia e conectividade

## 🚀 Passo a Passo Resumido

### Task 1 - Migração de Criptografia
1. **Acessar RDS Console** - Localizar banco não criptografado
2. **Criar snapshot** - Backup do banco original
3. **Aguardar snapshot** - Status "Available" (10-15 min)
4. **Copiar snapshot** - Com criptografia habilitada
5. **Aguardar cópia** - Status "Available" (10-15 min)
6. **Restaurar instância** - Nova instância criptografada
7. **Validar migração** - Verificar criptografia e conectividade

## ⚠️ Pontos Importantes

### Limitações Técnicas
- **Não é possível** ativar criptografia em banco existente
- **Migração necessária** via snapshots
- **Tempo de processamento** - até 15 minutos por operação
- **Downtime** - Tempo de restauração necessário

### Requisitos de Negócio
- **Manter** todos os dados e configurações
- **Não remover** banco original (DevOps cuidará)
- **Manter** mesma classe de instância (db.t3.micro)
- **Não gerar** custos adicionais

### Configurações Críticas
- **DB instance class:** db.t3.micro (obrigatório)
- **VPC e Security Groups:** Mesmos do banco original
- **KMS key:** aws/rds (default) ou customizada
- **Storage encrypted:** Automaticamente habilitado

## 🔍 Solução Principal

### Estratégia: Snapshot + Restore
Como não é possível ativar criptografia diretamente em um banco existente, a estratégia é:

1. **Criar snapshot** do banco não criptografado
2. **Copiar snapshot** com criptografia habilitada
3. **Restaurar** nova instância a partir do snapshot criptografado

### Comandos de Validação
```bash
# Verificar status da instância original
aws rds describe-db-instances \
  --db-instance-identifier original-db-name

# Verificar snapshots
aws rds describe-db-snapshots \
  --db-snapshot-identifier unencrypted-db-snapshot

# Verificar nova instância
aws rds describe-db-instances \
  --db-instance-identifier encrypted-mysql-db
```

## 📊 Dificuldade e Tempo

**Dificuldade:** ⭐⭐☆☆☆  
**Tempo estimado:** 35-50 minutos

## 🎓 Lições Aprendidas

### Criptografia RDS
- **Não é possível** ativar em instâncias existentes
- **Migração via snapshot** é a abordagem padrão
- **KMS integration** é transparente
- **Performance impact** é mínimo

### Processo de Migração
- **Planejamento** é essencial para minimizar downtime
- **Testes** devem ser feitos em ambiente de desenvolvimento
- **Backup** sempre antes de mudanças críticas
- **Validação** é crucial após migração

### Best Practices
- **Sempre criptografar** novos bancos de dados
- **Use chaves KMS** customizadas para produção
- **Monitore** performance após migração
- **Documente** processo para futuras migrações

## 🔗 Recursos Adicionais

### Documentação AWS
- [RDS User Guide](https://docs.aws.amazon.com/rds/)
- [RDS Encryption](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html)
- [RDS Snapshots](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateSnapshot.html)
- [KMS for RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingKMS.html)

### Conceitos Relacionados
- [Database Security Best Practices](https://docs.aws.amazon.com/rds/latest/userguide/CHAP_BestPractices.Security.html)
- [RDS Backup and Restore](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_CommonTasks.BackupRestore.html)
- [VPC Security Groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

### Ferramentas Úteis
- [AWS CLI RDS Commands](https://docs.aws.amazon.com/cli/latest/reference/rds/)
- [RDS Pricing Calculator](https://aws.amazon.com/rds/pricing/)
- [CloudWatch for RDS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/rds-metricscollected.html)

## ✅ Critérios de Sucesso

### Task 1 - Database Encryption Migration
- [ ] Snapshot criado do banco original
- [ ] Snapshot copiado com criptografia habilitada
- [ ] Nova instância restaurada a partir do snapshot criptografado
- [ ] Storage encrypted configurado como "Yes"
- [ ] DB instance class mantida como db.t3.micro
- [ ] VPC e Security Groups mantidos
- [ ] Conectividade validada
- [ ] Validação no Jam marcada como "Completed"

## 🚨 Troubleshooting Comum

### Snapshot não é criado
- Verificar permissões IAM para RDS
- Confirmar que a instância está em estado "Available"
- Aguardar se a instância estiver em manutenção

### Cópia com criptografia falha
- Verificar se a região suporta criptografia
- Confirmar que a chave KMS existe
- Verificar permissões para a chave KMS

### Restauração falha
- Verificar se o subnet group existe
- Confirmar que os security groups são válidos
- Verificar se o nome da instância é único

### Performance após migração
- Monitorar métricas de CPU e memória
- Verificar latência de consultas
- Ajustar parâmetros se necessário

## 💡 Dicas de Otimização

### Segurança
- **KMS Keys:** Use chaves customizadas para maior controle
- **Access Control:** Configure IAM policies adequadas
- **Audit:** Habilite CloudTrail para auditoria
- **Backup:** Mantenha backups criptografados

### Performance
- **Impacto mínimo:** Criptografia usa hardware acceleration
- **Latência:** Aumento desprezível (< 1ms)
- **Throughput:** Mantido com criptografia
- **CPU:** Uso adicional mínimo

### Custos
- **Instância:** Mesmo custo (db.t3.micro)
- **Storage:** Sem custo adicional
- **KMS:** $1/mês por chave customizada
- **Data transfer:** Custos normais

## 🎯 Cenário de Negócio

### Contexto
Você é um **engenheiro AWS** e seu gerente solicitou que você criptografe o banco de dados MySQL existente. Ele entende que a criptografia não pode ser simplesmente ativada em um banco existente, então deixou para você descobrir como fazer isso.

### Desafio
- **Banco MySQL RDS** sem criptografia
- **Requisitos de segurança** e compliance
- **Impossibilidade** de ativar criptografia diretamente
- **Necessidade** de manter dados e configurações

### Solução
- **Migração via snapshots** para nova instância criptografada
- **Manutenção** de todas as configurações
- **Sem custos adicionais** - mesma classe de instância
- **Preservação** do banco original para DevOps

## 📊 Timeline Estimado

| Etapa | Tempo Estimado | Descrição |
|-------|----------------|-----------|
| **Snapshot Creation** | 10-15 min | Criar snapshot do banco original |
| **Snapshot Copy** | 10-15 min | Copiar com criptografia |
| **Instance Restore** | 10-15 min | Restaurar nova instância |
| **Validation** | 5 min | Verificar configurações |
| **Total** | **35-50 min** | Tempo total do processo |

---

**🎉 Boa sorte com o desafio!**

> **💭 Reflexão:** A migração de criptografia de banco de dados RDS demonstra a importância de planejamento em mudanças de segurança. Embora não seja possível ativar criptografia diretamente, o processo via snapshots é robusto e permite migração sem perda de dados, mantendo a continuidade do negócio.
