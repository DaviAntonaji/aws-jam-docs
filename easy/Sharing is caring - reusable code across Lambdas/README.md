# Sharing is caring - reusable code across Lambdas

## 📋 Visão Geral

Este desafio foca em **AWS Lambda Layers** e como compartilhar código entre múltiplas funções Lambda de forma eficiente. Você aprenderá a criar, versionar e gerenciar layers para reutilização de código, implementando estratégias de deploy canary.

## 🎯 Objetivos de Aprendizado

- ✅ Criar e configurar AWS Lambda Layers
- ✅ Compartilhar código entre múltiplas funções Lambda
- ✅ Implementar estratégias de versionamento de layers
- ✅ Executar deploy canary para testar novas versões
- ✅ Gerenciar compatibilidade de runtime e arquitetura
- ✅ Entender validação automática de labs AWS

## 🏗️ Arquitetura

```
┌─────────────────┐    ┌─────────────────┐
│   Lambda Func 1 │    │   Lambda Func 2 │
│                 │    │                 │
└─────────┬───────┘    └─────────┬───────┘
          │                      │
          └──────────┬───────────┘
                     │
            ┌────────▼────────┐
            │  Lambda Layer  │
            │ tattooine-common│
            └─────────────────┘
```

## 📁 Estrutura do Projeto

```
Sharing is caring - reusable code across Lambdas/
├── README.md          # Este arquivo
├── task1.md          # Criar e configurar o Layer inicial
└── task2.md          # Versionamento e deploy canary
```

## 🚀 Pré-requisitos

- **AWS Account** com permissões para Lambda e S3
- **Runtime:** Node.js 22.x
- **Arquitetura:** x86_64
- **Região:** Qualquer região AWS (ajuste nos URIs S3)

## 📚 Recursos S3

- **Task 1:** `s3://aws-jam-challenge-resources-{REGION}/lambda-layers-shared-code/task-one/layer-task-one.zip`
- **Task 2:** `s3://aws-jam-challenge-resources-{REGION}/lambda-layers-shared-code/task-two/layer-task-two.zip`

> **⚠️ Importante:** Substitua `{REGION}` pela sua região AWS (ex.: `us-east-1`)

## 🎮 Como Executar

### Task 1: Setup Inicial
1. Leia o arquivo [`task1.md`](./task1.md)
2. Crie o layer `tattooine-common`
3. Anexe às duas funções Lambda
4. Teste a configuração

### Task 2: Versionamento e Deploy Canary
1. Leia o arquivo [`task2.md`](./task2.md)
2. Publique nova versão do layer
3. Implemente deploy canary em apenas uma função
4. Valide e faça rollback se necessário

## 🔧 Conceitos Técnicos

### Lambda Layers
- **Reutilização de código:** Compartilhe bibliotecas entre funções
- **Versionamento:** Mantenha múltiplas versões do mesmo layer
- **Compatibilidade:** Configure runtime e arquitetura corretos
- **Estrutura:** Para Node.js, use `nodejs/node_modules/<pacote>`

### Deploy Canary
- **Teste gradual:** Implemente mudanças em uma função por vez
- **Redução de risco:** Evite impactar toda a aplicação
- **Rollback rápido:** Volte para versão anterior se necessário
- **Validação:** Teste antes de aplicar em produção

## 🎓 Lições Aprendidas (Baseado em Feedback Real)

### ⚠️ Validação Automática de Labs
- **Siga as dicas literalmente:** O validador automático pode estar "hard-coded" para soluções específicas
- **Documente diferenças:** Separe o que é "correto tecnicamente" do que é "requerido pelo lab"
- **Teste após cada mudança:** Execute a função após cada alteração de policy/layer

### 🔍 Troubleshooting Comum
- **Runtime.ImportModuleError:** Verifique se o layer está anexado e compatível
- **Timeout de rede:** Confirme configuração de Security Groups e VPC
- **Permissões restritas:** Em labs, algumas ações podem estar bloqueadas no Console

### 💡 Boas Práticas
- **Least Privilege:** Use permissões mínimas necessárias
- **Versionamento:** Mantenha múltiplas versões para rollback
- **Teste incremental:** Valide cada mudança antes de prosseguir
- **Documentação:** Registre o que funciona vs. o que o lab espera

## 📖 Recursos Adicionais

- [AWS Lambda Layers Documentation](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html)
- [Lambda Layer Best Practices](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html#configuration-layers-best-practices)
- [Node.js Runtime Support](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html)
- [Deploy Canary Patterns](https://docs.aws.amazon.com/lambda/latest/dg/configuration-versions.html)

## 🏆 Critérios de Sucesso

- [ ] Layer criado e configurado corretamente
- [ ] Ambas as funções Lambda usando o layer inicial
- [ ] Nova versão do layer publicada
- [ ] Deploy canary implementado com sucesso
- [ ] Testes executados e validados
- [ ] Estratégia de rollback testada
- [ ] Validação automática do lab aprovada

## 🆘 Troubleshooting

### Problemas Comuns

**Runtime.ImportModuleError**
- Verifique se o layer está anexado corretamente
- Confirme compatibilidade de runtime (Node.js 22.x)
- Valide arquitetura (x86_64)
- Confirme estrutura do ZIP (`nodejs/node_modules/`)

**Layer não encontrado**
- Confirme o nome do layer (`tattooine-common`)
- Verifique se a versão está selecionada corretamente
- Valide permissões IAM

**Incompatibilidade de arquitetura**
- Funções devem estar em x86_64
- Layer deve ser compatível com x86_64
- Não misturar arm64 com x86_64

**Validação do lab não passa**
- Siga as dicas do lab literalmente
- Execute a função após cada mudança
- Verifique se está usando o formato exato esperado
- Documente diferenças entre "correto" e "esperado pelo lab"

### 🔄 Estratégias de Rollback

1. **Voltar para versão anterior do layer**
2. **Remover/ajustar ordem dos layers**
3. **Verificar logs detalhados no CloudWatch**
4. **Testar com evento simples**

## 🎯 Dicas Finais

- **Ambiente restrito:** Labs podem ter permissões limitadas no Console
- **Validação automática:** Pode procurar por elementos específicos (nomes de policies, statements exatos)
- **Execução vazia:** Às vezes 200 com body vazio é sucesso suficiente
- **Documentação:** Registre o que funciona para referência futura

---

**🎉 Boa sorte com o desafio!**

> **💭 Reflexão:** Este desafio ensina não apenas sobre Lambda Layers, mas também sobre como navegar validações automáticas e ambientes restritos - habilidades valiosas para cenários reais de produção.