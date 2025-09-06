# Trace with AWS Lambda Powertools 📊

## 📋 Visão Geral

Este projeto implementa observabilidade avançada em funções AWS Lambda usando AWS Lambda Powertools e X-Ray para rastreamento distribuído. O objetivo é demonstrar como instrumentar aplicações serverless para obter visibilidade completa do fluxo de execução, identificação de gargalos e debugging eficiente.

## 🎯 Objetivos

- **Implementar** tracing distribuído com AWS X-Ray
- **Instrumentar** funções Lambda com Powertools
- **Criar** subsegmentos para operações DynamoDB
- **Demonstrar** observabilidade completa de aplicações serverless
- **Facilitar** debugging e otimização de performance

## 🏗️ Arquitetura

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   AWS Lambda    │────│   AWS X-Ray      │────│   DynamoDB      │
│   (GetUser)     │    │   (Tracing)      │    │   (Users Table) │
│                 │    │                  │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                       │                       │
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Lambda Powertools│    │   CloudWatch     │    │   IAM Roles     │
│   (Instrumentation)│    │   (Logs)        │    │   (Permissions) │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## 📁 Estrutura do Projeto

```
Trace with AWS Lambda Powertools/
├── README.md              # Este arquivo
├── task-1.md              # Task 1: Executar função Lambda
├── task2.md               # Task 2: Ativar X-Ray tracing
├── task3.md               # Task 3: Instrumentar com Powertools
└── lambda.py              # Código da função Lambda
```

## 🚀 Tasks Implementadas

### Task 1: Executar Função Lambda
**Objetivo:** Executar a função Lambda `GetUser` e capturar o secret retornado

**Funcionalidades:**
- ✅ Configuração de evento de teste
- ✅ Execução da função Lambda
- ✅ Captura do secret do response
- ✅ Validação via console AWS

**Comando de teste:**
```bash
aws lambda invoke \
  --region us-east-1 \
  --function-name GetUser \
  --payload '{}' \
  response.json
```

### Task 2: Ativar X-Ray Tracing
**Objetivo:** Ativar o AWS X-Ray tracing na função Lambda e capturar Trace ID

**Funcionalidades:**
- ✅ Ativação do Active tracing
- ✅ Configuração de permissões IAM
- ✅ Execução de teste com tracing
- ✅ Captura do Trace ID

**Configuração:**
- **Console:** Configuration → Monitoring and operations tools → AWS X-Ray → Active tracing (ON)
- **Permissão:** `AWSXRayDaemonWriteAccess`

### Task 3: Instrumentar com Powertools
**Objetivo:** Instrumentar a função Lambda com AWS Lambda Powertools para traces detalhados

**Funcionalidades:**
- ✅ Adição do Lambda Powertools layer
- ✅ Configuração de variáveis de ambiente
- ✅ Instrumentação do código com Tracer
- ✅ Criação de subsegmentos para DynamoDB
- ✅ Subsegmentos customizados para código

**Configuração:**
```bash
# Variáveis de ambiente
POWERTOOLS_SERVICE_NAME=jam
POWERTOOLS_LOG_LEVEL=INFO
POWERTOOLS_TRACER_CAPTURE_RESPONSE=false
```

## 🔧 Componentes Técnicos

### Lambda Function (`lambda.py`)
- **Runtime:** Python 3.11/3.12
- **Dependências:** AWS Lambda Powertools, boto3
- **Instrumentação:** Tracer, patch_all()
- **Operações:** DynamoDB GetItem

### AWS Lambda Powertools
- **Tracer:** Criação de segmentos e subsegmentos
- **Auto-instrumentation:** patch_all() para boto3
- **Service naming:** Via variável de ambiente
- **Error handling:** Captura automática de erros

### AWS X-Ray
- **Tracing:** Rastreamento distribuído
- **Segments:** Segmentos de função Lambda
- **Subsegments:** Operações DynamoDB e código customizado
- **Service map:** Visualização de dependências

## 🛠️ Configuração e Deploy

### Pré-requisitos
- Account ID e Region do AWS JAM
- Função Lambda `GetUser` acessível
- Permissões para modificar configurações
- Tabela DynamoDB `Users` (ou similar)

### Passos de Deploy
1. **Ativar X-Ray tracing** na função Lambda
2. **Adicionar Lambda Powertools layer**
3. **Configurar variáveis de ambiente**
4. **Instrumentar código** com Tracer
5. **Deploy e testar** funcionalidades

### Layers Necessários
- **Python:** `AWSLambdaPowertoolsPythonV2`
- **Node.js:** `AWSLambdaPowertoolsTypeScript`

## 📊 Resultados e Benefícios

### ✅ Funcionalidades Implementadas
- **Tracing automático** com AWS X-Ray
- **Instrumentação** com Lambda Powertools
- **Subsegmentos** para operações DynamoDB
- **Observabilidade** completa de aplicações serverless
- **Debugging eficiente** com traces detalhados

### 🎯 Benefícios Alcançados
- **Visibilidade completa** do fluxo de execução
- **Identificação rápida** de gargalos de performance
- **Debugging eficiente** de aplicações distribuídas
- **Métricas detalhadas** de latência e throughput
- **Monitoramento proativo** de erros e exceções

## 🔍 Observabilidade Implementada

### X-Ray Traces
- **Lambda Handler** - Segmento principal da função
- **DynamoDB Operations** - Subsegmentos automáticos
- **Custom Code** - Subsegmentos manuais (GetUserById)
- **Error Tracking** - Captura automática de erros
- **Performance Metrics** - Latência e throughput

### CloudWatch Integration
- **Structured Logging** - Logs estruturados com Powertools
- **Correlation IDs** - Rastreamento entre serviços
- **Custom Metrics** - Métricas de negócio
- **Alarms** - Alertas proativos

## 🎯 Checklist de Validação

**O que o avaliador vai ver no X-Ray:**

- ✅ **Service name = jam** (vem do `POWERTOOLS_SERVICE_NAME`)
- ✅ **Trace inclui Lambda Handler** (segmento criado pelo Powertools)
- ✅ **Trace inclui DynamoDB API call** (subsegmento `AWS::DynamoDB::GetItem`)
- ✅ **Subsegmento do código** (ex.: `GetUserById`) - opcional, mas recomendado

## 🔍 Troubleshooting

| Problema | Solução |
|----------|---------|
| **Active tracing não aparece** | Verificar se está na aba Configuration correta |
| **Erro de permissão** | Aceitar a sugestão de anexar AWSXRayDaemonWriteAccess |
| **Layer não encontrado** | Verificar região e versão do runtime |
| **Service name não aparece** | Verificar variável `POWERTOOLS_SERVICE_NAME` |
| **Subsegmentos não aparecem** | Verificar se `patch_all()` foi chamado |
| **Trace ID não muda** | Aguardar alguns segundos e executar novo teste |

## 📚 Recursos Adicionais

### Documentação Oficial
- [AWS Lambda Powertools](https://awslabs.github.io/aws-lambda-powertools-python/)
- [AWS X-Ray](https://docs.aws.amazon.com/xray/)
- [AWS Lambda](https://docs.aws.amazon.com/lambda/)
- [Amazon DynamoDB](https://docs.aws.amazon.com/dynamodb/)

### Conceitos Importantes
- **Distributed Tracing** - Rastreamento distribuído
- **Observability** - Observabilidade de aplicações
- **Serverless Monitoring** - Monitoramento serverless
- **Performance Optimization** - Otimização de performance

## 🏆 Dicas para Competições

### Preparação
- ✅ **Conheça** AWS X-Ray e Lambda Powertools
- ✅ **Pratique** com instrumentação de código
- ✅ **Entenda** conceitos de observabilidade
- ✅ **Familiarize-se** com CloudWatch e X-Ray console

### Durante a Competição
- ⚡ **Ative** X-Ray tracing primeiro
- ⚡ **Adicione** Lambda Powertools layer
- ⚡ **Configure** variáveis de ambiente
- ⚡ **Instrumente** código com Tracer
- ⚡ **Teste** e valide traces no X-Ray

### Tempo Estimado
- **Task 1**: ~10 minutos
- **Task 2**: ~15 minutos  
- **Task 3**: ~20 minutos
- **Total**: ~45 minutos

## 👥 Contribuição

Este projeto foi desenvolvido como parte do AWS JAM Challenge. Para contribuições ou melhorias, siga as melhores práticas de desenvolvimento e documentação.

---

**Desenvolvido com ❤️ usando AWS Lambda, X-Ray e Powertools**

*Última atualização: $(date)*
