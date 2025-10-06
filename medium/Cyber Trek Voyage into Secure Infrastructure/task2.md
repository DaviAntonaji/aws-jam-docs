# Task 2: Secure Communication Protocol Challenge

**Pontos Possíveis:** 30  
**Penalidade por Dica:** 0  
**Pontos Disponíveis:** 30

## 🎯 Background

Sua organização está usando o Amazon CloudFront Distribution para servir conteúdo estático de um bucket Amazon S3. Eles estão preocupados que alguém na rede possa interceptar (eavesdrop) a comunicação entre o cliente e o website porque os clientes estão se conectando ao website usando HTTP.

## 📋 Your Task

Como cyber adventurer, sua responsabilidade é navegar pelos caminhos intrincados do ciberespaço e garantir que toda comunicação entre o cliente e o CloudFront não possa ser conduzida por meio de um protocolo inseguro. Sua missão é proteger a integridade dos dados e a privacidade do usuário contra potenciais interceptadores e adversários cibernéticos.

## 🚀 Getting Started

Use o botão **Open AWS Console** no topo da tela do desafio para abrir seu console AWS e ir para o Amazon CloudFront Distribution.

## 📦 Inventory

- **Amazon CloudFront Distribution:** Consulte o Amazon CloudFront distribution ID na seção Output Properties

## 🛠️ Services You Should Use

- Amazon CloudFront

## ✅ Task Validation

A tarefa será concluída automaticamente assim que você encontrar a solução. Além disso, você sempre pode verificar seu progresso pressionando o botão "Check my progress" na tela de detalhes do desafio.

---

## 🔍 Resolução Detalhada

### 🧩 Contexto do Problema

A organização estava servindo conteúdo estático do Amazon S3 através de uma distribuição Amazon CloudFront. Durante a análise de segurança, foi identificado que o site permitia conexões via HTTP, o que poderia expor os dados a ataques de interceptação (eavesdropping) e comprometer a privacidade dos usuários.

### ⚙️ Causa Raiz

- Por padrão, a distribuição CloudFront estava configurada para aceitar solicitações tanto em HTTP quanto em HTTPS
- Isso permitia que usuários acessassem o site de forma não criptografada, representando um risco à integridade e confidencialidade das comunicações

### 🧠 Etapas da Solução

#### 1. Identificação do Recurso

- **CloudFront Distribution ID:** (exemplo: E2TUXQI3IFLTF6)
- **Origem (Origin):** Bucket S3 static-website-jam-XXXXXX

#### 2. Ajuste de Comportamento (Behavior)

No console da AWS, realize o seguinte procedimento:

1. Acesse o **Amazon CloudFront Console**
2. Selecione a distribuição (exemplo: E2TUXQI3IFLTF6)
3. Acesse o menu **Behaviors** (Comportamentos)
4. Clique em **Edit** no comportamento padrão **Default (*)**
5. Altere o parâmetro **Viewer Protocol Policy** de:
   - `HTTP and HTTPS` → para → **`Redirect HTTP to HTTPS`**
6. Salve as alterações

### 🔧 Passo a Passo Detalhado

#### No Console AWS:

1. **CloudFront Console** → **Distributions**
2. Selecione sua distribuição
3. Aba **Behaviors**
4. Selecione o comportamento **Default (*)** → **Edit**
5. Role até encontrar **Viewer Protocol Policy**
6. Selecione: **Redirect HTTP to HTTPS**
7. **Save changes**
8. Aguarde o status da distribuição mudar para **Deployed** (pode levar 5-15 minutos)

### 🧾 Resultado Obtido

Após a atualização, qualquer requisição feita via HTTP é automaticamente redirecionada para HTTPS, garantindo que:

- ✅ Todas as comunicações ocorram sob criptografia TLS
- ✅ Nenhum dado trafegue em texto puro
- ✅ O site siga as boas práticas de segurança em transporte recomendadas pela AWS

### 🔐 Verificação

| Teste | Resultado | Status |
|-------|-----------|--------|
| Acesso via http://dxxxxx.cloudfront.net | Redirecionado automaticamente para HTTPS | ✅ |
| Acesso via https://dxxxxx.cloudfront.net | Carrega normalmente com certificado válido | ✅ |
| Verificação "Check my progress" | Task concluída com sucesso (30 pontos) | ✅ |

### 📊 Testando o Redirecionamento

```bash
# Teste 1: Verificar redirecionamento HTTP → HTTPS
curl -I http://dxxxxx.cloudfront.net

# Resultado esperado:
# HTTP/1.1 301 Moved Permanently
# Location: https://dxxxxx.cloudfront.net/

# Teste 2: Verificar HTTPS funciona
curl -I https://dxxxxx.cloudfront.net

# Resultado esperado:
# HTTP/2 200 OK
```

### 🔒 Opções de Viewer Protocol Policy

Entenda as diferenças:

| Opção | Comportamento | Uso Recomendado |
|-------|---------------|-----------------|
| **HTTP and HTTPS** | Aceita ambos os protocolos | ❌ Não recomendado (inseguro) |
| **Redirect HTTP to HTTPS** | Redireciona HTTP para HTTPS | ✅ **Recomendado** |
| **HTTPS Only** | Rejeita requisições HTTP | ⚠️ Pode causar erros para usuários |

## 🏁 Conclusão

✅ **Secure Communication Protocol Challenge concluído com sucesso.**

A distribuição CloudFront agora redireciona automaticamente todas as conexões HTTP para HTTPS, assegurando a integridade e confidencialidade dos dados transmitidos entre cliente e servidor.

---

## 🔧 Troubleshooting

### Problema: HTTP ainda não está redirecionando

**Possíveis causas:**
1. Deploy do CloudFront ainda não completou
2. Cache do navegador com versão antiga
3. DNS ainda apontando para configuração antiga

**Soluções:**
```bash
# 1. Verifique o status da distribuição
# No console: Status deve estar "Deployed"

# 2. Limpe cache do navegador ou use modo incógnito

# 3. Teste com curl para evitar cache
curl -L -I http://dxxxxx.cloudfront.net
# A flag -L segue redirecionamentos
```

### Problema: Certificado SSL inválido

- CloudFront fornece certificado SSL gratuito
- Se usar domínio customizado, precisa configurar certificado no ACM
- Para domínio cloudfront.net, o certificado é automático

### Problema: Site não carrega após mudança

1. Aguarde 5-15 minutos para propagação
2. Verifique se o comportamento Default (*) foi editado
3. Confirme que salvou as mudanças
4. Teste diretamente via HTTPS primeiro

### Verificação Rápida

```bash
# Verificar headers de redirecionamento
curl -v http://dxxxxx.cloudfront.net 2>&1 | grep -i location

# Deve retornar:
# < Location: https://dxxxxx.cloudfront.net/
```

## 📚 Conceitos Aprendidos

### HTTPS e Segurança em Trânsito
- **TLS/SSL:** Criptografia de dados em trânsito
- **Redirecionamento:** Força uso de protocolo seguro
- **Certificados:** Autenticação e criptografia

### CloudFront Behaviors
- **Viewer Protocol Policy:** Controle de protocolos aceitos
- **Cache Behaviors:** Regras de como conteúdo é servido
- **Origin Protocol Policy:** Comunicação CloudFront → Origin

### Boas Práticas
- ✅ Sempre use HTTPS em produção
- ✅ Configure redirecionamento automático
- ✅ Monitore tentativas de acesso HTTP
- ✅ Use HSTS headers para segurança adicional

## 🎯 Próximo Nível

Após completar esta task, considere:
- **HSTS (HTTP Strict Transport Security):** Header que força HTTPS
- **Custom SSL Certificates:** Para domínios próprios via ACM
- **CloudFront Functions:** Para adicionar headers de segurança
- **WAF:** Web Application Firewall para proteção adicional
