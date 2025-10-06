# 🚀 Cyber Trek: Voyage into Secure Infrastructure

## 📋 Visão Geral

Bem-vindo ao **Cyber Trek: Voyage into Secure Infrastructure**, uma jornada emocionante de aventura cibernética fictícia. Neste desafio, você embarcará em uma expedição ao coração da infraestrutura digital segura. Como aventureiro cibernético, sua missão é navegar pelos cenários de segurança do Amazon CloudFront e Amazon S3, fortificando sua fortaleza digital contra ameaças cibernéticas iminentes.

Você é um especialista rookie em segurança cibernética encarregado de proteger o site estático "Cyber Trek Voyage" hospedado no Amazon Web Services (AWS). Prepare-se para embarcar em uma jornada perigosa através das vastas extensões da infraestrutura segura, onde cada decisão pode significar a diferença entre vitória e derrota.

## 🎯 Objetivos de Aprendizado

- ✅ Implementar controle de acesso restrito entre CloudFront e S3 usando OAC
- ✅ Configurar redirecionamento automático HTTP para HTTPS
- ✅ Otimizar políticas de cache para balancear performance e atualização de conteúdo
- ✅ Habilitar versionamento de objetos para proteção contra exclusões acidentais
- ✅ Aplicar princípios de least privilege em políticas de bucket
- ✅ Garantir criptografia em trânsito para todas as comunicações
- ✅ Entender arquitetura CloudFront + S3 para sites estáticos

## 🏗️ Arquitetura

```
Internet
    ↓
Amazon CloudFront Distribution
├── HTTPS (Redirect HTTP → HTTPS)
├── Cache Policy (TTL = 1 hour)
├── Origin Access Control (OAC)
└── Origin: Amazon S3 Bucket
    ├── Bucket Policy (CloudFront only)
    ├── Block Public Access (Enabled)
    └── Versioning (Enabled)
```

## 🛠️ Serviços Utilizados

- **Amazon CloudFront** - CDN global para distribuição de conteúdo
- **Amazon S3** - Armazenamento de objetos e hospedagem de site estático
- **IAM** - Controle de acesso e políticas
- **AWS Secrets Manager** - Armazenamento de credenciais (implícito)

## 📚 Conceitos Principais

### 1. **Origin Access Control (OAC)**
- Método moderno para restringir acesso do CloudFront ao S3
- Substitui o OAI (Origin Access Identity) legado
- Permite acesso apenas via CloudFront, bloqueando acesso público direto

### 2. **HTTPS e Segurança em Trânsito**
- Redirecionamento automático HTTP → HTTPS
- Criptografia TLS para proteção de dados
- Prevenção de ataques de interceptação (eavesdropping)

### 3. **Cache Performance e TTL**
- Balanceamento entre performance e atualização de conteúdo
- Default TTL de 3600 segundos (1 hora)
- Otimização para atualização periódica do conteúdo

### 4. **S3 Versioning**
- Proteção contra exclusões acidentais
- Histórico de modificações de objetos
- Capacidade de restauração rápida

## 🚀 Passo a Passo Detalhado

### **Task 1: Access Control Lockdown Quest** (45 pontos)

#### Objetivo
Restringir o acesso ao bucket S3 para que apenas a distribuição CloudFront autorizada possa acessar os objetos.

#### Contexto do Problema
O site apresentava erro `AccessDenied` ao ser acessado pelo domínio CloudFront porque a política do bucket S3 não estava configurada corretamente para permitir acesso via Origin Access Control (OAC).

#### Solução

**1. Identificar os Recursos**
- CloudFront Distribution ID: (verificar em Output Properties)
- Bucket S3: `static-website-jam-*` (nome começa com este prefixo)

**2. Confirmar Configuração OAC**
- Vá para **CloudFront** → **Distributions** → sua distribuição
- Aba **Origins** → verifique que está usando **Origin Access Control**

**3. Configurar Bucket Policy**

Vá para **S3** → seu bucket → **Permissions** → **Bucket policy**

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowCloudFrontOACOnly",
      "Effect": "Allow",
      "Principal": {
        "Service": "cloudfront.amazonaws.com"
      },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::static-website-jam-XXXXXX/*",
      "Condition": {
        "StringEquals": {
          "AWS:SourceArn": "arn:aws:cloudfront::<ACCOUNT_ID>:distribution/<DISTRIBUTION_ID>"
        }
      }
    },
    {
      "Sid": "DenyInsecureTransport",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::static-website-jam-XXXXXX/*",
      "Condition": {
        "Bool": {
          "aws:SecureTransport": "false"
        }
      }
    }
  ]
}
```

**Substitua:**
- `static-website-jam-XXXXXX` pelo nome real do seu bucket
- `<ACCOUNT_ID>` pelo número da sua conta AWS (12 dígitos)
- `<DISTRIBUTION_ID>` pelo ID da sua distribuição CloudFront

**4. Validar Configuração**
- ✅ Block all public access: **Habilitado**
- ✅ Acesso direto ao S3: **Negado** (Access Denied)
- ✅ Acesso via CloudFront: **Funciona normalmente**

---

### **Task 2: Secure Communication Protocol Challenge** (30 pontos)

#### Objetivo
Garantir que toda comunicação entre cliente e CloudFront seja exclusivamente via HTTPS.

#### Contexto do Problema
O site permitia conexões HTTP não criptografadas, expondo dados a potenciais ataques de interceptação.

#### Solução

**1. Acessar Configuração de Behaviors**
- **CloudFront** → sua distribuição
- Aba **Behaviors**
- Selecione o comportamento **Default (*)** → **Edit**

**2. Configurar Viewer Protocol Policy**
- Localize: **Viewer Protocol Policy**
- Altere de: `HTTP and HTTPS`
- Para: **`Redirect HTTP to HTTPS`**
- Salve as alterações

**3. Aguardar Deploy**
- Status da distribuição deve mudar para **Deployed**
- Pode levar alguns minutos

**4. Validar Redirecionamento**
```bash
# Teste HTTP (deve redirecionar)
curl -I http://dxxxxxx.cloudfront.net

# Teste HTTPS (deve funcionar)
curl -I https://dxxxxxx.cloudfront.net
```

---

### **Task 3: Cache Performance Optimization Expedition** (45 pontos)

#### Objetivo
Otimizar o cache do CloudFront para atualizar automaticamente a cada 1 hora, sincronizando com o ciclo de atualização do S3.

#### Contexto do Problema
O site não exibia conteúdo atualizado porque o cache estava configurado com TTL muito alto, mantendo objetos antigos nos edge locations.

#### Solução

**1. Acessar Configuração de Behaviors**
- **CloudFront** → sua distribuição
- Aba **Behaviors**
- Selecione **Default (*)** → **Edit**

**2. Criar ou Selecionar Cache Policy**

**Opção A: Criar nova Cache Policy**
- Em **Cache policy**, clique em **Create policy**
- Nome: `one-hour-ttl`
- Configure:

| Parâmetro | Valor | Descrição |
|-----------|-------|-----------|
| Minimum TTL | `0` seconds | Permite atualização imediata |
| Default TTL | `3600` seconds (1 hour) | Cache renovado a cada hora |
| Maximum TTL | `3600` seconds (1 hour) | Garante consistência |

**Opção B: Editar comportamento diretamente**
- Altere para: **Cache policy and origin request policy (recommended)**
- Selecione a policy criada ou configure TTLs customizados

**3. Configurações Adicionais de Cache**
- **Headers:** None (mantém cache simples)
- **Query strings:** None (evita variações desnecessárias)
- **Cookies:** None (melhora performance)

**4. Salvar e Aguardar Deploy**
- Salve as alterações
- Aguarde status **Deployed**

**5. Validar Atualização de Cache**
- Atualize conteúdo no S3
- Aguarde até 1 hora
- Verifique se o site exibe novo conteúdo

---

### **Task 4: Version Control Vigilance Assignment** (30 pontos)

#### Objetivo
Ativar versionamento no bucket S3 para proteção contra exclusões acidentais e manter histórico de alterações.

#### Contexto do Problema
Um objeto crítico foi acidentalmente excluído, causando interrupção no serviço. A equipe teve que recriar manualmente porque não havia versões anteriores.

#### Solução

**1. Acessar Configuração do Bucket**
- **S3** → seu bucket `static-website-jam-*`
- Aba **Properties**

**2. Habilitar Versioning**
- Localize a seção **Bucket Versioning**
- Clique em **Edit**
- Selecione: **Enable**
- **Save changes**

**3. Validar Versionamento**
```bash
# Via AWS CLI
aws s3api get-bucket-versioning --bucket static-website-jam-XXXXXX

# Resposta esperada:
{
    "Status": "Enabled"
}
```

**4. Testar Recuperação (Opcional)**
- Faça upload de um arquivo
- Atualize o mesmo arquivo
- Na aba **Objects** → **Show versions**
- Você verá múltiplas versões do objeto

**5. Restaurar Versão Anterior (Se necessário)**
- Selecione a versão desejada
- **Actions** → **Download** ou **Delete delete marker**

## 🔍 Validação Completa

### Checklist de Segurança
- [ ] **Bucket privado:** Block all public access habilitado
- [ ] **Acesso restrito:** Apenas CloudFront pode acessar S3
- [ ] **HTTPS obrigatório:** Todas as conexões redirecionadas
- [ ] **Cache otimizado:** TTL de 1 hora configurado
- [ ] **Versioning ativo:** Proteção contra exclusões
- [ ] **Least privilege:** Políticas com permissões mínimas

### Testes de Validação

**Teste 1: Acesso Direto ao S3 (deve falhar)**
```bash
curl -I https://static-website-jam-XXXXXX.s3.amazonaws.com/index.html
# Esperado: 403 Forbidden ou Access Denied
```

**Teste 2: Acesso via CloudFront (deve funcionar)**
```bash
curl -I https://dxxxxxx.cloudfront.net/
# Esperado: 200 OK
```

**Teste 3: Redirecionamento HTTP (deve redirecionar)**
```bash
curl -I http://dxxxxxx.cloudfront.net/
# Esperado: 301 ou 302 com Location: https://...
```

**Teste 4: Cache Header**
```bash
curl -I https://dxxxxxx.cloudfront.net/
# Verifique headers: Cache-Control, Age, X-Cache
```

## 🎓 Conceitos Aprendidos

### **CloudFront + S3 Architecture**
- **OAC vs OAI:** Diferenças e quando usar cada um
- **Bucket policies:** Configuração para acesso via CloudFront
- **Cache behaviors:** Controle de como conteúdo é cacheado
- **Viewer protocols:** Controle de protocolos aceitos

### **Segurança em Profundidade**
- **Least privilege:** Permissões mínimas necessárias
- **Defense in depth:** Múltiplas camadas de segurança
- **Encryption in transit:** HTTPS em todas as conexões
- **Access control:** Restrição por ARN e condições

### **Performance e Disponibilidade**
- **Cache optimization:** Balanceamento de TTLs
- **Global distribution:** Edge locations para baixa latência
- **Version control:** Proteção e recuperação de dados
- **Content freshness:** Atualização automática de cache

## ⚠️ Pontos de Atenção

### **Origin Access Control (OAC)**
- **Obrigatório:** Use o ARN completo da distribuição na policy
- **Service principal:** Sempre use `cloudfront.amazonaws.com`
- **Condição StringEquals:** AWS:SourceArn é case-sensitive

### **Cache Configuration**
- **TTL values:** Minimum ≤ Default ≤ Maximum
- **Content updates:** Cache pode demorar até o TTL expirar
- **Invalidations:** Use com cautela (tem custos)

### **Versioning**
- **Custos:** Armazena todas as versões (aumenta custos)
- **Delete markers:** Exclusões criam markers, não removem
- **Lifecycle policies:** Configure para gerenciar versões antigas

### **Deploy Time**
- **CloudFront:** Mudanças levam 5-15 minutos para propagar
- **Cache:** Espere o TTL expirar para ver mudanças
- **Testing:** Use invalidations para testes rápidos

## 🔧 Troubleshooting Comum

### **403 Access Denied via CloudFront**
- Verifique se OAC está configurado na origem
- Confirme que a bucket policy inclui o ARN correto
- Valide que o account ID está correto na policy

### **HTTP não redireciona para HTTPS**
- Aguarde deploy da distribuição completar
- Limpe cache do navegador
- Teste com curl ou modo incógnito

### **Conteúdo não atualiza**
- Verifique se o TTL está configurado corretamente
- Aguarde o tempo do TTL expirar
- Use invalidation para forçar atualização

### **Versioning não funciona**
- Confirme que está habilitado em Properties
- Verifique se o status é "Enabled"
- Use "Show versions" para ver versões ocultas

## 📖 Recursos Adicionais

### **Documentação AWS**
- [CloudFront Origin Access Control](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)
- [CloudFront Cache Behaviors](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesCacheBehavior)
- [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html)
- [S3 Bucket Policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-policies.html)

### **Boas Práticas**
- **Security:** Use HTTPS, OAC e bucket policies restritivas
- **Performance:** Configure cache TTLs apropriados
- **Cost optimization:** Use lifecycle policies para versões antigas
- **Monitoring:** Configure CloudWatch alarms e logs

### **Próximos Passos**
- **WAF:** Adicionar Web Application Firewall
- **Custom domains:** Configurar domínios próprios
- **Lambda@Edge:** Processar requisições nas edges
- **CloudFront Functions:** Transformações leves de conteúdo

## 🏆 Critérios de Sucesso

- [ ] **Task 1:** Acesso restrito apenas via CloudFront (45 pts)
- [ ] **Task 2:** HTTPS obrigatório com redirecionamento (30 pts)
- [ ] **Task 3:** Cache atualizado a cada 1 hora (45 pts)
- [ ] **Task 4:** Versioning habilitado no bucket (30 pts)
- [ ] **Total:** 150 pontos

## 🎯 Cenários de Aplicação

### **Ambiente Corporativo**
- **Sites estáticos:** Landing pages, documentação, SPAs
- **Distribuição global:** Baixa latência para usuários mundiais
- **Segurança:** Proteção de conteúdo sensível
- **Compliance:** HTTPS obrigatório para regulamentações

### **Aplicações Web Modernas**
- **React/Vue/Angular:** Deploy de SPAs
- **JAMstack:** Sites estáticos com APIs
- **E-commerce:** Catálogos de produtos
- **Marketing:** Sites promocionais e campanhas

---

**🎉 Parabéns!** Você completou o Cyber Trek: Voyage into Secure Infrastructure! Você implementou com sucesso uma arquitetura segura e performática para distribuição de conteúdo estático usando CloudFront e S3.

> **💡 Dica:** Esta arquitetura é a base para muitas aplicações web modernas. Combine com Lambda@Edge, API Gateway e serviços serverless para criar aplicações completas e escaláveis na AWS.