# 🚀 Foundational - Serverless Deployment Pipeline with AWS DevOps Tools

## 📋 Visão Geral

Este desafio foca na **implementação de um pipeline de CI/CD completo** para aplicações serverless usando ferramentas DevOps da AWS. O objetivo é aprender sobre **automação de deploy**, **versionamento de código** e **integração entre serviços AWS** para criar um fluxo de desenvolvimento profissional.

## 🎯 Objetivos de Aprendizado

- ✅ Implementar **pipeline de CI/CD** com AWS DevOps Tools
- ✅ Configurar **versionamento** com AWS CodeCommit
- ✅ Automatizar **deploy** com AWS CodePipeline
- ✅ Integrar **API Gateway** com AWS Lambda
- ✅ Desenvolver habilidades de **troubleshooting** em pipelines
- ✅ Entender **validação rígida** em labs hands-on

## 🏗️ Arquitetura do Desafio

### Serviços AWS Envolvidos:
- **AWS CodeCommit** - Repositório Git gerenciado
- **AWS CodePipeline** - Pipeline de CI/CD
- **AWS Lambda** - Ambiente de execução serverless
- **Amazon API Gateway** - Interface de API
- **AWS CodeBuild** - Serviço de build (via buildspec.yml)

### Fluxo do Pipeline:
```
CodeCommit → CodePipeline → CodeBuild → Lambda Deploy → API Gateway
```

### Cenário:
Pipeline Pioneers precisa automatizar o deploy de sua aplicação serverless Node.js, utilizando um pipeline completo de DevOps com validação automática.

## 📚 Tasks Disponíveis

### 📝 [Task 1 - CodeCommit Setup](./task1.md)
**Foco:** Configuração inicial do repositório e upload de arquivos

**Conceitos principais:**
- Acesso ao AWS CodeCommit
- Upload de arquivos obrigatórios (index.js, buildspec.yml)
- Configuração do branch main
- Preparação para integração com pipeline

**Dificuldade:** ⭐⭐☆☆☆  
**Tempo estimado:** 15-20 minutos

---

### ❓ [Task 2 - API Gateway Knowledge](./task2.md)
**Foco:** Conhecimento teórico sobre Amazon API Gateway

**Conceitos principais:**
- Tipos de API suportados (HTTP, REST, WebSocket)
- Soluções custo-efetivas para alta demanda
- Serviços de logging e monitoramento (CloudTrail)
- Escolha de arquiteturas adequadas

**Dificuldade:** ⭐☆☆☆☆  
**Tempo estimado:** 10-15 minutos

---

### 🔧 [Task 3 - Pipeline Configuration](./task3.md)
**Foco:** Configuração e correção do pipeline de CI/CD

**Conceitos principais:**
- Identificação de problemas no pipeline
- Correção de configuração de branch (develop → main)
- Execução de Release change
- Validação de deploy bem-sucedido

**Dificuldade:** ⭐⭐⭐☆☆  
**Tempo estimado:** 20-30 minutos

---

### 🌐 [Task 4 - API Gateway Integration](./task4.md)
**Foco:** Integração API Gateway com Lambda e validação de resposta

**Conceitos principais:**
- Lambda Proxy Integration
- Troubleshooting de validação rígida em labs
- Diferença entre teste interno e validador de produção
- Deploy via pipeline para correções
- Importância de seguir instruções específicas

**Dificuldade:** ⭐⭐⭐⭐☆  
**Tempo estimado:** 30-45 minutos

## 🚀 Como Começar

### Pré-requisitos
- **AWS Account** com permissões adequadas para DevOps Tools
- **Conhecimento básico** de Git, CI/CD e Lambda
- **Ambiente de lab** com recursos pré-configurados
- **Acesso** aos serviços CodeCommit, CodePipeline, Lambda e API Gateway

### Ordem Recomendada
1. **Task 1** - CodeCommit Setup (configuração inicial)
2. **Task 2** - API Gateway Knowledge (conhecimento teórico)
3. **Task 3** - Pipeline Configuration (correção de pipeline)
4. **Task 4** - API Gateway Integration (integração e validação)

### Estrutura do Projeto
```
Foundational - Serverless Deployment Pipeline with AWS DevOps Tools/
├── README.md          # Este arquivo - visão geral
├── task1.md          # CodeCommit Setup - configuração inicial
├── task2.md          # API Gateway Knowledge - questões teóricas
├── task3.md          # Pipeline Configuration - correção de pipeline
└── task4.md          # API Gateway Integration - integração final
```

## 🎓 Conceitos Fundamentais

### 🔄 Pipeline de CI/CD
- **CodeCommit:** Repositório Git gerenciado pela AWS
- **CodePipeline:** Orquestração de stages de deploy
- **CodeBuild:** Execução de builds via buildspec.yml
- **Lambda Deploy:** Deploy automático de funções serverless

### 🌐 Integração API Gateway + Lambda
- **Lambda Proxy Integration:** Integração direta sem transformação
- **Response Format:** Objeto com statusCode, headers e body
- **Content-Type:** Adequação do tipo de conteúdo
- **Deploy Stages:** Diferença entre teste interno e produção

### ⚠️ Validação em Labs Hands-on
- **Validação rígida:** Labs esperam outputs específicos
- **Instruções críticas:** Dicas step-by-step são essenciais
- **Teste vs Produção:** Diferenças entre ambientes
- **Troubleshooting:** Identificação de problemas específicos

## 🚨 Troubleshooting Comum

### Problemas de Pipeline

#### Pipeline falha com "no branch named develop was found"
- **Causa:** Pipeline configurado para branch inexistente
- **Solução:** Alterar configuração de branch no Source stage

#### Deploy não executa após Release change
- **Causa:** Pipeline não detecta mudanças ou falha em stage anterior
- **Solução:** Verificar logs do pipeline e executar Release change novamente

### Problemas de API Gateway

#### Status 200 mas lab não aprova
- **Causa:** Conteúdo da resposta não atende critérios específicos
- **Solução:** Revisar instruções e ajustar body da resposta Lambda

#### Permissões negadas para alterações
- **Causa:** Ambiente de lab com permissões restritas
- **Solução:** Focar em soluções que não requerem permissões adicionais

### Estratégias de Resolução
1. **Leia instruções cuidadosamente** - Dicas contêm informações críticas
2. **Teste incrementalmente** - Valide cada mudança antes de prosseguir
3. **Foque no conteúdo** - Não apenas funcionalidade, mas output específico
4. **Use pipeline para deploy** - Mudanças de código via CodePipeline
5. **Documente soluções** - Registre o que funcionou para referência

## 💡 Boas Práticas

### 🔄 Pipeline de CI/CD
- **Branch strategy:** Use branches consistentes (main vs develop)
- **Buildspec.yml:** Configure adequadamente para ambiente Node.js
- **Release change:** Execute após mudanças significativas
- **Monitoramento:** Acompanhe logs de execução do pipeline

### 🌐 Integração Lambda + API Gateway
- **Lambda Proxy:** Use formato correto de resposta
- **Content-Type:** Adeque ao tipo de conteúdo retornado
- **Error handling:** Implemente tratamento de erros adequado
- **Testing:** Teste tanto internamente quanto via Invoke URL

### 📋 Desenvolvimento
- **Versionamento:** Use Git adequadamente para controle de versão
- **Documentação:** Mantenha README e comentários atualizados
- **Validação:** Teste localmente antes de fazer commit
- **Deploy:** Use pipeline para todas as mudanças de produção

## 🏆 Critérios de Sucesso

- [ ] **Repositório configurado** com arquivos necessários
- [ ] **Pipeline funcionando** sem erros de execução
- [ ] **Deploy automático** para Lambda executado com sucesso
- [ ] **API Gateway integrado** retornando respostas corretas
- [ ] **Validação de lab** aprovada para todas as tasks
- [ ] **Conhecimento prático** de DevOps Tools aplicado

## 📖 Recursos Adicionais

### Documentação AWS
- [AWS CodeCommit User Guide](https://docs.aws.amazon.com/codecommit/)
- [AWS CodePipeline User Guide](https://docs.aws.amazon.com/codepipeline/)
- [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/)
- [Amazon API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/)

### Ferramentas Úteis
- [AWS CLI CodeCommit Commands](https://docs.aws.amazon.com/cli/latest/reference/codecommit/)
- [AWS CLI CodePipeline Commands](https://docs.aws.amazon.com/cli/latest/reference/codepipeline/)
- [AWS Console DevOps Tools](https://console.aws.amazon.com/codesuite/)

## 🎯 Próximos Passos

Após completar este desafio, considere:
- **Automação avançada:** Implementar pipelines mais complexos
- **Monitoramento:** Adicionar CloudWatch e alertas
- **Segurança:** Implementar IAM roles e políticas adequadas
- **Certificações:** Preparar-se para exames AWS DevOps

---

**🎉 Boa sorte com o pipeline!**

> **💭 Reflexão:** Este desafio combina conceitos fundamentais de DevOps com serviços AWS, demonstrando como automatizar deploy de aplicações serverless de forma profissional e escalável.
