# Task 6: NLB Target IPv6 Only

## 🎯 Objetivo

**Task 6:** NLB Target IPv6 Only  
**Pontos Possíveis:** 12  
**Penalidade de Pista:** 0  
**Pontos Disponíveis:** 12

## 📋 Contexto

### Situação Atual
Sua aplicação usa Network Load Balancer (NLB). O NLB chamado `Jam-NLB` está configurado em modo dualstack.

### Objetivo
Você foi solicitado a garantir que seu NLB suporte targets rodando com IPv6 em subnets IPv6-only.

### Conceito Importante
Você notará que pode acessar seu NLB configurado com target group que responde apenas em IPv6 (target group `Jam-NLB-IPv6-Only`), mesmo quando acessar através de IPv4. O NLB é responsável por "traduzir" a comunicação entre IPv4 e IPv6.

## 🛠️ Inventário

### Recursos Disponíveis
- **Network Load Balancer:** `Jam-NLB` (configurado em dualstack)
- **Target Group:** `Jam-NLB-IPv6-Only` (instâncias IPv6-only)
- **Comandos de teste:** Disponíveis em Output Properties

### Comandos de Teste
- **IPv4 test command:** `Task6IPv4Command`
- **IPv6 test command:** `Task6IPv6Command`

## 🔧 Sua Tarefa

1. Alterar o NLB `Jam-NLB` para usar o target group `Jam-NLB-IPv6-Only`
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
- Na aba **"Listeners"**, selecione o listener (porta TCP/HTTP configurada)
- Clique em **"Edit"**

#### Configurar Forwarding
- Altere a ação default para **Forward** → **`Jam-NLB-IPv6-Only`**
- Clique em **"Save changes"**

#### Aguardar Propagação
- Aguarde ~3 minutos para propagar

### 2. Validar Configuração

#### Acessar Session Manager
- **SSM** → **Session Manager** → **Start session** na `Jam-Instance-Test`

#### Executar Testes
Execute os comandos que aparecem em **Output Properties**:

```bash
# Teste IPv4
curl --ipv4 <Task6IPv4Command>

# Teste IPv6
curl --ipv6 <Task6IPv6Command>
```

### 3. Interpretar Resultados

#### Comportamento Esperado
- **IPv4 request:** NLB traduz IPv4→IPv6 para o target
- **IPv6 request:** Comunicação direta IPv6→IPv6
- **Ambos funcionam:** Graças à tradução do NLB

#### Exemplo de Resposta IPv4
```
Jam IPv6 with ALB and NLB

You requested using IPv4 address '98.88.216.104'.
Server behind Load Balancer is IPv6 '2001:db8::1'.

As Load Balancer is dualstack, it translated your request from IPv4 to IPv6.

Request detail:
HTTP_X_FORWARDED_FOR=98.88.216.104
HTTP_X_FORWARDED_PORT=80
HTTP_X_FORWARDED_PROTO=http
REMOTE_ADDR=2001:db8::2
REMOTE_PORT=2868
SERVER_ADDR=2001:db8::1
```

#### Exemplo de Resposta IPv6
```
Jam IPv6 with ALB and NLB

You requested using IPv6 address '2600:1f18:3a26:4100:5ed8:d11d:6918:4282'.
Server behind Load Balancer is also IPv6 '2001:db8::1'.

Request detail:
HTTP_X_FORWARDED_FOR=2600:1f18:3a26:4100:5ed8:d11d:6918:4282
HTTP_X_FORWARDED_PORT=80
HTTP_X_FORWARDED_PROTO=http
REMOTE_ADDR=2001:db8::2
REMOTE_PORT=2868
SERVER_ADDR=2001:db8::1
```

## 🧪 Validação

### Critério de Sucesso
A tarefa será automaticamente completada quando você realizar as requisições curl usando IPv4 e IPv6.

### Verificação Manual
Clique no botão **"Check my progress"** na tela de detalhes do desafio.

### Validação Adicional
Ambos devem retornar resposta ✅. Mesmo com target IPv6-only, o NLB cuida da tradução e funciona também para IPv4.

## 📚 Conceitos Aprendidos

### NLB Translation IPv4→IPv6
- **Bidirectional:** NLB traduz em ambas as direções
- **IPv4 client → IPv6 target:** Tradução automática
- **IPv6 client → IPv6 target:** Comunicação direta
- **High performance:** Ultra-low latency mesmo com tradução

### IPv6-Only Targets com NLB
- **Modern architecture:** Targets nativos IPv6
- **Future-proof:** Preparado para mundo IPv6-only
- **High performance:** Máxima performance com IPv6
- **Backward compatibility:** Suporte IPv4 via tradução

### Network Load Balancer Advantages
- **Layer 4:** Trabalha na camada de transporte
- **Ultra-low latency:** Latência extremamente baixa
- **Static IP:** IPs estáticos por AZ
- **Connection preservation:** Mantém conexões ativas

## 🎓 Lições Importantes

1. **NLB traduz IPv4→IPv6:** Tradução automática transparente
2. **Targets IPv6-only são viáveis:** NLB cuida da compatibilidade
3. **High performance:** NLB mantém performance mesmo com tradução
4. **Propagação é crucial:** Aguardar até 3 minutos

## 🔍 Comparação ALB vs NLB IPv6

### Translation Performance
| Aspecto | ALB | NLB |
|---------|-----|-----|
| **IPv4→IPv6** | ✅ | ✅ (mais rápido) |
| **IPv6→IPv4** | ✅ | ✅ (mais rápido) |
| **Latency** | Média | Ultra-low |
| **Throughput** | Médio | Alto |

### Use Cases
- **ALB:** Web applications, HTTP/HTTPS routing
- **NLB:** High-performance apps, Gaming, IoT

## 🚀 Benefícios

### Para Performance
- **Ultra-low latency:** NLB é mais rápido que ALB
- **High throughput:** Suporta mais conexões simultâneas
- **IPv6→IPv6:** Comunicação direta (máxima performance)
- **IPv4→IPv6:** Tradução otimizada

### Para Arquitetura
- **Modern targets:** Infraestrutura IPv6 nativa
- **Future-proof:** Preparado para transição IPv6-only
- **Flexibility:** Suporta clientes IPv4 e IPv6
- **Scalability:** IPv6 oferece endereços praticamente ilimitados

## 🔧 Configurações Avançadas

### Target Group IPv6
- **Protocol:** TCP, UDP, TCP_UDP
- **Port:** Porta de destino IPv6
- **Health check:** Verificações IPv6
- **Target type:** Instance, IP, Lambda

### Health Checks IPv6
- **Protocol:** TCP, HTTP, HTTPS
- **Port:** Porta IPv6
- **Path:** Para health checks HTTP/HTTPS
- **IPv6 addresses:** Targets com endereços IPv6

## 📊 Monitoramento IPv6

### CloudWatch Metrics
- **ActiveConnectionCount:** Conexões IPv4 e IPv6
- **NewConnectionCount:** Novas conexões por protocolo
- **HealthyHostCount:** Targets IPv6 saudáveis
- **ConsumedLCUs:** Load Balancer Capacity Units

### Logs IPv6
- **Access logs:** Registro de requisições IPv4/IPv6
- **Target response logs:** Logs de resposta IPv6

## 🌐 IPv6 Benefits

### Endereçamento
- **Practically unlimited:** Endereços IPv6 são praticamente ilimitados
- **No NAT required:** Elimina necessidade de NAT
- **Direct addressing:** Comunicação direta entre dispositivos

### Performance
- **Larger packets:** IPv6 suporta pacotes maiores
- **Simplified headers:** Headers mais simples e eficientes
- **Better routing:** Roteamento mais eficiente

---

**🎯 Resultado:** NLB configurado com target IPv6-only, demonstrando alta performance com tradução IPv4→IPv6 e preparação para o futuro IPv6.