# Deny external attacks from IPv6

## 📋 Visão Geral

Este desafio foca na **segurança IPv6** em ambientes AWS, abordando um problema crítico de segurança onde uma instância EC2 tem acesso público irrestrito via IPv6. O objetivo é implementar uma solução que bloqueie ataques externos mantendo a funcionalidade de saída, sem custos adicionais.

## 🎯 Objetivo

Implementar uma solução de segurança IPv6 que **bloqueie todo acesso público de entrada** via IPv6 para uma instância EC2 vulnerável, mantendo a **capacidade de conexões de saída** para a internet, sem usar NAT Gateway ou NAT Instance devido a restrições de custo.

## 🔧 Conceitos Principais

- **Egress-Only Internet Gateway (EIGW)** - Componente de rede para IPv6 seguro
- **Route Tables** - Controle de direcionamento de tráfego IPv6
- **IPv6 Security** - Proteção contra ataques externos via IPv6
- **Cost Optimization** - Solução sem custos adicionais
- **Network Architecture** - Configuração de VPC para segurança

## 🏗️ Arquitetura

### Situação Inicial (Insegura)
```
Internet IPv6 ←→ Internet Gateway ←→ VPC (AWS-Jam-FixIPV6) ←→ EC2 Instance
     ↑                                    ↓
   Acesso público                    Vulnerável (RDP porta 3389)
```

### Situação Final (Segura)
```
Internet IPv6 → Egress-Only IGW → VPC (AWS-Jam-FixIPV6) ← EC2 Instance
     ↑ (bloqueado)                    ↓ (permitido)
   Acesso negado                  Saída liberada
```

## 📚 Tarefas

### [Task 1: Egress-Only Internet Gateway (IPv6)](./task1.md)

**Objetivo:** Implementar Egress-Only Internet Gateway para bloquear acesso público IPv6

**Problema identificado:**
- Instância EC2 com acesso público IPv6 irrestrito
- Porta 3389 (RDP) acessível publicamente via IPv6
- Risco crítico de segurança

**Conceitos abordados:**
- Criação e configuração de Egress-Only Internet Gateway
- Modificação de Route Tables para IPv6
- Teste de conectividade IPv6 (entrada e saída)
- Comparação entre IGW e EIGW
- Troubleshooting de configurações de rede IPv6

## 🚀 Passo a Passo Resumido

### Task 1 - Implementação de Segurança IPv6
1. **Verificar vulnerabilidade** - Testar acesso RDP via IPv6
2. **Criar Egress-Only Internet Gateway** - Anexar à VPC
3. **Configurar Route Table** - Alterar rota IPv6 de IGW para EIGW
4. **Validar segurança** - Confirmar bloqueio de entrada
5. **Testar conectividade** - Verificar saída IPv6 funcionando
6. **Verificar no Jam** - Confirmar Task 1 marcada como completa

## ⚠️ Pontos Importantes

### Segurança IPv6
- **IPv6 é habilitado por padrão** em muitas VPCs AWS
- **Acesso público** pode ser um risco de segurança significativo
- **Egress-Only IGW** é a solução padrão para IPv6 seguro
- **Defense in depth** - múltiplas camadas de segurança

### Configuração de Rede
- **Route Tables** controlam direcionamento de tráfego IPv6
- **Internet Gateway** permite acesso bidirecional
- **Egress-Only IGW** permite apenas saída
- **Configuração** é simples mas efetiva

### Otimização de Custos
- **Egress-Only Internet Gateway** é gratuito
- **NAT Gateway** tem custos mensais e por dados
- **NAT Instance** requer instância EC2 adicional
- **Solução sem custos** adicionais

## 🔍 Solução Principal

### Egress-Only Internet Gateway
O **Egress-Only Internet Gateway (EIGW)** é um componente de rede que:
- ✅ **Permite tráfego de saída** IPv6 da VPC para a internet
- ❌ **Bloqueia tráfego de entrada** IPv6 da internet para a VPC
- 💰 **Sem custos adicionais** (diferente do NAT Gateway)

### Configuração Necessária
1. **Criar Egress-Only Internet Gateway** na VPC
2. **Modificar Route Table** para usar EIGW em vez de IGW
3. **Testar conectividade** para validar a solução

### Comandos de Validação
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

## 📊 Dificuldade e Tempo

**Dificuldade:** ⭐⭐☆☆☆  
**Tempo estimado:** 20-30 minutos

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

## 🔗 Recursos Adicionais

### Documentação AWS
- [VPC User Guide](https://docs.aws.amazon.com/vpc/)
- [IPv6 in VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-migrate-ipv6.html)
- [Egress-Only Internet Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/egress-only-internet-gateway.html)
- [Route Tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html)

### Conceitos Relacionados
- [IPv6 Security Best Practices](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-best-practices.html)
- [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)
- [Security Groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

### Ferramentas Úteis
- [Port Checker Online](https://portchecker.co/)
- [IPv6 Test Tools](https://test-ipv6.com/)
- [AWS CLI VPC Commands](https://docs.aws.amazon.com/cli/latest/reference/ec2/)

## ✅ Critérios de Sucesso

### Task 1 - Egress-Only Internet Gateway
- [ ] Vulnerabilidade IPv6 identificada (porta 3389 acessível)
- [ ] Egress-Only Internet Gateway criado e anexado à VPC
- [ ] Route table atualizada com rota IPv6 para EIGW
- [ ] Acesso público IPv6 bloqueado (RDP não acessível)
- [ ] Conectividade de saída IPv6 mantida
- [ ] Configuração salva e aplicada
- [ ] Validação no Jam marcada como "Completed"

## 🚨 Troubleshooting Comum

### Egress-Only Internet Gateway não criado
- Verificar permissões IAM para criar recursos VPC
- Confirmar região correta no console
- Aguardar propagação (pode levar alguns minutos)

### Route table não atualizada
- Verificar se está editando a route table correta
- Confirmar que o EIGW está anexado à VPC
- Salvar as mudanças na route table

### Acesso de saída não funciona
- Verificar se a rota IPv6 está correta
- Confirmar que o EIGW está ativo
- Testar conectividade IPv6 da instância

### Acesso de entrada ainda funciona
- Verificar se a rota IPv6 foi realmente alterada
- Confirmar que o EIGW está sendo usado
- Testar novamente após alguns minutos

## 💡 Dicas de Otimização

### Segurança
- **Defense in depth** - Use Security Groups + EIGW + Network ACLs
- **Monitoramento** - Configure CloudWatch para alertas de segurança
- **Auditoria** - Use CloudTrail para rastrear mudanças de rede
- **Documentação** - Mantenha registro de configurações de segurança

### Performance
- **Route optimization** - Minimize número de rotas desnecessárias
- **Monitoring** - Acompanhe métricas de rede via CloudWatch
- **Testing** - Valide configurações antes de aplicar em produção

### Custos
- **EIGW é gratuito** - Use em vez de NAT Gateway quando possível
- **Data transfer** - Monitore custos de transferência de dados
- **Resource tagging** - Use tags para controle de custos

## 🎯 Cenário de Negócio

### Contexto
Você é um **especialista em rede** que acabou de ingressar na ABC Corp, assumindo a infraestrutura AWS de um funcionário anterior que saiu abruptamente. Durante sua auditoria de segurança inicial, descobriu um problema crítico de segurança.

### Desafio
- **Instância EC2** com acesso público IPv6 irrestrito
- **Porta 3389 (RDP)** acessível publicamente
- **Restrições de custo** - não pode usar NAT Gateway
- **Necessidade** de manter conectividade de saída

### Solução
- **Egress-Only Internet Gateway** para bloquear entrada
- **Modificação de Route Table** para usar EIGW
- **Sem custos adicionais** - solução gratuita
- **Segurança mantida** - acesso de saída preservado

---

**🎉 Boa sorte com o desafio!**

> **💭 Reflexão:** Este desafio demonstra a importância de entender as diferenças entre IPv4 e IPv6 em ambientes AWS, e como a AWS oferece ferramentas específicas como o Egress-Only Internet Gateway para resolver problemas de segurança IPv6 de forma elegante e econômica.
