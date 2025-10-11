# Task 1: Getting Access to Private Node via Bastion Host

**Pontos Possíveis:** 45  
**Penalidade de Dica:** 0  
**Pontos Disponíveis:** 45  
**Check my progress:** Disponível

---

## 🚨 AVISO - TASK COM PROBLEMA DE PERMISSÕES

> **❌ ESTA TASK NÃO PODE SER COMPLETADA**
> 
> **Problema:** O usuário do laboratório não possui permissões IAM para modificar Security Groups. Especificamente, faltam:
> - `ec2:AuthorizeSecurityGroupIngress`
> - `ec2:AuthorizeSecurityGroupEgress`
>
> **Erro retornado:** `You are not authorized to perform: ec2:AuthorizeSecurityGroupIngress`
>
> Esta documentação serve para fins educacionais e demonstra o troubleshooting realizado.

---

## 📖 Background

Para investigar os problemas de falha de comunicação de rede entre a instância Amazon EC2 provisionada em rede privada e o serviço AWS Systems Manager, os detalhes da instância EC2 privada são fornecidos juntamente com os detalhes de um **Bastion Host** (servidor de salto).

Como a instância EC2 afetada está em uma rede privada, ela não pode ser acessada diretamente para troubleshooting. Portanto, você recebe outro **Bastion Host** (jump server) na mesma Amazon VPC, mas em uma subnet pública.

Você terá que:
1. Primeiro conectar ao Bastion Host (jump server)
2. De lá, conectar à instância EC2 privada via RDP (Remote Desktop Protocol)

### 🔴 Problema Observado

Ao tentar conectar o Bastion Host, você observou que esta instância EC2 **não tem conectividade com a Internet**. Para acessar a instância do seu escritório doméstico, você precisa configurar as definições de rede que habilitarão RDP assim como acesso à Internet para a instância EC2 Bastion.

## 🎯 Sua Tarefa

Sua tarefa é:

1. ✅ **Identificar** a instância Windows EC2 Bastion (jump server)
2. ❌ **Habilitar RDP e acesso à Internet** no Security Group da instância (BLOQUEADO)
3. ❌ **Conectar** à instância EC2 Bastion via RDP (IMPOSSÍVEL sem passo 2)

## 📚 Getting Started

### Identificar a Instância Bastion

Do Console de Gerenciamento EC2, identifique a instância EC2 Bastion referenciando o `BastionInstanceID` fornecido na seção **Output Properties**.

### Habilitar RDP e Acesso à Internet

**⚠️ ESTE É O PASSO QUE ESTÁ QUEBRADO**

Por favor, garanta que o acesso RDP à instância Bastion seja permitido da sua rede de origem adicionando a regra inbound correspondente no Security Group associado (especifique Source como **"My IP"**).

Adicionalmente, verifique se o tráfego de Internet é permitido na regra outbound do mesmo Security Group.

### Conectar à Instância EC2 Bastion via RDP

Após habilitar RDP e acesso à Internet, conecte à instância Windows EC2 Bastion via cliente RDP da sua máquina Windows de origem (para macOS, baixe o aplicativo Microsoft Remote Desktop da App Store) usando seu endereço IPv4 público que pode ser determinado do Console de Gerenciamento EC2 referenciando o ID da Instância EC2 fornecido e as credenciais de login do usuário na seção Output Properties.

## 📦 Inventário

- **Amazon EC2 Windows Instance** chamada `Bastion-JumpServer`
- **Private Amazon EC2 Windows Instance** chamada `Private-ProductionServer`
- **Security Group** anexado à instância EC2 Bastion chamado `Bastion-SecurityGroup`
- Verifique a seção **Output Properties** para:
  - EC2 Instance ID
  - Security Group ID
  - Credenciais de login

## 🛠️ Serviços que Você Deve Usar

- **Amazon Elastic Compute Cloud (Amazon EC2)**
- **Acesso via Remote Desktop Protocol (RDP) client**

## ✅ Validação da Tarefa

Uma vez que você tenha habilitado RDP e acesso à Internet para a instância EC2 Bastion, por favor conecte à mesma via RDP usando as credenciais de login fornecidas do seu endereço de origem permitido.

Se você conseguir conectar com sucesso, então prossiga para validar esta tarefa inserindo seu endereço IPv4 público de origem no campo de entrada, para o qual você permitiu o acesso RDP no Security Group da instância.

**Formato esperado:**
```
seu-ip-publico/32
```

**Exemplo:**
Se seu endereço IPv4 público de origem de onde você consegue conectar a instância via RDP é `54.32.12.34`, então insira no campo de entrada desta tarefa:
```
54.32.12.34/32
```

### ⚠️ NOTAS IMPORTANTES

- O endereço IPv4 de origem que você inserir no campo de entrada da tarefa deve ser aquele para o qual você permitiu acesso RDP no Security Group da instância
- Se você está conectado a uma conexão VPN, por favor garanta que o endereço IPv4 selecionado pela opção Source como **My IP** no Security Group da instância é o correto
- Se você encontrar qualquer problema de RDP, então desconecte da VPN, modifique a regra inbound novamente para escolher Source como **My IP** e então tente novamente a conexão RDP

---

## 🔍 Resolução & Análise Técnica

### 🧾 Relato Técnico Completo

#### Objetivo da Task

Habilitar:
- Acesso **RDP** (porta TCP 3389) a partir do meu IP público
- Tráfego de saída **HTTPS** (porta 443 → 0.0.0.0/0) para o Bastion Host

Conforme instruções do enunciado e da seção "Help me get started".

---

### 📋 Passos Executados & Troubleshooting

#### 1️⃣ Localização da Instância Bastion

**Ação:**
- Acessei EC2 Console → Instances
- Localizei a instância com ID: `i-0acc57204998d2389`
- Nome: `Bastion-JumpServer`

**Informações coletadas:**
```
Instance ID: i-0acc57204998d2389
Instance Type: (verificar no console)
Availability Zone: (verificar no console)
Public IPv4: (disponível no console)
Security Group: sg-02c44112d02f50131
```

**Status:** ✅ Instância identificada com sucesso

---

#### 2️⃣ Verificação de Conectividade de Rede

**Análise da Subnet:**

**Navegação:** VPC → Subnets → Subnet da instância Bastion

**Verificações:**
- [x] Subnet é **pública** (tem rota para Internet Gateway)
- [x] Route Table contém rota: `0.0.0.0/0 → igw-0feceaf2265bffc0f`
- [x] Internet Gateway está **attached** à VPC

**Resultado:** ✅ Acesso à Internet via IGW confirmado no nível de subnet

---

#### 3️⃣ Verificação de Network ACLs

**Navegação:** VPC → Network ACLs → NACL da subnet pública

**Inbound Rules verificadas:**
| Rule # | Type | Protocol | Port Range | Source | Allow/Deny |
|--------|------|----------|------------|--------|------------|
| 100 | RDP | TCP | 3389 | 0.0.0.0/0 | ALLOW |
| 110 | HTTPS | TCP | 443 | 0.0.0.0/0 | ALLOW |
| 120 | HTTP | TCP | 80 | 0.0.0.0/0 | ALLOW |
| 130 | Custom TCP | TCP | 1024-65535 | 0.0.0.0/0 | ALLOW |
| * | All | All | All | 0.0.0.0/0 | DENY |

**Outbound Rules verificadas:**
| Rule # | Type | Protocol | Port Range | Destination | Allow/Deny |
|--------|------|----------|------------|-------------|------------|
| 100 | RDP | TCP | 3389 | 0.0.0.0/0 | ALLOW |
| 110 | HTTPS | TCP | 443 | 0.0.0.0/0 | ALLOW |
| 120 | HTTP | TCP | 80 | 0.0.0.0/0 | ALLOW |
| 130 | Custom TCP | TCP | 1024-65535 | 0.0.0.0/0 | ALLOW |
| * | All | All | All | 0.0.0.0/0 | DENY |

**Análise:**
- ✅ Porta 3389 (RDP) permitida inbound e outbound
- ✅ Porta 443 (HTTPS) permitida inbound e outbound
- ✅ Portas efêmeras (1024-65535) permitidas para tráfego de retorno
- ✅ ACLs estão **corretas e permissivas**

**Resultado:** ✅ Network ACLs não são o problema

---

#### 4️⃣ Análise do Security Group

**Navegação:** EC2 → Security Groups → `Bastion-SecurityGroup` (sg-02c44112d02f50131)

**Inbound Rules encontradas:**

| Type | Protocol | Port Range | Source | Description |
|------|----------|------------|--------|-------------|
| RDP | TCP | 3389 | **10.0.0.0/32** | ⚠️ "Edit this rule and specify source as MyIP" |

**Análise:**
- ⚠️ Fonte está limitada a `10.0.0.0/32` (um único IP privado)
- ⚠️ A descrição da regra indica **explicitamente** que deve ser editada
- ⚠️ Deveria ser alterada para **"My IP"** (meu IP público)

**Outbound Rules encontradas:**

| Type | Protocol | Port Range | Destination | Description |
|------|----------|------------|-------------|-------------|
| HTTPS | TCP | 443 | **10.0.0.0/32** | ⚠️ "Edit this rule and choose Anywhere-IPv4 destination" |

**Análise:**
- ⚠️ Destino está limitado a `10.0.0.0/32` (um único IP privado)
- ⚠️ A descrição da regra indica **explicitamente** que deve ser editada
- ⚠️ Deveria ser alterada para **"Anywhere-IPv4"** (`0.0.0.0/0`)

**Resultado:** ⚠️ Security Group precisa ser modificado conforme descrições

---

#### 5️⃣ Tentativa de Modificação do Security Group

**Ação tentada:**
1. EC2 → Security Groups → sg-02c44112d02f50131
2. Aba **"Inbound rules"** → **"Edit inbound rules"**
3. Tentei modificar a regra 3389 para Source = **"My IP"**

**Resultado:**
```
❌ You are not authorized to perform: ec2:AuthorizeSecurityGroupIngress
```

**Ação tentada:**
1. Aba **"Outbound rules"** → **"Edit outbound rules"**
2. Tentei modificar a regra 443 para Destination = **"Anywhere-IPv4"** (0.0.0.0/0)

**Resultado:**
```
❌ You are not authorized to perform: ec2:AuthorizeSecurityGroupEgress
```

---

### 🚨 Problema Identificado

#### Causa Raiz: Permissões IAM Faltantes

O usuário do laboratório (`AWSLabsUser-...`) **não possui** as seguintes permissões IAM necessárias:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:AuthorizeSecurityGroupIngress",
        "ec2:AuthorizeSecurityGroupEgress"
      ],
      "Resource": "*"
    }
  ]
}
```

#### Impacto

**Não é possível:**
- ✅ Ver Security Groups (permissão de leitura existe)
- ✅ Ver as regras existentes
- ❌ **Modificar regras inbound** (permissão faltando)
- ❌ **Modificar regras outbound** (permissão faltando)
- ❌ Adicionar novas regras
- ❌ Remover regras existentes

**Consequência final:**
- ❌ Impossível habilitar RDP do meu IP
- ❌ Impossível habilitar saída HTTPS para Internet
- ❌ Impossível conectar ao Bastion via RDP
- ❌ Impossível validar a Task 1
- ❌ Impossível prosseguir para Task 2

---

### 📊 Checklist de Troubleshooting Completo

| Item Verificado | Status | Observação |
|----------------|--------|------------|
| Instância Bastion identificada | ✅ OK | i-0acc57204998d2389 |
| Instância em subnet pública | ✅ OK | Subnet tem rota para IGW |
| Route Table com rota 0.0.0.0/0 → IGW | ✅ OK | igw-0feceaf2265bffc0f |
| Internet Gateway attached | ✅ OK | Anexado à VPC |
| Public IPv4 associado | ✅ OK | IP público disponível |
| Network ACL - Inbound 3389 | ✅ OK | Permitido de 0.0.0.0/0 |
| Network ACL - Outbound 443 | ✅ OK | Permitido para 0.0.0.0/0 |
| Network ACL - Portas efêmeras | ✅ OK | 1024-65535 permitidas |
| Security Group existe | ✅ OK | sg-02c44112d02f50131 |
| SG - Regra 3389 criada | ✅ OK | Mas com source incorreto |
| SG - Regra 443 criada | ✅ OK | Mas com destination incorreto |
| SG - Descrições indicam edição | ✅ OK | Instruções claras nas regras |
| **Permissões IAM para editar SG** | ❌ **FALTANDO** | **BLOQUEIO CRÍTICO** |

---

### 🛠️ O Que Deveria Ser Feito (Procedimento Teórico)

Se as permissões IAM estivessem corretas, estes seriam os passos:

#### Passo 1: Modificar Inbound Rule

**Console:** EC2 → Security Groups → sg-02c44112d02f50131

**Ações:**
1. Aba **"Inbound rules"**
2. Click **"Edit inbound rules"**
3. Encontre a regra com porta **3389**
4. **Modificar:**
   - Type: `RDP`
   - Protocol: `TCP`
   - Port range: `3389`
   - Source: **My IP** (selecionar da lista dropdown)
   - Description: `RDP from my public IP`
5. Click **"Save rules"**

**Resultado esperado:**
- Source seria automaticamente preenchido com meu IP público atual
- Formato: `123.45.67.89/32`

#### Passo 2: Modificar Outbound Rule

**Ações:**
1. Aba **"Outbound rules"**
2. Click **"Edit outbound rules"**
3. Encontre a regra com porta **443**
4. **Modificar:**
   - Type: `HTTPS`
   - Protocol: `TCP`
   - Port range: `443`
   - Destination: **Anywhere-IPv4** (0.0.0.0/0)
   - Description: `HTTPS to Internet`
5. Click **"Save rules"**

**Resultado esperado:**
- Destination: `0.0.0.0/0`
- Permitindo saída HTTPS para qualquer endereço

#### Passo 3: Conectar via RDP

**No Windows:**
1. Abrir **Remote Desktop Connection** (mstsc.exe)
2. Computer: `<Public IPv4 do Bastion>` (do console EC2)
3. Click **Connect**
4. Username: `<fornecido em Output Properties>`
5. Password: `<fornecido em Output Properties>`
6. Click **OK**

**No macOS:**
1. Baixar **Microsoft Remote Desktop** da App Store
2. Abrir aplicativo
3. Click **"Add PC"**
4. PC name: `<Public IPv4 do Bastion>`
5. User account: Add username e password
6. Click **Add**
7. Double-click no PC para conectar

#### Passo 4: Validar Conectividade

**Dentro da sessão RDP:**
1. Abrir PowerShell ou CMD
2. Testar conectividade à Internet:
   ```powershell
   Test-NetConnection -ComputerName google.com -Port 443
   ```
3. Resultado esperado: `TcpTestSucceeded: True`

#### Passo 5: Validar Task

**No lab:**
1. Copiar seu IP público (o mesmo usado no Security Group)
2. Adicionar `/32` ao final
3. Submeter no campo de validação

**Exemplo:**
```
123.45.67.89/32
```

---

### 💡 Soluções de Contorno

#### Opção 1: Reportar ao Suporte

**Ações:**
1. Abrir ticket com suporte do AWS Jam
2. Informar o problema de permissões IAM
3. Fornecer detalhes:
   - Lab name: "The Silent Network Crisis"
   - Task: Task 1
   - Erro: `ec2:AuthorizeSecurityGroupIngress` e `ec2:AuthorizeSecurityGroupEgress`
4. Solicitar correção

#### Opção 2: Ambiente Próprio

Se você tem uma conta AWS própria, recrie o cenário:

**Recursos necessários:**
```
1. VPC com CIDR 10.0.0.0/16
2. Subnet pública (10.0.1.0/24)
3. Subnet privada (10.0.2.0/24)
4. Internet Gateway anexado
5. Route Table pública com rota 0.0.0.0/0 → IGW
6. 2 instâncias Windows EC2:
   - Bastion na subnet pública
   - Private na subnet privada
7. Security Groups:
   - Bastion-SG com regras RDP e HTTPS
   - Private-SG com regras necessárias
```

**Pratique:**
- Configuração de Security Groups
- Conexão RDP via Bastion
- Troubleshooting de rede
- Configuração de VPC Endpoints (Task 2)

#### Opção 3: Uso Educacional

**Aproveite para aprender:**
- ✅ Conceitos de Bastion Hosts
- ✅ Diferenças entre Security Groups e NACLs
- ✅ Troubleshooting sistemático de rede
- ✅ Ordem de verificação (Route → NACL → SG → OS → App)
- ✅ Importância de permissões IAM adequadas

---

## 📚 Conceitos Importantes

### 1. Bastion Hosts (Jump Servers)

**Definição:**
Instância EC2 em subnet pública que serve como ponto de entrada seguro para acessar recursos em subnets privadas.

**Características:**
- Localizado em subnet pública
- Tem IP público ou Elastic IP
- Security Group muito restritivo
- Usado para "pular" para instâncias privadas
- Também chamado de "jump server" ou "jump box"

**Benefícios:**
- Reduz superfície de ataque
- Ponto único de acesso (auditável)
- Logs centralizados
- Pode ter 2FA/MFA obrigatório

### 2. Security Groups vs. Network ACLs

**Security Groups:**
- ✅ **Stateful:** Tráfego de retorno automático
- ✅ **Instance-level:** Aplica-se à instância
- ✅ **Allow rules only:** Somente permissões (não deny)
- ✅ **Evaluated together:** Todas as regras são aplicadas

**Network ACLs:**
- ❌ **Stateless:** Precisa de regras explícitas ida/volta
- ❌ **Subnet-level:** Aplica-se à subnet inteira
- ❌ **Allow and Deny:** Pode ter regras de negação
- ❌ **Rule order matters:** Processadas em ordem numérica

### 3. Troubleshooting de Conectividade RDP

**Ordem de verificação:**
1. **Network layer:**
   - Route tables corretas?
   - Internet Gateway anexado?
   - NAT Gateway funcional (se aplicável)?

2. **Subnet layer:**
   - Network ACL permite porta 3389 inbound?
   - Network ACL permite portas efêmeras outbound?

3. **Instance layer:**
   - Security Group permite porta 3389 do meu IP?
   - Security Group permite outbound?

4. **OS layer:**
   - Windows Firewall permite RDP?
   - Serviço Remote Desktop está rodando?

5. **Application layer:**
   - RDP está habilitado no Windows?
   - Usuário tem permissão para login remoto?

### 4. My IP Option

**O que faz:**
- Detecta automaticamente seu IP público atual
- Preenche no formato CIDR (/32)
- Útil para evitar erros de digitação

**Cuidados:**
- Se usa VPN, o IP será o da VPN
- IP pode mudar (ISP dinâmico)
- Corporate networks podem ter IPs diferentes

---

## 🎯 Checklist de Validação (Teórico)

Se o lab funcionasse, use este checklist:

- [ ] Instância Bastion identificada
- [ ] Public IPv4 anotado
- [ ] Credenciais obtidas (Output Properties)
- [ ] Security Group identificado
- [ ] Inbound rule 3389 modificada (My IP)
- [ ] Outbound rule 443 modificada (0.0.0.0/0)
- [ ] Cliente RDP preparado
- [ ] Conexão RDP estabelecida
- [ ] Internet funcional dentro da sessão
- [ ] IP público confirmado (whatismyip.com)
- [ ] Validação submetida (formato /32)
- [ ] Task 1 completada

---

## 📝 Conclusão

### Status Final

| Aspecto | Status | Detalhes |
|---------|--------|----------|
| Infraestrutura de rede | ✅ Validada | Subnets, IGW, routes OK |
| Network ACLs | ✅ Corretas | Portas permitidas |
| Security Group | ⚠️ Criado | Regras existem mas incorretas |
| Descrições de regras | ✅ Claras | Indicam o que fazer |
| **Permissões IAM** | ❌ **FALTANDO** | **Bloqueio total** |
| Task 1 completável | 🔴 **NÃO** | Bloqueada por IAM |

### Lições Aprendidas

1. **Troubleshooting sistemático funciona:**
   - Verificamos cada camada metodicamente
   - Identificamos o problema exato
   - Documentamos tudo claramente

2. **IAM é crítico:**
   - Permissões adequadas são essenciais
   - Mesmo com infraestrutura correta, sem IAM nada funciona
   - Sempre verifique permissões no troubleshooting

3. **Documentação importa:**
   - As descrições das regras eram claras
   - Mas não ajudaram sem as permissões
   - Boa documentação + permissões = sucesso

4. **Labs podem ter bugs:**
   - Nem sempre o problema é seu
   - Valide sistematicamente
   - Reporte problemas quando encontrar

---

**⚠️ Esta task não pode ser completada até que as permissões IAM sejam corrigidas no laboratório.**
