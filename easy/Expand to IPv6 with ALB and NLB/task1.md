# Task 1: ALB IP Address Type Dualstack

## 🎯 Objetivo

**Task 1:** ALB IP Address Type Dualstack  
**Pontos Possíveis:** 16  
**Penalidade de Pista:** 0  
**Pontos Disponíveis:** 16

## 📋 Contexto

### Problema
Sua aplicação usa Application Load Balancer (ALB). O ALB chamado `Jam-ALB` foi criado com tipo de endereço IP IPv4. Seus clientes só conseguem acessar sua aplicação usando IPv4. Com IPv6, falha.

### Solução Necessária
Você foi solicitado a garantir que seu ALB suporte IPv4 e IPv6, para que clientes possam enviar requisições com ambas as versões de IP.

Tudo mais já está preparado para seu ALB funcionar com IPv6 também, conforme definido nos requisitos dualstack.

## 🛠️ Inventário

### Recursos Disponíveis
- **Application Load Balancer:** `Jam-ALB` (inicialmente IPv4-only)
- **Console:** EC2 Console (Load Balancers estão no EC2)

## 🔧 Sua Tarefa

Alterar o ALB chamado `Jam-ALB` para usar o tipo de endereço IP `dualstack`.

> **⚠️ Importante:** Load Balancers pertencem ao console EC2.

Você não precisa alterar nada mais, apenas o tipo de endereço IP.

## ✅ Solução Passo a Passo

### 1. Acessar o Console AWS
- Navegue para o **EC2 Console**
- No menu lateral, clique em **"Load Balancers"**

### 2. Localizar o ALB
- Encontre o ALB chamado **`Jam-ALB`**
- Clique nele para selecioná-lo

### 3. Editar Configurações
- Clique no botão **"Edit"** (ou "Modify")
- Procure a opção **"IP address type"**
- Atualmente estará marcado apenas como **`ipv4`**

### 4. Alterar para Dualstack
- Altere de **`ipv4`** para **`dualstack`**
- Clique em **"Save"** para salvar as alterações

### 5. Aguardar Propagação
- Aguarde alguns minutos para as mudanças se propagarem
- O ALB agora suportará tanto IPv4 quanto IPv6

## 🧪 Validação

### Critério de Sucesso
A tarefa será automaticamente completada assim que você realizar a alteração do tipo de endereço IP do ALB.

### Verificação Manual
Alternativamente, você pode sempre verificar seu progresso clicando no botão **"Check my progress"** na tela de detalhes do desafio.

## 📚 Conceitos Aprendidos

### Dualstack Load Balancer
- **Definição:** Suporta tanto IPv4 quanto IPv6 simultaneamente
- **Benefício:** Permite acesso via ambos os protocolos
- **DNS:** Retorna tanto endereços IPv4 quanto IPv6

### IPv4 vs IPv6
- **IPv4:** Formato tradicional (ex: 192.168.1.1)
- **IPv6:** Formato moderno (ex: 2001:db8::1)
- **Dualstack:** Suporta ambos os formatos

### Application Load Balancer
- **Layer 7:** Trabalha na camada de aplicação
- **Protocolos:** HTTP e HTTPS
- **Features:** Content-based routing, SSL termination

## 🎓 Lições Importantes

1. **Load Balancers estão no EC2 Console:** Não no console de Load Balancing
2. **Dualstack é simples:** Apenas uma configuração a alterar
3. **Propagação leva tempo:** Aguardar alguns minutos
4. **IPv6 é o futuro:** Preparar aplicações para transição

## 🔍 Próximos Passos

Após completar esta tarefa:
- O ALB `Jam-ALB` suportará IPv4 e IPv6
- Estará pronto para as próximas tarefas (configuração de targets)
- Clientes poderão acessar via ambos os protocolos

---

**🎯 Resultado:** ALB configurado como dualstack, resolvendo o problema de acessibilidade IPv6 dos usuários.