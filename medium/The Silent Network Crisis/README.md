# ⚠️ The Silent Network Crisis

## 🚨 AVISO IMPORTANTE - DESAFIO COM PROBLEMAS

> **❌ ESTE DESAFIO ESTÁ INCOMPLETO/QUEBRADO**
> 
> **Problema identificado:** O laboratório AWS possui **limitações de permissões IAM** que impedem a conclusão da Task 1. O usuário do lab não tem permissões para modificar Security Groups (`ec2:AuthorizeSecurityGroupIngress` e `ec2:AuthorizeSecurityGroupEgress`), o que é necessário para completar o desafio.
>
> **Status:** 🔴 Não pode ser completado sem correção do lab pela AWS
>
> **Recomendação:** Use este desafio apenas para **fins educacionais** e compreensão de troubleshooting de rede. Não utilize em competições até que o problema seja corrigido.

---

## 📋 Visão Geral

Este desafio aborda **troubleshooting de conectividade de rede** entre instâncias EC2 privadas e AWS Systems Manager, além de configuração de Bastion Hosts (jump servers) para acesso a recursos em redes privadas.

### 🎯 Cenário

**AnyCompany Solutions**, uma empresa líder em cibersegurança, executa suas cargas de trabalho mais sensíveis em instâncias Amazon EC2 dentro de uma rede privada completamente isolada do mundo exterior. Para gerenciar esses nós, eles dependem do **AWS Systems Manager**, que funcionava perfeitamente até recentemente.

Após uma auditoria rigorosa de rede para fortalecer o perímetro de segurança, **novas restrições impostas inadvertidamente cortaram a conexão** entre as instâncias EC2 privadas e o AWS Systems Manager.

Com um lançamento crítico de software iminente, programado para deployment via **AWS Systems Manager Run Command**, a pressão está aumentando.

**Você, como Alex Mercer, Engenheiro Cloud líder**, foi urgentemente chamado para resolver este problema antes que a janela de deployment se feche. Todo o projeto depende da sua habilidade de **restaurar a comunicação** entre esses nós isolados e o AWS Systems Manager.

---

## 🎓 O Que Você Deveria Aprender (Se o Lab Funcionasse)

- ✅ Configurar e usar **Bastion Hosts** (jump servers)
- ✅ Gerenciar **Security Groups** para acesso RDP
- ✅ Troubleshooting de conectividade de rede em VPCs
- ✅ Diagnosticar problemas de comunicação com **AWS Systems Manager**
- ✅ Configurar **VPC Endpoints** para serviços AWS
- ✅ Entender arquitetura de rede privada vs. pública
- ✅ Análisar **Network ACLs** e **Route Tables**

## 🛠️ Serviços AWS Envolvidos

- **Amazon EC2:** Instâncias Windows (Bastion e Private)
- **AWS Systems Manager:** Gerenciamento de instâncias
- **Amazon VPC:** Networking e isolamento
- **Security Groups:** Firewall de instância
- **Network ACLs:** Firewall de subnet
- **VPC Endpoints:** Conectividade privada com serviços AWS
- **IAM:** Permissões (onde o problema está)

## 📦 Inventário

- ✅ **Bastion-JumpServer:** Instância Windows EC2 em subnet pública
- ✅ **Private-ProductionServer:** Instância Windows EC2 em subnet privada
- ✅ **Bastion-SecurityGroup:** Security Group do Bastion
- ✅ **VPC** com subnets pública e privada
- ✅ **Internet Gateway** anexado à VPC
- ✅ Credenciais de login fornecidas (Output Properties)

## 🎯 Estrutura de Tarefas

### ❌ Task 1: Getting access to private node via Bastion Host (45 pontos)

**Objetivo:** Habilitar RDP e acesso à Internet no Bastion Host

**O que deveria ser feito:**
1. Identificar a instância Bastion EC2
2. Modificar Security Group para permitir RDP (porta 3389) do seu IP
3. Modificar Security Group para permitir saída HTTPS (porta 443) para 0.0.0.0/0
4. Conectar via RDP ao Bastion
5. Validar inserindo seu IP público

**🔴 PROBLEMA ENCONTRADO:**
- O Security Group já está criado com as regras corretas (3389 e 443)
- As descrições das regras indicam explicitamente para editá-las
- **MAS:** O usuário do lab não tem permissão IAM para executar:
  - `ec2:AuthorizeSecurityGroupIngress`
  - `ec2:AuthorizeSecurityGroupEgress`
- **Resultado:** Impossível modificar as regras conforme solicitado

**Erro retornado:**
```
You are not authorized to perform: ec2:AuthorizeSecurityGroupIngress
```

### ❓ Task 2: (Não documentada)

Presumivelmente deveria envolver:
- Conectar ao servidor privado via Bastion
- Diagnosticar problemas de conectividade com Systems Manager
- Configurar VPC Endpoints ou corrigir rotas

**Status:** Não pode ser alcançada sem completar Task 1

---

## 🚨 Análise Técnica do Problema

### ✅ O Que Está Correto

#### 1. Infraestrutura de Rede
- **Subnet pública:** Corretamente configurada com rota para Internet Gateway
  - Route Table: `0.0.0.0/0 → igw-0feceaf2265bffc0f` ✅
- **Internet Gateway:** Anexado à VPC ✅
- **Public IPv4:** Instância Bastion tem IP público associado ✅

#### 2. Network ACLs
- **Inbound rules:** Permite portas 3389, 443, 80 e efêmeras (1024-65535) ✅
- **Outbound rules:** Permite as mesmas portas ✅
- **ACLs:** Configuradas corretamente, não são o problema ✅

#### 3. Security Group Existente
- **Nome:** `Bastion-SecurityGroup` (sg-02c44112d02f50131)
- **Regras criadas:** Já existem regras para 3389 (inbound) e 443 (outbound)
- **Descrições:** Indicam claramente o que deve ser modificado
  - Inbound 3389: "Edit this rule and specify source as MyIP"
  - Outbound 443: "Edit this rule and choose Anywhere-IPv4 destination"

### ❌ O Que Está Quebrado

#### Permissões IAM Faltantes

O usuário do laboratório (`AWSLabsUser-...`) **não possui** as seguintes permissões necessárias:

```json
{
  "Effect": "Deny",
  "Action": [
    "ec2:AuthorizeSecurityGroupIngress",
    "ec2:AuthorizeSecurityGroupEgress"
  ]
}
```

**Consequência:** Impossível modificar as regras do Security Group, impedindo a conclusão da Task 1.

### 🔍 Validação Realizada

#### Checklist de Troubleshooting
- [x] **Subnet pública com rota para IGW:** Verificado ✅
- [x] **Internet Gateway anexado:** Verificado ✅
- [x] **Elastic/Public IP associado:** Verificado ✅
- [x] **Network ACLs permissivas:** Verificado ✅
- [x] **Security Group existente:** Verificado ✅
- [x] **Regras de SG com descrições claras:** Verificado ✅
- [ ] **Permissões IAM para modificar SG:** ❌ **FALTANDO**

---

## 🛠️ O Que Deveria Ser Feito (Se Funcionasse)

### Task 1: Passo a Passo (Teórico)

#### 1️⃣ Identificar a Instância Bastion

**Console:** EC2 → Instances
- Procure por: `Bastion-JumpServer`
- Ou use o Instance ID de Output Properties
- Anote o **Public IPv4 address**

#### 2️⃣ Modificar Security Group - Inbound Rule

**Console:** EC2 → Security Groups → `Bastion-SecurityGroup`

**Ação necessária:**
1. Aba **"Inbound rules"** → **"Edit inbound rules"**
2. Encontre a regra para porta **3389** (RDP)
3. **Edit:**
   - Type: `RDP`
   - Protocol: `TCP`
   - Port: `3389`
   - Source: **My IP** (isso pega seu IP público automaticamente)
   - Description: `RDP from my IP`
4. **Save rules**

**🔴 PROBLEMA:** Retorna erro de permissão

#### 3️⃣ Modificar Security Group - Outbound Rule

**Ação necessária:**
1. Aba **"Outbound rules"** → **"Edit outbound rules"**
2. Encontre a regra para porta **443** (HTTPS)
3. **Edit:**
   - Type: `HTTPS`
   - Protocol: `TCP`
   - Port: `443`
   - Destination: **Anywhere-IPv4** (`0.0.0.0/0`)
   - Description: `HTTPS to Internet`
4. **Save rules**

**🔴 PROBLEMA:** Retorna erro de permissão

#### 4️⃣ Conectar via RDP

**Windows:**
1. Abra **Remote Desktop Connection** (mstsc.exe)
2. Computer: `<Public IPv4 do Bastion>`
3. Username: `<fornecido em Output Properties>`
4. Password: `<fornecido em Output Properties>`
5. Connect

**macOS:**
1. Baixe **Microsoft Remote Desktop** da App Store
2. Add PC → endereço do Bastion
3. Insira credenciais
4. Connect

#### 5️⃣ Validar Task

**Input esperado:** Seu IP público no formato CIDR
```
123.45.67.89/32
```

> **💡 Dica:** Se você usa VPN, garanta que o IP seja o correto

---

## 💡 Solução de Contorno (Workaround)

Como o problema é de **permissões IAM do lab**, existem algumas possíveis soluções:

### Opção 1: Contatar Suporte do Lab
- Reportar o problema de permissões IAM
- Solicitar que adicionem as permissões necessárias à role do lab

### Opção 2: Simular em Conta Própria
Se você tem uma conta AWS própria:

1. **Crie a infraestrutura:**
   ```
   - VPC com subnet pública e privada
   - Internet Gateway
   - 2 instâncias Windows EC2 (Bastion e Private)
   - Security Groups configurados
   ```

2. **Pratique o troubleshooting:**
   - Configure Security Groups corretamente
   - Teste conectividade RDP
   - Configure VPC Endpoints para Systems Manager
   - Teste comunicação da instância privada com SSM

### Opção 3: Uso Educacional
- Use este material para **aprender os conceitos**
- Entenda o fluxo de troubleshooting
- Compreenda como Security Groups, NACLs e route tables funcionam
- Pratique análise de conectividade de rede

---

## 📚 Recursos Úteis

### Documentação AWS
- [AWS Systems Manager Prerequisites](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-prereqs.html)
- [Security Groups for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html)
- [VPC Endpoints for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-create-vpc.html)
- [Bastion Hosts on AWS](https://aws.amazon.com/solutions/implementations/linux-bastion/)

### Troubleshooting
- [Troubleshoot RDP connections to EC2](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/troubleshoot-connect-windows-instance.html)
- [Systems Manager Connection Troubleshooting](https://docs.aws.amazon.com/systems-manager/latest/userguide/troubleshooting-remote-commands.html)

---

## 🎓 Conceitos Aprendidos (Apesar do Problema)

### 1. Bastion Hosts (Jump Servers)
Instâncias EC2 em subnets públicas que servem como ponto de entrada seguro para acessar recursos em subnets privadas.

**Características:**
- Em subnet pública com IP público
- Security Group restritivo (apenas IPs confiáveis)
- Usado para "pular" para instâncias privadas
- Logs de acesso para auditoria

### 2. Security Groups
Firewalls stateful de instância que controlam tráfego inbound e outbound.

**Importantes:**
- **Stateful:** Resposta de tráfego permitido é automaticamente permitida
- **Default deny:** Por padrão, todo tráfego inbound é negado
- **Múltiplos SGs:** Uma instância pode ter até 5 Security Groups

### 3. Network ACLs
Firewalls stateless de subnet.

**Diferenças vs. Security Groups:**
- **Stateless:** Precisa de regras explícitas para tráfego de ida E volta
- **Subnet-level:** Aplica-se a toda a subnet
- **Rules ordering:** Regras são processadas em ordem numérica
- **Deny rules:** Pode ter regras de DENY explícitas

### 4. VPC Endpoints para Systems Manager
Para que instâncias privadas acessem Systems Manager sem Internet:

**Endpoints necessários:**
- `com.amazonaws.<region>.ssm`
- `com.amazonaws.<region>.ssmmessages`
- `com.amazonaws.<region>.ec2messages`
- `com.amazonaws.<region>.s3` (Gateway Endpoint)

### 5. Troubleshooting de Conectividade

**Ordem de verificação:**
1. ✅ Route Tables (caminho existe?)
2. ✅ Network ACLs (subnet permite?)
3. ✅ Security Groups (instância permite?)
4. ✅ Firewall do SO (Windows/Linux permite?)
5. ✅ Aplicação (serviço está ouvindo?)

---

## 🏆 Critérios de Sucesso (Se Funcionasse)

- [ ] Identificar instância Bastion corretamente
- [ ] Entender configuração de Security Groups
- [ ] Modificar regras de SG (inbound e outbound)
- [ ] Conectar via RDP ao Bastion
- [ ] Validar com IP público correto
- [ ] (Task 2) Conectar à instância privada
- [ ] (Task 2) Diagnosticar problema de Systems Manager
- [ ] (Task 2) Implementar solução (VPC Endpoints?)

---

## 📊 Status do Desafio

| Componente | Status | Observação |
|------------|--------|------------|
| Infraestrutura de rede | ✅ OK | Subnets, IGW, routes corretos |
| Network ACLs | ✅ OK | Configuradas permissivamente |
| Security Groups | ⚠️ Criados | Mas não podem ser modificados |
| Permissões IAM | ❌ FALTANDO | Bloqueio crítico |
| Task 1 | 🔴 Bloqueada | Por falta de permissões |
| Task 2 | ⚠️ Desconhecida | Não pode ser alcançada |

---

## 🎯 Próximos Passos (Se Quiser Praticar)

1. **Reportar o problema** ao suporte do AWS Jam
2. **Criar ambiente próprio** para praticar os conceitos
3. **Estudar** os recursos de documentação fornecidos
4. **Praticar** outros desafios que estejam funcionando
5. **Voltar** quando o lab for corrigido

---

## 💭 Reflexão Final

Este desafio é um excelente exemplo de troubleshooting de rede na AWS e uso de Bastion Hosts, mas infelizmente está inacessível devido a problemas de configuração do laboratório. 

Os conceitos são válidos e importantes, mas a experiência prática está comprometida. Use este material como referência educacional e pratique os conceitos em um ambiente próprio ou aguarde correção do lab.

---

**⚠️ IMPORTANTE:** Não use este desafio em competições ou para pontuação até que o problema de permissões IAM seja resolvido pela equipe do AWS Jam.
