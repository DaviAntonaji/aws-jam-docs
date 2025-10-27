# Put Security Manager on duty!

## 📋 Visão Geral

Este desafio AWS Jam foca na **migração segura de dados** de SAP ASE (Sybase) para Amazon RDS for SQL Server, implementando **criptografia end-to-end** e **certificados CA** durante todo o processo de migração. O objetivo é garantir a segurança máxima durante a transição de um sistema crítico de 25 anos.

## 🎯 Objetivos do Desafio

- Migrar dados de SAP ASE para RDS SQL Server com segurança máxima
- Implementar conexões SSL/TLS com certificados CA
- Configurar AWS Secrets Manager para credenciais seguras
- Criar endpoints DMS com criptografia end-to-end
- Resolver problemas de autorização IAM e KMS
- Garantir integridade e segurança dos dados durante migração

## 🏗️ Arquitetura

```
[SAP ASE on EC2] 
        ↓ (SSL + CA Certificate)
[DMS Source Endpoint] 
        ↓ (Encrypted Migration)
[DMS Target Endpoint] 
        ↓ (SSL + Secrets Manager)
[RDS SQL Server]
```

## 📚 Estrutura do Desafio

### Task 1: CONNECT SECURELY TO SOURCE SAP ASE DATABASE - 60 pontos
- **Objetivo**: Criar endpoint DMS de origem conectando-se ao SAP ASE com SSL e certificado CA
- **Serviços**: AWS DMS, AWS Secrets Manager, IAM, KMS
- **Foco**: Configuração segura de conexão com certificados e secrets

### Task 2: CREATE USER DATABASE AND TARGET ENDPOINT FOR RDS - 30 pontos  
- **Objetivo**: Criar banco de dados no RDS SQL Server e endpoint DMS de destino
- **Serviços**: AWS Step Functions, AWS DMS, AWS Secrets Manager, IAM, KMS
- **Foco**: Automação via Step Functions e resolução de problemas de autorização

### Task 3: [Em desenvolvimento]
- **Status**: ⚠️ **NÃO COMPLETO AINDA**
- **Nota**: Esta tarefa será implementada em breve

## 🔧 Componentes Principais

### AWS Database Migration Service (DMS)
- **Source Endpoint**: Conexão segura com SAP ASE usando SSL + CA Certificate
- **Target Endpoint**: Conexão com RDS SQL Server usando Secrets Manager
- **Replication Instance**: Instância para testar conexões e migração

### AWS Secrets Manager
- **SAP Secrets**: Credenciais do SAP ASE (host, porta, usuário, senha)
- **RDS Secrets**: Credenciais do RDS SQL Server
- **KMS Encryption**: Criptografia com chaves gerenciadas pelo cliente

### AWS Step Functions
- **Database Creation**: Automação da criação do banco `pubs2` no RDS
- **IAM Integration**: Execução com roles específicas e resolução de permissões

### Segurança e Certificados
- **CA Certificate**: Certificado de autoridade certificadora para SSL
- **SSL Mode**: `verify-ca` para validação completa de certificados
- **End-to-End Encryption**: Criptografia em trânsito e em repouso

## 📝 Status do Desafio

- ✅ **Task 1**: Conexão segura SAP ASE - **COMPLETO**
- ⚠️ **Task 2**: Criação de banco e endpoint destino - **EM PROGRESSO** (problemas de KMS)
- ⚠️ **Task 3**: **EM DESENVOLVIMENTO** - Retornará em breve

## 🚨 Problemas Identificados

### Task 2 - Problemas de Autorização KMS
- **Problema**: Lambda não consegue desencriptar segredo devido a permissões KMS
- **Causa**: Key policy da CMK não autoriza a execution role da Lambda
- **Status**: Requer acesso administrativo para editar key policy ou usar chave gerenciada AWS

### Soluções Tentadas
- ✅ Adicionado `lambda:InvokeFunction` à role do Step Functions
- ✅ Adicionado `secretsmanager:GetSecretValue` à role da Lambda
- ✅ Adicionado `kms:Decrypt` à role da Lambda
- ❌ **Bloqueio**: Usuário do lab não tem `access-analyzer:ValidatePolicy`

## 🚀 Próximos Passos

Este desafio está em desenvolvimento ativo. A Task 1 foi concluída com sucesso, estabelecendo a conexão segura com SAP ASE. A Task 2 está parcialmente implementada, mas requer resolução de problemas de permissões KMS para conclusão completa.

### Resolução Recomendada para Task 2:
1. **Editar key policy** da CMK para incluir a execution role da Lambda
2. **Usar chave gerenciada AWS** (`aws/secretsmanager`) em vez de CMK
3. **Criar novo segredo** com chave gerenciada AWS e reexecutar Step Function

---

**Nota**: Este desafio faz parte da coleção AWS Jam Challenges e está sendo desenvolvido progressivamente. Volte em breve para ver a implementação completa das Tasks 2 e 3!