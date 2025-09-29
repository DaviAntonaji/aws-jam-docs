# Task 2: ALB Target IPv4 Only

## 🎯 Objetivo

**Task 2:** ALB Target IPv4 Only  
**Pontos Possíveis:** 12  
**Penalidade de Pista:** 0  
**Pontos Disponíveis:** 12

## 📋 Contexto

### Situação Atual
O `Jam-ALB` já está configurado em modo dualstack (IPv4 + IPv6).

### Objetivo
Agora precisamos configurar o ALB para usar apenas o Target Group `Jam-ALB-IPv4-Only`, que contém instâncias/subnets apenas com IPv4.

### Conceito Importante
Mesmo acessando via IPv6, o ALB consegue entregar o tráfego porque ele faz a tradução para o target IPv4.

## 🛠️ Inventário

### Recursos Disponíveis
- **Application Load Balancer:** `Jam-ALB` (configurado como dualstack)
- **Target Group:** `Jam-ALB-IPv4-Only` (instâncias IPv4-only)
- **Instância de Teste:** `Jam-Instance-Test` (via Session Manager)

### Comandos de Teste
- **IPv4 test command:** `Task2IPv4Command`
- **IPv6 test command:** `Task2IPv6Command`

## 🔧 Sua Tarefa

1. Alterar o ALB `Jam-ALB` para usar o target group `Jam-ALB-IPv4-Only`
2. Conectar na instância `Jam-Instance-Test` usando Session Manager
3. Fazer requisição curl usando IPv4
4. Fazer requisição curl usando IPv6

> **⚠️ Importante:** Load Balancers pertencem ao console EC2.

## ✅ Solução Passo a Passo

### 1. Configurar ALB Target Group

#### Acessar o Console
- Vá até **EC2 Console** → **Load Balancers**
- Clique em **`Jam-ALB`**

#### Alterar Listener
- Vá na aba **"Listeners"**
- Selecione o listener (normalmente porta 80 ou 443)
- Clique em **"Edit rules"**

#### Configurar Forwarding
- Altere a ação default para **Forward** → **`Jam-ALB-IPv4-Only`**
- Clique em **"Save"**

#### Aguardar Propagação
- Aguarde ~3 minutos para a propagação

### 2. Validar Configuração

#### Acessar Session Manager
- Vá em **Systems Manager** → **Session Manager**
- Clique no botão **"Start session"** (canto superior direito, botão laranja)
- Selecione a instância **`Jam-Instance-Test`**
- Clique em **"Start session"** novamente

#### Executar Testes
No terminal Linux que abrir, execute os comandos fornecidos em **Output Properties**:

```bash
# Teste IPv4
curl --ipv4 http://Jam-ALB-1865640067.us-east-1.elb.amazonaws.com/cgi-bin/task-a

# Teste IPv6  
curl --ipv6 http://Jam-ALB-1865640067.us-east-1.elb.amazonaws.com/cgi-bin/task-a
```

### 3. Interpretar Resultados

#### Resposta IPv4
```
Jam IPv6 with ALB and NLB

You requested using IPv4 address '98.88.216.104'.
Server behind Load Balancer is also IPv4 '10.0.3.67'.

Request detail:
HTTP_X_FORWARDED_FOR=98.88.216.104
HTTP_X_FORWARDED_PORT=80
HTTP_X_FORWARDED_PROTO=http
REMOTE_ADDR=10.0.0.92
REMOTE_PORT=20250
SERVER_ADDR=10.0.3.67
```

#### Resposta IPv6
```
Jam IPv6 with ALB and NLB

You requested using IPv6 address '2600:1f18:3a26:4100:5ed8:d11d:6918:4282'.
Server behind Load Balancer is IPv4 '10.0.3.67'.

As Load Balancer is dualstack, it translated your request from IPv6 to IPv4.

Request detail:
HTTP_X_FORWARDED_FOR=2600:1f18:3a26:4100:5ed8:d11d:6918:4282
HTTP_X_FORWARDED_PORT=80
HTTP_X_FORWARDED_PROTO=http
REMOTE_ADDR=10.0.1.56
REMOTE_PORT=2868
SERVER_ADDR=10.0.3.67
```

## 🧪 Validação

### Critério de Sucesso
A tarefa será automaticamente completada quando você realizar as requisições curl usando IPv4 e IPv6.

### Verificação Manual
Clique no botão **"Check my progress"** na tela de detalhes do desafio.

## 📚 Conceitos Aprendidos

### ALB Translation
- **IPv6 → IPv4:** ALB traduz requisições IPv6 para targets IPv4
- **Headers preservados:** `HTTP_X_FORWARDED_FOR` mostra IP original
- **Transparente:** Cliente não percebe a tradução

### Target Groups
- **IPv4-only:** Targets em subnets apenas IPv4
- **Health checks:** Verificam disponibilidade dos targets
- **Load balancing:** Distribuem tráfego entre targets saudáveis

### Dualstack Benefits
- **Flexibilidade:** Suporta clientes IPv4 e IPv6
- **Migration path:** Permite migração gradual
- **Backward compatibility:** Mantém suporte IPv4

## 🎓 Lições Importantes

1. **ALB faz tradução automática:** IPv6→IPv4 e IPv4→IPv6
2. **Targets podem ser IPv4-only:** ALB cuida da tradução
3. **Headers mostram IP original:** `HTTP_X_FORWARDED_FOR`
4. **Propagação leva tempo:** Aguardar ~3 minutos

## 🔍 Troubleshooting

### Problemas Comuns
- **"Not yet completed":** Aguardar propagação completa
- **Comandos não funcionam:** Usar exatamente os comandos do Output Properties
- **Timeout:** Verificar health status dos targets

### Validação
- Ambos os testes (IPv4 e IPv6) devem funcionar
- Headers devem mostrar IPs diferentes
- Server sempre será IPv4 (target IPv4-only)

---

**🎯 Resultado:** ALB configurado com target IPv4-only, mas ainda acessível via IPv6 devido à tradução automática.