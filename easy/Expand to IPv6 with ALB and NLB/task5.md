# Task 5: NLB Target IPv4 Only

## 🎯 Objetivo

**Task 5:** NLB Target IPv4 Only  
**Pontos Possíveis:** 12  
**Penalidade de Pista:** 0  
**Pontos Disponíveis:** 12

## 📋 Contexto

### Situação Atual
Sua aplicação usa Network Load Balancer (NLB). O NLB chamado `Jam-NLB` está configurado em modo dualstack.

### Objetivo
Você foi solicitado a garantir que seu NLB suporte targets rodando com IPv4 em subnets IPv4-only.

### Conceito Importante
Você notará que pode acessar seu NLB configurado com target group que responde apenas em IPv4 (target group `Jam-NLB-IPv4-Only`), mesmo quando acessar através de IPv6. O NLB é responsável por "traduzir" a comunicação entre IPv4 e IPv6.

## 🛠️ Inventário

### Recursos Disponíveis
- **Network Load Balancer:** `Jam-NLB` (configurado em dualstack)
- **Target Group:** `Jam-NLB-IPv4-Only` (instâncias IPv4-only)
- **Comandos de teste:** Disponíveis em Output Properties

### Comandos de Teste
- **IPv4 test command:** `Task5IPv4Command`
- **IPv6 test command:** `Task5IPv6Command`

## 🔧 Sua Tarefa

1. Alterar o NLB `Jam-NLB` para usar o target group `Jam-NLB-IPv4-Only`
2. Conectar na instância `Jam-Instance-Test` usando Session Manager
3. Fazer requisição curl usando IPv4
4. Fazer requisição curl usando IPv6

> **⚠️ Importante:** Load Balancers pertencem ao console EC2.

> **⏱️ Atenção:** Pode levar tempo após você alterar o Load Balancer para usar o novo target group. Aguarde até 3 minutos para a mudança se aplicar e propagar. O Load Balancer ainda pode apontar para o target group antigo até ser aplicado!

## ✅ Solução Passo a Passo

### 1. Configurar NLB Target Group

#### Acessar o Console
- **EC2 Console** → **Load Balancers** → **`Jam-NLB`**

#### Alterar Listener
- Na aba **"Listeners"**, clique no listener configurado (porta TCP, normalmente 80 ou 443)
- Clique em **"Edit"**

#### Configurar Forwarding
- Altere a ação default para **Forward** → **`Jam-NLB-IPv4-Only`**
- Clique em **"Save"**

#### Aguardar Propagação
- Aguarde até 3 minutos para a propagação

### 2. Validar Configuração

#### Acessar Session Manager
- **SSM** → **Session Manager** → **Start session** na `Jam-Instance-Test`

#### Executar Testes
Execute os comandos que o challenge fornece em **Output Properties**:

```bash
# Teste IPv4
curl --ipv4 <Task5IPv4Command>

# Teste IPv6
curl --ipv6 <Task5IPv6Command>
```

### 3. Interpretar Resultados

#### Comportamento Esperado
- **IPv4 request:** Comunicação direta IPv4→IPv4
- **IPv6 request:** NLB traduz IPv6→IPv4 para o target
- **Ambos funcionam:** Graças à tradução do NLB

#### Exemplo de Resposta IPv4
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

#### Exemplo de Resposta IPv6
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

### Validação Adicional
Ambos devem responder ✅ (porque o NLB traduz IPv6→IPv4).

## 📚 Conceitos Aprendidos

### NLB Translation IPv6→IPv4
- **Bidirectional:** NLB traduz em ambas as direções
- **IPv6 client → IPv4 target:** Tradução automática
- **IPv4 client → IPv4 target:** Comunicação direta
- **Preserve source IP:** Mantém IP original do cliente

### Network Load Balancer Features
- **Layer 4:** Trabalha na camada de transporte
- **High performance:** Ultra-low latency
- **Connection preservation:** Mantém conexões ativas
- **Static IP:** IPs estáticos por AZ

### Target Communication
O load balancer se comunica com targets baseado no tipo de endereço IP do target group.

## 🎓 Lições Importantes

1. **NLB traduz IPv6→IPv4:** Tradução automática transparente
2. **Targets IPv4-only funcionam:** NLB cuida da compatibilidade
3. **High performance:** NLB é mais rápido que ALB
4. **Propagação é crucial:** Aguardar até 3 minutos

## 🔍 Diferenças ALB vs NLB

### Translation Capabilities
| Aspecto | ALB | NLB |
|---------|-----|-----|
| **IPv4→IPv6** | ✅ | ✅ |
| **IPv6→IPv4** | ✅ | ✅ |
| **Performance** | Média | Alta |
| **Layer** | 7 (HTTP) | 4 (TCP) |

### Use Cases
- **ALB:** Web applications, HTTP/HTTPS
- **NLB:** High-performance apps, TCP/UDP, Gaming

## 🚀 Benefícios

### Para Performance
- **Ultra-low latency:** NLB é mais rápido
- **Connection preservation:** Mantém conexões ativas
- **Static IP:** IPs estáticos por AZ

### Para Arquitetura
- **IPv4 targets:** Compatibilidade com infraestrutura existente
- **IPv6 clients:** Suporte para clientes modernos
- **Migration path:** Permite migração gradual

## 🔧 Configurações Avançadas

### Target Group Settings
- **Protocol:** TCP, UDP, TCP_UDP
- **Port:** Porta de destino
- **Health check:** Configurações de verificação
- **Stickiness:** Session affinity (se aplicável)

### Health Checks
- **Protocol:** TCP, HTTP, HTTPS
- **Port:** Porta de destino
- **Path:** Para health checks HTTP/HTTPS
- **Interval:** Frequência das verificações

---

**🎯 Resultado:** NLB configurado com target IPv4-only, demonstrando alta performance com tradução IPv6→IPv4.