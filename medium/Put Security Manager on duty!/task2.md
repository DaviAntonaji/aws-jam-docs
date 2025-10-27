# Task 2: CREATE USER DATABASE AND TARGET ENDPOINT FOR RDS

## 📊 Informações da Tarefa
- **Pontos Possíveis:** 30
- **Penalidade por Dica:** 0
- **Pontos Disponíveis:** 30

## 🎯 Objetivo

Criar um banco de dados de usuário (`pubs2`) na instância RDS for SQL Server e um endpoint DMS de destino para migrar dados do banco SAP ASE.

## 📋 Contexto

Nesta tarefa, um banco de dados de usuário (`pubs2`) sob a instância RDS for SQL Server e um endpoint DMS de destino precisam ser criados. Uma AWS Step Function está disponível para criar o banco de dados de usuário, mas falhará com problema de autorização. Você pode corrigir este problema adicionando a política necessária na role IAM.

## 🎯 Sua Tarefa

Você deve primeiro criar um banco de dados de usuário sob a instância RDS for SQL Server executando a Step Function e depois criar o endpoint DMS de destino para migrar os dados do banco SAP ASE.

> **⚠️ IMPORTANTE:** Certifique-se de que a conexão seja bem-sucedida!

## 🔧 Como Começar

1. Verifique a aba **Output Properties** na página inicial do JAM
2. Crie a conexão segura usando DMS
3. Clique em **Open AWS Console**
4. Navegue até **Step Functions**
5. Execute a Step Function e corrija o problema de autorização

### 📝 Input JSON para Step Function

Forneça o valor JSON abaixo no input (opcional, substitua os valores de "replace-it-with-the-value-of-RDSSecretManagerARN" pelo valor de `RDSSecretManagerARN` da seção output properties da página inicial do Jam):

```json
{ 
    "RDSSecretManagerARN": "replace-it-with-the-value-of-RDSSecretManagerARN",
    "DB_NAME": "pubs2"
}
```

## 📦 Inventário

Sua conta AWS foi provisionada com os seguintes recursos:

### 🗄️ Banco de Dados e Migração
- **RDS for SQL Server endpoint:** Identificador da instância do banco SQL Server
  - Referência: `RDSSQLServerEndpoint` (output properties)
- **Step Function:** Nome da Step Function para criar banco de dados de usuário para SQL Server
  - Referência: `StepFunctionRDSCreateDB` (output properties)

### 🔐 Segurança e Credenciais
- **IAM Role:** Role IAM necessária para criar o endpoint
  - Referência: `DMSIAMRole` (output properties)
- **AWS Secrets Manager for RDS SQL Server:** ARN do Secret Manager contendo propriedades de conexão do RDS
  - Referência: `RDSSecretManagerARN` (output properties)

### 📋 Recursos da Task Anterior
Consulte o Inventário da tarefa anterior para detalhes de IAM Role, ReplicationInstance e VPC necessários para criar o endpoint de destino.

## 🛠️ Serviços a Utilizar

- **AWS Step Functions**
- **AWS Database Migration Service**

## ✅ Validação da Tarefa

A tarefa será automaticamente concluída assim que você criar com sucesso o endpoint DMS de destino usando o Secret Manager com um banco de dados de usuário.

---

## 🧭 Passo a Passo Detalhado

### 🎯 Objetivo da Task 2

Executar o Step Function `StepFunctionRDSCreateDB` para criar o banco `pubs2` dentro do RDS for SQL Server, e em seguida criar um DMS target endpoint usando o segredo `RDSSecretManagerARN`.

### 🧠 Contexto Inicial

O Step Function falha por falta de permissões IAM na role de execução. A state machine chama uma Lambda interna que lê o segredo do RDS no Secrets Manager e cria o database.

### 🪜 Etapas Executadas

#### 1️⃣ Permitir Execução da Lambda pelo Step Functions

**Sintoma inicial:**
```
AccessDeniedException: is not authorized to perform: lambda:InvokeFunction ...
```

**Ações realizadas:**
- Incluímos `lambda:InvokeFunction` na inline policy da execution role do Step Functions
- Também adicionamos uma resource-based policy na Lambda (tentar pelo console → bloqueada pelo Access Analyzer)
- Ajustamos permissões considerando possível permissions boundary

**Resultado:**
- ✅ **Erro mudou:** o Step Functions passou a conseguir invocar a Lambda
- ❌ **Novo erro de KMS** (próxima etapa)

#### 2️⃣ Corrigir Acesso da Lambda ao Segredo do RDS (Secrets Manager + KMS)

**Novo sintoma:**
```
An error occurred (AccessDeniedException) when calling the GetSecretValue operation:
Access to KMS is not allowed
```

**Ações realizadas:**
- Adicionamos `secretsmanager:GetSecretValue` e `kms:Decrypt` na execution role da Lambda
- Condition para restringir ao segredo correto via Secrets Manager
- Verificamos se existia permissions boundary na role da Lambda
- Tentamos inserir a role como Key user na chave KMS que criptografa o segredo
- Tentamos adicionar manualmente um bloco JSON na key policy permitindo `kms:Decrypt` para a role da Lambda

**Problema encontrado:**
- O console bloqueou a edição JSON devido à falta de permissão `access-analyzer:ValidatePolicy`
- Usuário do lab não possui esta permissão

**Resultado:**
- ✅ **Mudança de erro:** indica que a Lambda passou a ser invocada corretamente e está chamando o Secrets Manager
- ❌ **Ainda falta acesso** da Lambda à CMK que cifra o segredo

---

## 🧭 Situação Atual

### ✅ O que Funcionou
| Etapa | Ação | Efeito |
|-------|------|--------|
| 1 | Adicionar `lambda:InvokeFunction` à role do Step Functions | Step Function passou a invocar a Lambda |
| 2 | Confirmar execution role da Lambda e dar `secretsmanager:GetSecretValue` | Lambda passou a chamar o Secrets Manager |
| 3 | Adicionar `kms:Decrypt` na role da Lambda | Mensagem de erro mudou (confirmando que o problema é o KMS) |

### ❌ O que Ainda Impede a Conclusão
| Problema | Causa Provável | Solução Necessária |
|----------|----------------|-------------------|
| Access to KMS is not allowed | A KMS key usada no segredo não autoriza a execution role da Lambda | Editar a key policy da CMK para incluir a role da Lambda como Key user |
| Falta de permissão `access-analyzer:ValidatePolicy` | O usuário de laboratório (AWS Labs) não tem permissão para editar policies JSON diretamente | Necessário acesso administrativo ou usar a tela "Key users" do KMS |

---

## 💡 Próximos Passos Recomendados

### 🔧 Soluções Possíveis

#### Opção 1: Editar Key Policy da CMK
1. **Editar a key policy** ou Key users da CMK para incluir a execution role da Lambda
2. **Adicionar a role** como Key user com permissões `kms:Decrypt`

#### Opção 2: Usar Chave Gerenciada AWS
1. **Se o lab não permitir** editar key policy, criar um novo segredo com a chave gerenciada pela AWS (`aws/secretsmanager`)
2. **Repetir a execução** do Step Function com o novo segredo

### 🚀 Após Execução Bem-Sucedida

1. **Step Function executada** com sucesso (database `pubs2` criado)
2. **Criar o DMS target endpoint** para o RDS usando o segredo
3. **Testar a conexão** na mesma replication instance da Task 1

---

## 🧾 Resumo Final

### ✅ Problemas Resolvidos
- **Problema original:** Step Function não autorizado a invocar Lambda → **RESOLVIDO**
- **Comunicação:** Step Functions e Lambda comunicam-se corretamente

### ⚠️ Estado Atual
- **Lambda executa**, mas não consegue desencriptar segredo
- **Problema isolado:** acesso KMS (key policy)
- **Limitação do lab:** usuário não tem privilégio para editar KMS key

### 🎯 Próximas Ações Necessárias
1. **Dar `kms:Decrypt`** à execution role da Lambda via Key policy / Key users
2. **OU usar segredo** com chave gerenciada AWS (`aws/secretsmanager`)
3. **Criar novo segredo** com chave gerenciada AWS e reexecutar Step Function

---

## 🔍 Troubleshooting Detalhado

### 🔐 Problemas de KMS
- **Sintoma:** "Access to KMS is not allowed"
- **Causa:** Key policy da CMK não autoriza a execution role da Lambda
- **Solução:** Editar key policy ou usar chave gerenciada AWS

### 🛡️ Problemas de Permissões
- **Sintoma:** "access-analyzer:ValidatePolicy" não permitido
- **Causa:** Usuário do lab não tem permissões administrativas
- **Solução:** Usar interface "Key users" ou criar novo segredo

### 🔄 Workflow de Resolução
1. **Identificar** a CMK que criptografa o segredo
2. **Verificar** key policy atual
3. **Adicionar** execution role da Lambda como Key user
4. **Testar** execução do Step Function
5. **Criar** DMS target endpoint após sucesso

---

## 🎉 Próximos Passos

Após resolver os problemas de KMS e completar esta tarefa, você terá:
- ✅ **Banco `pubs2`** criado no RDS SQL Server
- ✅ **DMS target endpoint** configurado
- ✅ **Conexão testada** e validada
- ✅ **Base preparada** para migração de dados

**Status do desafio:**
- ✅ **Task 1:** Conexão segura SAP ASE - COMPLETO
- ⚠️ **Task 2:** Criação de banco e endpoint destino - EM PROGRESSO (problemas KMS)
- ⚠️ **Task 3:** Em desenvolvimento futuro