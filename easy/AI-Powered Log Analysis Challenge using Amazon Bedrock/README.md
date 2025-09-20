# 🤖 AI-Powered Log Analysis Challenge using Amazon Bedrock

## 📋 Visão Geral

Este desafio foca na **análise automatizada de logs** usando Amazon Bedrock com o modelo Amazon Nova Lite. O objetivo é resolver problemas de integração e permissões para criar um sistema que analise logs do CloudWatch e forneça insights em linguagem natural.

## 🎯 Objetivo

Resolver problemas de integração em um sistema de análise automatizada de logs que usa Amazon Bedrock para processar dados do CloudWatch Logs e fornecer insights inteligentes sobre eventos de segurança e operacionais.

## 🔧 Conceitos Principais

- **Amazon Bedrock** - Plataforma de IA generativa da AWS
- **Amazon Nova Lite** - Modelo de linguagem para análise de dados
- **AWS Lambda** - Processamento serverless de logs
- **Amazon CloudWatch Logs** - Coleta e armazenamento de logs
- **Amazon EventBridge** - Orquestração de eventos e triggers
- **IAM Roles & Policies** - Configuração de permissões para Bedrock
- **Throttling & Quotas** - Limitações de rate limiting em ambiente de treinamento

## 🏗️ Arquitetura

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ CloudWatch      │    │ EventBridge     │    │ Lambda Function │
│ Log Groups      │───▶│ Rules           │───▶│ bedrock-api-    │
│                 │    │ (Scheduled)     │    │ function        │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                        │
                                                        ▼
                                               ┌─────────────────┐
                                               │ Amazon Bedrock  │
                                               │ Nova Lite Model │
                                               │                 │
                                               └─────────────────┘
                                                        │
                                                        ▼
                                               ┌─────────────────┐
                                               │ Log Analysis    │
                                               │ Results         │
                                               │ (Plain English) │
                                               └─────────────────┘
```

## 📚 Tarefas

### [Task 1: Enabling Amazon Nova Model Access in Bedrock](./TASK1.MD)

**Objetivo:** Resolver erro de acesso ao modelo Amazon Nova Lite no Bedrock

**Problema identificado:**
- Lambda function `bedrock-api-function` falhando com erro `AccessDeniedException`
- Modelo `amazon.nova-lite-v1:0` não acessível
- Sistema de análise de logs não funcionando

**Conceitos abordados:**
- Diagnóstico de erros de permissão em Bedrock
- Configuração de acesso a modelos Amazon Nova
- Troubleshooting de integração Lambda + Bedrock
- Configuração de IAM roles para Bedrock
- Entendimento de quotas e throttling em ambiente de treinamento

### [Task 2: Fix the Lambda Timeout and Memory Issue](./TASK2.md)

**Objetivo:** Otimizar recursos da Lambda para processar interações com Bedrock

**Problema identificado:**
- Timeouts prematuros (3 segundos insuficientes)
- Limitação de memória (128 MB insuficiente)
- Falhas em chamadas cross-region ao Bedrock

**Conceitos abordados:**
- Right-sizing de recursos Lambda
- Configuração de timeout adequado para IA
- Otimização de memória para processamento de respostas complexas
- Trade-off entre performance e custo
- Monitoramento de métricas CloudWatch

### [Task 3: Validation Test of Summarization by Lambda Invocation](./TASK3.md)

**Objetivo:** Configurar automação via EventBridge para análise de logs duas vezes por dia

**Problema identificado:**
- Lambda function sem trigger automático
- Análise de logs dependente de execução manual
- Necessidade de relatórios alinhados aos turnos de segurança

**Conceitos abordados:**
- Configuração de EventBridge Schedule Rules
- Automação de execução Lambda com rate expressions
- Integração EventBridge → Lambda para processamento batch
- Otimização de custos com scheduling inteligente
- Monitoramento de execuções automatizadas

## 🚀 Passo a Passo Resumido

### Task 1 - Resolução de Acesso ao Modelo Nova Lite
1. **Identificar o problema** - Lambda function falhando com AccessDeniedException
2. **Analisar logs** - Verificar CloudWatch Logs da função Lambda
3. **Diagnosticar permissões** - Identificar falta de acesso ao modelo Nova Lite
4. **Configurar acesso ao modelo** - Ativar Amazon Nova Lite no Bedrock
5. **Testar integração** - Executar função Lambda para validar correção
6. **Verificar funcionamento** - Confirmar análise de logs em linguagem natural

### Task 2 - Otimização de Recursos Lambda
1. **Identificar problemas de performance** - Timeouts e limitação de memória
2. **Acessar configuração Lambda** - Navegar para Configuration → General configuration
3. **Ajustar memória** - Aumentar de 128 MB para 256 MB
4. **Ajustar timeout** - Aumentar de 3 segundos para 60 segundos
5. **Salvar configurações** - Aplicar mudanças na função
6. **Testar execução** - Validar que função executa sem erros
7. **Verificar funcionamento** - Confirmar processamento completo de logs

### Task 3 - Automação via EventBridge
1. **Identificar necessidade** - Análise de logs manual não escalável
2. **Configurar trigger Lambda** - Adicionar EventBridge como trigger
3. **Criar regra de scheduling** - Configurar rate expression para 12h
4. **Ajustar configurações** - Definir horários alinhados aos turnos
5. **Testar automação** - Validar execução via EventBridge
6. **Verificar scheduling** - Confirmar execuções automáticas funcionando
7. **Validar no Jam** - Confirmar Task 3 marcada como completa

## ⚠️ Pontos Importantes

### Configuração de Acesso ao Bedrock
- **Modelos Amazon Nova** precisam ser ativados explicitamente
- **IAM Roles** devem ter permissões específicas para Bedrock
- **Rate Limiting** - Ambiente de treinamento tem quotas limitadas
- **Throttling** - Pode ocorrer com múltiplas execuções simultâneas

### Troubleshooting Comum
- **AccessDeniedException** - Geralmente indica falta de acesso ao modelo
- **Throttling errors** - Aguardar entre execuções em ambiente de treinamento
- **Model not accessible** - Verificar se modelo está habilitado na região

### Limitações do Ambiente de Treinamento
- **Requests per Minute (RPM)** limitados
- **Tokens per Minute (TPM)** limitados  
- **Tokens per Day (TPD)** limitados
- **Executar código sequencialmente** para evitar throttling

## 🔍 Solução Principal

### Ativação do Modelo Amazon Nova Lite
O problema principal é que o modelo Amazon Nova Lite não está habilitado no Bedrock. A solução envolve:

1. **Acessar Amazon Bedrock Console**
2. **Navegar para Model Access**
3. **Localizar Amazon Nova Lite**
4. **Ativar o modelo** para uso
5. **Aguardar propagação** das permissões

### Comandos de Validação
```bash
# Testar função Lambda após correção
aws lambda invoke \
  --function-name bedrock-api-function \
  --payload '{}' \
  response.json

# Verificar logs da função
aws logs describe-log-groups \
  --log-group-name-prefix /aws/lambda/bedrock-api-function
```

## 📊 Dificuldade e Tempo

**Dificuldade:** ⭐⭐☆☆☆  
**Tempo estimado:** 15-30 minutos

## 🎓 Lições Aprendidas

### Amazon Bedrock
- **Model Access** - Modelos precisam ser explicitamente habilitados
- **Regional Availability** - Verificar disponibilidade por região
- **Rate Limiting** - Importante em ambientes de treinamento
- **Cost Management** - Modelos têm custos associados por token

### Troubleshooting de Integração
- **Error Messages** - AccessDeniedException indica problema de permissão
- **IAM Configuration** - Roles precisam de permissões específicas
- **Service Dependencies** - Bedrock depende de configurações prévias
- **Propagation Time** - Mudanças podem levar alguns minutos

### Boas Práticas
- **Teste Incremental** - Validar após cada mudança
- **Rate Limiting** - Respeitar quotas em ambiente de treinamento
- **Error Handling** - Implementar retry logic para throttling
- **Monitoring** - Usar CloudWatch para acompanhar execuções

## 🔗 Recursos Adicionais

### Documentação AWS
- [Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/)
- [Amazon Nova Models](https://docs.aws.amazon.com/bedrock/latest/userguide/models.html)
- [Bedrock Model Access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html)
- [Bedrock IAM Policies](https://docs.aws.amazon.com/bedrock/latest/userguide/iam-policies.html)

### Conceitos Relacionados
- [AWS Lambda with Bedrock](https://docs.aws.amazon.com/lambda/latest/dg/bedrock.html)
- [CloudWatch Logs Integration](https://docs.aws.amazon.com/cloudwatch/latest/logs/)
- [EventBridge Rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html)

### Ferramentas Úteis
- [AWS CLI Bedrock Commands](https://docs.aws.amazon.com/cli/latest/reference/bedrock/)
- [Bedrock Pricing Calculator](https://aws.amazon.com/bedrock/pricing/)
- [CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html)

## ✅ Critérios de Sucesso

### Task 1 - Enabling Amazon Nova Model Access
- [ ] Erro AccessDeniedException identificado
- [ ] Modelo Amazon Nova Lite ativado no Bedrock
- [ ] Lambda function executando sem erros
- [ ] Sistema de análise de logs funcionando
- [ ] Logs sendo processados e analisados pelo Nova Lite
- [ ] Validação no Jam marcada como "Completed"

### Task 2 - Fix Lambda Timeout and Memory Issue
- [ ] Problemas de timeout identificados
- [ ] Memória ajustada para 256 MB
- [ ] Timeout ajustado para 60 segundos
- [ ] Lambda function executando sem timeout
- [ ] Sem erros de memória insuficiente
- [ ] Processamento completo de logs com Bedrock
- [ ] Validação no Jam marcada como "Completed"

### Task 3 - Validation Test of Summarization by Lambda Invocation
- [ ] Necessidade de automação identificada
- [ ] EventBridge trigger configurado para Lambda
- [ ] Schedule expression rate(12 hours) configurado
- [ ] Regra de EventBridge ativada e funcionando
- [ ] Execuções automáticas ocorrendo a cada 12h
- [ ] Logs de execução disponíveis no CloudWatch
- [ ] Análise de logs automatizada funcionando
- [ ] Validação no Jam marcada como "Completed"

## 🚨 Troubleshooting Comum

### AccessDeniedException Persistent
- Verificar se modelo está ativado na região correta
- Confirmar que IAM role tem permissões para Bedrock
- Aguardar propagação das mudanças (pode levar alguns minutos)
- Verificar se não há políticas de deny explícitas

### Throttling Issues
- Executar operações sequencialmente, não em paralelo
- Aguardar 2 minutos entre tentativas se throttling persistir
- Considerar reiniciar o lab se problemas continuarem
- Usar rate limiting apropriado em código de produção

### Lambda Function Still Failing
- Verificar logs detalhados no CloudWatch
- Confirmar que payload está no formato correto
- Validar se EventBridge rules estão configuradas
- Testar função diretamente via console AWS

### Timeout Issues After Task 2
- Se ainda houver timeouts, aumentar para 2-3 minutos
- Verificar latência de rede para Bedrock
- Considerar usar VPC endpoints se aplicável
- Monitorar métricas de duração no CloudWatch

### Memory Issues After Task 2
- Se ainda houver erros de memória, aumentar para 512 MB ou 1 GB
- Verificar se resposta do Bedrock não está sendo truncada
- Otimizar processamento de logs para reduzir uso de memória
- Implementar streaming se resposta for muito grande

### Model Not Available
- Verificar região do Bedrock (modelos podem não estar disponíveis em todas)
- Confirmar que modelo está na lista de modelos acessíveis
- Verificar se há quotas disponíveis para o modelo
- Aguardar ativação completa (pode levar alguns minutos)

## 💡 Dicas de Otimização

### Performance
- **Batch Processing** - Processar múltiplos logs em uma chamada
- **Caching** - Implementar cache para logs similares
- **Async Processing** - Usar processamento assíncrono para logs grandes
- **Error Handling** - Implementar retry logic com backoff exponencial
- **Right-sizing Lambda** - Ajustar memória e timeout baseado no uso real
- **Cold Start Optimization** - Considerar provisioned concurrency se necessário

### Cost Optimization
- **Token Management** - Otimizar tamanho dos prompts
- **Selective Processing** - Processar apenas logs relevantes
- **Compression** - Comprimir logs antes do envio
- **Monitoring** - Acompanhar uso e custos via CloudWatch

---

**🎉 Boa sorte com o desafio!**

> **💭 Reflexão:** Este desafio demonstra como a IA generativa pode automatizar tarefas tediosas como análise manual de logs, transformando dados técnicos em insights compreensíveis. A resolução do problema de acesso ao modelo Nova Lite é um exemplo clássico de troubleshooting de integração entre serviços AWS.
