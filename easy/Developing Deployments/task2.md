# 📌 Task 2: Criar Aplicação e Deployment Group do CodeDeploy

## 🎯 Objetivo

Criar:
- **Aplicação CodeDeploy** chamada `jam-app`
- **Deployment Group** chamado `jam`

Com as seguintes configurações:
- **Tipo de implantação**: In-place
- **Estilo de implantação**: One-at-a-time
- **Rollback automático** em caso de falha
- **Sem Load Balancer**
- **Service role**: `Jam-CodeDeploy` (já existe)

## 🛠️ Passo a Passo - Console AWS

### 1. Abrir o CodeDeploy

#### Navegação
- **Console AWS** → Pesquisar **CodeDeploy**
- Acessar o serviço AWS CodeDeploy

### 2. Criar a Aplicação

#### Configuração da Aplicação
- Clique em **Create application**
- **Name**: `jam-app`
- **Compute platform**: `EC2/On-premises`
- Clique em **Create**

#### Resultado
- Aplicação `jam-app` criada com sucesso
- Pronto para configurar deployment groups

### 3. Criar o Deployment Group

#### Acesso ao Deployment Group
- Dentro da app `jam-app`, clique em **Create deployment group**

#### Configurações Básicas
- **Name**: `jam`
- **Service role**: Selecione `Jam-CodeDeploy` (já existe)

#### Tipo de Deployment
- **Deployment type**: `In-place`

#### Configuração do Ambiente
- **Environment configuration**:
  - Escolha **Amazon EC2 Auto Scaling groups**
  - Selecione a tag/Auto Scaling group que já vem configurada pelo lab
  - **Exemplo**: `jam-ASG` ou similar
  - **Nota**: Na challenge normalmente já existe um Auto Scaling Group; marque o que aparecer

#### Configurações de Deployment
- **Deployment configuration**: `CodeDeployDefault.OneAtATime`
  - Isso garante **one-at-a-time**
- **Load Balancer**: **Desmarque** (não usar)
- **Rollback**: **Marque** `Enable rollback if deployment fails`

#### Finalização
- Clique em **Create**

## 📊 Configurações Detalhadas

### Aplicação CodeDeploy
| Configuração | Valor |
|--------------|-------|
| **Nome** | `jam-app` |
| **Plataforma** | EC2/On-premises |
| **Tipo** | In-place deployment |

### Deployment Group
| Configuração | Valor |
|--------------|-------|
| **Nome** | `jam` |
| **Service Role** | `Jam-CodeDeploy` |
| **Deployment Type** | In-place |
| **Environment** | Auto Scaling Groups |
| **Deployment Config** | `CodeDeployDefault.OneAtATime` |
| **Load Balancer** | Desabilitado |
| **Rollback** | Habilitado |

## 🔧 Conceitos Importantes

### In-place Deployment
- **Definição**: Atualiza instâncias existentes
- **Vantagem**: Não cria novas instâncias
- **Uso**: Ideal para aplicações que precisam manter estado

### One-at-a-time
- **Definição**: Atualiza uma instância por vez
- **Vantagem**: Mantém disponibilidade durante o deploy
- **Configuração**: `CodeDeployDefault.OneAtATime`

### Rollback Automático
- **Definição**: Reverte deployment em caso de falha
- **Benefício**: Reduz impacto de deployments com problemas
- **Configuração**: `Enable rollback if deployment fails`

## ✅ Resultado

- ✅ **Aplicação `jam-app`** criada com sucesso
- ✅ **Deployment Group `jam`** configurado
- ✅ **Configurações de deployment** aplicadas
- ✅ **Rollback automático** habilitado
- ✅ **Pronto para deployment** na Task 3

## 🔗 Próximos Passos

Com a aplicação e deployment group configurados, continue para a [Task 3](./task3.md) para executar o deployment usando o artefato do S3.