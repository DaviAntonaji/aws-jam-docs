# 📊 Unified Data Querying with Amazon Athena

## 📋 Visão Geral

Este desafio foca na **análise de dados unificada** usando **Amazon Athena** para consultar diferentes fontes de dados através de **Federated Queries**. O objetivo é aprender sobre **análise de dados**, **consultas SQL** e **integração entre diferentes tipos de dados** (CSV, DynamoDB, MySQL).

## 🎯 Objetivos de Aprendizado

- ✅ Dominar **consultas SQL** no Amazon Athena
- ✅ Analisar **datasets CSV** armazenados no S3
- ✅ Implementar **Federated Queries** com DynamoDB
- ✅ Executar **JOINs federados** entre diferentes fontes
- ✅ Desenvolver habilidades de **troubleshooting** de conectores
- ✅ Entender **limitações de ambientes de lab**

## 🏗️ Arquitetura do Desafio

### Serviços AWS Envolvidos:
- **Amazon Athena** - Serviço de consulta sem servidor
- **Amazon S3** - Armazenamento de datasets CSV
- **Amazon DynamoDB** - Banco NoSQL para Federated Query
- **Amazon RDS MySQL** - Banco relacional para JOIN federado
- **AWS Lambda** - Conectores federados (DynamoDB, MySQL)

### Fontes de Dados:
- **CSV Files** - Datasets de jogos armazenados no S3
- **DynamoDB Tables** - Dados de campeões em formato NoSQL
- **MySQL Database** - Dados relacionais de títulos e informações

### Cenário:
Análise de dados de jogos usando diferentes fontes de dados, demonstrando como o Amazon Athena pode unificar consultas sobre dados heterogêneos.

## 📚 Tasks Disponíveis

### 📊 [Task 1 - Athena Setup](./task1.md)
**Foco:** Configuração inicial do ambiente Athena

**Conceitos principais:**
- Configuração do Amazon Athena Console
- Configuração de Query Result Location no S3
- Criação de tabelas a partir de dados CSV
- Primeiros passos com consultas SQL

**Dificuldade:** ⭐⭐☆☆☆  
**Tempo estimado:** 15-20 minutos

---

### 🎮 [Task 2 - CSV Data Analysis](./task2.md)
**Foco:** Análise de dados CSV com consultas SQL

**Conceitos principais:**
- Consultas COUNT() para análise estatística
- Filtragem com WHERE para dados específicos
- Análise de datasets de jogos ranqueados
- Interpretação de resultados de consultas

**Dificuldade:** ⭐⭐⭐☆☆  
**Tempo estimado:** 20-30 minutos

---

### 🔗 [Task 3 - DynamoDB Federated Query](./task3.md)
**Foco:** Consultas federadas com DynamoDB

**Conceitos principais:**
- Configuração de data source federado
- Consultas SQL sobre dados NoSQL
- CAST() para conversão de tipos de dados
- Troubleshooting de conectores federados

**Dificuldade:** ⭐⭐⭐⭐☆  
**Tempo estimado:** 30-45 minutos

---

### 🌐 [Task 4 - MySQL Federated Query](./task4.md)
**Foco:** JOIN federado entre DynamoDB e MySQL

**Conceitos principais:**
- JOIN entre diferentes fontes de dados
- Conectores MySQL para Athena
- Troubleshooting de problemas de infraestrutura
- Identificação de problemas de provisionamento

**Dificuldade:** ⭐⭐⭐⭐⭐  
**Tempo estimado:** 45-60 minutos (pode ser bloqueada por problemas de lab)

## 🚀 Como Começar

### Pré-requisitos
- **AWS Account** com permissões adequadas para Athena, S3, DynamoDB
- **Conhecimento básico** de SQL e análise de dados
- **Ambiente de lab** com recursos pré-configurados
- **Paciência** para troubleshooting de conectores

### Ordem Recomendada
1. **Task 1** - Athena Setup (configuração inicial)
2. **Task 2** - CSV Data Analysis (consultas básicas)
3. **Task 3** - DynamoDB Federated Query (consultas federadas)
4. **Task 4** - MySQL Federated Query (JOIN federado - pode ter problemas)

### Estrutura do Projeto
```
Unified Data Querying with Amazon Athena/
├── README.md          # Este arquivo - visão geral
├── task1.md          # Athena Setup - configuração inicial
├── task2.md          # CSV Data Analysis - análise de dados CSV
├── task3.md          # DynamoDB Federated Query - consultas federadas
└── task4.md          # MySQL Federated Query - JOIN federado
```

## 🎓 Conceitos Fundamentais

### 📊 Amazon Athena:
- **Serviço sem servidor** para análise de dados
- **SQL padrão** para consultas familiares
- **Integração com S3** para datasets grandes
- **Custo por query** executada (pay-per-use)

### 🔗 Federated Queries:
- **Conectores Lambda** para diferentes fontes de dados
- **Data sources** configurados para DynamoDB, MySQL, etc.
- **Schema mapping** entre diferentes formatos de dados
- **JOINs federados** entre fontes heterogêneas

### 📈 Análise de Dados:
- **COUNT()** para estatísticas básicas
- **WHERE** para filtragem de dados
- **CAST()** para conversão de tipos
- **JOIN** para combinação de dados

### ⚠️ Limitações de Labs:
- **Problemas de provisionamento** podem bloquear tasks
- **Conectores federados** dependem de configuração adequada
- **Caracteres especiais** em credenciais podem causar falhas
- **Troubleshooting** é parte essencial do aprendizado

## 🚨 Troubleshooting Comum

### Problemas de Conectores Federados

#### Erro: "GENERIC_USER_ERROR" com URLDecoder
- **Causa:** Senha contém caractere `&` que quebra parsing de URL
- **Solução:** Reprovisionar conector com senha sem caracteres especiais
- **Status:** Problema de infraestrutura do lab

#### Erro: "Table not found" em Federated Query
- **Causa:** Data source não configurado ou tabela não existe
- **Solução:** Verificar configuração do conector e refresh de metadados

#### Erro: "Access denied" para DynamoDB
- **Causa:** Permissões IAM insuficientes para o conector
- **Solução:** Verificar políticas IAM do conector Lambda

### Problemas de Consultas SQL

#### Erro: "Column not found"
- **Causa:** Nome da coluna incorreto ou case diferente
- **Solução:** Usar DESCRIBE para verificar estrutura da tabela

#### Zero resultados retornados
- **Causa:** Filtro muito restritivo ou dados não existem
- **Solução:** Testar sem WHERE para verificar dados disponíveis

### Estratégias de Resolução
1. **Verifique conectores** antes de executar queries federadas
2. **Use DESCRIBE** para entender estrutura de dados
3. **Teste queries simples** antes de queries complexas
4. **Documente problemas** de infraestrutura para referência

## 💡 Boas Práticas

### 🔍 Análise de Dados:
- **Comece simples:** Use COUNT(*) para entender volume de dados
- **Filtre gradualmente:** Adicione WHERE clauses incrementalmente
- **Valide resultados:** Confirme se números fazem sentido
- **Documente descobertas:** Registre insights obtidos

### 🔗 Federated Queries:
- **Configure conectores** adequadamente antes de usar
- **Use aspas duplas** para nomes com caracteres especiais
- **CAST tipos** quando necessário para JOINs
- **Teste conectividade** antes de queries complexas

### 📊 Consultas SQL:
- **Use LIMIT** para controlar resultados grandes
- **DISTINCT** para evitar duplicatas em JOINs
- **LOWER()** para comparações case-insensitive
- **Comentários** para documentar queries complexas

## 🏆 Critérios de Sucesso

- [ ] **Ambiente Athena** configurado corretamente
- [ ] **Consultas CSV** executadas com sucesso
- [ ] **Federated Queries** funcionando (quando possível)
- [ ] **Análise de dados** realizada com insights obtidos
- [ ] **Troubleshooting** aplicado para problemas encontrados
- [ ] **Conhecimento prático** de análise de dados aplicado

## 📖 Recursos Adicionais

### Documentação AWS
- [Amazon Athena User Guide](https://docs.aws.amazon.com/athena/)
- [Athena Federated Query](https://docs.aws.amazon.com/athena/latest/ug/connect-to-a-data-source.html)
- [Athena SQL Reference](https://docs.aws.amazon.com/athena/latest/ug/functions.html)

### Ferramentas Úteis
- [AWS Console Athena](https://console.aws.amazon.com/athena/)
- [Athena Query Editor](https://console.aws.amazon.com/athena/home?region=us-east-1#/query-editor)
- [AWS CLI Athena Commands](https://docs.aws.amazon.com/cli/latest/reference/athena/)

## 🎯 Próximos Passos

Após completar este desafio, considere:
- **Análise avançada:** Implementar consultas mais complexas
- **Visualização:** Integrar com QuickSight para dashboards
- **Automação:** Criar workflows de análise de dados
- **Certificações:** Preparar-se para exames AWS Data Analytics

## ⚠️ Observações Importantes

### Problemas Conhecidos:
- **Task 4 pode ser bloqueada** por problemas de provisionamento do lab
- **Conectores federados** podem ter problemas de configuração
- **Ambientes de lab** podem ter limitações não documentadas

### Estratégias de Aprendizado:
- **Foque no conhecimento** mesmo quando tasks são bloqueadas
- **Documente problemas** encontrados para referência futura
- **Aplique conceitos** em ambientes próprios quando possível
- **Compartilhe experiências** com a comunidade

---

**🎉 Boa sorte com a análise de dados!**

> **💭 Reflexão:** Este desafio demonstra o poder do Amazon Athena para unificar análise de dados de diferentes fontes, mas também ensina sobre as complexidades de troubleshooting em ambientes de lab e a importância de documentar problemas encontrados.
