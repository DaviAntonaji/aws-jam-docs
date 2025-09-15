# 📌 Task 3 – Adjust Inference Parameters

## 🎯 Objetivo

Testar como os parâmetros **Temperature**, **Top P** e **Length** afetam a resposta do modelo Amazon Nova Lite.

## 🛠️ Passos Realizados

### 1. Abrir Playground
- Entrei no **Amazon Bedrock Console → Playgrounds → Chat/Text**
- Modelo selecionado: **Amazon Nova Lite**
- Usei o mesmo prompt da Task 2 (gatekeeper com 3 opções para o viajante)

### 2. Rodar Primeira Configuração (Alta Criatividade)

#### Parâmetros Ajustados
```yaml
temperature: 0.9
top_p: 0.9
length: 1000
```

#### Execução
- Cliquei em **Run**
- **Resultado**: Narrativa mais criativa e variada, com detalhes inesperados e linguagem mais artística

### 3. Rodar Segunda Configuração (Baixa Criatividade)

#### Parâmetros Ajustados
```yaml
temperature: 0.1
top_p: 0.1
length: 1024
```

#### Execução
- Cliquei em **Run**
- **Resultado**: Narrativa mais previsível e repetitiva, menos criativa, muito mais focada em respostas determinísticas

## 📊 Comparação dos Parâmetros

| Configuração | Temperature | Top P | Resultado |
|--------------|-------------|-------|-----------|
| **Alta Criatividade** | 0.9 | 0.9 | Saída diversificada, criativa, estilo livre |
| **Baixa Criatividade** | 0.1 | 0.1 | Saída rígida, determinística, pouca variação |

## 🔧 Explicação dos Parâmetros

### Temperature (0.0 - 1.0)
- **Baixa (0.1)**: Respostas mais determinísticas e previsíveis
- **Alta (0.9)**: Respostas mais criativas e variadas

### Top P (0.0 - 1.0)
- **Baixo (0.1)**: Considera apenas tokens mais prováveis
- **Alto (0.9)**: Considera um conjunto maior de tokens possíveis

### Length
- Define o número máximo de tokens na resposta
- Afeta o tamanho e detalhamento da saída

## ✅ Resultado

- **Alta temperatura/Top P** → Saída diversificada, criativa, estilo livre
- **Baixa temperatura/Top P** → Saída rígida, determinística, com pouca variação

## 🔗 Próximos Passos

Agora que você entende os parâmetros de inferência, continue para a [Task 4](./task4.md) para gerar imagens com Amazon Nova Canvas.