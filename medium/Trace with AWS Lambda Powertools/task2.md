# Task 2 – Trace with AWS Lambda Powertools

## 🎯 Objetivo

Ativar o AWS X-Ray tracing na função Lambda `GetUser` e capturar o Trace ID para validação da Task 2.

## 📋 Pré-requisitos

- Task 1 concluída (função `GetUser` funcionando)
- Acesso ao Console AWS
- Permissões para modificar configurações da Lambda

## 🚀 Passo a Passo (Mínimo Esforço)

### 1. Abrir a Função

1. **Console AWS** → **Lambda** → abra **GetUser**

### 2. Ativar o X-Ray (Active Tracing)

1. Aba **Configuration** → no menu lateral selecione **Monitoring and operations tools**
2. Em **AWS X-Ray**, habilite **Active tracing** (toggle ON) → **Save**
3. Se o papel (role) da Lambda não tiver permissão, o console vai sugerir anexar `AWSXRayDaemonWriteAccess`. **Aceite**

### 3. Executar um Teste

1. Clique **Test** (como na Task 1)
2. Use o mesmo evento de teste (ex.: `{}`) → **rode**

### 4. Copiar o Trace ID para Validação

1. Na área **Execution results**, procure o bloco **X-Ray** e copie o **Trace ID** (formato: `1-xxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx`)
2. **Alternativo:** Clique no link **View X-Ray traces** que aparece após a execução; o Trace ID aparecerá na página do X-Ray

## 🔍 Conferir os Detalhes no X-Ray (Opcional, mas Recomendado)

### Navegação no Console

1. **Console AWS** → **X-Ray** → **Traces** (ou **Service map**)
2. Abra o trace mais recente (o mesmo Trace ID) e verifique:

### O que Verificar

- ✅ **Segmento da Lambda** com marcadores de:
  - **Init** (cold start quando houver)
  - **Invoke** 
  - **Overhead/Shutdown**
- ✅ **Linhas do tempo** ajudam a visualizar o "entre" (tempo fora do handler) e o encerramento

## 💻 Alternativas para Obter o Trace ID

### Via CloudWatch Logs

1. Após o teste, vá em **Logs da função** → **último log stream**
2. Procure entradas contendo **Tracing** ou o link do X-Ray
3. Em muitos casos há referência ao trace

### Via AWS CLI

```bash
# Ajuste a região e a janela de tempo (últimos 5 min)
aws xray get-trace-summaries \
  --region us-east-1 \
  --start-time "$(date -u -d '5 minutes ago' +%s)" \
  --end-time   "$(date -u +%s)" \
  --query "TraceSummaries[0].Id" \
  --output text
```

**Copie o ID retornado** (o TraceId).

## 🔧 O que Muda com o X-Ray (Sem Tocar no Código)?

### Funcionalidades Automáticas

- ✅ A Lambda passa a enviar **segments automaticamente**
- ✅ Você verá **init duration**, **invoke** e **overhead/shutdown** na linha do tempo do trace
- ✅ Se futuramente você instrumentar código (SDK X-Ray), dará para abrir **subsegments** (DynamoDB, HTTP, etc.), mas não é necessário para esta task

## ✅ O que Enviar para Concluir a Task 2

1. **Execute a Lambda** como no passo 3
2. **Envie o X-Ray Trace ID** copiado do resultado do teste (ou da página do X-Ray/Traces)

## 🎯 Resultado Esperado

- ✅ X-Ray tracing ativado na função Lambda
- ✅ Trace ID capturado com sucesso
- ✅ Task 2 validada com o Trace ID correto

## 🔍 Troubleshooting

| Problema | Solução |
|----------|---------|
| **Active tracing não aparece** | Verificar se está na aba Configuration correta |
| **Erro de permissão** | Aceitar a sugestão de anexar AWSXRayDaemonWriteAccess |
| **Trace ID não aparece** | Aguardar alguns segundos após a execução |
| **X-Ray não carrega** | Verificar região e permissões do usuário |
