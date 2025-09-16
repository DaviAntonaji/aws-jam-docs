# 📌 Task 1: Criar Bucket S3

## 🎯 Objetivo

Criar um bucket Amazon S3 para ingestão de imagens e documentos que irão acionar automaticamente a função Lambda para processamento com Amazon Rekognition.

## 🛠️ Atividade Realizada

### Criação do Bucket S3

#### Configurações do Bucket
- **Nome**: `da-rekognition-16-09-2025-19-47`
- **Região**: `ap-southeast-2` (Sydney)
- **Data de criação**: 16/09/2025

#### Configurações de Segurança Mantidas
- ✅ **Block all public access**: Habilitado
- ✅ **ACLs desativadas**: Controle de acesso via IAM
- ✅ **Versioning**: Desligado (padrão)
- ✅ **Encryption**: Configurações padrão de segurança

## 🔧 Configurações Detalhadas

### Nomenclatura do Bucket
- **Convenção**: `da-rekognition-[data]-[hora]`
- **Unicidade**: Nome globalmente único
- **Identificação**: Fácil identificação do propósito

### Região Selecionada
- **ap-southeast-2**: Sydney, Austrália
- **Considerações**: Latência e compliance
- **Disponibilidade**: Serviços necessários disponíveis

### Configurações de Segurança
| Configuração | Status | Justificativa |
|--------------|--------|---------------|
| **Block all public access** | ✅ Habilitado | Previne acesso público acidental |
| **ACLs desativadas** | ✅ Desativadas | Controle via IAM policies |
| **Versioning** | ❌ Desligado | Padrão para este uso caso |
| **Encryption** | ✅ Padrão | Criptografia automática |

## 🏗️ Propósito do Bucket

### Função Principal
- **Ingestão**: Receber imagens e documentos
- **Trigger**: Acionar função Lambda automaticamente
- **Processamento**: Servir como origem para Amazon Rekognition

### Integração com Lambda
- **Event-driven**: Upload dispara processamento
- **Serverless**: Sem gerenciamento de infraestrutura
- **Automático**: Processamento imediato após upload

## ✅ Resultado Esperado

### Bucket Criado com Sucesso
- ✅ **Bucket S3** configurado e operacional
- ✅ **Configurações de segurança** aplicadas
- ✅ **Pronto para integração** com AWS Lambda
- ✅ **Preparado para Task 2** (conexão com Lambda)

### Próximos Passos
- **Task 2**: Configurar evento de notificação S3
- **Integração**: Conectar bucket com função Lambda
- **Teste**: Validar processamento automático

## 🔗 Próximos Passos

Com o bucket S3 criado, continue para a [Task 2](./task2.md) para configurar a integração com AWS Lambda e testar o processamento automático de imagens.