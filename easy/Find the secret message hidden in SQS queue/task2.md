# TASK 2 — Pós-mortem (bem honesto) — Lab Lambda + SQS

## 📋 Resumo em 1 linha
Fizemos tudo "certo" tecnicamente, mas a Task 2 só passou quando seguimos ao pé da letra a dica do lab, que exigia um statement específico numa inline policy com nome específico, mesmo sendo redundante.

## 🎯 Contexto

**Objetivo:** Colocar a Lambda dentro da VPC com acesso ao SQS via VPCE (Task 1) e, depois, ajustar IAM (identity-based) com mínimo privilégio para a app ler da `Jam-Challenge-Queue` e enviar para `ResultQueue` (Task 2).

**Ambiente:** Cheio de restrições de permissão no Console (usuário do lab), então várias ações comuns estavam bloqueadas:
- `iam:CreatePolicy`
- `sqs:SetQueueAttributes`
- `sqs:ListQueues`
- `ec2:DescribeVpcEndpointServices`
- `sqs:SendMessage` via UI, etc.

## ✅ O que tentamos — Task 1 (timeouts)

### Diagnóstico inicial
Lambda em VPC com timeout ao chamar SQS → típico de SGs errados no Interface VPCE e/ou endpoint_url forçando público.

### Correções de rede (que funcionaram)
- **endpoint-sg** (do VPCE SQS): Inbound 443 apenas from `lambda-sg` (sem CIDR da VPC / 0.0.0.0/0)
- **lambda-sg:** Outbound 443 para o `endpoint-sg` (ou All outbound)
- Confirmamos que a Lambda estava na VPC/subnets corretas com o `lambda-sg`

### Sintoma validado
Timeout sumiu e virou erro explícito do SQS (`QueueDoesNotExist`/`AccessDenied`), que é exatamente o que a Task 1 queria.

> **✅ Task 1 concluída** quando paramos de usar CIDR e passamos a usar SG→SG (least privilege de rede).

## 🔧 O que tentamos — Task 2 (IAM mínima + execução)

### Caminho técnico lógico (antes da dica)
Montamos uma inline policy mínima na `Jam-Challenge-Role` com:

- `sqs:GetQueueUrl` em `*` (limitação do SQS)
- **Origem** (`Jam-Challenge-Queue`): `ReceiveMessage` (+ às vezes `GetQueueAttributes`/`ChangeMessageVisibility`/`DeleteMessage`)
- **Destino** (`ResultQueue`): `SendMessage` (+ opcional `GetQueueAttributes`)
- Mantivemos KMS conforme o CMK do lab
- Executamos a Lambda (200 "" quando a fila estava vazia, o que é sucesso em termos de app)

### Problemas que trombamos
**Usuário do console sem permissão pra:**
- Criar policy gerenciada (`iam:CreatePolicy`)
- Editar Queue Policy (`sqs:SetQueueAttributes`) — de qualquer forma, o lab diz que Queue Policy está fora do escopo
- Listar filas (`sqs:ListQueues`) e Enviar mensagem via UI (`sqs:SendMessage`), então era difícil "provar" o fluxo fim-a-fim com uma mensagem real

**Mesmo com a execução 200 (vazia), o checker não marcava a Task 2 como concluída.**

### Ajustes que não destravaram o checker
- Variantes de least privilege "correto" (com/sem `GetQueueAttributes`, com/sem `ChangeMessageVisibility`, com/sem `DeleteMessage`)
- Executar a Lambda depois de salvar cada variante (o checker seguia pedindo "Please make sure Lambda function is successfully executed.")

## 🔑 Por que tivemos que usar a dica do lab (e passou)

### A dica oficial mandava
Editar a inline policy `LambdaExecutionRolePolicy` (nome específico!) e adicionar exatamente este statement:

```json
{
  "Action": [
    "sqs:ReceiveMessage",
    "sqs:GetQueueUrl"
  ],
  "Resource": [
    "arn:aws:sqs:*:*:Jam-Challenge-Queue"
  ],
  "Effect": "Allow"
}
```

### O checker provavelmente procura literalmente
- Policy inline com aquele nome (`LambdaExecutionRolePolicy`)
- Ações exatas (`ReceiveMessage` + `GetQueueUrl`)
- ARN com wildcard no formato `arn:aws:sqs:*:*:Jam-Challenge-Queue`

**Depois de salvar exatamente esse bloco (sem remover o resto) e executar a Lambda, a Task 2 passou.**

> **🔑 Moral do lab:** O validador está "hard-coded" para aquele statement específico numa inline policy específica; não basta estar correto tecnicamente — tem que bater com o que o script espera.

## ❌ Por que algumas abordagens "certas" não passaram

- **Least privilege "de verdade"** (ex.: restringir por ARN com região/conta, adicionar só ações realmente usadas, e/ou políticas no VPCE/Queue) não é o que o checker busca
- **Queue Policy** (resource-based) estava fora do escopo — mesmo que resolvesse, o checker não valida por ali
- **Execução 200** com body vazio é sucesso de app, mas o checker às vezes precisa ver a execução pós-policy e a policy exata que ele espera

## 📚 Lições e recomendações

### Para Labs com Validador
- **Siga a dica literalmente** quando o "certo" não bater com o que o robozinho espera
- **Documente** o que é "correto" (para produção) e o que é "requerido pelo lab" (para passar a validação)
- **Em ambientes restritos**, prefira identity-based policy na role (como o lab pede) e evite depender de Queue Policy/CLI quando não há permissão

### Para Prova Funcional
Ter pelo menos 1 mensagem na fila ajuda; mas aqui o bloqueio de permissão no console (`sqs:SendMessage`) atrapalhou — então passamos com execução vazia mesmo, após a policy no formato pedido.

## ✅ Estado Final (que passou)

### Task 1
- **endpoint-sg:** Inbound 443 from `lambda-sg` (sem CIDR)
- **lambda-sg:** Outbound 443 para `endpoint-sg` (ou All outbound)
- **Timeout sumiu** → erro explícito do SQS (OK para Task 1)

### Task 2
- **Inline LambdaExecutionRolePolicy** com o statement exato da dica (além do que já tínhamos)
- **Execução** da `Jam-Challenge-Lambda` após salvar a policy
- **Checker aceitou**

## 🏭 O que eu faria em produção (fora do lab)

### IAM (least privilege) real
- **Origem:** `ReceiveMessage` (+ `GetQueueAttributes`/`ChangeMessageVisibility` se usado) no ARN exato
- **Destino:** `SendMessage` (+ `GetQueueAttributes` se usado) no ARN exato
- **GetQueueUrl** inevitavelmente em `*`

### Rede
- **SG de VPCE** permitindo só `lambda-sg` em 443, sem CIDR
- **lambda-sg** com outbound 443 pro VPCE
- **Opcional:** restringir com Endpoint Policy e Queue Policy (`aws:SourceVpce`, `aws:PrincipalArn`) — mas isso o lab não queria

---

> **💭 Reflexão:** Este desafio ensina não apenas sobre VPC Endpoints e IAM, mas também sobre como navegar validações automáticas e ambientes restritos - habilidades valiosas para cenários reais de produção.