# Medium Difficulty - AWS JAM Challenges 🎯

## 📋 Visão Geral

Esta pasta contém projetos de **dificuldade média** do AWS JAM, focados em implementações práticas de serviços AWS avançados. Cada projeto inclui documentação completa, código-fonte e guias detalhados para facilitar o aprendizado e reutilização em competições.

## 🚀 Projetos Disponíveis

### 1. Automate EKS Access Controls using Bedrock Agent 🤖

**Objetivo:** Automatizar o gerenciamento de EKS Access Entries usando Amazon Bedrock Agent com interface de linguagem natural.

#### 🎯 Funcionalidades
- ✅ **Criação automatizada** de EKS Access Entries
- ✅ **Deleção automatizada** de EKS Access Entries  
- ✅ **Configuração automática** de EKS Pod Identity Association
- ✅ **Interface de linguagem natural** para todas as operações

#### 🛠️ Tecnologias
- **Amazon Bedrock** - Agentes de IA
- **Amazon EKS** - Kubernetes gerenciado
- **AWS Lambda** - Processamento serverless
- **AWS IAM** - Gerenciamento de identidade
- **OpenAPI 3.0** - Especificação de APIs

#### 📊 Resultados
- **Redução de 90%** no tempo de configuração manual
- **Eliminação de erros** de configuração
- **Automação completa** do ciclo de vida de Access Entries

#### 📁 Estrutura
```
Automate EKS Access Controls using Bedrock Agent/
├── README.md              # Documentação completa
├── task1.md               # Create EKS Access Entry
├── task2.md               # Delete EKS Access Entry
├── task3.md               # Update IAM Role for Pod Identity
└── utils/
    ├── openai-schema.yaml # Schema OpenAPI
    └── lambda.js          # Função Lambda principal
```

---

### 2. Trace with AWS Lambda Powertools 📊

**Objetivo:** Implementar observabilidade avançada em funções Lambda usando AWS Lambda Powertools e X-Ray para rastreamento distribuído.

#### 🎯 Funcionalidades
- ✅ **Tracing automático** com AWS X-Ray
- ✅ **Instrumentação** com Lambda Powertools
- ✅ **Subsegmentos** para operações DynamoDB
- ✅ **Observabilidade** completa de aplicações serverless

#### 🛠️ Tecnologias
- **AWS Lambda** - Computação serverless
- **AWS X-Ray** - Rastreamento distribuído
- **AWS Lambda Powertools** - Observabilidade e produtividade
- **Amazon DynamoDB** - Banco NoSQL
- **Python/Node.js** - Runtimes de desenvolvimento

#### 📊 Resultados
- **Visibilidade completa** do fluxo de execução
- **Identificação rápida** de gargalos
- **Debugging eficiente** de aplicações distribuídas
- **Métricas detalhadas** de performance

#### 📁 Estrutura
```
Trace with AWS Lambda Powertools/
├── README.md              # Documentação completa
├── task-1.md              # Executar função Lambda
├── task2.md               # Ativar X-Ray tracing
├── task3.md               # Instrumentar com Powertools
└── lambda.py              # Código da função Lambda
```

## 🎯 Guia Rápido para Competições

### Preparação Prévia
1. **Familiarize-se** com os serviços AWS principais
2. **Pratique** com AWS CLI e Console
3. **Entenda** conceitos de IAM e segurança
4. **Estude** observabilidade (CloudWatch, X-Ray)

### Durante a Competição
1. **Leia** cuidadosamente os requisitos
2. **Use** a documentação como referência rápida
3. **Siga** os guias passo-a-passo
4. **Teste** cada etapa antes de prosseguir
5. **Valide** resultados com ferramentas AWS

### Troubleshooting Comum
| Problema | Solução Rápida |
|----------|----------------|
| **Erro de permissão** | Verificar políticas IAM |
| **Região incorreta** | Confirmar região no console |
| **Função não encontrada** | Verificar nome e região |
| **Trace não aparece** | Aguardar alguns segundos |

## 🛠️ Tecnologias Principais

### Core AWS Services
- **Amazon Bedrock** - IA generativa e agentes
- **Amazon EKS** - Kubernetes gerenciado
- **AWS Lambda** - Computação serverless
- **Amazon DynamoDB** - Banco NoSQL
- **AWS X-Ray** - Observabilidade distribuída
- **AWS IAM** - Gerenciamento de identidade

### Frameworks e Ferramentas
- **AWS Lambda Powertools** - Observabilidade e produtividade
- **OpenAPI 3.0** - Especificação de APIs
- **AWS SDK v3** - SDKs oficiais da AWS
- **boto3** - SDK Python para AWS

## 📚 Recursos de Aprendizado

### Documentação Oficial
- [AWS Lambda Powertools](https://awslabs.github.io/aws-lambda-powertools-python/)
- [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/)
- [Amazon EKS](https://docs.aws.amazon.com/eks/)
- [AWS X-Ray](https://docs.aws.amazon.com/xray/)

### Conceitos Importantes
- **Serverless Architecture** - Computação sem servidor
- **Observability** - Observabilidade de aplicações
- **Infrastructure as Code** - Infraestrutura como código
- **API Design** - Design de APIs RESTful
- **Security Best Practices** - Melhores práticas de segurança

## 🏆 Dicas para Competições

### Estratégia
- ⚡ **Comece** com projetos mais simples
- ⚡ **Use** a documentação como referência
- ⚡ **Teste** frequentemente
- ⚡ **Valide** cada etapa

### Ferramentas Essenciais
- **AWS CLI** - Interface de linha de comando
- **AWS Console** - Interface web
- **CloudWatch Logs** - Logs e monitoramento
- **X-Ray Console** - Rastreamento distribuído

### Tempo de Execução
- **Projeto EKS + Bedrock**: ~45-60 minutos
- **Projeto Lambda + Powertools**: ~30-45 minutos
- **Total estimado**: ~1.5-2 horas

## 📖 Próximos Passos

1. **Explore** os projetos individuais
2. **Leia** a documentação completa
3. **Pratique** em ambiente de desenvolvimento
4. **Adapte** para seus cenários específicos
5. **Compartilhe** conhecimento com a comunidade

---

**Desenvolvido para acelerar seu sucesso em competições AWS! 🚀**

*Última atualização: $(date)*
