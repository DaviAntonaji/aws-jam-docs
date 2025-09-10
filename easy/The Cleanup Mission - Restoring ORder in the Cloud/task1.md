# Task 1 – VPC Cleanup

## 🎯 Objetivo
Remover completamente os VPCs marcados para deleção (VPC-A-marked-for-deletion e VPC-B-marked-for-deletion) e todos os seus recursos associados.

## 📋 Pré-requisitos
- Acesso ao console AWS com permissões adequadas para VPC
- Identificação dos VPCs através do Inventory/Output properties

## 🔧 Passos Detalhados

### 🔎 Passo 1 – Identificar os VPCs
**Localização:** Console AWS → VPC → Your VPCs

**Ação:**
- Localize os IDs informados no Inventory/Output properties
- Identifique: `VPC-A-marked-for-deletion` e `VPC-B-marked-for-deletion`
- Estes são os VPCs que precisam ser completamente removidos

### 🔗 Passo 2 – Remover o Peering Connection
**Localização:** VPC → Peering connections

**Ação:**
- Procure o peering connection que conecta VPC-A ↔ VPC-B
- **Delete o peering connection**
- ⚠️ **Importante:** Sem remover o peering, o console não permitirá deletar os VPCs

### 🌐 Passo 3 – Desanexar Internet Gateway
**Localização:** VPC → Internet Gateways

**Ação:**
- Se houver um IGW anexado ao VPC marcado:
  1. Clique no IGW → Actions → Detach from VPC
  2. Após desanexar, delete o IGW

### 🧩 Passo 4 – Excluir NAT Gateways
**Localização:** VPC → NAT Gateways

**Ação:**
- Delete o NAT Gateway associado ao VPC
- ⚠️ **Observação:** Antes de excluir, libere o Elastic IP associado (seção Elastic IPs)

### 📡 Passo 5 – Remover Network Interfaces
**Localização:** VPC → Network Interfaces (ENIs)

**Ação:**
- Filtre pelo VPC marcado para deleção
- Delete as interfaces que ainda existirem
- **Nota:** Podem estar ligadas a NAT, peering, ou endpoints de serviço

### 🚪 Passo 6 – Excluir Route Tables e Subnets
**Route Tables:**
- Vá em Route Tables
- Delete as rotas customizadas ligadas ao VPC

**Subnets:**
- Vá em Subnets
- Delete todas as subnets do VPC

### 🛑 Passo 7 – Excluir o VPC
**Localização:** VPC → Your VPCs

**Ação:**
- Selecione `VPC-A-marked-for-deletion` e `VPC-B-marked-for-deletion`
- Clique Actions → Delete VPC
- Confirme a deleção

## ✅ Validação
- Verifique que ambos os VPCs foram completamente removidos
- Confirme que não há recursos órfãos relacionados aos VPCs deletados
- O lab deve marcar a task como completa após a remoção bem-sucedida

## 🚨 Troubleshooting
- **Erro de dependência:** Verifique se todos os recursos foram removidos na ordem correta
- **Peering não deleta:** Confirme que não há tráfego ativo através do peering
- **NAT Gateway:** Libere o Elastic IP antes de deletar o NAT Gateway
- **ENIs:** Algumas podem estar associadas a serviços AWS - verifique todas as dependências