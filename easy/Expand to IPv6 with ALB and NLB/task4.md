# Task 4: NLB IP Address Type Dualstack

## 🎯 Objetivo

**Task 4:** NLB IP Address Type Dualstack  
**Pontos Possíveis:** 16  
**Penalidade de Pista:** 0  
**Pontos Disponíveis:** 16

## 📋 Contexto

### Problema
Sua aplicação usa Network Load Balancer (NLB). O NLB chamado `Jam-NLB` foi criado com tipo de endereço IP IPv4. Seus clientes só conseguem acessar sua aplicação usando IPv4. Com IPv6, falha.

### Solução Necessária
Você foi solicitado a garantir que seu NLB suporte IPv4 e IPv6, para que clientes possam enviar requisições com ambas as versões de IP.

Tudo mais já está preparado para seu NLB funcionar com IPv6 também, conforme definido nos requisitos dualstack.

## 🛠️ Inventário

### Recursos Disponíveis
- **Network Load Balancer:** `Jam-NLB` (inicialmente IPv4-only)
- **Console:** EC2 Console (Load Balancers estão no EC2)

## 🔧 Sua Tarefa

Alterar o NLB chamado `Jam-NLB` para usar o tipo de endereço IP `dualstack`.

> **⚠️ Importante:** Load Balancers pertencem ao console EC2.

Você não precisa alterar nada mais, apenas o tipo de endereço IP.

## ✅ Solução Passo a Passo

### 1. Acessar o Console AWS
- Navegue para **EC2 Console** → **Load Balancers**
- Localize o **`Jam-NLB`**

### 2. Editar Configurações
- Clique no **`Jam-NLB`**
- Clique em **"Edit IP Address Type"**

### 3. Alterar para Dualstack
- Em **"IP address type"**, altere de **`ipv4`** para **`dualstack`**
- Clique em **"Save"**

### 4. Aguardar Propagação
- Aguarde alguns minutos para as mudanças se propagarem
- O NLB agora suportará tanto IPv4 quanto IPv6

## 🧪 Validação

### Critério de Sucesso
A tarefa será automaticamente completada assim que você realizar a alteração do tipo de endereço IP do NLB.

### Verificação Manual
Alternativamente, você pode sempre verificar seu progresso clicando no botão **"Check my progress"** na tela de detalhes do desafio.

## 📚 Conceitos Aprendidos

### Network Load Balancer (NLB)
- **Layer 4:** Trabalha na camada de transporte (TCP/UDP)
- **High Performance:** Baixa latência e alta throughput
- **Static IP:** Pode ter endereços IP estáticos
- **Connection Preservation:** Mantém conexões ativas

### Dualstack NLB
- **IPv4 + IPv6:** Suporta ambos os protocolos simultaneamente
- **DNS Resolution:** Retorna tanto endereços IPv4 quanto IPv6
- **Translation:** Faz tradução automática entre protocolos

### Diferenças ALB vs NLB
| Aspecto | ALB (Application) | NLB (Network) |
|---------|-------------------|---------------|
| **Layer** | 7 (HTTP/HTTPS) | 4 (TCP/UDP) |
| **Performance** | Média | Alta |
| **Features** | Content routing | Static IP |
| **Use Case** | Web apps | High performance |

## 🎓 Lições Importantes

1. **NLB é Layer 4:** Trabalha com TCP/UDP, não HTTP
2. **Dualstack é simples:** Apenas uma configuração a alterar
3. **High performance:** NLB é mais rápido que ALB
4. **Static IP:** NLB pode ter IPs estáticos

## 🔍 Características do NLB

### Vantagens
- **Ultra-low latency:** Latência extremamente baixa
- **Static IP addresses:** IPs estáticos para cada AZ
- **Preserve source IP:** Mantém IP original do cliente
- **Long-lived connections:** Suporta conexões longas

### Casos de Uso
- **High-performance applications:** Apps que precisam de máxima performance
- **Static IP requirements:** Quando IPs estáticos são necessários
- **TCP/UDP traffic:** Tráfego que não é HTTP/HTTPS
- **Gaming applications:** Jogos online com baixa latência

## 🚀 Próximos Passos

Após completar esta tarefa:
- O NLB `Jam-NLB` suportará IPv4 e IPv6
- Estará pronto para as próximas tarefas (configuração de targets)
- Clientes poderão acessar via ambos os protocolos

## 🔧 Configurações Adicionais

### Health Checks
- **Protocol:** TCP, HTTP, HTTPS
- **Port:** Porta de destino
- **Path:** Para health checks HTTP/HTTPS
- **Interval:** Frequência das verificações

### Target Groups
- **Protocol:** TCP, UDP, TCP_UDP
- **Port:** Porta de destino
- **Health check:** Configurações de verificação
- **Stickiness:** Session affinity (se aplicável)

## 📊 Monitoramento

### CloudWatch Metrics
- **ActiveConnectionCount:** Número de conexões ativas
- **NewConnectionCount:** Novas conexões por minuto
- **ConsumedLCUs:** Load Balancer Capacity Units consumidas
- **HealthyHostCount:** Número de targets saudáveis

### Logs
- **Access logs:** Registro de requisições (opcional)
- **Target response logs:** Logs de resposta dos targets

---

**🎯 Resultado:** NLB configurado como dualstack, preparado para alta performance com suporte IPv4 e IPv6.