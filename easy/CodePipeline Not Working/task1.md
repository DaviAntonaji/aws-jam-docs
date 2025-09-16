# 📌 Task 1: Troubleshooting & Fix – CodePipeline / CodeCommit / CloudFormation

## 🎯 Objetivo

Diagnosticar e corrigir um pipeline AWS CodePipeline que está em estado de falha, resolvendo problemas de configuração entre Source e Deploy stages.

## 🏗️ Contexto do Sistema

**Pipeline existente** em AWS CodePipeline estava em estado **Failed**:

- **Source**: CodeCommit repo `challenge-codecommit`
- **Deploy**: CloudFormation Stack
- **Status**: Pipeline falhando com erros de configuração

### ❌ Erro Inicial Identificado
```
File [template.yaml] does not exist in artifact [SourceApp]
```

## 🔍 Diagnóstico Detalhado

### Problema Principal
- **Source stage** estava produzindo o artifact chamado `SourceApp`
- **Deploy stage** (CloudFormation) estava configurado para procurar arquivo `template.yaml`
- **Arquivo real** no CodeCommit repo estava em: `infrastructure-as-code/working.template.yaml`
- **Mismatch**: Caminho/arquivo no Deploy não batia com o real

### Problema Secundário
Tentativa inicial de salvar o Source stage com **Amazon CloudWatch Events** resultou em erro de permissão:
```
Could not create service role: cwe-role-...
User is not authorized to perform: iam:CreateRole
```

## 🛠️ Correções Realizadas

### 1. Source Stage

#### Configurações Ajustadas
- **Repository name**: `challenge-codecommit`
- **Branch**: Selecionada branch padrão do repo (ex.: `main`)
- **Output artifacts**: Ajustado para `SourceApp` (para manter consistência com Deploy)
- **Change detection options**: Trocado de **Amazon CloudWatch Events** para **AWS CodePipeline (polling)**

#### Benefícios da Mudança
- ✅ Evita necessidade de criar role `cwe-role`
- ✅ Simplifica configuração de permissões
- ✅ Reduz dependências IAM

### 2. Deploy Stage (CloudFormation)

#### Configurações Corrigidas
- **Input artifacts**: `SourceApp`
- **Template file**: Atualizado de `template.yaml` para `infrastructure-as-code/working.template.yaml`
- **Capabilities**: Marcadas opções `CAPABILITY_IAM` e `CAPABILITY_NAMED_IAM`
- **Stack name**: Mantido conforme configuração existente (`PipelineStack`)

#### Explicação das Capabilities
| Capability | Função |
|------------|--------|
| **CAPABILITY_IAM** | Permite criar/atualizar recursos IAM |
| **CAPABILITY_NAMED_IAM** | Permite criar recursos IAM com nomes específicos |

### 3. Save Pipeline

#### Configuração de Salvamento
- Ao clicar em **Save** no topo
- Na popup **"Save pipeline changes"**, marcar a caixa:
  - ✅ **"No resource updates needed for this source action change"**
- Isso evitou erro de `iam:CreateRole`

### 4. Execução

#### Processo de Deploy
- Após ajustes, o pipeline foi **salvo corretamente**
- Pipeline foi **disparado** (via Release change)
- **Executou com sucesso**
- **Resultado**: CloudFormation stack criada/atualizada sem erros

## 📊 Resumo das Correções

| Componente | Problema | Solução |
|------------|----------|---------|
| **Source Stage** | CloudWatch Events sem permissão | Mudou para CodePipeline polling |
| **Deploy Stage** | Caminho de template incorreto | Atualizou para `infrastructure-as-code/working.template.yaml` |
| **Capabilities** | Permissões CloudFormation insuficientes | Habilitou `CAPABILITY_IAM` e `CAPABILITY_NAMED_IAM` |
| **Save Pipeline** | Erro de criação de role | Marcou "No resource updates needed" |

## ✅ Resultado Final

### Pipeline Corrigido e Funcional
- ✅ **Source** → CodeCommit gera o artifact `SourceApp`
- ✅ **Deploy** → CloudFormation consome `SourceApp`
- ✅ **Template** → Usa `infrastructure-as-code/working.template.yaml`
- ✅ **Permissões** → Configurações corretas aplicadas

### Problemas Eliminados
- ❌ **Arquivo inexistente**: Resolvido com caminho correto
- ❌ **Criação de role (cwe-role)**: Evitado com polling
- ❌ **Permissões IAM**: Configuradas adequadamente

## 🔧 Lições Aprendidas

### Troubleshooting de Pipeline
- **Verificar caminhos**: Sempre validar estrutura real do repositório
- **Permissões IAM**: Considerar alternativas mais simples (polling vs CloudWatch Events)
- **Capabilities CloudFormation**: Habilitar permissões necessárias para recursos IAM

### Boas Práticas
- **Consistência de nomes**: Manter nomes de artifacts consistentes entre stages
- **Validação prévia**: Testar configurações antes de salvar
- **Documentação**: Registrar problemas e soluções para referência futura

## 🔗 Próximos Passos

Com o pipeline corrigido, você pode:
- **Monitorar execuções** futuras
- **Aplicar correções similares** em outros pipelines
- **Implementar validações** para prevenir problemas similares
- **Expandir pipeline** com novos stages conforme necessário