# 📌 Task 5 – Invoking Amazon Nova Lite via Python (Bedrock Runtime API)

## 🎯 Objetivo

Aprender a invocar o modelo **Amazon Nova Lite** de forma programática usando a **Amazon Bedrock Runtime API** com Python.

## 🛠️ Passos Realizados

### 1. Abrir Código Base
- Utilizei o exemplo fornecido no desafio para invocar modelos no Bedrock via **boto3**

### 2. Identificar Parâmetros de Inferência
- A seção `inf_params` precisava ser ajustada
- O enunciado fornecia os valores corretos, mas os nomes das chaves deveriam seguir o código base
- **Exemplo**: `max_new_tokens` em vez de `maxTokenCount`

### 3. Atualizar Parâmetros

#### Código Final
```python
inf_params = {
    "max_new_tokens": 2048,
    "top_p": 0.7,
    "temperature": 0.6
}
```

#### Explicação dos Parâmetros
| Parâmetro | Valor | Função |
|-----------|-------|--------|
| `max_new_tokens` | 2048 | Número máximo de tokens na resposta |
| `top_p` | 0.7 | Controle de diversidade (0.0-1.0) |
| `temperature` | 0.6 | Controle de criatividade (0.0-1.0) |

### 4. Executar Validação
- Colei o trecho no campo **Submit Answer**
- O sistema validou e marcou a Task como concluída

## 💻 Código Completo de Exemplo

```python
import boto3
import json

# Inicializar cliente Bedrock
bedrock = boto3.client('bedrock-runtime')

# Parâmetros de inferência
inf_params = {
    "max_new_tokens": 2048,
    "top_p": 0.7,
    "temperature": 0.6
}

# Invocar modelo
response = bedrock.invoke_model(
    modelId="amazon.nova-lite-v1:0",
    body=json.dumps({
        "messages": [{"role": "user", "content": "Seu prompt aqui"}],
        "inferenceConfig": inf_params
    })
)

# Processar resposta
result = json.loads(response['body'].read())
print(result['content'][0]['text'])
```

## 🔧 Configuração do Ambiente

### Pré-requisitos
```bash
pip install boto3
```

### Configuração AWS
```bash
aws configure
# Ou definir variáveis de ambiente:
# AWS_ACCESS_KEY_ID
# AWS_SECRET_ACCESS_KEY
# AWS_DEFAULT_REGION
```

## ✅ Resultado

- ✅ **Código atualizado** com os parâmetros corretos
- ✅ **Task validada** com sucesso
- ✅ **API funcional** para invocação do modelo Amazon Nova Lite
- ✅ **Parâmetros ajustados** para controle de saída

## 🚀 Próximos Passos

Agora que você completou todas as tasks, você tem:
- Acesso configurado aos modelos Amazon Nova
- Experiência com diferentes modelos e parâmetros
- Conhecimento sobre geração de imagens
- Código funcional para invocação via API

## 🔗 Recursos Adicionais

- [Bedrock Runtime API Documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime.html)
- [boto3 Bedrock Reference](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime.html)
- [Amazon Nova Models Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-nova.html)