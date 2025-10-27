# Task 1: CONNECT SECURELY TO SOURCE SAP ASE DATABASE

## 📊 Informações da Tarefa
- **Pontos Possíveis:** 60
- **Penalidade por Dica:** 0
- **Pontos Disponíveis:** 60

## 🎯 Objetivo

Criar um endpoint DMS de origem para conectar-se ao banco de dados SAP ASE de forma segura usando certificado CA e AWS Secrets Manager.

## 📋 Contexto

Para migrar dados do SAP ASE para RDS for SQL Server, é necessário criar um endpoint de origem DMS. O banco de dados SAP ASE foi criado em uma instância Amazon EC2.

## 🎯 Sua Tarefa

Você deve criar um endpoint de origem DMS para conectar-se ao banco de dados SAP de forma segura usando **Certificado CA** e **AWS Secrets Manager**. Consulte os detalhes mencionados na seção Inventário abaixo.

> **⚠️ IMPORTANTE:** Teste a conexão assim que o endpoint estiver pronto!

### 📝 Nota Importante
Você pode ignorar com segurança a mensagem de erro abaixo durante a criação do endpoint de origem:

> **Erro esperado:** Pode aparecer uma mensagem de erro específica - ignore-a e prossiga com o teste de conexão.

## 🔧 Como Começar

1. Verifique a aba **Output Properties** na página inicial do JAM
2. Crie a conexão segura usando DMS
3. Clique em **Open AWS Console**
4. Navegue até **Database Migration Service**
5. Crie uma conexão segura usando **Endpoints**

## 📦 Inventário

Sua conta AWS foi provisionada com os seguintes recursos:

### 🌐 Infraestrutura
- **Amazon VPC:** VPC com nome `DMS-Jam-VPC` criada para este desafio
- **SAP ASE Server:** Instância Amazon EC2 onde reside o banco SAP ASE
  - Referência: `SAPEC2Instance` (output properties)
- **SAP ASE Database:** Para este desafio usaremos o banco `pubs2`

### 🔐 Segurança e Credenciais
- **CA Certificate:** Certificado emitido do on-prem para conexão SSL com SAP
  - **Download:** [Clique aqui para baixar o certificado](link-do-certificado)
- **AWS Secrets Manager:** ARN do Secrets Manager contendo propriedades de conexão do SAP
  - Referência: `SAPSecretManagerARN` (output properties)

### 🔑 Permissões e Instâncias
- **IAM Role:** Role IAM necessária para criar o endpoint
  - Referência: `DMSIAMRole` (output properties)
- **Replication Instance:** Instância de replicação para testar conexão do endpoint
  - Referência: `DMSReplicationInstanceName` (output properties)

## 🛠️ Serviços a Utilizar

- **AWS Database Migration Service**

## ✅ Validação da Tarefa

A tarefa será automaticamente concluída assim que você criar com sucesso o endpoint de origem DMS usando o Secrets Manager e Certificado CA. Alternativamente, você pode clicar em "Check my progress" para verificar a tarefa.

---

## 🧭 Passo a Passo Detalhado

### 📋 0️⃣ Preparação - Valores Necessários

**Obtenha estes valores do "Output Properties" do JAM:**

- **`SAPSecretManagerARN`** → ARN do segredo com host/porta/db/usuário/senha do SAP ASE
- **`DMSReplicationInstanceName`** → nome da replication instance
- **`DMSIAMRole`** → IAM Role para o endpoint
- **`SAPEC2Instance`** → EC2 onde roda o ASE (porta do listener — comum: 5000)
- **CA Certificate** → arquivo .pem (link "Click here to download the certificate")

> **💡 Nota:** O DMS usa `engine_name: sybase` para SAP ASE.

### 1️⃣ Importar o CA Certificate no DMS

#### Via Console AWS
1. Abra **AWS DMS** → **Certificates** → **Create certificate**
2. **Certificate identifier:** `sap-ase-onprem-ca`
3. **Import certificate** → faça upload do arquivo .pem fornecido
4. Clique em **Create**
5. **Guarde o Certificate ARN** gerado

#### Via CLI (Alternativa)
```bash
aws dms import-certificate \
  --certificate-identifier sap-ase-onprem-ca \
  --certificate-pem "file://./onprem-ca.pem"
```

### 2️⃣ Criar o Source Endpoint do SAP ASE

#### Via Console AWS (Recomendado)
1. **AWS DMS** → **Endpoints** → **Create endpoint**
2. **Endpoint type:** `Source`
3. **Endpoint identifier:** `src-sap-ase-pubs2`
4. **Source engine:** `SAP ASE (Sybase)`
5. **Access to endpoint database:** `Provide access information from AWS Secrets Manager`
6. **Secrets Manager ARN:** cole o valor de `SAPSecretManagerARN`
7. **Secrets Manager access role:** selecione o `DMSIAMRole` (ou informe o ARN)
8. **SSL settings:**
   - **SSL mode:** `verify-ca`
   - **CA certificate:** selecione `sap-ase-onprem-ca` (importado acima)
9. **Additional:**
   - **KMS key:** deixe o padrão do JAM (se aplicável)
   - **VPC:** automaticamente deve ser a `DMS-Jam-VPC`
10. Clique em **Create endpoint**

#### Via CLI (Alternativa)
```bash
# Descobrir ARN do certificado (se não anotou)
CERT_ARN=$(aws dms describe-certificates \
  --query "Certificates[?CertificateIdentifier=='sap-ase-onprem-ca'].CertificateArn" \
  --output text)

# Criar endpoint usando Secrets Manager + verify-ca
aws dms create-endpoint \
  --endpoint-identifier src-sap-ase-pubs2 \
  --endpoint-type source \
  --engine-name sybase \
  --secrets-manager-arn "<SAPSecretManagerARN>" \
  --secrets-manager-access-role-arn "<DMSIAMRole>" \
  --ssl-mode verify-ca \
  --certificate-arn "$CERT_ARN"
```

### 3️⃣ Testar a Conexão

#### Via Console AWS
1. Após criar o endpoint: **Actions** → **Test connection**
2. **Replication instance:** escolha `DMSReplicationInstanceName`
3. Clique **Run test** e aguarde status = `successful`

#### Via CLI (Alternativa)
```bash
# Pegar ARN do endpoint recém-criado
EP_ARN=$(aws dms describe-endpoints \
  --filters "Name=endpoint-id,Values=src-sap-ase-pubs2" \
  --query "Endpoints[0].EndpointArn" --output text)

# Testar conexão
aws dms test-connection \
  --replication-instance-arn "$(aws dms describe-replication-instances \
      --filters Name=replication-instance-id,Values=<DMSReplicationInstanceName> \
      --query 'ReplicationInstances[0].ReplicationInstanceArn' --output text)" \
  --endpoint-arn "$EP_ARN"

# Acompanhar status (opcional)
aws dms describe-connections \
  --filters Name=endpoint-arn,Values="$EP_ARN" \
  --query "Connections[0].Status"
```

---

## 🔍 Troubleshooting - Checklist Rápido

### 🌐 Networking
- [ ] A Replication Instance está na mesma VPC/subnet que o EC2 do ASE?
- [ ] Security Group do ASE permite inbound da SG da replication instance na porta do ASE (ex.: 5000)
- [ ] NACLs/Rotas permitem tráfego entre as subnets

### 🔐 Secrets Manager
- [ ] O segredo tem os campos corretos (host/port/database/username/password)
- [ ] O `DMSIAMRole` tem permissão `secretsmanager:GetSecretValue` no ARN do segredo

### 🔒 SSL/CA
- [ ] SslMode = `verify-ca` e certificate importado é o CA raiz/chain correto do "on-prem"
- [ ] Reimporte o .pem se o arquivo tiver espaços extras/encodings estranhos

### 🗄️ Engine/Database
- [ ] `engine_name = sybase` e Database = `pubs2` (conforme desafio)
- [ ] O ASE está ouvindo na porta esperada e aceita TDS/ct-lib remoto

---

## ✅ Conclusão e Validação

Com o endpoint criado e **Test connection = successful**, o JAM marca a Task 1 como concluída.

### 🎯 Próximos Passos
A partir daí, você já pode partir para as próximas tasks de migração:
- Mapeamento de tabelas
- Tarefas do DMS
- Criação de endpoints de destino

---

## 💡 Dicas Importantes

### 🔧 Configurações Críticas
- **SSL Mode:** Sempre use `verify-ca` para validação completa
- **Engine Name:** Use `sybase` para SAP ASE
- **Database:** Use `pubs2` conforme especificado
- **Secrets Manager:** Sempre use ARN completo do segredo

### ⚠️ Armadilhas Comuns
- **NÃO ignore** mensagens de erro de SSL/certificado
- **Verifique** se o certificado foi importado corretamente
- **Confirme** que a replication instance está na mesma VPC
- **Teste sempre** a conexão após criar o endpoint

### 🚀 Otimizações
- **Use Secrets Manager** em vez de credenciais hardcoded
- **Configure SSL** para criptografia em trânsito
- **Monitore logs** do DMS para troubleshooting
- **Valide certificados** antes da importação

---

## 🎉 Próximos Passos

Após completar esta tarefa, você estará pronto para a **Task 2: CREATE USER DATABASE AND TARGET ENDPOINT FOR RDS**, onde criará o banco de dados no RDS SQL Server e o endpoint de destino DMS.