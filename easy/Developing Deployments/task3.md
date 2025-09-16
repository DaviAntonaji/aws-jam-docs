# 📌 Task 3: Criar o Deployment

## 🎯 Objetivo

Fazer um deployment CodeDeploy usando:
- **Application**: `jam-app`
- **Deployment Group**: `jam`
- **Fonte**: O `source.zip` enviado para o S3 na Task 1
- **Comportamento**: Sobrescrever o conteúdo existente

## 🛠️ Passo a Passo - Console AWS

### 1. Abrir CodeDeploy

#### Navegação
- **Console AWS** → **CodeDeploy**
- Clique em **Applications** → selecione **`jam-app`**

### 2. Iniciar Deployment

#### Acesso ao Deployment
- Clique em **Create deployment**

#### Configuração do Deployment Group
- **Deployment group**: Escolha **`jam`**

### 3. Application Revision (Source)

#### Configuração da Fonte
- **My application is stored in**: `Amazon S3`

#### Revision Location
- **Bucket**: Selecione o bucket informado na challenge
  - **Exemplo**: `jam-codedeploy-xxxx`
- **Key**: `source.zip`
- **Bundle type**: `zip`

### 4. Deployment Settings

#### Configurações de Deployment
- **Deployment type**: Já estará como **In-place** (vem do deployment group)
- **File options**: **Marque** `Overwrite content` (ou `Overwrite files in the deployment location`)

### 5. Criar Deployment

#### Finalização
- Clique em **Create deployment**

#### Monitoramento
- Acompanhe o status: deve passar por **Created** → **In progress** → **Succeeded**

## 📊 Status do Deployment

### Estados Possíveis
| Status | Descrição |
|--------|-----------|
| **Created** | Deployment criado, aguardando início |
| **In progress** | Deployment em execução |
| **Succeeded** | Deployment concluído com sucesso |
| **Failed** | Deployment falhou (rollback automático) |
| **Stopped** | Deployment interrompido manualmente |

### Monitoramento em Tempo Real
- **Console CodeDeploy**: Acompanhe progresso detalhado
- **CloudWatch Logs**: Verifique logs de execução
- **EC2 Instances**: Monitore instâncias sendo atualizadas

## ✅ Validação

### Validação Automática
- A **plataforma do lab** detecta automaticamente quando o deployment termina em **Succeeded**
- **Task marcada como concluída** automaticamente

### Teste Manual (Opcional)

#### Acesso à Aplicação
1. Vá em **AWS Systems Manager** → **Parameter Store**
2. Abra o parâmetro **`/sj/codedeploy/dns`**
3. Copie o **Value** e cole no navegador

#### Resultado Esperado
- A página deve mostrar o texto atualizado no `index.html`
- **Exemplo**: "Today is Friday" ou o dia atual
- **Confirmação**: "SecurityJamCodeDeployCompleted"

## 🔧 Troubleshooting

### Problemas Comuns

#### Deployment Falha
- **Verificar**: Logs do CodeDeploy
- **Solução**: Rollback automático será executado
- **Ação**: Corrigir problemas no `appspec.yml` ou scripts

#### Timeout de Scripts
- **Verificar**: Configurações de timeout no `appspec.yml`
- **Solução**: Aumentar valores de timeout se necessário

#### Permissões
- **Verificar**: Service role `Jam-CodeDeploy`
- **Solução**: Confirmar permissões adequadas

### Logs Importantes
```bash
# CloudWatch Logs - CodeDeploy Agent
/aws/codedeploy-agent/

# Logs de Scripts
/opt/codedeploy-agent/deployment-root/
```

## 🎉 Resultado Final

- ✅ **Deployment executado** com sucesso
- ✅ **Aplicação atualizada** nas instâncias EC2
- ✅ **Nginx configurado** com novo conteúdo
- ✅ **Validação automática** concluída
- ✅ **Task finalizada** com sucesso

## 🔗 Próximos Passos

Com o deployment concluído, você tem:
- **Sistema de deployment automatizado** funcionando
- **Aplicação web** rodando nas instâncias EC2
- **Conhecimento prático** de AWS CodeDeploy
- **Pipeline completo** de deploy automatizado

## 💡 Lições Aprendidas

- **CodeDeploy** facilita deployments automatizados
- **Lifecycle hooks** controlam o processo de deploy
- **Rollback automático** reduz riscos
- **Monitoramento** é essencial para troubleshooting
- **Estrutura de artefatos** deve seguir padrões específicos