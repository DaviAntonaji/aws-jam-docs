# Task 1: Database Encryption Migration

## 🎯 Objetivo

Migrar um banco de dados MySQL RDS **não criptografado** para uma versão **criptografada**, mantendo todos os dados e configurações, sem custos adicionais e seguindo as melhores práticas de segurança AWS.

## 📊 Cenário

### Situação Inicial
Como **engenheiro AWS**, seu gerente solicitou que você criptografe o banco de dados MySQL existente. Ele entende que a criptografia não pode ser simplesmente ativada em um banco existente, então deixou para você descobrir como fazer isso.

### Requisitos do Negócio
- ✅ **Criptografar** o banco de dados MySQL existente
- ✅ **Manter** todos os dados e configurações
- ✅ **Não remover** o banco original (DevOps cuidará disso)
- ✅ **Manter** a mesma classe de instância (db.t3.micro)
- ✅ **Não gerar** custos adicionais

### Limitações Técnicas
- ❌ **Não é possível** ativar criptografia em banco existente
- ❌ **Migração necessária** via snapshots
- ⏱️ **Tempo de processamento** - até 15 minutos por operação

## 🔍 Estratégia de Migração

### Abordagem: Snapshot + Restore
Como não é possível ativar criptografia diretamente em um banco existente, a estratégia é:

1. **Criar snapshot** do banco não criptografado
2. **Copiar snapshot** com criptografia habilitada
3. **Restaurar** nova instância a partir do snapshot criptografado

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

## 🚀 Implementação Passo a Passo

### 1. Acessar RDS Console

#### Navegação Inicial
1. **Abrir AWS Console**
2. **Navegar para** RDS → Databases
3. **Localizar** o banco de dados MySQL não criptografado
4. **Anotar** configurações importantes:
   - Instance class (deve ser db.t3.micro)
   - VPC e Security Groups
   - Região AWS

### 2. Criar Snapshot Manual

#### Configuração do Snapshot
1. **Selecionar** o banco de dados não criptografado
2. **Clicar** Actions → Take snapshot
3. **Configurar** o snapshot:
   - **Snapshot name:** `unencrypted-db-snapshot`
   - **Description:** `Snapshot before encryption migration`
4. **Clicar** "Create snapshot"

#### Via AWS CLI
```bash
# Criar snapshot manual
aws rds create-db-snapshot \
  --db-instance-identifier your-db-instance \
  --db-snapshot-identifier unencrypted-db-snapshot
```

### 3. Aguardar Criação do Snapshot

#### Monitoramento
1. **Navegar para** RDS → Snapshots
2. **Localizar** o snapshot criado
3. **Aguardar** status mudar para "Available"
4. **Tempo estimado:** 10-15 minutos

#### Verificação
```bash
# Verificar status do snapshot
aws rds describe-db-snapshots \
  --db-snapshot-identifier unencrypted-db-snapshot \
  --query 'DBSnapshots[0].Status'
```

### 4. Copiar Snapshot com Criptografia

#### Configuração da Cópia
1. **Selecionar** o snapshot não criptografado
2. **Clicar** Actions → Copy snapshot
3. **Configurar** a cópia:
   - **Destination region:** Mesma região atual
   - **New DB snapshot identifier:** `encrypted-db-snapshot`
   - **Encryption:** ✅ Enable encryption
   - **KMS key:** `aws/rds` (default) ou chave customizada
4. **Clicar** "Copy snapshot"

#### Via AWS CLI
```bash
# Copiar snapshot com criptografia
aws rds copy-db-snapshot \
  --source-db-snapshot-identifier unencrypted-db-snapshot \
  --target-db-snapshot-identifier encrypted-db-snapshot \
  --kms-key-id aws/rds
```

### 5. Aguardar Cópia Criptografada

#### Monitoramento
1. **Aguardar** status "Available" do snapshot criptografado
2. **Tempo estimado:** 10-15 minutos
3. **Verificar** que o snapshot tem criptografia habilitada

### 6. Restaurar Nova Instância

#### Configuração da Restauração
1. **Selecionar** o snapshot criptografado
2. **Clicar** Actions → Restore snapshot
3. **Configurar** a nova instância:

#### Configurações Obrigatórias
- **DB instance identifier:** `encrypted-mysql-db` (ou nome único)
- **DB instance class:** `db.t3.micro` (obrigatório)
- **VPC:** Mesma VPC do banco original
- **Security Groups:** Mesmos security groups
- **Storage encrypted:** ✅ Automaticamente habilitado

#### Configurações Adicionais
- **DB name:** Mesmo nome do banco original
- **Master username:** Mesmo usuário
- **Master password:** Nova senha (recomendado)
- **Backup retention:** 7 dias (padrão)
- **Monitoring:** Habilitar Enhanced monitoring (opcional)

#### Via AWS CLI
```bash
# Restaurar instância a partir do snapshot criptografado
aws rds restore-db-instance-from-db-snapshot \
  --db-instance-identifier encrypted-mysql-db \
  --db-snapshot-identifier encrypted-db-snapshot \
  --db-instance-class db.t3.micro \
  --vpc-security-group-ids sg-xxxxxxxxx \
  --db-subnet-group-name your-subnet-group
```

### 7. Validação Final

#### Verificações Necessárias
1. **Nova instância** aparece em RDS → Databases
2. **Status** deve ser "Available"
3. **Storage encrypted:** ✅ Yes
4. **DB instance class:** db.t3.micro
5. **VPC e Security Groups:** Mesmos do original

#### Teste de Conectividade
```bash
# Testar conectividade com a nova instância
mysql -h encrypted-mysql-db.xxxxxxxxx.region.rds.amazonaws.com \
  -u username -p database_name
```

## ✅ Resultado

### Migração Concluída
- ✅ **Nova instância** MySQL RDS criptografada criada
- ✅ **Todos os dados** migrados com sucesso
- ✅ **Configurações** mantidas (VPC, Security Groups)
- ✅ **Custo** mantido (mesma classe db.t3.micro)
- ✅ **Banco original** preservado para DevOps

### Validação no Jam
1. **Voltar ao painel** do challenge
2. **Clicar** "Check my progress"
3. **Task 1** marcada como **Completed** ✅

## 🔍 Detalhes Técnicos

### Criptografia RDS
- **Encryption at rest:** Dados criptografados no storage
- **Encryption in transit:** SSL/TLS para conexões
- **KMS integration:** Chaves gerenciadas pela AWS
- **Performance impact:** Mínimo (hardware acceleration)

### Tipos de Criptografia
| Tipo | Descrição | Status |
|------|-----------|--------|
| **Storage Encryption** | Dados em disco | ✅ Habilitado |
| **Encryption in Transit** | Conexões SSL/TLS | ✅ Habilitado |
| **KMS Key** | Chave de criptografia | ✅ aws/rds ou customizada |

### Configuração de Storage
```json
{
  "StorageEncrypted": true,
  "KmsKeyId": "arn:aws:kms:region:account:key/aws/rds",
  "StorageType": "gp2",
  "AllocatedStorage": 20,
  "MaxAllocatedStorage": 100
}
```

## 🚨 Troubleshooting

### Problemas Comuns

#### Snapshot não é criado
- **Verificar permissões** IAM para RDS
- **Confirmar** que a instância está em estado "Available"
- **Aguardar** se a instância estiver em manutenção

#### Cópia com criptografia falha
- **Verificar** se a região suporta criptografia
- **Confirmar** que a chave KMS existe
- **Verificar** permissões para a chave KMS

#### Restauração falha
- **Verificar** se o subnet group existe
- **Confirmar** que os security groups são válidos
- **Verificar** se o nome da instância é único

### Comandos de Diagnóstico
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

## 💡 Considerações Importantes

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

### Limitações
- **Não reversível:** Não é possível desabilitar criptografia
- **Snapshot dependency:** Requer snapshot para migração
- **Downtime:** Tempo de restauração necessário
- **Cross-region:** Limitações para cópia entre regiões

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

## 📊 Timeline Estimado

| Etapa | Tempo Estimado | Descrição |
|-------|----------------|-----------|
| **Snapshot Creation** | 10-15 min | Criar snapshot do banco original |
| **Snapshot Copy** | 10-15 min | Copiar com criptografia |
| **Instance Restore** | 10-15 min | Restaurar nova instância |
| **Validation** | 5 min | Verificar configurações |
| **Total** | **35-50 min** | Tempo total do processo |

---

**🎉 Task 1 Concluída!**

> **💭 Reflexão:** A migração de criptografia de banco de dados RDS demonstra a importância de planejamento em mudanças de segurança. Embora não seja possível ativar criptografia diretamente, o processo via snapshots é robusto e permite migração sem perda de dados, mantendo a continuidade do negócio.
