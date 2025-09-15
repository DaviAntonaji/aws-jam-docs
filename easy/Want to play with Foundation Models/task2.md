# 📌 Task 2 – IT'S PLAY TIME!

## 🎯 Objetivo

Gerar uma narrativa de personagem em dois modelos diferentes no **Amazon Bedrock Playground** (Nova Lite e Nova Micro) e comparar os resultados.

## 🛠️ Passos Realizados

### 1. Abrir Playground
- Acessei o **Amazon Bedrock Console**
- Naveguei para **Playgrounds → Chat/Text**

### 2. Rodar com Amazon Nova Lite

#### Configuração
- Selecionei o modelo **Amazon Nova Lite**
- Escrevi o seguinte prompt:

```
You are a game developer. 
Create a narrative for a new character in my role-playing game. 
The character is a gatekeeper to a mystical world. 
A traveler approaches the gatekeeper to enter the mystical world. 
The gatekeeper should provide the traveler with three distinct options for how they may gain entry.
```

#### Execução
- Cliquei em **Run** para gerar a resposta
- **Resultado**: Narrativa detalhada, com descrições criativas e bem estruturadas para os três caminhos do viajante

### 3. Rodar com Amazon Nova Micro

#### Configuração
- Alterei o modelo para **Amazon Nova Micro**
- Reutilizei o mesmo prompt

#### Execução
- Cliquei em **Run** para gerar a resposta
- **Resultado**: Narrativa mais curta e direta, com menos detalhamento, mas cumprindo o pedido das 3 opções

## 📊 Comparação dos Resultados

| Aspecto | Amazon Nova Lite | Amazon Nova Micro |
|---------|------------------|-------------------|
| **Criatividade** | Mais criativa, texto elaborado | Resposta simples e objetiva |
| **Detalhamento** | Descrições ricas e complexas | Menos detalhamento |
| **Uso** | Ideal para histórias complexas | Mais econômica em custo |
| **Velocidade** | Processamento mais lento | Resposta mais rápida |

## ✅ Resultado

- Ambos os modelos geraram narrativas válidas seguindo o prompt
- **Nova Lite** oferece maior qualidade e criatividade
- **Nova Micro** é mais eficiente e econômico

## 🔗 Próximos Passos

Agora que você experimentou os modelos, continue para a [Task 3](./task3.md) para aprender sobre parâmetros de inferência.