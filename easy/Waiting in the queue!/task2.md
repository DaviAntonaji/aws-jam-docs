# Waiting in the queue! — Task 2

## 🎯 Objetivo

Garantir que a função **MyFunctionFixIT (Lambda)** tenha as **permissões mínimas necessárias** para ler e processar mensagens da fila **MyQueue (SQS)** via event source mapping.

---

## 🧩 Ambiente real (recursos do lab)

- Lambda (Function): `LabStack-prewarm-a9e422d5-1632-4c3-MyFunctionFixIT-Zvkm5nYEr8Hf`
- Execution role (IAM Role): `LabStack-prewarm-a9e422d5--LambdaExecutionRoleFixIt-5UkqSEiglrqQ`
- SQS Queue ARN: `arn:aws:sqs:us-east-1:389680303072:LabStack-prewarm-a9e422d5-1632-4c3c-aa8e-d6a6641dfd78-q3vBo-MyQueue-57cb6raofSrq`

> Restrição do desafio: não anexar novas managed policies. Ajustar apenas a inline policy `sqs` da role de execução.

---

## 🧭 Passos realizados (via Lambda)

1) Console → **Lambda** → **Functions** → `LabStack-prewarm-a9e422d5-1632-4c3-MyFunctionFixIT-Zvkm5nYEr8Hf`.
2) Aba **Configuration** → seção **Permissions**.
3) Em **Execution role**, clicar no link da role `LabStack-prewarm-a9e422d5--LambdaExecutionRoleFixIt-5UkqSEiglrqQ`.
4) Em **Permissions**, localizar a inline policy chamada `sqs` → **Edit policy (JSON)**.
5) Substituir pelo JSON de menor privilégio, restrito apenas ao ARN da `MyQueue`.

---

## 🔐 Ações mínimas necessárias para consumir do SQS

- `sqs:ReceiveMessage`
- `sqs:DeleteMessage`
- `sqs:GetQueueAttributes`
- `sqs:GetQueueUrl`
- `sqs:ChangeMessageVisibility`

> Observação: `sqs:SendMessage` não é necessário para a Lambda consumir mensagens da fila.

---

## 📄 Inline Policy (JSON) aplicada

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowLambdaToPollOnlyThisQueue",
      "Effect": "Allow",
      "Action": [
        "sqs:ReceiveMessage",
        "sqs:DeleteMessage",
        "sqs:GetQueueAttributes",
        "sqs:GetQueueUrl",
        "sqs:ChangeMessageVisibility"
      ],
      "Resource": "arn:aws:sqs:us-east-1:389680303072:LabStack-prewarm-a9e422d5-1632-4c3c-aa8e-d6a6641dfd78-q3vBo-MyQueue-57cb6raofSrq"
    }
  ]
}
```

---

## ✅ Validação

- Lambda → Function → `...MyFunctionFixIT...` → **Configuration** → **Triggers** → verificar trigger SQS apontando para `MyQueue` e como Enabled.
- Publicar mensagem no SNS (`MySNSTopic`) da Task 1 → mensagem deve chegar na `MyQueue` → trigger SQS invoca a Lambda.
- Lambda → **Monitor** → confirmar `Invocations` e logs de execução.

---

## 📌 Conclusão

Ajustamos a inline policy `sqs` na role `LabStack-prewarm-a9e422d5--LambdaExecutionRoleFixIt-5UkqSEiglrqQ` via caminho direto pela Lambda. Com as permissões mínimas limitadas ao ARN da `MyQueue`, o event source mapping SQS → `MyFunctionFixIT` volta a disparar corretamente, concluindo a Task 2.
