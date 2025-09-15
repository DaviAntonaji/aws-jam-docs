# 📌 Task 4 – Generating Images with Amazon Nova Canvas

## 🎯 Objetivo

Criar uma imagem para o cenário do jogo (viajante se aproximando do gatekeeper para entrar no mundo místico) usando o modelo **Amazon Nova Canvas**.

## 🛠️ Passos Realizados

### 1. Abrir Playground de Imagens
- No **Amazon Bedrock Console**, acessei **Playgrounds → Image**
- Selecionei o modelo **Amazon Nova Canvas**

### 2. Definir Prompt

#### Prompt Principal
```
A mystical gatekeeper standing before a large portal to another world, approached by a lone traveler. The scene should be fantasy style, with glowing lights, magical aura, and dramatic atmosphere.
```

#### Prompt Negativo (Opcional)
```
no modern buildings, no sci-fi technology
```
*Nota: Pode ser usado para evitar elementos indesejados na imagem*

### 3. Ajustar Parâmetros

| Parâmetro | Valor | Descrição |
|-----------|-------|-----------|
| **Prompt Strength** | 10 | Máxima aderência ao prompt |
| **Size** | 1024x1024 | Resolução padrão |
| **Aspect Ratio** | 1:1 | Proporção quadrada |
| **Number of Images** | 1 | Gera uma única imagem |

### 4. Gerar Imagem
- Cliquei em **Generate**
- O modelo retornou uma imagem fiel ao cenário descrito, com viajante e gatekeeper em frente ao portal místico

## 🎨 Resultado da Geração

- **Imagem gerada com sucesso** usando Amazon Nova Canvas
- **Configuração aplicada**: Prompt Strength 10 → saída bem alinhada com o pedido
- **Cenário**: Viajante e gatekeeper em frente ao portal místico
- **Estilo**: Fantasy com atmosfera dramática e elementos mágicos

## 🔧 Parâmetros de Geração de Imagem

### Prompt Strength
- **Valor**: 0-10
- **Função**: Controla quão fiel a imagem será ao prompt
- **10**: Máxima fidelidade ao prompt

### Size
- **Opções**: 1024x1024, 1024x768, 768x1024
- **Impacto**: Afeta a resolução e qualidade da imagem

### Aspect Ratio
- **1:1**: Quadrado (ideal para redes sociais)
- **16:9**: Widescreen (ideal para apresentações)
- **4:3**: Retrângulo (formato clássico)

## ✅ Resultado

- ✅ Imagem gerada com sucesso
- ✅ Cenário fiel ao prompt
- ✅ Qualidade adequada para uso em jogo
- ✅ Task concluída com sucesso

## 🔗 Próximos Passos

Agora que você gerou imagens, continue para a [Task 5](./task5.md) para aprender a invocar modelos via API Python.