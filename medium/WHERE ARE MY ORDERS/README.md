# WHERE ARE MY ORDERS

## 📋 Visão Geral

Este desafio AWS Jam foca na implementação de um sistema de processamento de pedidos automatizado usando **Amazon EventBridge** e **AWS Lambda**. O objetivo é configurar um fluxo de eventos que direcione automaticamente pedidos de comida e bebida para suas respectivas funções Lambda de processamento.

## 🎯 Objetivos do Desafio

- Configurar regras de eventos no Amazon EventBridge
- Implementar funções Lambda para processamento de pedidos
- Configurar variáveis de ambiente necessárias
- Estabelecer um fluxo automatizado de processamento de pedidos

## 🏗️ Arquitetura

```
[OrdersLambdaFunction] 
        ↓ (publica eventos)
[OrderEventBus] 
        ↓ (event rules)
[FoodOrdersLambdaFunction] + [BeverageOrdersLambdaFunction]
        ↓ (salva dados)
[DynamoDB Tables]
```

## 📚 Estrutura do Desafio

### Task 1: CONFIGURE MY BUS (EVENT RULES) - 60 pontos
- **Objetivo**: Criar regras de eventos no EventBridge para direcionar pedidos
- **Serviços**: Amazon EventBridge, AWS Lambda
- **Foco**: Configuração de event rules no OrderEventBus

### Task 2: ADDRESS MY CONFIGURATIONS - 45 pontos  
- **Objetivo**: Configurar variáveis de ambiente nas funções Lambda
- **Serviços**: AWS Lambda
- **Foco**: Environment variables para integração com DynamoDB e EventBridge

### Task 3: [Em desenvolvimento]
- **Status**: ⚠️ **NÃO COMPLETO AINDA**
- **Nota**: Esta tarefa será implementada em breve

## 🔧 Componentes Principais

### EventBridge
- **OrderEventBus**: Event bus customizado para processamento de pedidos
- **Event Rules**: Regras para direcionar eventos baseados no tipo de pedido

### Lambda Functions
- **OrdersLambdaFunction**: Publica eventos no EventBridge
- **FoodOrdersLambdaFunction**: Processa pedidos de comida
- **BeverageOrdersLambdaFunction**: Processa pedidos de bebida

### DynamoDB
- **FoodOrders Table**: Armazena pedidos de comida
- **BeverageOrders Table**: Armazena pedidos de bebida

## 📝 Status do Desafio

- ✅ **Task 1**: Configuração de Event Rules - **COMPLETO**
- ✅ **Task 2**: Configuração de Environment Variables - **COMPLETO**  
- ⚠️ **Task 3**: **EM DESENVOLVIMENTO** - Retornaremos em breve para finalizar

## 🚀 Próximos Passos

Este desafio está em desenvolvimento ativo. As primeiras duas tarefas foram concluídas com sucesso, estabelecendo a base do sistema de processamento de pedidos. A terceira tarefa será implementada em breve para completar o fluxo de trabalho.

---

**Nota**: Este desafio faz parte da coleção AWS Jam Challenges e está sendo desenvolvido progressivamente. Volte em breve para ver a implementação completa da Task 3!