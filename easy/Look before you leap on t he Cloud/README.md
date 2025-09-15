# Look before you leap on the Cloud

## 🎯 Visão Geral

Este challenge foca em **configurações de segurança e permissões** em ambientes AWS, explorando cenários comuns onde pequenos erros de configuração podem causar grandes problemas de conectividade e acesso. O nome "Look before you leap" enfatiza a importância de **analisar cuidadosamente** as configurações antes de implementar mudanças em produção.

## 📋 Descrição do Challenge

O desafio simula um ambiente de produção onde **4 problemas críticos** de configuração precisam ser identificados e corrigidos:

1. **Lambda VPC Connectivity** - Função sem acesso à internet
2. **IAM Permissions** - Lambda sem permissões para S3
3. **KMS Key Policy** - Perda de controle administrativo
4. **Cross-Account Access** - Permissões excessivas em bucket S3

### Cenário
Você é um **Cloud Engineer** responsável por resolver problemas de conectividade e segurança que estão impedindo o funcionamento correto de uma aplicação crítica. Cada task representa um problema real que pode ocorrer em ambientes de produção.

## 🎓 Objetivos de Aprendizado

### Conceitos Técnicos
- ✅ **VPC Networking:** Configuração de Lambda em VPC com acesso à internet
- ✅ **IAM Permissions:** Gestão de roles e policies para serviços AWS
- ✅ **KMS Security:** Controle de acesso a chaves de criptografia
- ✅ **Cross-Account Security:** Implementação de least privilege entre contas

### Habilidades Práticas
- ✅ **Troubleshooting:** Diagnóstico de problemas de conectividade e permissões
- ✅ **Security Best Practices:** Aplicação de princípios de segurança
- ✅ **AWS Console Navigation:** Uso eficiente dos consoles AWS
- ✅ **Policy Management:** Criação e edição de policies JSON

## 📚 Tasks do Challenge

### [Task 1: VPC Lambda doesn't work](./task1.md)
**🔧 Problema:** Lambda em VPC sem conectividade com internet  
**🎯 Solução:** Mover Lambda para subnets privadas com NAT Gateway  
**⏱️ Tempo estimado:** 15-20 minutos  
**🔍 Conceitos:** VPC, Subnets, NAT Gateway, Lambda networking

### [Task 2: Lambda não consegue ler/escrever no S3](./task2.md)
**🔧 Problema:** Função Lambda sem permissões para operações CRUD no S3  
**🎯 Solução:** Anexar policy IAM com permissões específicas para o bucket  
**⏱️ Tempo estimado:** 10-15 minutos  
**🔍 Conceitos:** IAM Roles, S3 Permissions, Least Privilege

### [Task 3: Perda de controle administrativo da chave KMS](./task3.md)
**🔧 Problema:** Security Admin sem acesso para gerenciar chave KMS  
**🎯 Solução:** Adicionar Security Admin Role à Key Policy  
**⏱️ Tempo estimado:** 20-25 minutos  
**🔍 Conceitos:** KMS Key Policies, Role Assumption, Administrative Access

### [Task 4: Cross-account access no bucket S3](./task4.md)
**🔧 Problema:** Bucket policy permitindo acesso de conta inteira  
**🎯 Solução:** Restringir acesso apenas ao role específico  
**⏱️ Tempo estimado:** 15-20 minutos  
**🔍 Conceitos:** Cross-Account Security, Bucket Policies, Principal Specification

## 🏗️ Arquitetura do Ambiente

```
┌─────────────────────────────────────────────────────────────┐
│                    AWS Account (Main)                       │
│                                                             │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │                      VPC                                │ │
│  │                                                         │ │
│  │  ┌─────────────────┐    ┌─────────────────────────────┐ │ │
│  │  │ Public Subnet   │    │     Private Subnet          │ │ │
│  │  │                 │    │                             │ │ │
│  │  │  NAT Gateway    │    │  Lambda Function            │ │ │
│  │  │                 │    │  (MyFunction)               │ │ │
│  │  └─────────────────┘    │                             │ │ │
│  │                         │  EC2 Instance               │ │ │
│  │                         │  (Web Server)               │ │ │
│  │                         └─────────────────────────────┘ │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                             │
│  ┌─────────────────┐    ┌─────────────────┐                │
│  │   S3 Bucket     │    │   KMS Key       │                │
│  │   (Task 2 & 4)  │    │   (Task 3)      │                │
│  └─────────────────┘    └─────────────────┘                │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│              AWS Account (Partner - 739275461757)           │
│                                                             │
│  ┌─────────────────┐                                        │
│  │ IAM Role        │                                        │
│  │ S3CrossAccount  │                                        │
│  │ Access          │                                        │
│  └─────────────────┘                                        │
└─────────────────────────────────────────────────────────────┘
```

## 🚀 Como Começar

### Pré-requisitos
- **AWS Account** com permissões administrativas
- **Ambiente de lab** configurado (AWS Jam)
- **Conhecimento básico** de VPC, IAM, S3, KMS
- **AWS CLI** configurado (opcional, mas recomendado)

### Ordem Recomendada de Execução
1. **Task 1** (VPC Lambda) - Base de rede
2. **Task 2** (S3 Permissions) - Permissões básicas
3. **Task 4** (Cross-Account) - Segurança entre contas
4. **Task 3** (KMS) - Mais complexo, pode requerer dicas

### Estratégia de Resolução
```
1. 📖 Ler a task completamente
2. 🔍 Identificar o problema específico
3. 🧪 Reproduzir o erro (quando possível)
4. 🔧 Implementar a correção
5. ✅ Validar a solução
6. 📝 Documentar o aprendizado
```

## 🎯 Dificuldade e Tempo

| Task | Dificuldade | Tempo Est. | Conceitos Principais |
|------|-------------|------------|---------------------|
| **Task 1** | ⭐⭐☆☆☆ | 15-20 min | VPC, Networking |
| **Task 2** | ⭐⭐☆☆☆ | 10-15 min | IAM, S3 Permissions |
| **Task 4** | ⭐⭐⭐☆☆ | 15-20 min | Cross-Account Security |
| **Task 3** | ⭐⭐⭐⭐☆ | 20-25 min | KMS, Key Policies |

**Total estimado:** 60-80 minutos

## 🎓 Lições Aprendidas Principais

### 🔐 Segurança
- **Least Privilege:** Sempre conceder apenas permissões mínimas necessárias
- **Resource Specificity:** Usar ARNs específicos em vez de wildcards
- **Cross-Account Controls:** Nunca usar `root` como principal
- **Key Management:** KMS usa exclusivamente Key Policies

### 🌐 Networking
- **Lambda VPC:** Funções em VPC precisam de subnets privadas para internet
- **NAT Gateway:** Essencial para conectividade de saída
- **Security Groups:** Regras adequadas para tráfego

### 🛠️ Troubleshooting
- **CloudWatch Logs:** Primeira fonte de diagnóstico
- **Policy Simulator:** Testar permissões antes de aplicar
- **Step-by-step:** Validar cada mudança incrementalmente
- **Lab Validators:** Podem ter expectativas específicas de formato

## ⚠️ Armadilhas Comuns

### Task 1 - VPC Lambda
- ❌ **Erro:** Colocar Lambda em subnet pública esperando IP público
- ✅ **Correto:** Lambda em subnet privada com rota para NAT

### Task 2 - S3 Permissions
- ❌ **Erro:** Esquecer de separar permissões bucket vs object
- ✅ **Correto:** `ListBucket` no bucket, `GetObject` nos objetos

### Task 3 - KMS
- ❌ **Erro:** Criar statement separado (tecnicamente correto)
- ✅ **Correto:** Adicionar ao array do statement existente

### Task 4 - Cross-Account
- ❌ **Erro:** Usar `root` como principal
- ✅ **Correto:** Especificar role exato

## 🔍 Ferramentas Úteis

### AWS Console
- **Lambda Console:** Configuração VPC e permissões
- **IAM Console:** Gestão de roles e policies
- **S3 Console:** Bucket policies e permissions
- **KMS Console:** Key policies e key management

### AWS CLI Commands
```bash
# Verificar configuração Lambda
aws lambda get-function --function-name MyFunction

# Testar permissões S3
aws s3 ls s3://bucket-name/

# Verificar Key Policy
aws kms get-key-policy --key-id key-id --policy-name default

# Assumir role cross-account
aws sts assume-role --role-arn arn:aws:iam::ACCOUNT:role/ROLE --role-session-name test
```

### Debugging Tools
- **CloudWatch Logs:** Logs detalhados das funções
- **CloudTrail:** Auditoria de chamadas de API
- **VPC Flow Logs:** Análise de tráfego de rede
- **IAM Policy Simulator:** Teste de permissões

## 🏆 Critérios de Sucesso

### Por Task
- ✅ **Task 1:** Lambda acessa internet e EC2 privado
- ✅ **Task 2:** Lambda realiza CRUD no S3 sem erros
- ✅ **Task 3:** Security Admin gerencia chave KMS
- ✅ **Task 4:** Apenas role específico acessa bucket

### Geral
- ✅ **Compreensão:** Entender o "porquê" de cada correção
- ✅ **Aplicação:** Saber aplicar em cenários similares
- ✅ **Troubleshooting:** Diagnosticar problemas similares
- ✅ **Best Practices:** Implementar segurança adequada

## 🔗 Recursos Adicionais

### Documentação AWS
- [VPC User Guide](https://docs.aws.amazon.com/vpc/)
- [IAM User Guide](https://docs.aws.amazon.com/iam/)
- [S3 User Guide](https://docs.aws.amazon.com/s3/)
- [KMS Developer Guide](https://docs.aws.amazon.com/kms/)

### Best Practices
- [AWS Security Best Practices](https://aws.amazon.com/security/security-resources/)
- [Well-Architected Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/)
- [IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

## 🆘 Troubleshooting Geral

### Se uma task não valida
1. **Revisar logs:** CloudWatch para erros específicos
2. **Verificar sintaxe:** JSON policies devem ser válidas
3. **Testar manualmente:** Reproduzir operação esperada
4. **Usar dicas:** Labs podem ter expectativas específicas
5. **Documentar diferenças:** Entre "correto" e "aceito pelo lab"

### Problemas de permissão
1. **Verificar roles:** Função está usando o role correto?
2. **Checar policies:** Todas as permissões necessárias?
3. **Validar recursos:** ARNs estão corretos?
4. **Testar isoladamente:** Uma permissão por vez

---

**🎉 Boa sorte com o challenge!**

> **💭 Reflexão:** Este challenge não é apenas sobre configurar serviços AWS, mas sobre desenvolver uma mentalidade de segurança e troubleshooting sistemático. As habilidades aprendidas aqui são essenciais para qualquer profissional de cloud.
