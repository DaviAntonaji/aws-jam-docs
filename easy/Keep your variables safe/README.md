# 🔐 Keep your variables safe

## 📋 Visão Geral

Este desafio foca na **segurança de dados sensíveis** em funções AWS Lambda, ensinando como criptografar variáveis de ambiente usando AWS KMS (Key Management Service) com Customer Managed Keys (CMK).

## 🎯 Objetivo

Configurar variáveis de ambiente de uma função Lambda para ficarem **criptografadas em repouso** com uma Customer Managed Key (CMK) no KMS e, opcionalmente, **em trânsito** utilizando os helpers do console AWS.

## 🔧 Conceitos Principais

- **AWS Lambda** - Configuração de variáveis de ambiente
- **AWS KMS** - Criptografia com Customer Managed Keys (CMK)
- **Segurança em repouso** - Criptografia de dados armazenados
- **Segurança em trânsito** - Criptografia durante transmissão
- **IAM Permissions** - Permissões necessárias para KMS
- **AWS Console Helpers** - Ferramentas de criptografia integradas

## 🏗️ Arquitetura

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   AWS Lambda    │    │   AWS KMS       │    │  Environment    │
│   Function      │◄───┤   Customer      │◄───┤  Variables      │
│                 │    │   Managed Key   │    │  (Encrypted)    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 📚 Tarefas

### [Task 1: Configurar Criptografia de Variáveis de Ambiente](./task1.md)

**Objetivo:** Implementar criptografia KMS para variáveis de ambiente Lambda

**Conceitos abordados:**
- Configuração de variáveis de ambiente em Lambda
- Seleção e configuração de Customer Managed Key
- Ativação de criptografia em repouso
- Configuração opcional de criptografia em trânsito
- Troubleshooting de permissões IAM

## 🚀 Passo a Passo Resumido

1. **Acessar função Lambda** no console AWS
2. **Configurar variáveis de ambiente** na seção Configuration
3. **Ativar criptografia KMS** selecionando Customer Managed Key
4. **Informar ARN da chave KMS** configurada no ambiente
5. **Habilitar helpers** para criptografia em trânsito (opcional)
6. **Salvar configurações** e validar no Jam

## ⚠️ Pontos Importantes

### Permissões Necessárias
A role `myLambdaFunctionExecutionRole` precisa ter:
- `kms:Encrypt`
- `kms:Decrypt` 
- `kms:GenerateDataKey*`
- `kms:DescribeKey`

### Troubleshooting Comum
- **Access denied to access-analyzer:ValidatePolicy** - Erro visual que pode ser ignorado
- **Permissões KMS** - Verificar se a role tem as permissões necessárias
- **ARN da chave** - Usar o ARN correto fornecido no ambiente do lab

## 🔍 Exemplo de Configuração

### Variável de Ambiente
```
Key: databaseUser
Value: admin
```

### ARN da Chave KMS
```
arn:aws:kms:ap-southeast-2:593529499886:key/1565ecdc-f0e7-4b2f-9d6d-60d545a2a40f
```

## 📊 Dificuldade e Tempo

**Dificuldade:** ⭐⭐☆☆☆  
**Tempo estimado:** 15-30 minutos

## 🎓 Lições Aprendidas

### Segurança de Dados
- **Criptografia em repouso** protege dados armazenados
- **Customer Managed Keys** oferecem maior controle sobre criptografia
- **Variáveis de ambiente** podem conter dados sensíveis que precisam proteção

### Boas Práticas AWS
- **Least privilege** - Aplicar apenas permissões necessárias
- **Defesa em profundidade** - Múltiplas camadas de segurança
- **Monitoramento** - Acompanhar uso e acesso às chaves KMS

### Troubleshooting
- **Erros visuais** podem não impactar funcionalidade
- **Ambientes de lab** têm limitações específicas
- **Documentação** de soluções que funcionam

## 🔗 Recursos Adicionais

### Documentação AWS
- [AWS Lambda Environment Variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html)
- [AWS KMS Customer Managed Keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys)
- [AWS KMS Best Practices](https://docs.aws.amazon.com/kms/latest/developerguide/best-practices.html)

### Conceitos Relacionados
- [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) - Alternativa para segredos
- [AWS Systems Manager Parameter Store](https://aws.amazon.com/systems-manager/features/) - Parâmetros seguros
- [AWS IAM Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) - Controle de acesso

## ✅ Critérios de Sucesso

- [ ] Variáveis de ambiente configuradas na função Lambda
- [ ] Customer Managed Key selecionada para criptografia
- [ ] Criptografia em repouso ativada
- [ ] Criptografia em trânsito configurada (se solicitada)
- [ ] Validação no Jam marcada como "Completed"
- [ ] Compreensão dos conceitos de segurança implementados

---

**🎉 Boa sorte com o desafio!**

> **💭 Reflexão:** Este desafio ensina uma das práticas mais importantes em segurança de aplicações cloud - a proteção adequada de dados sensíveis. Dominar esses conceitos é fundamental para qualquer profissional que trabalha com AWS e segurança.
