# Task 1: Egress-Only Internet Gateway (IPv6)

## 🎯 Objetivo

Implementar uma solução de segurança IPv6 que **bloqueie todo acesso público de entrada** via IPv6 para a instância EC2, mantendo a **capacidade de conexões de saída** para a internet, sem usar NAT Gateway ou NAT Instance devido a restrições de custo.

## 📊 Cenário

### Situação Inicial
Você acabou de ingressar na **ABC Corp** como especialista em rede, assumindo a infraestrutura AWS de um funcionário anterior que saiu abruptamente. Durante sua auditoria de segurança inicial, descobriu um **problema crítico de segurança**:

- ✅ **EC2 instance** na VPC `AWS-Jam-FixIPV6` 
- ❌ **Acesso público IPv6 irrestrito** - risco de segurança significativo
- ❌ **Porta 3389 (RDP)** acessível publicamente via IPv6

### Requisitos de Segurança
A equipe de segurança solicitou uma solução IPv6 abrangente que:

- ✅ **Bloqueie todo acesso público IPv6 de entrada** para mitigar o risco imediato
- ✅ **Mantenha a capacidade de conexões de saída** para a internet via IPv6
- ❌ **Não use NAT Gateway ou NAT Instance** (restrições de otimização de custo)

## 🔍 Verificação Inicial

### Teste de Conectividade IPv6
Antes de implementar a solução, **verifique que a porta 3389 está aberta** no endereço IPv6 da instância:

#### Opção 1: Ferramenta Online
1. **Acesse** https://portchecker.co/
2. **Digite** o endereço IPv6 da instância e porta 3389
3. **Clique** "Check" para verificar se a porta está aberta

#### Opção 2: Telnet (se tiver conectividade IPv6)
```bash
# Abrir terminal/prompt de comando
telnet [IPv6_address] 3389

# Se conseguir conectar, a porta está aberta
```

#### Opção 3: Teste RDP
1. **Use um cliente RDP** que suporte IPv6
2. **Tente conectar** ao endereço IPv6 da instância
3. **Confirme** que a conexão é bem-sucedida

### Resultado Esperado
- ✅ **Porta 3389 acessível** via IPv6 (confirmando vulnerabilidade)
- ✅ **RDP funcionando** via endereço IPv6 público

## 🔧 Solução: Egress-Only Internet Gateway

### Conceito da Solução
O **Egress-Only Internet Gateway (EIGW)** é um componente de rede que:
- ✅ **Permite tráfego de saída** IPv6 da VPC para a internet
- ❌ **Bloqueia tráfego de entrada** IPv6 da internet para a VPC
- 💰 **Sem custos adicionais** (diferente do NAT Gateway)

### Arquitetura da Solução
```
Internet IPv6
    ↓
Egress-Only Internet Gateway (EIGW)
    ↓
VPC (AWS-Jam-FixIPV6)
    ↓
EC2 Instance
```

## 🚀 Implementação Passo a Passo

### 1. Criar Egress-Only Internet Gateway

#### Via AWS Console
1. **Acessar VPC Console** → Amazon VPC
2. **Navegar para** "Egress-only internet gateways"
3. **Clicar** "Create egress-only internet gateway"
4. **Selecionar** a VPC `AWS-Jam-FixIPV6`
5. **Adicionar tag** (opcional): `Name: IPv6-Security-EIGW`
6. **Clicar** "Create egress-only internet gateway"
7. **Anotar** o ID do EIGW criado (ex: `eigw-xxxxxxxxx`)

#### Via AWS CLI
```bash
# Criar Egress-Only Internet Gateway
aws ec2 create-egress-only-internet-gateway \
  --vpc-id vpc-xxxxxxxxx \
  --tag-specifications 'ResourceType=egress-only-internet-gateway,Tags=[{Key=Name,Value=IPv6-Security-EIGW}]'
```

### 2. Configurar Route Table

#### Identificar Route Table
1. **Acessar VPC Console** → Route tables
2. **Localizar** a route table associada ao subnet da instância
3. **Verificar** a rota IPv6 atual (provavelmente apontando para IGW)

#### Rota IPv6 Atual (Problemática)
```
Destination: ::/0
Target: igw-xxxxxxxxx (Internet Gateway)
```

#### Editar Rota IPv6
1. **Selecionar** a route table do subnet da instância
2. **Ir para aba** "Routes"
3. **Localizar** a rota IPv6 com destino `::/0`
4. **Clicar** "Edit routes"
5. **Editar** a rota IPv6:
   - **Destination:** `::/0` (manter)
   - **Target:** `eigw-xxxxxxxxx` (Egress-Only Internet Gateway)
6. **Clicar** "Save changes"

#### Via AWS CLI
```bash
# Listar route tables
aws ec2 describe-route-tables \
  --filters "Name=vpc-id,Values=vpc-xxxxxxxxx"

# Editar rota IPv6
aws ec2 replace-route \
  --route-table-id rtb-xxxxxxxxx \
  --destination-ipv6-cidr-block ::/0 \
  --egress-only-internet-gateway-id eigw-xxxxxxxxx
```

### 3. Verificar Configuração

#### Route Table Final
```
Destination: ::/0
Target: eigw-xxxxxxxxx (Egress-Only Internet Gateway)
```

#### Validação
- ✅ **Egress-Only Internet Gateway** criado e anexado à VPC
- ✅ **Route table** atualizada com rota IPv6 para EIGW
- ✅ **Configuração** salva e aplicada

## ✅ Resultado

### Segurança Implementada
- ✅ **Acesso público IPv6 bloqueado** - Instância não mais acessível via IPv6
- ✅ **Conexões de saída mantidas** - Instância pode acessar internet via IPv6
- ✅ **Sem custos adicionais** - EIGW é gratuito (diferente do NAT Gateway)
- ✅ **Sem alteração de Security Groups** - Solução puramente de roteamento

### Teste de Validação
Após implementar a solução:

#### Teste 1: Acesso de Entrada (deve falhar)
```bash
# Tentar conectar via RDP IPv6 (deve falhar)
telnet [IPv6_address] 3389
# Resultado esperado: Connection refused ou timeout
```

#### Teste 2: Acesso de Saída (deve funcionar)
```bash
# Na instância EC2, testar conectividade de saída
ping6 google.com
# Resultado esperado: Resposta de ping bem-sucedida
```

## 🔍 Detalhes Técnicos

### Egress-Only Internet Gateway vs Internet Gateway

| Aspecto | Internet Gateway (IGW) | Egress-Only Internet Gateway (EIGW) |
|---------|------------------------|-------------------------------------|
| **Tráfego de Entrada** | ✅ Permitido | ❌ Bloqueado |
| **Tráfego de Saída** | ✅ Permitido | ✅ Permitido |
| **Custo** | Gratuito | Gratuito |
| **Uso** | IPv4 e IPv6 | Apenas IPv6 |
| **NAT** | Não necessário | Não necessário |

### Arquitetura de Rede IPv6

#### Antes (Inseguro)
```
Internet IPv6 ←→ Internet Gateway ←→ VPC ←→ EC2 Instance
     ↑                                    ↓
   Acesso público                    Vulnerável
```

#### Depois (Seguro)
```
Internet IPv6 → Egress-Only IGW → VPC ← EC2 Instance
     ↑ (bloqueado)                    ↓ (permitido)
   Acesso negado                  Saída liberada
```

### Route Table Configuration
```json
{
  "RouteTableId": "rtb-xxxxxxxxx",
  "Routes": [
    {
      "DestinationCidrBlock": "0.0.0.0/0",
      "GatewayId": "igw-xxxxxxxxx",
      "State": "active"
    },
    {
      "DestinationIpv6CidrBlock": "::/0",
      "EgressOnlyInternetGatewayId": "eigw-xxxxxxxxx",
      "State": "active"
    }
  ]
}
```

## 🚨 Troubleshooting

### Problemas Comuns

#### Egress-Only Internet Gateway não criado
- **Verificar permissões** IAM para criar recursos VPC
- **Confirmar região** correta no console
- **Aguardar propagação** (pode levar alguns minutos)

#### Route table não atualizada
- **Verificar** se está editando a route table correta
- **Confirmar** que o EIGW está anexado à VPC
- **Salvar** as mudanças na route table

#### Acesso de saída não funciona
- **Verificar** se a rota IPv6 está correta
- **Confirmar** que o EIGW está ativo
- **Testar** conectividade IPv6 da instância

### Comandos de Diagnóstico
```bash
# Verificar Egress-Only Internet Gateways
aws ec2 describe-egress-only-internet-gateways

# Verificar route tables
aws ec2 describe-route-tables \
  --filters "Name=vpc-id,Values=vpc-xxxxxxxxx"

# Testar conectividade IPv6 da instância
aws ec2 describe-instances \
  --instance-ids i-xxxxxxxxx \
  --query 'Reservations[0].Instances[0].Ipv6Addresses'
```

## 💡 Considerações Importantes

### Segurança
- **EIGW bloqueia** apenas tráfego IPv6 de entrada
- **Security Groups** ainda são necessários para IPv4
- **Network ACLs** podem ser usados para controle adicional
- **Defense in depth** - múltiplas camadas de segurança

### Custos
- **Egress-Only Internet Gateway** é gratuito
- **Data transfer** de saída tem custos normais
- **Sem custos** de NAT Gateway ou NAT Instance
- **Otimização** de custos mantida

### Limitações
- **Apenas IPv6** - não afeta tráfego IPv4
- **Bidirecional** - bloqueia entrada, permite saída
- **VPC-wide** - afeta toda a VPC, não apenas uma instância
- **Não configurável** - comportamento fixo do EIGW

## 🎓 Lições Aprendidas

### Segurança IPv6
- **IPv6 é habilitado por padrão** em muitas VPCs
- **Acesso público** pode ser um risco de segurança
- **Egress-Only IGW** é a solução padrão para IPv6 seguro
- **Defense in depth** é essencial

### Networking AWS
- **Route tables** controlam direcionamento de tráfego
- **Internet Gateways** permitem acesso bidirecional
- **Egress-Only IGW** permite apenas saída
- **Configuração** é simples mas efetiva

### Troubleshooting
- **Teste antes e depois** para validar mudanças
- **Verifique route tables** para problemas de conectividade
- **Use ferramentas online** para testar acessibilidade
- **Documente** configurações para referência futura

---

**🎉 Task 1 Concluída!**

> **💭 Reflexão:** O Egress-Only Internet Gateway é uma solução elegante para segurança IPv6, oferecendo proteção contra ataques externos mantendo a funcionalidade de saída, tudo sem custos adicionais. Esta solução demonstra como a AWS oferece ferramentas específicas para diferentes cenários de segurança.