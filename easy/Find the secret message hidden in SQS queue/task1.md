# TASK 1 — Fix Lambda timeouts by restricting SQS VPC Endpoint to Lambda SG (Least Privilege)

## Objetivo
Eliminar timeouts da Lambda ao acessar o SQS dentro da VPC e aplicar princípio do menor privilégio na rede.

## Ambiente (lab)

- **VPC:** `JAM-Challenge`
- **Lambda:** `Jam-Challenge-Lambda`
- **VPC Endpoint:** Interface para SQS
- **Security Groups:**
  - `endpoint-sg` (associado ao VPC Endpoint do SQS)
  - `lambda-sg` (associado à Lambda)

> **Requisito do lab:** "Please allow HTTPS traffic from lambda security group only"  
> (O SG do endpoint não deve aceitar tráfego por CIDR da VPC.)

## 1) Configurar endpoint-sg (VPC Endpoint do SQS)

### Caminho
**EC2** → **Security Groups** → selecione `endpoint-sg` → **Inbound rules**

### Ações
1. **Remover** qualquer regra Inbound com CIDR (ex.: `10.192.0.0/16`, `0.0.0.0/0`, `::/0`, "self", etc.)
2. **Adicionar** a regra:
   - **Type:** `HTTPS`
   - **Port:** `443`
   - **Source:** `Security group` → `lambda-sg`
3. **Salvar** as regras

> **Resultado:** O endpoint só aceita conexões HTTPS vindas do SG da Lambda.

## 2) Configurar lambda-sg (Lambda)

### Caminho
**EC2** → **Security Groups** → selecione `lambda-sg` → **Outbound rules**

### Ações
Garantir que há saída para o endpoint. **Duas opções válidas no lab:**

**Opção A (aceita no lab):**
- **Type:** `All traffic`
- **Destination:** `0.0.0.0/0`

**Opção B (mais estrito):**
- **Type:** `HTTPS`
- **Port:** `443`
- **Destination:** `Security group` → `endpoint-sg`

> **Importante:** Não criar Inbound no `lambda-sg` (não é necessário para conexões iniciadas pela Lambda).

### Lembrete
Security Groups são **stateful** — basta Outbound na Lambda e Inbound no endpoint.

## 3) Confirmar associação da Lambda

### Caminho
**Lambda** → **Functions** → `Jam-Challenge-Lambda` → **Configuration** → **VPC**

### Ações
Verificar que a função está na **VPC JAM-Challenge**, usando **subnets privadas** e o **Security Group lambda-sg**.

Salvar caso tenha sido necessário ajustar.

## Validação (o que comprova a Task 1)

1. **(Opcional)** Em **General configuration**, aumentar **Timeout** da função para 10–15s apenas para teste
2. **Executar Test** (Console da Lambda)
3. **Resultado esperado** após correção de SGs:
   - O timeout desaparece
   - A execução passa a retornar um erro explícito do SQS (ex.: `AWS.SimpleQueueService.NonExistentQueue` ou `AccessDenied`)
4. **Clicar** em "Check my progress" no lab

> **Observação:** Erros explícitos de SQS nessa fase são esperados (permissões lógicas/código ficam para a Task 2). O objetivo da Task 1 é corrigir rede/SG e eliminar o timeout.

## Estado Final (Snapshot das Regras)

### endpoint-sg — Inbound
```
HTTPS (TCP 443)   Source: lambda-sg
(sem outras regras; nenhuma por CIDR)
```

### lambda-sg — Outbound
**Opção A (aceita no lab):**
```
All traffic → 0.0.0.0/0
```

**OU Opção B (mais estrito):**
```
HTTPS (TCP 443) → Destination: endpoint-sg
```

### lambda-sg — Inbound
```
(nenhuma regra necessária)
```

## 🆘 Troubleshooting Rápido

**Se voltar o timeout:**

1. ✅ Verifique se o `endpoint-sg` tem **Inbound 443** com **Source = lambda-sg** (e sem CIDR)
2. ✅ Verifique se o `lambda-sg` tem **Outbound** permitindo 443 ao `endpoint-sg` (ou All outbound)
3. ✅ Confirme que a função está com o `lambda-sg` aplicado na VPC correta
4. **(Opcional)** Aumente temporariamente o timeout da função para ver o erro explícito