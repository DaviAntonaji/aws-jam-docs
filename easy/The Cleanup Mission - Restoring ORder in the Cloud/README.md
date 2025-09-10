# 🧹 The Cleanup Mission - Restoring Order in the Cloud

## 📋 Visão Geral

Este desafio foca na **limpeza e organização de recursos AWS** que foram deixados após a conclusão de projetos. O objetivo é aprender sobre **dependências entre recursos** e a **ordem correta de deleção** para evitar recursos órfãos e custos desnecessários.

## 🎯 Objetivos de Aprendizado

- ✅ Entender **dependências entre recursos AWS**
- ✅ Aprender a **ordem correta de deleção** de recursos
- ✅ Identificar e resolver **recursos órfãos**
- ✅ Implementar **boas práticas de limpeza** de infraestrutura
- ✅ Desenvolver habilidades de **troubleshooting** de dependências

## 🏗️ Arquitetura do Desafio

### Recursos Envolvidos:
- **VPCs** marcados para deleção
- **Security Groups** órfãos
- **Peering Connections** entre VPCs
- **Internet Gateways** e **NAT Gateways**
- **Elastic Network Interfaces (ENIs)**
- **Route Tables** e **Subnets**
- **Instâncias EC2** associadas

### Cenário:
Após a conclusão de um projeto, vários recursos foram deixados na conta AWS:
- 2 VPCs marcados para deleção
- 1 Security Group órfão com dependências ativas
- Diversos recursos de rede associados

## 📚 Tasks Disponíveis

### 🔧 [Task 1 - VPC Cleanup](./task1.md)
**Foco:** Remoção completa de VPCs e recursos associados

**Conceitos principais:**
- Identificação de VPCs marcados para deleção
- Remoção de Peering Connections
- Desanexação de Internet Gateways
- Exclusão de NAT Gateways e ENIs
- Deleção de Route Tables e Subnets
- Remoção final dos VPCs

**Dificuldade:** ⭐⭐⭐☆☆  
**Tempo estimado:** 45-60 minutos

---

### 🛡️ [Task 2 - Security Group Cleanup](./task2.md)
**Foco:** Remoção de Security Groups órfãos com dependências

**Conceitos principais:**
- Identificação de dependências de Security Groups
- Terminação de instâncias EC2 associadas
- Liberação automática de ENIs
- Deleção de ENIs standalone
- Remoção final do Security Group

**Dificuldade:** ⭐⭐☆☆☆  
**Tempo estimado:** 30-45 minutos

## 🚀 Como Começar

### Pré-requisitos
- **AWS Account** com permissões adequadas para VPC e EC2
- **Conhecimento básico** de VPC, Security Groups e EC2
- **Ambiente de lab** com recursos pré-configurados

### Ordem Recomendada
1. **Task 1** - VPC Cleanup (mais complexo, múltiplas dependências)
2. **Task 2** - Security Group Cleanup (mais direto, foco em EC2)

### Estrutura do Projeto
```
The Cleanup Mission - Restoring ORder in the Cloud/
├── README.md          # Este arquivo - visão geral
├── task1.md          # VPC Cleanup - remoção completa de VPCs
└── task2.md          # Security Group Cleanup - remoção de SGs órfãos
```

## 🎓 Conceitos Fundamentais

### 🔗 Dependências de Recursos AWS
- **VPCs** são containers para outros recursos de rede
- **Security Groups** podem ser referenciados por múltiplos recursos
- **ENIs** são criadas automaticamente para vários serviços
- **Peering Connections** conectam VPCs e impedem deleção

### 📋 Ordem de Deleção
1. **Recursos de aplicação** (EC2, RDS, etc.)
2. **Recursos de rede** (ENIs, NAT Gateways)
3. **Conectividade** (Peering, Internet Gateways)
4. **Infraestrutura base** (Subnets, Route Tables)
5. **Containers** (VPCs, Security Groups)

### ⚠️ Armadilhas Comuns
- **Deleção prematura:** Tentar deletar recursos antes de suas dependências
- **ENIs órfãs:** Interfaces deixadas por serviços AWS
- **Elastic IPs:** Não liberados antes de deletar NAT Gateways
- **Peering ativo:** Conexões com tráfego impedem deleção

## 🚨 Troubleshooting

### Problemas Comuns

#### VPC não pode ser deletado
- **Causa:** Dependências ativas (peering, ENIs, NAT Gateways)
- **Solução:** Remover todas as dependências na ordem correta

#### Security Group não pode ser deletado
- **Causa:** Instâncias EC2 ou ENIs ainda referenciando
- **Solução:** Terminar instâncias e deletar ENIs primeiro

#### ENIs não podem ser deletadas
- **Causa:** Associadas a serviços AWS (NAT, endpoints)
- **Solução:** Deletar o serviço associado primeiro

### Estratégias de Resolução
1. **Identifique todas as dependências** antes de começar
2. **Use a interface AWS** para verificar recursos associados
3. **Siga a ordem correta** de deleção
4. **Verifique após cada passo** se a dependência foi resolvida
5. **Documente o processo** para referência futura

## 💡 Boas Práticas

### 🧹 Limpeza de Recursos
- **Sempre limpe recursos** após conclusão de projetos
- **Use tags** para identificar recursos de projetos específicos
- **Implemente políticas** de limpeza automática quando possível
- **Monitore custos** para identificar recursos órfãos

### 🔍 Identificação de Dependências
- **Use AWS Console** para visualizar dependências
- **Consulte AWS CLI** para listar recursos associados
- **Implemente scripts** para automatizar limpeza
- **Documente dependências** conhecidas

### 📊 Monitoramento
- **Configure alertas** para recursos órfãos
- **Use AWS Config** para rastrear mudanças
- **Implemente CloudTrail** para auditoria
- **Revise regularmente** recursos não utilizados

## 🏆 Critérios de Sucesso

- [ ] **VPCs completamente removidos** sem recursos órfãos
- [ ] **Security Groups deletados** com todas as dependências resolvidas
- [ ] **Compreensão das dependências** entre recursos AWS
- [ ] **Habilidades de troubleshooting** desenvolvidas
- [ ] **Conhecimento de ordem de deleção** aplicado

## 📖 Recursos Adicionais

### Documentação AWS
- [VPC User Guide](https://docs.aws.amazon.com/vpc/)
- [Security Groups Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-security-groups.html)
- [EC2 Network Interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html)

### Ferramentas Úteis
- [AWS CLI VPC Commands](https://docs.aws.amazon.com/cli/latest/reference/ec2/)
- [AWS Console VPC Dashboard](https://console.aws.amazon.com/vpc/)
- [AWS Resource Groups](https://aws.amazon.com/resource-groups/)

## 🎯 Próximos Passos

Após completar este desafio, considere:
- **Automação:** Implementar scripts para limpeza automática
- **Governança:** Estabelecer políticas de limpeza de recursos
- **Monitoramento:** Configurar alertas para recursos órfãos
- **Certificações:** Preparar-se para exames AWS focados em governança

---

**🎉 Boa sorte com a limpeza!**

> **💭 Reflexão:** Este desafio não é apenas sobre deletar recursos, mas sobre entender como a infraestrutura AWS se conecta e como gerenciar dependências de forma eficiente - habilidades essenciais para qualquer profissional de cloud.
