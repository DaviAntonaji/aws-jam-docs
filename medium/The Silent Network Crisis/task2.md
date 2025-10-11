# Task 2: (Não Acessível)

---

## 🚨 AVISO - TASK INACESSÍVEL

> **❌ ESTA TASK NÃO PODE SER ALCANÇADA**
> 
> **Motivo:** A Task 1 está bloqueada devido a problemas de permissões IAM, impedindo o acesso ao Bastion Host. Sem completar a Task 1, é impossível prosseguir para a Task 2.
>
> **Status:** 🔴 Conteúdo desconhecido

---

## 📖 Contexto

A Task 2 presumivelmente envolveria:

### Possíveis Objetivos (Estimados)

Com base no cenário geral do desafio "The Silent Network Crisis", a Task 2 provavelmente incluiria:

1. **Conectar à instância privada via Bastion:**
   - Usar RDP do Bastion para acessar `Private-ProductionServer`
   - Estabelecer "salto" através do jump server

2. **Diagnosticar problema de Systems Manager:**
   - Investigar por que a instância privada não se conecta ao AWS Systems Manager
   - Verificar conectividade de rede
   - Analisar logs do SSM Agent

3. **Identificar causa raiz:**
   - Ausência de VPC Endpoints para Systems Manager?
   - Problemas de roteamento?
   - Security Groups bloqueando tráfego?
   - IAM Role faltando ou incorreta?

4. **Implementar solução:**
   - Criar VPC Endpoints necessários:
     - `com.amazonaws.<region>.ssm`
     - `com.amazonaws.<region>.ssmmessages`
     - `com.amazonaws.<region>.ec2messages`
     - `com.amazonaws.<region>.s3` (Gateway Endpoint)
   - Ou configurar NAT Gateway se for estratégia diferente
   - Atualizar Security Groups
   - Verificar IAM Instance Profile

5. **Validar conectividade:**
   - Testar Run Command do Systems Manager
   - Verificar status da instância no SSM Console
   - Confirmar que deployment pode prosseguir

---

## 🎓 Conceitos que Provavelmente Seriam Abordados

### 1. AWS Systems Manager Session Manager

**O que é:**
Capacidade de conectar a instâncias EC2 sem precisar de SSH/RDP, bastion hosts, ou IPs públicos.

**Requisitos:**
- SSM Agent instalado e rodando
- IAM Instance Profile com permissões adequadas
- Conectividade de rede para endpoints do SSM
- Instância registrada no Systems Manager

### 2. VPC Endpoints para Systems Manager

**Por que são necessários:**
Instâncias em subnets privadas (sem acesso à Internet) precisam de VPC Endpoints para comunicar com serviços AWS sem sair da rede AWS.

**Endpoints necessários para SSM:**

| Endpoint | Tipo | Propósito |
|----------|------|-----------|
| `com.amazonaws.region.ssm` | Interface | API calls do Systems Manager |
| `com.amazonaws.region.ssmmessages` | Interface | Session Manager connections |
| `com.amazonaws.region.ec2messages` | Interface | Comunicação agent-to-service |
| `com.amazonaws.region.s3` | Gateway | Download de patches, scripts |

### 3. IAM Instance Profile

**Política necessária:**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ssm:UpdateInstanceInformation",
        "ssmmessages:CreateControlChannel",
        "ssmmessages:CreateDataChannel",
        "ssmmessages:OpenControlChannel",
        "ssmmessages:OpenDataChannel",
        "s3:GetObject"
      ],
      "Resource": "*"
    }
  ]
}
```

Ou use a política gerenciada: `AmazonSSMManagedInstanceCore`

### 4. Security Groups para VPC Endpoints

**Inbound rules necessárias:**
```
Type: HTTPS
Protocol: TCP
Port: 443
Source: Security Group da instância privada (ou CIDR da VPC)
```

**Por que:** A instância precisa alcançar os endpoints pela porta 443 (HTTPS)

### 5. Troubleshooting de SSM Connectivity

**Passo a passo:**
1. **Verificar SSM Agent:**
   ```powershell
   # Windows
   Get-Service AmazonSSMAgent
   
   # Logs em: C:\ProgramData\Amazon\SSM\Logs\amazon-ssm-agent.log
   ```

2. **Verificar IAM Instance Profile:**
   - EC2 Console → Instance → Security → IAM Role
   - Deve ter políticas SSM

3. **Verificar conectividade de rede:**
   ```powershell
   # Testar resolução DNS dos endpoints
   Test-NetConnection ssm.region.amazonaws.com -Port 443
   Test-NetConnection ssmmessages.region.amazonaws.com -Port 443
   Test-NetConnection ec2messages.region.amazonaws.com -Port 443
   ```

4. **Verificar Security Groups:**
   - Instância deve poder fazer outbound HTTPS (443)
   - VPC Endpoints devem aceitar inbound HTTPS da instância

5. **Verificar no SSM Console:**
   - Systems Manager → Fleet Manager
   - Instância deve aparecer como "Online" ou "Managed"

---

## 🛠️ Solução Provável (Baseada em Cenário)

### Cenário Mais Provável

Dado o contexto ("auditoria de rede cortou conexão com SSM"), a causa mais provável seria:

**Problema:** Remoção de NAT Gateway ou bloqueio de rotas durante auditoria

**Soluções possíveis:**

#### Opção A: Implementar VPC Endpoints (Recomendado)

**Vantagens:**
- Não precisa de NAT Gateway (economia)
- Tráfego permanece na rede AWS (segurança)
- Melhor performance
- Mais alinhado com "auditoria de segurança"

**Implementação:**
1. Criar VPC Endpoints Interface (ssm, ssmmessages, ec2messages)
2. Criar VPC Endpoint Gateway (S3)
3. Associar aos Security Groups corretos
4. Verificar DNS resolution habilitado
5. Testar conectividade

#### Opção B: Restaurar rota via NAT Gateway

**Vantagens:**
- Mais simples se NAT já existe
- Permite acesso geral à Internet

**Implementação:**
1. Verificar se NAT Gateway existe e está Available
2. Adicionar rota na subnet privada: `0.0.0.0/0 → NAT Gateway`
3. Verificar Security Groups
4. Testar conectividade

---

## 📚 Recursos Úteis

### Documentação AWS
- [Setting Up AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up.html)
- [VPC Endpoints for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-create-vpc.html)
- [Troubleshooting Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/troubleshooting-remote-commands.html)
- [SSM Agent Troubleshooting](https://docs.aws.amazon.com/systems-manager/latest/userguide/troubleshooting-ssm-agent.html)

### Guias de Implementação
- [AWS PrivateLink for Systems Manager](https://aws.amazon.com/blogs/mt/using-aws-privatelink-to-connect-aws-systems-manager-to-private-subnets/)
- [Bastion Host Best Practices](https://aws.amazon.com/blogs/security/how-to-record-ssh-sessions-established-through-a-bastion-host/)

---

## 🎯 Possível Checklist (Teórico)

Se pudéssemos acessar a Task 2:

- [ ] Conectar ao Bastion via RDP (Task 1 completa)
- [ ] Do Bastion, conectar à instância privada via RDP
- [ ] Verificar status do SSM Agent na instância privada
- [ ] Verificar IAM Instance Profile
- [ ] Diagnosticar problema de conectividade
- [ ] Identificar causa raiz (endpoints faltando, rotas, SG, etc.)
- [ ] Implementar solução (VPC Endpoints ou NAT)
- [ ] Configurar Security Groups dos endpoints
- [ ] Testar conectividade dos endpoints
- [ ] Verificar instância aparece no Fleet Manager
- [ ] Testar Run Command
- [ ] Validar deployment pode prosseguir
- [ ] Submeter resposta da Task 2

---

## 💡 Como Praticar Estes Conceitos

### Em Conta AWS Própria

**1. Criar infraestrutura:**
```
- VPC com subnet pública e privada
- Internet Gateway
- NAT Gateway (opcional)
- 2 instâncias EC2 Windows
- Security Groups
```

**2. Configurar Systems Manager:**
- Criar IAM Instance Profile com política SSM
- Anexar à instância privada
- Verificar SSM Agent instalado

**3. Testar conectividade:**
- Usar Session Manager para conectar
- Testar Run Command

**4. Simular problema:**
- Remover rota para NAT Gateway
- Observar perda de conectividade

**5. Implementar solução:**
- Criar VPC Endpoints para SSM
- Configurar Security Groups
- Validar conectividade restaurada

**6. Comparar custos:**
- NAT Gateway: ~$32/mês + data transfer
- VPC Endpoints: ~$7.20/mês/endpoint + data transfer
- Para SSM, endpoints são mais econômicos

### Laboratórios Alternativos

**AWS Workshops:**
- [Systems Manager Workshops](https://workshops.aws/)
- Procure por "Systems Manager" ou "Session Manager"

**AWS Skill Builder:**
- Cursos sobre Systems Manager
- Labs práticos gratuitos

**Qwiklabs / A Cloud Guru:**
- Labs guiados de Systems Manager
- Cenários de troubleshooting

---

## 📝 Conclusão

Embora não seja possível acessar e documentar a Task 2 devido ao bloqueio na Task 1, podemos inferir que ela provavelmente abordaria:

1. **Acesso a instâncias privadas** via Bastion Host
2. **Diagnóstico de problemas** de conectividade com AWS Systems Manager
3. **Implementação de VPC Endpoints** ou outra solução de rede
4. **Validação da solução** com Run Command

Estes são conceitos fundamentais de networking e gerenciamento na AWS, especialmente para ambientes com requisitos rigorosos de segurança.

---

**⚠️ IMPORTANTE:** Para acessar e completar a Task 2, primeiro é necessário que o problema de permissões IAM da Task 1 seja corrigido.

---

## 🎓 Aprendizados (Mesmo Sem Acesso)

Mesmo sem poder completar este desafio, você pode aprender:

1. **Arquiteturas de rede seguras** com subnets privadas
2. **Bastion Hosts** para acesso controlado
3. **VPC Endpoints** para serviços AWS
4. **AWS Systems Manager** para gerenciamento sem SSH/RDP
5. **Troubleshooting sistemático** de conectividade
6. **Trade-offs** entre diferentes soluções (NAT vs Endpoints)

**Recomendação:** Pratique estes conceitos em um ambiente próprio ou em labs que estejam funcionando corretamente!

---

**🔗 Voltar para:** [README Principal](./README.md) | [Task 1](./task1.md)

