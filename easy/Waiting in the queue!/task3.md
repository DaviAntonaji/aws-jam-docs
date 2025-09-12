# Waiting in the queue! — Task 3

## 🎯 Objetivo

Recriar (ou habilitar) o event source mapping entre a **SQS MyQueue** e a **Lambda MyFunctionFixIT**. As permissões já foram ajustadas na Task 2; agora o foco é o gatilho (trigger).

---

## 🧭 Passo a passo (Console)

1) Abrir **Lambda → Functions → MyFunctionFixIT → Configuration → Triggers**.
2) Se já existir um trigger SQS para `MyQueue`, verificar se está **Enabled**. Se estiver **Disabled**, clicar em **Enable**.
3) Se não existir, clicar em **Add trigger** e configurar:
   - Trigger: `SQS`
   - SQS queue: selecionar `MyQueue` (confira o ARN correto)
   - Batch size: `10` (padrão do lab está ok; usar 1–10 conforme necessário)
   - Batch window: `0s` (imediato)
   - Enable trigger: marcado
   - Save

---

## 🧪 Validação

- Publicar mensagem no `MySNSTopic` (Task 1) → deve chegar na `MyQueue`.
- Confirmar que o trigger SQS invoca a **MyFunctionFixIT**.
- Em **Lambda → Monitor**, verificar `Invocations` e logs de execução.

---

## 🚑 Erros comuns e correções

- “No invocations” com mensagens na fila: trigger não existe ou está **Disabled**.
- Mensagens retornando à fila repetidamente: `Visibility timeout` menor que o tempo de execução → aumente-o.
- “Access denied” no mapping: conferir Task 2 e manter apenas `sqs:ReceiveMessage`, `sqs:DeleteMessage`, `sqs:GetQueueAttributes`, `sqs:GetQueueUrl`, `sqs:ChangeMessageVisibility` no ARN da `MyQueue`.
- Lambda sem capacidade: `Reserved concurrency = 0` → ajustar.