# 📌 Task 2: Debugging AWS Lambda Function Errors in E-commerce Image Classification Pipeline

## 🎯 Objetivo

Resolver problemas de timeout na função Lambda e otimizar o pipeline de categorização de imagens para e-commerce.

## 🏗️ Contexto do Pipeline

**Fluxo de Dados**: S3 (upload) → Lambda (processa) → Rekognition (classifica) → DynamoDB (grava)

### ❌ Problema Identificado
- **Função**: `product-categorization-function`
- **Sintoma**: Encerramento prematuro por timeout
- **Causa**: Imagens complexas demoram mais para processar
- **Impacto**: Pipeline incompleto, dados não salvos no DynamoDB

## 🛠️ Passos Realizados

### 1. Acessar Configurações da Função

#### Navegação
- **Console AWS** → **Lambda** → **Functions**
- Selecionar `product-categorization-function`
- **Configuration** → **General configuration** → **Edit**

### 2. Ajustar Timeout

#### Configuração
- **Timeout**: Ajustado para **15:00** (valor máximo)
- **Justificativa**: Imagens complexas precisam de mais tempo para processamento

#### Valores Recomendados
| Tipo de Imagem | Timeout Sugerido |
|----------------|------------------|
| **Simples** | 3-5 minutos |
| **Complexa** | 10-15 minutos |
| **Máximo** | 15 minutos |

### 3. Otimizar Memória (Opcional)

#### Benefícios
- **CPU**: Cada aumento de memória fornece mais CPU
- **Throughput**: Processamento mais rápido
- **Eficiência**: Melhor utilização de recursos

#### Configuração Sugerida
- **Memória inicial**: 512 MB
- **Memória otimizada**: 1024 MB ou mais
- **Custo vs Performance**: Balancear conforme necessário

### 4. Validação e Teste

#### Teste de Upload
- **Ação**: Novo upload no S3
- **Verificação**: CloudWatch Logs
- **Resultado esperado**: Sem mensagens `Task timed out after ...`

#### Validação do Pipeline
- **S3**: Upload confirmado
- **Lambda**: Execução completa
- **Rekognition**: Classificação realizada
- **DynamoDB**: Dados gravados com sucesso

## 📊 Monitoramento via CloudWatch

### Logs Importantes
```bash
# Sucesso
✅ Task completed successfully
✅ Image classified as: [categoria]
✅ Data saved to DynamoDB

# Erro de Timeout
❌ Task timed out after X.XX seconds
❌ Function execution terminated
```

### Métricas a Observar
- **Duration**: Tempo de execução
- **Memory**: Uso de memória
- **Errors**: Número de erros
- **Throttles**: Limitações de concorrência

## 🔧 Otimizações Adicionais

### Para Produção (Não Requerido no Lab)
- **Retries assíncronos**: Para falhas temporárias
- **Fila SQS**: Entre S3 e Lambda para melhor controle
- **Dead Letter Queue**: Para mensagens que falharam
- **Monitoring**: Alertas automáticos

### Configurações Avançadas
```yaml
# Exemplo de configuração otimizada
Timeout: 15 minutes
Memory: 1024 MB
Reserved Concurrency: 10
Dead Letter Queue: Enabled
Retry Attempts: 3
```

## ⚠️ Observações Importantes

### Timeout vs Memória
- **Timeout**: Resolve problemas de execução longa
- **Memória**: Melhora velocidade de processamento
- **Custo**: Ambos aumentam custos, mas melhoram performance

### Imagens Complexas
- **Alta resolução**: Mais tempo de processamento
- **Múltiplos objetos**: Rekognition demora mais
- **Formatos especiais**: Podem precisar de conversão

## ✅ Resultado

- ✅ **Timeout resolvido** (15 minutos)
- ✅ **Pipeline completo** funcionando
- ✅ **CloudWatch Logs** limpos
- ✅ **DynamoDB** recebendo dados
- ✅ **Task concluída** com sucesso

## 🔗 Próximos Passos

Com o Lambda otimizado, continue para a [Task 3](./task3.md) para testar o pipeline completo e validar os resultados.