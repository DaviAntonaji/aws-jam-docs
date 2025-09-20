# Task 3: Validation Test of Summarization by Lambda Invocation

## 🎯 Objetivo

Configurar o **gatilho automático** para a função Lambda `bedrock-api-function`, garantindo que a análise dos logs via Amazon Bedrock ocorra automaticamente **duas vezes por dia** (intervalo de 12h), alinhado aos turnos da equipe de segurança.

## 📊 Cenário

### Situação Atual
- ✅ **CloudWatch Logs** já coleta os logs de aplicação/segurança
- ✅ **Lambda bedrock-api-function** processa logs e envia para o Bedrock  
- ❌ **Nenhum trigger configurado** para a função → nada era invocado automaticamente

### Necessidade do Negócio
- **Time de segurança** precisa de análises duas vezes ao dia
- **Alinhamento aos turnos** (início manhã e início noite)
- **Automatização** para evitar execução manual

## 🔧 Resolução Implementada

### 1. Criar o Vínculo EventBridge → Lambda

#### Configuração do Trigger
1. **Acessar Lambda Console** → Functions → `bedrock-api-function`
2. **Ir em Configuration** → **Triggers**
3. **Adicionar trigger** → Clique em "Add trigger"
4. **Selecionar EventBridge** (CloudWatch Events) como fonte
5. **Configurar regra** para scheduling

#### Configuração Visual
```
EventBridge (CloudWatch Events)
    ↓
Schedule Expression: rate(12 hours)
    ↓
Target: bedrock-api-function
```

### 2. Ajustar Regra no EventBridge

#### Navegação no Console
1. **Acessar EventBridge Console** → Event buses → Rules
2. **Localizar a regra** criada automaticamente para a Lambda
3. **Editar a regra** para ajustar o scheduling

#### Schedule Expression Configurado
```
rate(12 hours)
```

### 3. Configuração Detalhada

#### EventBridge Rule Settings
- **Rule Name:** `bedrock-api-function-schedule-rule`
- **Rule Type:** Schedule
- **Schedule Expression:** `rate(12 hours)`
- **State:** Enabled
- **Target:** Lambda function `bedrock-api-function`

#### Horários de Execução
```
Primeira execução: 00:00 UTC
Segunda execução: 12:00 UTC
Ciclo se repete diariamente
```

### 4. Teste e Validação

#### Teste Manual (Opcional)
1. **Invocar função manualmente** via Lambda Console
2. **Verificar logs** no CloudWatch
3. **Confirmar saída** 200 OK (mesmo com "No logs found")
4. **Validar integração** com Bedrock

#### Comandos de Teste
```bash
# Testar função Lambda diretamente
aws lambda invoke \
  --function-name bedrock-api-function \
  --payload '{}' \
  response.json

# Verificar logs da execução
aws logs describe-log-streams \
  --log-group-name /aws/lambda/bedrock-api-function \
  --order-by LastEventTime \
  --descending
```

### 5. Validação Final
1. **Voltar ao painel do Jam** → Check my progress
2. **Task 3** marcada como **Completed** ✅

## ✅ Resultado

### Automação Implementada
- ✅ **Sistema dispara a cada 12h** via EventBridge
- ✅ **Segurança tem relatórios** prontos no início de cada turno
- ✅ **Configuração otimiza custo** e evita processamento desnecessário de pequenos lotes

### Benefícios Alcançados
- **Análise consistente** - Sem dependência de execução manual
- **Alinhamento operacional** - Relatórios prontos nos turnos
- **Otimização de recursos** - Execuções programadas reduzem custos
- **Escalabilidade** - Fácil ajuste de frequência se necessário

## 🔍 Detalhes Técnicos

### EventBridge Schedule Expressions

#### Opções de Scheduling
```bash
# A cada 12 horas (implementado)
rate(12 hours)

# Diariamente às 8h e 20h UTC
cron(0 8,20 * * ? *)

# A cada 6 horas
rate(6 hours)

# Apenas dias úteis às 9h UTC
cron(0 9 ? * MON-FRI *)
```

#### Sintaxe Rate Expression
```
rate(value unit)

Onde:
- value: número positivo
- unit: minute(s), hour(s), day(s)
```

### Arquitetura Final
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ EventBridge     │    │ Lambda Function │    │ Amazon Bedrock  │
│ Schedule Rule   │───▶│ bedrock-api-    │───▶│ Nova Lite       │
│ rate(12 hours)  │    │ function        │    │ Analysis        │
└─────────────────┘    └─────────────────┘    └─────────────────┘
        │                        │                        │
        │                        ▼                        ▼
        │               ┌─────────────────┐    ┌─────────────────┐
        │               │ CloudWatch      │    │ Log Analysis    │
        └──────────────▶│ Logs            │    │ Results         │
         (Every 12h)    │ Processing      │    │ (Plain English) │
                        └─────────────────┘    └─────────────────┘
```

## 📊 Monitoramento e Métricas

### CloudWatch Metrics para Acompanhar
- **EventBridge Rule Invocations** - Número de triggers executados
- **Lambda Duration** - Tempo de execução da análise
- **Lambda Errors** - Taxa de erro das execuções
- **Bedrock API Calls** - Número de chamadas para análise

### Logs Importantes
```bash
# EventBridge rule executions
/aws/events/rule/bedrock-api-function-schedule-rule

# Lambda function logs
/aws/lambda/bedrock-api-function

# Bedrock API logs (se habilitado)
/aws/bedrock/model-invocations
```

## 🚨 Troubleshooting

### Problemas Comuns

#### Rule não está disparando
- **Verificar estado** da regra (deve estar "Enabled")
- **Confirmar target** está configurado corretamente
- **Checar permissões** do EventBridge para invocar Lambda

#### Lambda não está sendo invocada
- **Verificar resource-based policy** da Lambda
- **Confirmar IAM permissions** para EventBridge
- **Checar CloudWatch Events** para erros

#### Execuções com erro
- **Analisar CloudWatch Logs** da função
- **Verificar configuração** de timeout e memória (Task 2)
- **Confirmar acesso** ao Bedrock (Task 1)

### Comandos de Diagnóstico
```bash
# Verificar regras do EventBridge
aws events list-rules --name-prefix bedrock

# Verificar targets da regra
aws events list-targets-by-rule --rule bedrock-api-function-schedule-rule

# Verificar métricas da função
aws cloudwatch get-metric-statistics \
  --namespace AWS/Lambda \
  --metric-name Invocations \
  --dimensions Name=FunctionName,Value=bedrock-api-function \
  --start-time 2024-01-01T00:00:00Z \
  --end-time 2024-01-02T00:00:00Z \
  --period 3600 \
  --statistics Sum
```

## 💡 Otimizações Futuras

### Melhorias Possíveis
- **Cron expression** para horários específicos (ex: 8h e 20h)
- **Dead Letter Queue** para falhas de processamento
- **SNS notifications** para alertas de execução
- **CloudWatch Alarms** para monitoramento proativo

### Configurações Avançadas
```json
{
  "ScheduleExpression": "cron(0 8,20 * * ? *)",
  "Description": "Execute log analysis at 8 AM and 8 PM UTC daily",
  "State": "ENABLED",
  "Targets": [
    {
      "Id": "1",
      "Arn": "arn:aws:lambda:region:account:function:bedrock-api-function",
      "DeadLetterConfig": {
        "Arn": "arn:aws:sqs:region:account:queue:bedrock-dlq"
      }
    }
  ]
}
```

## 🎓 Lições Aprendidas

### EventBridge Scheduling
- **Rate expressions** são ideais para intervalos regulares
- **Cron expressions** oferecem controle mais granular
- **State management** é crucial (Enabled/Disabled)

### Automação de IA
- **Scheduling adequado** otimiza custos de modelos de IA
- **Batch processing** é mais eficiente que execuções frequentes
- **Error handling** é essencial para automação confiável

### Operações de Segurança
- **Análise regular** melhora detecção de anomalias
- **Timing alinhado** aos turnos aumenta eficiência
- **Automação** reduz carga operacional manual

---

**🎉 Task 3 Concluída!**

> **💭 Reflexão:** A automação de análise de logs com IA representa uma evolução significativa em operações de segurança. O agendamento inteligente via EventBridge garante que insights estejam sempre disponíveis quando a equipe precisa, otimizando tanto custos quanto eficiência operacional.