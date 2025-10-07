# AWS Jam Challenges - Medium Level

## 📋 Visão Geral

Esta seção contém desafios de **nível médio** do AWS Jam, focados em implementações práticas de serviços AWS avançados e conceitos de observabilidade. Cada desafio é independente e pode ser executado separadamente.

## 🎯 Objetivos Gerais

- ✅ Implementar pipelines de segurança automatizados
- ✅ Implementar automação com IA generativa (Bedrock)
- ✅ Dominar observabilidade avançada (X-Ray + Powertools)
- ✅ Entender arquiteturas serverless complexas
- ✅ Aplicar melhores práticas de desenvolvimento
- ✅ Desenvolver habilidades em produção e troubleshooting

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

---

### 3. 🚀 [Cyber Trek: Voyage into Secure Infrastructure](./Cyber%20Trek%20Voyage%20into%20Secure%20Infrastructure/)

**Foco:** Amazon CloudFront, Amazon S3, Security, CDN, Origin Access Control

**Conceitos principais:**
- Implementação de Origin Access Control (OAC) para restringir acesso S3
- Configuração de redirecionamento HTTP para HTTPS
- Otimização de cache com TTL customizado (1 hora)
- Habilitação de S3 Versioning para proteção de dados
- Aplicação de princípios de least privilege em bucket policies
- Criptografia em trânsito com HTTPS obrigatório
- Arquitetura CloudFront + S3 para sites estáticos seguros

**Dificuldade:** ⭐⭐⭐☆☆  
**Tempo estimado:** 60-90 minutos

---

### 4. 🛡️ [Malware In your Bucket](./Malware%20In%20your%20Bucket/)

**Foco:** Amazon S3, AWS Lambda, CloudWatch Logs, Event-Driven Architecture, Segurança

**Conceitos principais:**
- Configuração de S3 Event Notifications para Lambda
- Implementação de pipeline de detecção de malware
- Troubleshooting de integrações S3 → Lambda
- Análise de logs com CloudWatch Logs Insights
- IAM Permissions para Lambda (Execution Role + Resource Policy)
- Arquitetura serverless para segurança automatizada

**Dificuldade:** ⭐⭐⭐☆☆  
**Tempo estimado:** 30-45 minutos

> **💡 Nota:** Desafio prático focado em troubleshooting de integrações serverless

---

### 5. 🌐 [Introverted and Extroverted Networks](./Introverted%20and%20Extroverted%20Networks/)

**Foco:** AWS Transit Gateway, VPC Networking, Egress VPC Pattern, Multi-VPC Architecture, Otimização de Custos

**Conceitos principais:**
- Implementação do padrão Egress VPC para centralizar saída para Internet
- Configuração e gerenciamento de AWS Transit Gateway
- Transit Gateway Attachments e Route Tables
- Roteamento complexo bidirecional entre múltiplas VPCs
- Otimização de custos removendo NAT Gateways redundantes
- Redução de superfície de ataque consolidando pontos de saída
- Troubleshooting avançado de roteamento VPC
- Arquitetura hub-and-spoke para ambientes enterprise

**Dificuldade:** ⭐⭐⭐⭐☆ Medium-Hard  
**Tempo estimado:** 90-120 minutos

**Tarefas:**
- **Task 1 (15 pts):** Design - Identificar padrão Egress VPC
- **Task 2 (30 pts):** Deploy - Criar Egress VPC com recursos
- **Task 3 (75 pts):** Routing - Configurar Transit Gateway (MAIS DIFÍCIL)
- **Task 4 (30 pts):** Optimize - Remover recursos desnecessários

> **⚠️ NOTA IMPORTANTE:** Task 3 é considerada a mais complexa do desafio devido ao roteamento bidirecional. Documentação inclui troubleshooting detalhado com resumo de depuração via ChatGPT.

---

## 🚀 Como Começar

### Pré-requisitos
- **AWS Account** com permissões para Transit Gateway, VPC, Bedrock, EKS, Lambda, X-Ray, CloudFront, S3
- **Conhecimento intermediário** de serviços AWS e networking
- **Ambiente de lab** configurado (quando aplicável)
- **Familiaridade** com conceitos de observabilidade, segurança e roteamento de rede

### Ordem Recomendada
1. **Malware In your Bucket** - S3 + Lambda (troubleshooting prático - 30min)
2. **Cyber Trek: Voyage into Secure Infrastructure** - CloudFront + S3 (segurança - 60min)
3. **Trace with AWS Lambda Powertools** - Observabilidade (intermediário - 45min)
4. **Introverted and Extroverted Networks** - Transit Gateway + VPC (networking avançado - 90min)
5. **Automate EKS Access Controls** - IA + Automação (mais complexo - 90min)

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

### 🌐 Transit Gateway + Multi-VPC Networking
- **Egress VPC Pattern:** Padrão para centralizar saída para Internet
- **Transit Gateway:** Hub de roteamento central entre VPCs
- **TGW Attachments:** Conexões entre TGW e VPCs
- **TGW Route Tables:** Roteamento avançado com propagação e rotas estáticas
- **Roteamento Bidirecional:** Configuração de ida e retorno de tráfego
- **Hub-and-Spoke:** Arquitetura para ambientes multi-VPC
- **VPC Route Tables:** Gerenciamento complexo de múltiplas route tables
- **Otimização de Custos:** Consolidação de NAT Gateways

### 🛡️ S3 + Lambda Security Pipeline
- **Event Notifications:** Gatilhos automáticos S3 → Lambda
- **IAM Permissions:** Execution Role + Resource Policy
- **Malware Detection:** Pipeline automatizado de segurança
- **CloudWatch Logs:** Monitoramento e análise de resultados
- **Event-Driven Architecture:** Arquitetura baseada em eventos

### 🚀 CloudFront + S3 Security
- **Origin Access Control (OAC):** Restrição de acesso moderno
- **Bucket Policies:** Controle granular de acesso
- **HTTPS Enforcement:** Redirecionamento e criptografia
- **Cache Optimization:** Balanceamento de TTLs
- **S3 Versioning:** Proteção contra exclusões

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

### 🌐 Transit Gateway + Multi-VPC
- **Rota 0.0.0.0/0 no TGW:** SEMPRE aponte para Egress VPC attachment (Static)
- **Egress Private RT:** 0.0.0.0/0 deve apontar para NAT, NÃO para TGW
- **Rotas de Retorno CRÍTICAS:** Adicione 10.x/16 → TGW em AMBAS route tables da Egress (private E public)
- **Public RT da Egress:** Necessária para o NAT Gateway rotear pacotes de retorno
- **Attachments:** Sempre use subnets PRIVADAS, nunca públicas
- **Estados Transitórios:** TGW leva 1-2min, NAT deletion 2-3min
- **Associações Explícitas:** Validador exige subnet associations explícitas em route tables
- **Troubleshooting:** Trace o caminho completo (ida E volta) de cada pacote

### 🛡️ S3 + Lambda Security Pipeline
- **Event Triggers:** Configure via Lambda console para permissões automáticas
- **Resource Policy:** S3 precisa de permissão explícita para invocar Lambda
- **Execution Role:** Lambda precisa de s3:GetObject + CloudWatch Logs
- **First Execution:** Aguarde 30-60 segundos para Log Group aparecer
- **Logs Insights:** Use queries para extrair informações específicas rapidamente

### 🚀 CloudFront + S3 Security
- **OAC Configuration:** Use ARN completo da distribuição na bucket policy
- **HTTPS Enforcement:** Configure redirecionamento automático
- **Cache TTLs:** Balance performance e atualização de conteúdo
- **Versioning:** Habilite para proteção contra exclusões
- **Deploy Time:** Aguarde 5-15 minutos para mudanças propagarem

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
- **IAM Permissions:** Verifique permissões específicas (X-Ray, EKS, CloudFront, etc.)
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

### Problemas Comuns - Transit Gateway + Multi-VPC
- **"Service did not connect via egress NAT":** Faltam rotas de retorno na Egress Public RT
- **Tráfego não sai:** Verificar rota 0.0.0.0/0 → Egress no TGW RT
- **Egress Private RT com 0.0.0.0/0 → TGW:** ERRO! Deve ser → NAT
- **Attachments Pending:** Aguardar TGW ficar Available primeiro
- **Cannot delete NAT:** Aguardar 2-3 minutos para deleção completa
- **Cannot delete subnet:** Verificar ENIs órfãs e deletar manualmente
- **IGW cannot delete:** Deve detach da VPC primeiro
- **Validador falha após limpeza:** Confirmar que não deletou subnets privadas ou attachments

### Problemas Comuns - S3 + Lambda
- **Lambda não é invocada:** Verificar se trigger está Enabled na aba Triggers
- **"No log group":** Lambda nunca executou; verificar trigger e permissões
- **Permission denied (S3):** Execution role sem s3:GetObject
- **Permission denied (Logs):** Execution role sem AWSLambdaBasicExecutionRole
- **Upload não dispara:** Verificar se arquivo foi para o bucket correto

### Problemas Comuns - CloudFront + S3
- **403 Access Denied via CloudFront:** Verificar OAC e bucket policy com ARN correto
- **HTTP não redireciona:** Aguardar deploy e limpar cache do navegador
- **Conteúdo não atualiza:** Verificar TTL e aguardar ou usar invalidation
- **Versioning não funciona:** Confirmar que está "Enabled" em Properties

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
1. **Use consoles AWS:** X-Ray, CloudWatch, Bedrock, CloudFront
2. **Monitore logs:** CloudWatch Logs com estrutura adequada
3. **Valide permissões:** IAM policies específicas para cada serviço
4. **Teste incrementalmente:** Valide cada componente antes de prosseguir

## 🎯 Dicas para Competições

### Preparação Específica
- ✅ **Conheça** Transit Gateway e Egress VPC pattern
- ✅ **Conheça** S3 Event Notifications e Lambda triggers
- ✅ **Conheça** CloudFront OAC e cache behaviors
- ✅ **Conheça** Bedrock Agents e OpenAPI
- ✅ **Pratique** com Lambda Powertools e roteamento VPC
- ✅ **Entenda** conceitos de EKS Access Entries
- ✅ **Familiarize-se** com X-Ray console e traces
- ✅ **Domine** route tables e roteamento bidirecional

### Durante a Competição
- ⚡ **Resolva** integrações S3 + Lambda primeiro (rápido)
- ⚡ **Configure** segurança CloudFront + S3
- ⚡ **Configure** observabilidade (X-Ray)
- ⚡ **Reserve tempo** para Transit Gateway (mais complexo)
- ⚡ **Trace caminhos** de ida E volta do tráfego (networking)
- ⚡ **Valide** schemas OpenAPI antes do deploy
- ⚡ **Teste** agentes Bedrock com Test Agent
- ⚡ **Monitore** traces e logs durante execução

### Tempo de Execução
- **Malware In your Bucket (S3 + Lambda):** ~30-45 minutos
- **Cyber Trek (CloudFront + S3):** ~60-90 minutos
- **Lambda Powertools:** ~45-60 minutos
- **Introverted and Extroverted Networks (Transit Gateway):** ~90-120 minutos
- **Bedrock + EKS:** ~60-90 minutos
- **Total estimado:** ~4.5-6 horas

## 🏭 Aplicação em Produção

### Melhorias Adicionais
- **Monitoring:** Configure alertas proativos
- **Security:** Implemente least privilege
- **Cost Optimization:** Monitore custos de CloudFront, Bedrock e X-Ray
- **Documentation:** Mantenha documentação atualizada
- **WAF:** Adicione proteção adicional ao CloudFront

### Considerações de Escala
- **Transit Gateway:** Suporta milhares de VPCs; planeje hierarquia de route tables
- **TGW Data Transfer:** Custos por GB transferido entre VPCs
- **NAT Gateway Bandwidth:** Até 45 Gbps por NAT; considere múltiplos para HA
- **VPC Endpoints:** Use para evitar custos de NAT com serviços AWS
- **S3 Events:** Limite de eventos por segundo (bucket throttling)
- **Lambda Concurrency:** Configure reserved concurrency para funções críticas
- **CloudWatch Logs:** Retenção de logs e custos de armazenamento
- **CloudFront:** Cache invalidations e custos de transferência
- **S3:** Lifecycle policies para versões antigas
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