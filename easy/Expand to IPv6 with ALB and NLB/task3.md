# Task 3: ALB Target IPv6 Only

## 🎯 Objetivo

**Task 3:** ALB Target IPv6 Only  
**Pontos Possíveis:** 12  
**Penalidade de Pista:** 0  
**Pontos Disponíveis:** 12

## 📋 Contexto

### Situação Atual
Sua aplicação usa Application Load Balancer (ALB). O ALB chamado `Jam-ALB` está configurado em modo dualstack.

### Objetivo
Você foi solicitado a garantir que seu ALB suporte targets rodando com IPv6 em subnets IPv6-only.

### Conceito Importante
Você notará que pode acessar seu ALB configurado com target group que responde apenas em IPv6 (target group `Jam-ALB-IPv6-Only`), mesmo quando acessar através de IPv4. O ALB é responsável por "traduzir" a comunicação entre IPv4 e IPv6.

## 🛠️ Inventário

### Recursos Disponíveis
- **Application Load Balancer:** `Jam-ALB` (configurado em dualstack)
- **Target Group:** `Jam-ALB-IPv6-Only` (instâncias IPv6-only)
- **Comandos de teste:** Disponíveis em Output Properties

### Comandos de Teste
- **IPv4 test command:** `Task3IPv4Command`
- **IPv6 test command:** `Task3IPv6Command`

## 🔧 Sua Tarefa

1. Alterar o ALB `Jam-ALB` para usar o target group `Jam-ALB-IPv6-Only`
2. Conectar na instância `Jam-Instance-Test` usando Session Manager
3. Fazer requisição curl usando IPv4
4. Fazer requisição curl usando IPv6

> **⚠️ Importante:** Load Balancers pertencem ao console EC2.

> **⏱️ Atenção:** Pode levar tempo após você alterar o Load Balancer para usar o novo target group. Aguarde até 3 minutos para a mudança se aplicar e propagar. O Load Balancer ainda pode apontar para o target group antigo até ser aplicado!

## ✅ Solução Passo a Passo

### 1. Configurar ALB Target Group

#### Acessar o Console
- **EC2 Console** → **Load Balancers** → **`Jam-ALB`**

#### Alterar Listener
- Aba **"Listeners"** → selecione o listener (geralmente HTTP:80)
- Clique em **"Edit rules"**

#### Configurar Forwarding
- Na ação default, escolha **Forward** → **`Jam-ALB-IPv6-Only`**
- Clique em **"Save"**

#### Aguardar Propagação
- Aguarde ~3 minutos para propagar

### 2. Validar Configuração

#### Acessar Session Manager
- **SSM** → **Session Manager** → **Start session** na `Jam-Instance-Test`

#### Executar Testes
Execute os comandos do painel **Output Properties**:

```bash
# Teste IPv4
curl --ipv4 <Task3IPv4Command>

# Teste IPv6
curl --ipv6 <Task3IPv6Command>
```

### 3. Interpretar Resultados

#### Comportamento Esperado
- **IPv4 request:** ALB traduz IPv4→IPv6 para o target
- **IPv6 request:** Comunicação direta IPv6→IPv6
- **Ambos funcionam:** Graças à tradução do ALB

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
Se as duas respostas vierem OK, clique **"Check my progress"** ✅

## 📚 Conceitos Aprendidos

### ALB Translation IPv4→IPv6
- **Bidirectional:** ALB traduz em ambas as direções
- **IPv4 client → IPv6 target:** Tradução automática
- **IPv6 client → IPv6 target:** Comunicação direta

### IPv6-Only Targets
- **Modern approach:** Targets nativos IPv6
- **Future-proof:** Preparado para mundo IPv6-only
- **Performance:** Sem overhead de tradução IPv6→IPv6

### Load Balancer Communication
O load balancer se comunica com targets baseado no tipo de endereço IP do target group.

## 🎓 Lições Importantes

1. **ALB traduz em ambas direções:** IPv4↔IPv6 automaticamente
2. **Targets IPv6-only são viáveis:** ALB cuida da compatibilidade
3. **Propagação é crucial:** Aguardar até 3 minutos
4. **Headers mostram tradução:** `HTTP_X_FORWARDED_FOR` preserva IP original

## 🔍 Troubleshooting

### Problemas Comuns
- **Target group antigo ainda ativo:** Aguardar propagação completa
- **Health checks falhando:** Verificar se targets IPv6 estão saudáveis
- **Comandos não funcionam:** Usar exatamente os comandos do Output Properties

### Verificações
- Ambos os protocolos devem funcionar
- Headers devem mostrar tradução (IPv4→IPv6)
- Server address deve ser IPv6 (target IPv6-only)

## 🚀 Benefícios

### Para Arquitetura
- **Flexibilidade:** Suporta clientes IPv4 e IPv6
- **Modernização:** Targets nativos IPv6
- **Escalabilidade:** Preparado para crescimento IPv6

### Para Performance
- **IPv6→IPv6:** Comunicação direta (mais rápida)
- **IPv4→IPv6:** Tradução transparente
- **Load balancing:** Distribui tráfego eficientemente

---

**🎯 Resultado:** ALB configurado com target IPv6-only, demonstrando tradução bidirecional IPv4↔IPv6.