# Waiting in the queue! — Task 1

## 🎯 Objetivo

Restaurar o fluxo de notificações para que o **MySNSTopic (SNS)** entregue mensagens no **MyQueue (SQS)**. Assim, as mensagens chegam ao SQS e podem ser processadas pela **MyFunctionFixIT (Lambda)**.

---

## ✅ Passos realizados

### 1) Corrigir a Access Policy do SQS
A fila **MyQueue** estava com `Resource` usando a **URL** da fila. Para o SNS publicar, é obrigatório usar o **Queue ARN**.

- ARN da fila:
```
arn:aws:sqs:us-east-1:389680303072:LabStack-prewarm-a9e422d5-1632-4c3c-aa8e-d6a6641dfd78-q3vBo-MyQueue-57cb6raofSrq
```

- ARN do tópico:
```
arn:aws:sns:us-east-1:389680303072:LabStack-prewarm-a9e422d5-1632-4c3c-aa8e-d6a6641dfd78-q3vBo5FnrBFmHJL387HMdK-2-MySNSTopic-FYAHpf6oZ1F0
```

#### Nova Access Policy aplicada

```json
{
  "Version": "2012-10-17",
  "Id": "MyQueuePolicy",
  "Statement": [
    {
      "Sid": "Allow-SendMessage-To-Queue-From-SNS-Topic",
      "Effect": "Allow",
      "Principal": { "Service": "sns.amazonaws.com" },
      "Action": "sqs:SendMessage",
      "Resource": "arn:aws:sqs:us-east-1:389680303072:LabStack-prewarm-a9e422d5-1632-4c3c-aa8e-d6a6641dfd78-q3vBo-MyQueue-57cb6raofSrq",
      "Condition": {
        "ArnEquals": {
          "aws:SourceArn": "arn:aws:sns:us-east-1:389680303072:LabStack-prewarm-a9e422d5-1632-4c3c-aa8e-d6a6641dfd78-q3vBo5FnrBFmHJL387HMdK-2-MySNSTopic-FYAHpf6oZ1F0"
        }
      }
    }
  ]
}
```

### 2) Criar assinatura SNS → SQS
No SNS (`MySNSTopic`), criar subscription com:
- Protocol: `SQS`
- Endpoint: ARN da fila (`MyQueue`)
- Raw Message Delivery: habilitado (opcional)

### 3) Teste de validação
- Publicar mensagem de teste no `MySNSTopic`.
- Confirmar chegada na `MyQueue` (Poll for messages).

Resultado: fluxo ativo e validado ✅

---

## 📌 Conclusão
O problema estava na `Resource` da policy da SQS (URL em vez de ARN). Corrigido isso e criada a assinatura, o fluxo SNS → SQS voltou a funcionar e está pronto para acionar a Lambda.
