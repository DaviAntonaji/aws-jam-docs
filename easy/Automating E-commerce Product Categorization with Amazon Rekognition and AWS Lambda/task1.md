# 📌 Task 1: Troubleshooting AWS Lambda Triggers for Automated E-commerce Image Categorization

## 🎯 Objetivo

Configurar e resolver problemas com triggers S3 para AWS Lambda em um sistema de categorização automática de produtos e-commerce.

## 🏗️ Contexto do Sistema

Sistema de categorização de produtos usando:

- **Amazon S3** - Upload de imagens de produtos
- **AWS Lambda** (`product-categorization-function`) - Processamento das imagens
- **Amazon Rekognition** - Classificação automática usando IA
- **Amazon DynamoDB** (`ProductCatalog`) - Armazenamento dos resultados

### ❌ Problema Identificado
Uploads no bucket **não disparavam o Lambda** automaticamente.

## 🛠️ Passos Realizados

### 1. Identificação do Bucket

#### Informações do Bucket
- **Nome**: `product-categorization-626380892899-ap-northeast-1`
- **Fonte**: Output Properties do lab
- **Região**: ap-northeast-1

#### Problema de Permissão
- Bucket **não aparecia listado** no console
- **Causa**: Falta de permissão `s3:ListAllMyBuckets`
- **Solução**: Acesso direto pelo nome/ARN

### 2. Acesso Direto ao Bucket

#### Métodos de Acesso
- **URL direta**: `https://s3.console.aws.amazon.com/s3/buckets/product-categorization-626380892899-ap-northeast-1`
- **Busca direta**: Usar nome exato no console
- **Navegação**: S3 → Buckets → [nome do bucket]

### 3. Configuração do Trigger

#### Localização
- **Caminho**: Bucket → Properties → Event notifications

#### Configuração do Evento
```yaml
Nome: invoke-product-categorization
Evento: All object create events
Destino: Lambda function → product-categorization-function
```

#### Passos Detalhados
1. Acessar **Properties** do bucket
2. Navegar para **Event notifications**
3. Clicar em **Create event notification**
4. Preencher configurações:
   - **Event name**: `invoke-product-categorization`
   - **Event types**: `All object create events`
   - **Destination**: `Lambda function`
   - **Function**: `product-categorization-function`

### 4. Teste e Validação

#### Upload de Teste
- **Arquivo**: `teste.jpg`
- **Local**: Bucket S3
- **Ação**: Upload via console

#### Verificação
- **CloudWatch Logs**: Confirmar execução do Lambda
- **Status**: Task marcada como concluída

## ⚠️ Observações Importantes

### Permissões Limitadas
- Mensagens de **"Insufficient permissions"** são esperadas no ambiente de lab
- **Seções afetadas**: Tags, Versioning, etc.
- **Impacto**: Nenhum na funcionalidade principal

### Pegadinha Principal
- **Problema**: Bucket não aparece na lista
- **Solução**: Acesso direto pelo nome/ARN
- **Dica**: Sempre verificar Output Properties do lab

## ✅ Resultado

- ✅ **Configuração corrigida**
- ✅ **Lambda invocado automaticamente** em novos uploads
- ✅ **Pipeline S3 → Lambda** funcionando
- ✅ **Task concluída** com sucesso

## 🔗 Próximos Passos

Com o trigger configurado, continue para a [Task 2](./task2.md) para resolver problemas de timeout e otimizar a função Lambda.