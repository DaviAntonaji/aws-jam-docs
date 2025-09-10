# AWS Jam Challenges - Easy Level

## 📋 Visão Geral

Esta seção contém desafios de **nível fácil** do AWS Jam, focados em conceitos fundamentais de AWS e boas práticas de segurança. Cada desafio é independente e pode ser executado separadamente.

## 🎯 Objetivos Gerais

- ✅ Aprender conceitos fundamentais de AWS
- ✅ Implementar boas práticas de segurança
- ✅ Entender arquiteturas de rede e aplicação
- ✅ Navegar validações automáticas de labs
- ✅ Desenvolver habilidades práticas em produção

## 📚 Desafios Disponíveis

### 1. 🔍 [Find the secret message hidden in SQS queue!](./Find%20the%20secret%20message%20hidden%20in%20SQS%20queue/)

**Foco:** AWS Lambda, VPC Endpoints, Security Groups, IAM

**Conceitos principais:**
- Diagnóstico de timeouts de Lambda em VPC
- Configuração de VPC Endpoints com Security Groups
- Implementação de least privilege na rede
- Navegação de validações automáticas de labs

**Dificuldade:** ⭐⭐☆☆☆  
**Tempo estimado:** 45-60 minutos

---

### 2. 🤝 [Sharing is caring - reusable code across Lambdas](./Sharing%20is%20caring%20-%20reusable%20code%20across%20Lambdas/)

**Foco:** AWS Lambda Layers, Versionamento, Deploy Canary

**Conceitos principais:**
- Criação e configuração de Lambda Layers
- Compartilhamento de código entre funções
- Estratégias de versionamento
- Deploy canary para testes graduais

**Dificuldade:** ⭐⭐☆☆☆  
**Tempo estimado:** 30-45 minutos

---

### 3. 🛡️ [Protect my CloudFront Origin](./Protect%20my%20CloudFront%20Origin/)

**Foco:** CloudFront, ALB, Security Groups, Proteção em Camadas

**Conceitos principais:**
- Identificação de vulnerabilidades de segurança
- Proteção L4 (Security Groups + Prefix Lists)
- Proteção L7 (Headers secretos + Listener Rules)
- Arquitetura de segurança em profundidade

**Dificuldade:** ⭐⭐⭐☆☆  
**Tempo estimado:** 60-90 minutos

---

### 4. 🧹 [The Cleanup Mission - Restoring Order in the Cloud](./The%20Cleanup%20Mission%20-%20Restoring%20ORder%20in%20the%20Cloud/)

**Foco:** VPC Cleanup, Security Groups, Dependências de Recursos, Governança

**Conceitos principais:**
- Identificação e resolução de dependências entre recursos AWS
- Ordem correta de deleção de recursos de infraestrutura
- Limpeza de VPCs, Security Groups e recursos órfãos
- Boas práticas de governança e limpeza de recursos

**Dificuldade:** ⭐⭐⭐☆☆  
**Tempo estimado:** 75-90 minutos

---

### 5. 🚀 [Foundational - Serverless Deployment Pipeline with AWS DevOps Tools](./Foundational%20-%20Serverless%20Deployment%20Pipeline%20with%20AWS%20DevOps%20Tools/)

**Foco:** CI/CD Pipeline, CodeCommit, CodePipeline, API Gateway, Lambda Integration

**Conceitos principais:**
- Implementação de pipeline completo de CI/CD com AWS DevOps Tools
- Configuração de versionamento com AWS CodeCommit
- Automação de deploy com AWS CodePipeline e CodeBuild
- Integração API Gateway com Lambda via Proxy Integration
- Troubleshooting de validação rígida em labs hands-on

**Dificuldade:** ⭐⭐⭐⭐☆  
**Tempo estimado:** 90-120 minutos

---

### 6. 📊 [Unified Data Querying with Amazon Athena](./Unified%20Data%20Querying%20with%20%20Amazon%20Athena/)

**Foco:** Análise de Dados, Federated Queries, SQL, S3, DynamoDB, MySQL

**Conceitos principais:**
- Consultas SQL sem servidor com Amazon Athena
- Análise de datasets CSV armazenados no S3
- Federated Queries com DynamoDB e MySQL
- JOINs federados entre diferentes fontes de dados
- Troubleshooting de conectores federados e problemas de infraestrutura

**Dificuldade:** ⭐⭐⭐⭐☆  
**Tempo estimado:** 90-120 minutos (Task 4 pode ser bloqueada por problemas de lab)

## 🚀 Como Começar

### Pré-requisitos
- **AWS Account** com permissões adequadas
- **Conhecimento básico** de serviços AWS
- **Ambiente de lab** configurado (quando aplicável)

### Ordem Recomendada
1. **Sharing is caring** - Conceitos de Lambda Layers (mais simples)
2. **Find the secret message** - Rede e segurança (intermediário)
3. **The Cleanup Mission** - Governança e limpeza de recursos (intermediário)
4. **Unified Data Querying with Amazon Athena** - Análise de dados e Federated Queries (avançado)
5. **Foundational - Serverless Deployment Pipeline** - DevOps e CI/CD (avançado)
6. **Protect my CloudFront Origin** - Segurança avançada (mais complexo)

### Estrutura Padrão
Cada desafio segue a estrutura:
```
Desafio/
├── README.md          # Visão geral e instruções
├── task1.md          # Primeira tarefa
├── task2.md          # Segunda tarefa
└── ...               # Tarefas adicionais
```

## 🎓 Lições Aprendidas (Comuns a Todos)

### ⚠️ Validação Automática de Labs
- **Siga as dicas literalmente:** Validadores podem estar "hard-coded"
- **Documente diferenças:** Separe "correto tecnicamente" vs "esperado pelo lab"
- **Teste após cada mudança:** Execute validações após cada alteração
- **Ambientes restritos:** Adapte-se às limitações do ambiente

### 🔧 Troubleshooting Comum
- **Timeouts de rede:** Verifique Security Groups e conectividade
- **Permissões restritas:** Use identity-based policies quando possível
- **Validação não passa:** Mesmo com execução correta, checker pode não aceitar
- **Documentação:** Registre soluções que funcionam

### 💡 Boas Práticas
- **Least Privilege:** Use permissões mínimas necessárias
- **Defesa em profundidade:** Implemente múltiplas camadas de proteção
- **Monitoramento:** Configure logs e alertas adequados
- **Documentação:** Mantenha registro de configurações e decisões

## 📖 Recursos Adicionais

### Documentação AWS
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)
- [AWS Security Best Practices](https://aws.amazon.com/security/security-resources/)
- [AWS Service Documentation](https://docs.aws.amazon.com/)

### Ferramentas Úteis
- [AWS CLI](https://aws.amazon.com/cli/)
- [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
- [AWS CloudWatch](https://aws.amazon.com/cloudwatch/)

## 🏆 Critérios de Sucesso Gerais

- [ ] **Compreensão conceitual:** Entender o "porquê" além do "como"
- [ ] **Implementação prática:** Configurar serviços corretamente
- [ ] **Validação:** Confirmar que soluções funcionam
- [ ] **Troubleshooting:** Resolver problemas comuns
- [ ] **Aplicação:** Transferir conhecimento para cenários reais

## 🆘 Suporte e Ajuda

### Problemas Comuns
- **Ambiente de lab:** Verifique se recursos estão disponíveis
- **Permissões:** Confirme que tem acesso necessário aos serviços
- **Validação:** Siga instruções do lab literalmente quando necessário
- **Timeout:** Aguarde propagação de mudanças (pode levar alguns minutos)

### Estratégias de Resolução
1. **Leia cuidadosamente:** Instruções e mensagens de erro
2. **Documente tentativas:** Registre o que funcionou e o que não funcionou
3. **Teste incrementalmente:** Valide cada mudança antes de prosseguir
4. **Use recursos disponíveis:** AWS Documentation, CloudWatch logs, etc.

## 🎯 Próximos Passos

Após completar os desafios "easy", considere:
- **Medium Level:** Desafios mais complexos com múltiplos serviços
- **Projetos práticos:** Implementar soluções similares em ambiente próprio
- **Certificações:** Preparar-se para exames AWS
- **Comunidade:** Compartilhar experiências e aprender com outros

---

**🎉 Boa sorte com os desafios!**

> **💭 Reflexão:** Estes desafios não são apenas sobre configurar serviços AWS, mas sobre desenvolver mentalidade de segurança, troubleshooting e pensamento arquitetural - habilidades essenciais para qualquer profissional de cloud.
