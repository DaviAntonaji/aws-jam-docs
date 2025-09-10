# Task 1 – Trace with AWS Lambda Powertools

## 🎯 Objetivo

Executar a função Lambda `GetUser` e capturar o secret retornado para validação da Task 1.

## 📋 Pré-requisitos

- Acesso ao Console AWS
- Credenciais válidas para o ambiente do desafio
- Região correta selecionada (canto superior direito do console)

## 🚀 Passo a Passo (Console AWS)

### 1. Acessar o Console AWS

1. Abra o console da AWS
2. Entre com seu usuário e selecione a **região correta** do ambiente do desafio (canto superior direito)

### 2. Navegar para AWS Lambda

1. **Services** → pesquise por **Lambda** → clique
2. Na lista de funções, procure por **GetUser** e clique no nome

### 3. Configurar Evento de Teste (Uma Vez Só)

1. Clique no botão **Test** (canto superior direito)
2. Se aparecer o pop-up "Configure test event", escolha **Create new test event**
3. Dê um nome (ex.: `test1`)
4. **Conteúdo do evento:** A dica diz que não precisa mudar nada; então deixe o JSON padrão ou simplesmente `{}`
5. Clique **Save**

### 4. Executar o Teste

1. Clique novamente em **Test**
2. Aguarde o resultado logo acima do editor (seção **Execution results**)

### 5. Capturar o Secret

1. No painel de resultado, olhe **Response (payload)** e também os **Function logs**
2. Haverá um campo/linha com algo como `"secret": "...."` ou uma mensagem contendo o secret
3. **Copie exatamente** o valor do secret (respeitando maiúsculas/minúsculas e símbolos)

### 6. Enviar para Validação

1. Volte à página do desafio/plataforma
2. Cole o secret no campo de submissão da **Task 1**

## 💻 Alternativa via AWS CLI (Opcional)

Se preferir/precisar rodar pelo terminal:

```bash
# Ajuste a REGIÃO se necessário (ex.: us-east-1)
aws lambda invoke \
  --region us-east-1 \
  --function-name GetUser \
  --payload '{}' \
  response.json

# Veja o resultado
cat response.json
```

**Procure pelo campo "secret"** dentro do `response.json` e envie esse valor na validação.

## ✅ Resultado Esperado

- ✅ Função Lambda executada com sucesso
- ✅ Secret capturado do response
- ✅ Task 1 validada com o secret correto

## 🔍 Troubleshooting

| Problema | Solução |
|----------|---------|
| **Função não encontrada** | Verificar região e nome da função |
| **Erro de permissão** | Verificar credenciais e políticas IAM |
| **Secret não encontrado** | Verificar logs da função e response payload |
| **Região incorreta** | Confirmar região no canto superior direito do console |