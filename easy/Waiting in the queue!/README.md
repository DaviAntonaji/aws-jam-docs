# Waiting in the queue!

## 📋 Visão Geral

Desafio focado em restaurar e operar o fluxo **SNS → SQS → Lambda**, corrigindo permissões, policies e o mapeamento de fonte de eventos para garantir processamento de mensagens.

## 🗂️ Estrutura

- `task1.md`: Corrigir policy da SQS e assinatura SNS → SQS
- `task2.md`: Conceder permissões mínimas para a Lambda consumir a fila
- `task3.md`: Recriar/habilitar o trigger SQS → Lambda e validar

## 🔗 Tarefas

- [Task 1 – SNS para SQS](./task1.md)
- [Task 2 – Permissões da Lambda para SQS](./task2.md)
- [Task 3 – Trigger SQS → Lambda](./task3.md)

## ✅ Objetivos de Aprendizado

- Diferenciar URL vs ARN em policies de SQS
- Configurar assinaturas do SNS para SQS
- Aplicar princípio de menor privilégio para consumo da fila
- Habilitar e validar mapeamento de fonte de evento SQS → Lambda

## 🏁 Critérios de Conclusão

- [ ] Mensagens publicadas no SNS chegam na SQS
- [ ] Lambda tem permissões mínimas para consumir a fila
- [ ] Trigger SQS → Lambda habilitado e invocando a função

---

Boa prática: monitore Dead-letter Queues (DLQ) e métricas de visibilidade para evitar perda de mensagens.

