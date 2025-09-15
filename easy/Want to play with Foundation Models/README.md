# 🤖 Want to play with Foundation Models

## 📋 Visão Geral

Este desafio apresenta uma introdução prática aos **Foundation Models (FMs)** da Amazon, especificamente a família **Amazon Nova**. Você aprenderá a configurar acesso, experimentar diferentes modelos no Playground, ajustar parâmetros de inferência, gerar imagens e invocar modelos via API.

## 🎯 Objetivos de Aprendizado

- Configurar acesso aos modelos Amazon Nova no Amazon Bedrock
- Comparar diferentes modelos de foundation (Nova Lite vs Nova Micro)
- Entender o impacto dos parâmetros de inferência (Temperature, Top P, Length)
- Gerar imagens usando Amazon Nova Canvas
- Invocar modelos programaticamente via Bedrock Runtime API

## 🛠️ Tecnologias Utilizadas

- **Amazon Bedrock** - Serviço gerenciado para Foundation Models
- **Amazon Nova Lite** - Modelo de texto para tarefas gerais
- **Amazon Nova Micro** - Modelo de texto otimizado para eficiência
- **Amazon Nova Canvas** - Modelo multimodal para geração de imagens
- **Python + boto3** - Para invocação programática via API

## 📚 Estrutura do Desafio

### [Task 1: Request Model Access no Amazon Bedrock](./task1.md)
- Solicitar acesso aos modelos Amazon Nova
- Configurar permissões no console
- Verificar status de ativação

### [Task 2: IT'S PLAY TIME!](./task2.md)
- Experimentar Amazon Nova Lite e Nova Micro
- Comparar respostas dos diferentes modelos
- Analisar diferenças de qualidade e estilo

### [Task 3: Adjust Inference Parameters](./task3.md)
- Explorar parâmetros Temperature, Top P e Length
- Testar configurações de alta e baixa criatividade
- Entender impacto na qualidade das respostas

### [Task 4: Generating Images with Amazon Nova Canvas](./task4.md)
- Criar imagens usando prompts textuais
- Ajustar parâmetros de geração (Prompt Strength, Size)
- Gerar arte para cenários de jogo

### [Task 5: Invoking Amazon Nova Lite via Python](./task5.md)
- Configurar invocação programática via boto3
- Ajustar parâmetros de inferência no código
- Validar configuração via API

## 🚀 Pré-requisitos

- Conta AWS com acesso ao Amazon Bedrock
- Permissões para solicitar acesso a modelos
- Python 3.x e boto3 (para Task 5)
- Conhecimento básico de AWS Console

## 📖 Conceitos Importantes

### Foundation Models (FMs)
Modelos de IA pré-treinados que podem ser adaptados para diversas tarefas sem necessidade de treinamento completo.

### Parâmetros de Inferência
- **Temperature**: Controla a aleatoriedade (0.0 = determinístico, 1.0 = muito criativo)
- **Top P**: Controla diversidade via amostragem de núcleo
- **Length**: Limite máximo de tokens na resposta

### Amazon Nova Family
- **Nova Lite**: Equilibrio entre qualidade e custo
- **Nova Micro**: Otimizado para eficiência e velocidade
- **Nova Canvas**: Multimodal para geração de imagens

## 🎮 Cenário do Desafio

Cada task utiliza um cenário de jogo RPG onde um viajante se aproxima de um gatekeeper místico para entrar em um mundo fantástico. Este contexto ajuda a demonstrar as capacidades dos modelos de forma prática e envolvente.

## ✅ Resultados Esperados

Ao final deste desafio, você terá:
- Acesso configurado aos modelos Amazon Nova
- Experiência prática com diferentes FMs
- Compreensão dos parâmetros de inferência
- Imagens geradas para seu projeto
- Código funcional para invocação via API

## 🔗 Links Úteis

- [Amazon Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [Amazon Nova Models](https://aws.amazon.com/bedrock/features/#Amazon_Nova)
- [Bedrock Runtime API Reference](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime.html)
- [boto3 Bedrock Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime.html)

---

**Duração estimada**: 2-3 horas  
**Nível**: Iniciante  
**Categoria**: AI/ML, Foundation Models
