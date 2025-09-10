# Task 2 – Security Group Cleanup

## 🎯 Objetivo
Remover o Security Group órfão `Production-SG-Marked-for-deletion` (sg-0fd898a7f26acf0ce) que foi deixado após a conclusão do projeto.

## 📋 Situação Inicial
- **Security Group:** `Production-SG-Marked-for-deletion` (sg-0fd898a7f26acf0ce)
- **Status:** Órfão, deixado após conclusão do projeto
- **Problema:** Não pode ser deletado devido a dependências ativas

## 🔍 Análise de Dependências

### Recursos Associados Identificados:
- **1 instância EC2** usando o Security Group
- **2 Elastic Network Interfaces (ENIs)** referenciando o Security Group

## 🔧 Passos Executados

### 1️⃣ Identificação de Dependências
**Localização:** EC2 → Security Groups → Production-SG-Marked-for-deletion

**Ação:**
- Analisou as dependências do Security Group
- Identificou recursos ativos que impediam a deleção

### 2️⃣ Resolução de Dependências

#### Terminação da Instância EC2
**Localização:** EC2 → Instances

**Ação:**
- Localizou a instância EC2 que utilizava o Security Group
- **Terminou a instância EC2** usando o Security Group

#### Verificação de ENIs
**Localização:** EC2 → Network Interfaces

**Ação:**
- Verificou que ENIs anexadas à instância terminada foram **automaticamente liberadas**
- Identificou ENIs standalone que ainda referenciam o Security Group
- **Deletou ENIs restantes** que ainda faziam referência ao Security Group

### 3️⃣ Deleção do Security Group
**Localização:** EC2 → Security Groups

**Ação:**
- Com todas as dependências resolvidas, **deletou o Security Group**
- Confirmou remoção bem-sucedida de `Production-SG-Marked-for-deletion`

## ✅ Validação
- **Status:** Security Group completamente removido
- **Dependências:** Todas as dependências foram resolvidas
- **Lab:** Task marcada como completa após deleção do Security Group

## 🚨 Troubleshooting Aplicado

### Problemas Encontrados:
- **Dependência de EC2:** Instância ativa impedindo deleção
- **Dependência de ENI:** Interfaces de rede ainda referenciando o SG

### Soluções Implementadas:
- **Terminação de instância:** Removeu dependência principal
- **Liberação automática de ENIs:** AWS liberou ENIs da instância terminada
- **Deleção manual de ENIs:** Removeu ENIs standalone restantes

## 📚 Lições Aprendidas

### ⚠️ Ordem de Deleção
1. **Instâncias EC2** primeiro
2. **ENIs** associadas
3. **Security Groups** por último

### 🔄 Liberação Automática
- ENIs anexadas a instâncias são **automaticamente liberadas** quando a instância é terminada
- ENIs standalone precisam ser **deletadas manualmente**

### 🎯 Validação de Dependências
- Sempre verificar **todas as dependências** antes de tentar deletar recursos
- Usar a interface AWS para identificar recursos associados
- Resolver dependências na **ordem correta** para evitar erros