# Task 2: Fix the Lambda Timeout and Memory Issue

## 📋 Objetivo

Garantir que a função `bedrock-api-function` tenha recursos suficientes para processar interações com o Amazon Bedrock sem falhar por **timeout** ou **falta de memória**.

## 🎯 Configuração Recomendada

**Configuração recomendada pelo time de produto:**
- **Memória:** 256 MB
- **Timeout:** 60 segundos

## 📊 Cenário Inicial

### Problema Identificado
A função `bedrock-api-function` estava configurada com **valores default**:
- **Memória:** 128 MB (insuficiente)
- **Timeout:** 3 segundos (muito baixo)

### Falhas Observadas
Durante testes, interações com o Bedrock apresentavam falhas por:

1. **Timeouts prematuros** - Processamento de logs + chamada cross-region ao modelo
2. **Limitação de memória** - Processamento de respostas mais complexas do modelo

## 🚀 Passo a Passo Detalhado

### 1. Acessar a Função Lambda
1. Acesse o **AWS Console**
2. Navegue para **Lambda** → **Functions**
3. Selecione `bedrock-api-function`

### 2. Configurar Memória
1. Vá para **Configuration** → **General configuration**
2. Clique em **Edit**
3. Ajuste **Memory** de `128 MB` → `256 MB`
4. Clique em **Save**

### 3. Configurar Timeout
1. No mesmo painel de configuração
2. Ajuste **Timeout** de `3s` → `1m` (60 seconds)
3. Clique em **Save**

### 4. Testar Execução
1. Na interface da Lambda, clique em **Test**
2. Execute a função para validar as mudanças
3. Verifique se executa com sucesso (sem timeout, sem erro de memória)

### 5. Validar no Jam
1. Volte para a tela do Challenge no Jam
2. Clique em **Check my progress**
3. Task 2 deve ser marcada como **Completed** ✅

## ✅ Resultado Esperado

### Melhorias Implementadas
A função agora tem recursos suficientes para lidar com:

- **Latência maior** em chamadas ao Bedrock em `eu-west-2`
- **Respostas longas** e processamento de múltiplos eventos de log
- **Processamento complexo** de análise de logs com IA

### Otimização de Recursos
- **Configuração otimizada** melhora a confiabilidade
- **Custo controlado** - aumento modesto nos recursos
- **Performance melhorada** - sem falhas por timeout ou memória

## 🔍 Configurações Específicas

### Antes (Default)
```
Memory: 128 MB
Timeout: 3 segundos
```

### Depois (Otimizado)
```
Memory: 256 MB
Timeout: 60 segundos
```

## ⚠️ Pontos Importantes

### Considerações de Performance
- **Cross-region calls** - Bedrock pode estar em região diferente
- **Model processing time** - Modelos de IA podem levar tempo para responder
- **Log processing** - Análise de logs pode ser computacionalmente intensiva

### Considerações de Custo
- **Memória dobrada** - Custo de execução aumenta proporcionalmente
- **Timeout maior** - Pode impactar custos se função executar por mais tempo
- **Trade-off** - Confiabilidade vs. Custo

### Troubleshooting
- **Se ainda houver timeouts** - Considere aumentar para 2-3 minutos
- **Se houver erros de memória** - Aumente para 512 MB ou 1 GB
- **Monitoramento** - Use CloudWatch para acompanhar métricas

## 📊 Métricas de Validação

### CloudWatch Metrics para Monitorar
- **Duration** - Tempo de execução da função
- **Memory Utilization** - Uso de memória durante execução
- **Error Rate** - Taxa de erro das execuções
- **Throttles** - Número de throttles

### Validação de Sucesso
- [ ] Função executa sem timeout
- [ ] Sem erros de memória insuficiente
- [ ] Bedrock responde corretamente
- [ ] Logs são processados e analisados
- [ ] Task 2 marcada como "Completed" no Jam

## 🎓 Lições Aprendidas

### Configuração de Lambda
- **Valores default** podem não ser adequados para todas as cargas de trabalho
- **Bedrock integration** requer mais recursos que operações simples
- **Cross-region latency** deve ser considerada no timeout

### Otimização de Recursos
- **Right-sizing** - Encontrar o equilíbrio entre recursos e custo
- **Performance vs. Cost** - Trade-off importante em ambientes de produção
- **Monitoring** - Essencial para validar otimizações

### Boas Práticas
- **Testar configurações** - Sempre validar após mudanças
- **Monitorar métricas** - Acompanhar performance e custos
- **Documentar mudanças** - Registrar configurações que funcionam

---

**🎉 Task 2 Concluída!**

> **💭 Reflexão:** Esta tarefa demonstra a importância de dimensionar corretamente os recursos de Lambda, especialmente quando integrando com serviços de IA que podem ter latência variável e processamento computacionalmente intensivo.