# AWS Jam Challenges - Medium Level

## 📋 Visão Geral

Esta seção contém desafios de **nível médio** do AWS Jam, focados em implementações práticas de serviços AWS avançados e conceitos de observabilidade. Cada desafio é independente e pode ser executado separadamente.

## 🎯 Objetivos Gerais

- ✅ Implementar automação com IA generativa (Bedrock)
- ✅ Dominar observabilidade avançada (X-Ray + Powertools)
- ✅ Entender arquiteturas serverless complexas
- ✅ Aplicar melhores práticas de desenvolvimento
- ✅ Desenvolver habilidades em produção

## 📚 Desafios Disponíveis

### 1. 🤖 [Automate EKS Access Controls using Bedrock Agent](./Automate%20EKS%20Access%20Controls%20using%20Bedrock%20Agent/)

**Foco:** Amazon Bedrock, EKS, Lambda, Automação com IA

**Conceitos principais:**
- Automação de EKS Access Entries via linguagem natural
- Configuração de Bedrock Agents com OpenAPI
- Integração Lambda + EKS + IAM
- EKS Pod Identity Association

**Dificuldade:** ⭐⭐⭐⭐☆  
**Tempo estimado:** 60-90 minutos

---

### 2. 📊 [Trace with AWS Lambda Powertools](./Trace%20with%20AWS%20Lambda%20Powertools/)

**Foco:** Observabilidade, AWS X-Ray, Lambda Powertools, Debugging

**Conceitos principais:**
- Tracing distribuído com AWS X-Ray
- Instrumentação com Lambda Powertools
- Subsegmentos para operações DynamoDB
- Observabilidade completa de aplicações serverless

**Dificuldade:** ⭐⭐⭐☆☆  
**Tempo estimado:** 45-60 minutos

> **💡 Nota:** Este desafio é mais acessível e pode ser feito antes do EKS/Bedrock

## 🚀 Como Começar

### Pré-requisitos
- **AWS Account** com permissões para Bedrock, EKS, Lambda, X-Ray
- **Conhecimento intermediário** de serviços AWS
- **Ambiente de lab** configurado (quando aplicável)
- **Familiaridade** com conceitos de observabilidade

### Ordem Recomendada
1. **Trace with AWS Lambda Powertools** - Observabilidade (conceitos fundamentais)
2. **Automate EKS Access Controls** - IA + Automação (mais complexo)

### Estrutura Padrão
Cada desafio segue a estrutura:
```
Desafio/
├── README.md          # Visão geral e instruções
├── task1.md          # Primeira tarefa
├── task2.md          # Segunda tarefa
├── task3.md          # Terceira tarefa
└── utils/            # Código e configurações (quando aplicável)
```

## 🔧 Conceitos Técnicos Avançados

### 🤖 Automação com IA (Bedrock)
- **Bedrock Agents:** Agentes de IA para automação
- **OpenAPI Schema:** Especificação de APIs para agentes
- **Linguagem Natural:** Interface intuitiva para operações complexas
- **Action Groups:** Grupos de ações para agentes

### 📊 Observabilidade Avançada
- **Distributed Tracing:** Rastreamento distribuído com X-Ray
- **Lambda Powertools:** Instrumentação avançada
- **Subsegments:** Segmentação detalhada de operações
- **Service Maps:** Visualização de dependências

### 🏗️ Arquiteturas Serverless
- **Event-driven:** Arquiteturas baseadas em eventos
- **Microservices:** Serviços independentes e escaláveis
- **API Design:** Design de APIs RESTful
- **Error Handling:** Tratamento robusto de erros

## 🎓 Lições Aprendidas (Específicas para Medium)

### 🤖 Automação com Bedrock
- **Schema Validation:** Valide OpenAPI schemas antes do deploy
- **Action Groups:** Configure corretamente os grupos de ações
- **Resource Policies:** Verifique permissões do Lambda para Bedrock
- **Testing:** Use Test Agent para validar funcionalidades

### 📊 Observabilidade
- **Layers:** Use layers oficiais do Lambda Powertools
- **Environment Variables:** Configure variáveis de ambiente corretamente
- **Service Naming:** Use nomes consistentes para serviços
- **Subsegments:** Crie subsegmentos para operações importantes

### 🔧 Troubleshooting Avançado
- **X-Ray Console:** Use o console X-Ray para debug
- **CloudWatch Logs:** Monitore logs estruturados
- **IAM Permissions:** Verifique permissões específicas (X-Ray, EKS, etc.)
- **Region Consistency:** Mantenha consistência de região

## 📖 Recursos Adicionais

### Documentação AWS
- [Amazon Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [AWS Lambda Powertools](https://awslabs.github.io/aws-lambda-powertools-python/)
- [AWS X-Ray Documentation](https://docs.aws.amazon.com/xray/)
- [Amazon EKS Documentation](https://docs.aws.amazon.com/eks/)

### Conceitos Avançados
- [OpenAPI Specification](https://swagger.io/specification/)
- [Distributed Tracing Patterns](https://aws.amazon.com/builders-library/distributed-tracing/)
- [Serverless Architecture Patterns](https://aws.amazon.com/serverless/)
- [Observability Best Practices](https://aws.amazon.com/builders-library/observability/)

## 🏆 Critérios de Sucesso Gerais

- [ ] **Implementação técnica:** Configurar serviços corretamente
- [ ] **Validação funcional:** Confirmar que soluções funcionam
- [ ] **Observabilidade:** Implementar monitoramento adequado
- [ ] **Documentação:** Manter código e configurações documentados
- [ ] **Aplicação prática:** Transferir conhecimento para cenários reais

## 🆘 Troubleshooting Específico

### Problemas Comuns - Bedrock + EKS
- **"Agent not found":** Verificar região e alias ativa
- **AccessDenied Lambda:** Verificar resource policy do Lambda
- **Schema errors:** Validar indentação YAML e tipos
- **Task validation:** Verificar frase exata no OpenAPI

### Problemas Comuns - X-Ray + Powertools
- **Active tracing não aparece:** Verificar aba Configuration correta
- **Permission errors:** Aceitar sugestão AWSXRayDaemonWriteAccess
- **Layer not found:** Verificar região e versão do runtime
- **Service name não aparece:** Verificar POWERTOOLS_SERVICE_NAME

### 🔍 Estratégias de Debug
1. **Use consoles AWS:** X-Ray, CloudWatch, Bedrock
2. **Monitore logs:** CloudWatch Logs com estrutura adequada
3. **Valide permissões:** IAM policies específicas para cada serviço
4. **Teste incrementalmente:** Valide cada componente antes de prosseguir

## 🎯 Dicas para Competições

### Preparação Específica
- ✅ **Conheça** Bedrock Agents e OpenAPI
- ✅ **Pratique** com Lambda Powertools
- ✅ **Entenda** conceitos de EKS Access Entries
- ✅ **Familiarize-se** com X-Ray console e traces

### Durante a Competição
- ⚡ **Configure** observabilidade primeiro (X-Ray)
- ⚡ **Valide** schemas OpenAPI antes do deploy
- ⚡ **Teste** agentes Bedrock com Test Agent
- ⚡ **Monitore** traces e logs durante execução

### Tempo de Execução
- **Lambda Powertools:** ~45-60 minutos
- **Bedrock + EKS:** ~60-90 minutos
- **Total estimado:** ~2-2.5 horas

## 🏭 Aplicação em Produção

### Melhorias Adicionais
- **Monitoring:** Configure alertas proativos
- **Security:** Implemente least privilege
- **Cost Optimization:** Monitore custos de Bedrock e X-Ray
- **Documentation:** Mantenha documentação atualizada

### Considerações de Escala
- **Bedrock:** Limites de rate e quotas
- **X-Ray:** Sampling rates para aplicações de alta escala
- **Lambda:** Cold starts e performance
- **EKS:** Cluster scaling e resource management

## 🎯 Próximos Passos

Após completar os desafios "medium", considere:
- **Advanced Level:** Desafios mais complexos com múltiplos serviços
- **Projetos práticos:** Implementar soluções similares em ambiente próprio
- **Certificações:** Preparar-se para exames AWS avançados
- **Especialização:** Focar em áreas específicas (AI/ML, Observability, etc.)

---

**🎉 Boa sorte com os desafios!**

> **💭 Reflexão:** Estes desafios medium não são apenas sobre configurar serviços AWS, mas sobre desenvolver mentalidade de automação, observabilidade e arquitetura - habilidades essenciais para profissionais sênior de cloud.