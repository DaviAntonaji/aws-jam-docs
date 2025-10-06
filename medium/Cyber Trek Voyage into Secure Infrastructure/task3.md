# Task 3: Cache Performance Optimization Expedition

**Pontos Possíveis:** 45  
**Penalidade por Dica:** 0  
**Pontos Disponíveis:** 45

## 🎯 Background

O website não está sendo atualizado com o conteúdo mais recente que é atualizado no bucket S3 a cada 1 hora. O website está mostrando conteúdo antigo.

## 📋 Your Task

Aventure-se nas profundezas do Amazon CloudFront e embarque em uma missão para resolver este problema e otimizar os mecanismos de cache. Sua missão é encontrar o equilíbrio perfeito entre eficiência de cache e atualização de conteúdo, garantindo entrega de conteúdo ultrarrápida enquanto combate o espectro da latência. De acordo com o caso de uso, o conteúdo é atualizado a cada 1 hora. Portanto, o cache deve ser atualizado a cada 1 hora.

## 🚀 Getting Started

Use o botão **Open AWS Console** no topo da tela do desafio para abrir seu console AWS e obter acesso ao Amazon CloudFront Distribution.

## 📦 Inventory

- **Amazon CloudFront Distribution:** Consulte o CloudFront distribution ID na seção Output Properties

## 🛠️ Services You Should Use

- Amazon CloudFront

## ✅ Task Validation

A tarefa será concluída automaticamente assim que você configurar o cache do CloudFront Distribution para atualizar a cada 1 hora. Além disso, você sempre pode verificar seu progresso pressionando o botão "Check my progress" na tela de detalhes do desafio.

---

## 🔍 Resolução Detalhada

### 🧩 Contexto do Problema

O site estático hospedado no Amazon S3 e distribuído por Amazon CloudFront apresentava um problema de cache desatualizado — o conteúdo do site não refletia as atualizações recentes que eram enviadas ao bucket S3 a cada hora.

Como resultado, os usuários viam conteúdo antigo, mesmo após novos arquivos serem carregados no bucket.

### ⚙️ Causa Raiz

- O CloudFront estava configurado com um tempo de vida de cache (TTL) muito alto
- Isso fazia com que os objetos permanecessem armazenados nos edge locations além do período em que novos conteúdos eram disponibilizados no S3
- Impedia a atualização automática dos objetos, exigindo invalidações manuais ou aguardo prolongado até o vencimento do cache

### 🧠 Etapas da Solução

#### 1. Identificação do Recurso

- **CloudFront Distribution ID:** (exemplo: E2TUXQI3IFLTF6)
- **Origem (Origin):** static-website-jam-XXXXXX.s3.amazonaws.com

#### 2. Acesso à Configuração de Cache

No console AWS:

1. Acesse **Amazon CloudFront**
2. Selecione a distribuição (exemplo: E2TUXQI3IFLTF6)
3. Acesse a aba **Behaviors** (Comportamentos)
4. Clique em **Edit** no comportamento padrão **Default (*)**
5. Localize a seção **Cache key and origin requests**

#### 3. Configurar Cache Policy

**Opção A: Criar uma Cache Policy Customizada**

1. Em **Cache Policy**, clique em **Create policy**
2. Configure a policy:

| Parâmetro | Valor | Descrição |
|-----------|-------|-----------|
| **Name** | `one-hour-ttl` | Nome descritivo |
| **Minimum TTL** | `0` seconds | Permite atualização imediata se necessário |
| **Default TTL** | `3600` seconds (1 hour) | ⭐ Define que o conteúdo será armazenado por 1 hora |
| **Maximum TTL** | `3600` seconds (1 hour) | Garante que objetos não fiquem além de 1 hora |
| **Headers** | None | Mantém cache simples e eficiente |
| **Query strings** | None | Evita múltiplas variações desnecessárias |
| **Cookies** | None | Reduz complexidade e melhora performance |

3. **Create policy**
4. Volte ao comportamento e selecione a policy criada

**Opção B: Editar Diretamente no Behavior**

Se preferir configurar diretamente:

1. Em **Cache policy**, selecione **Managed-CachingOptimized** ou crie uma customizada
2. Configure TTLs conforme tabela acima

### 🔧 Passo a Passo Completo

#### No Console AWS:

```
1. CloudFront Console → Distributions
2. Selecione sua distribuição
3. Aba "Behaviors"
4. Selecione "Default (*)" → Edit
5. Cache key and origin requests → Cache policy and origin request policy (recommended)
6. Cache policy → Create policy
7. Configure:
   - Name: one-hour-ttl
   - Description: Cache refreshes every hour
   - Minimum TTL: 0
   - Default TTL: 3600
   - Maximum TTL: 3600
8. Save policy
9. No behavior, selecione a policy criada
10. Save changes
11. Aguarde status "Deployed"
```

### 🧾 Resultado Obtido

Após aplicar as configurações:

- ✅ O cache do CloudFront é atualizado automaticamente a cada 1 hora
- ✅ O conteúdo refletido aos usuários está sempre sincronizado com o S3
- ✅ O site mantém ótimo desempenho, pois ainda utiliza cache em edge locations
- ✅ Respeita o ciclo de atualização esperado

### 🔍 Verificação

| Teste | Resultado | Status |
|-------|-----------|--------|
| Conteúdo atualizado no S3 | Refletido no site após 1 hora | ✅ |
| Teste de cache em edge location | Recarregamento eficiente, sem latência excessiva | ✅ |
| Política de cache validada | TTL padrão = 3600 segundos | ✅ |
| Validação "Check my progress" | Task concluída com sucesso (45 pontos) | ✅ |

### 📊 Entendendo TTLs

```
┌─────────────────────────────────────────────────┐
│  Minimum TTL (0s)                               │
│  ↓                                              │
│  ├─ Permite atualização imediata via headers   │
│                                                 │
│  Default TTL (3600s = 1 hora)                  │
│  ↓                                              │
│  ├─ Usado quando origin não especifica TTL     │
│  ├─ ⭐ ESTE É O VALOR CHAVE!                   │
│                                                 │
│  Maximum TTL (3600s = 1 hora)                  │
│  ↓                                              │
│  ├─ Garante que cache não exceda 1 hora        │
└─────────────────────────────────────────────────┘
```

### 🔐 Resultado Final

A distribuição CloudFront agora está configurada para manter equilíbrio ideal entre desempenho e atualização:

- ✅ Cache eficiente nas bordas (edge locations)
- ✅ Atualizações automáticas sincronizadas com a frequência de publicação (1 hora)
- ✅ Nenhuma necessidade de invalidação manual
- ✅ Performance global mantida

## 🏁 Conclusão

✅ **Cache Performance Optimization Expedition concluída com sucesso.**

O ambiente agora entrega o conteúdo mais recente do bucket S3 com desempenho otimizado e alta disponibilidade global, garantindo uma experiência rápida e segura aos usuários.

---

## 🔧 Troubleshooting

### Problema: Conteúdo ainda não atualiza após 1 hora

**Possíveis causas:**
1. Deploy do CloudFront ainda não completou
2. Cache do navegador armazenando versão antiga
3. TTL configurado incorretamente

**Soluções:**
```bash
# 1. Verificar status da distribuição
# No console: Status deve estar "Deployed"

# 2. Teste sem cache do navegador
curl -H "Cache-Control: no-cache" https://dxxxxx.cloudfront.net/

# 3. Verifique headers de cache
curl -I https://dxxxxx.cloudfront.net/
# Procure por:
# Cache-Control: max-age=3600
# Age: XXX (tempo em segundos desde último cache)
```

### Problema: Preciso atualizar imediatamente

Se precisar forçar atualização antes do TTL:

```bash
# Via Console:
# CloudFront → Invalidations → Create invalidation
# Paths: /* (para todos os arquivos)

# Via AWS CLI:
aws cloudfront create-invalidation \
  --distribution-id E2TUXQI3IFLTF6 \
  --paths "/*"
```

⚠️ **Nota:** Invalidations têm custo após as primeiras 1000 por mês

### Problema: Cache Policy não aparece no behavior

1. Certifique-se de criar a policy primeiro
2. Refresh da página do CloudFront
3. Verifique se está na mesma região/conta
4. Aguarde alguns segundos após criar a policy

### Verificação de Cache Headers

```bash
# Verificar headers de cache retornados
curl -I https://dxxxxx.cloudfront.net/index.html

# Headers importantes:
# Cache-Control: max-age=3600  ← TTL configurado
# Age: 1234                    ← Tempo desde último cache (segundos)
# X-Cache: Hit from cloudfront ← Se veio do cache
# X-Cache: Miss from cloudfront ← Se foi buscar no origin
```

## 📚 Conceitos Aprendidos

### Cache TTL (Time To Live)
- **Minimum TTL:** Menor tempo que objeto pode ficar em cache
- **Default TTL:** Usado quando origin não especifica
- **Maximum TTL:** Maior tempo permitido em cache

### Cache Behaviors
- **Path patterns:** Diferentes regras para diferentes caminhos
- **Cache policies:** Reutilizáveis entre behaviors
- **Origin request policies:** Controla o que é enviado ao origin

### Performance vs Freshness
```
Alta Performance          Conteúdo Atualizado
     ↑                           ↑
     │                           │
     │         ⭐                 │
     │      TTL = 1h             │
     │    (Ideal para           │
     │   este caso de uso)      │
     │                           │
     └───────────────────────────┘
```

### Cache Invalidation
- **Uso:** Forçar atualização antes do TTL
- **Custo:** Primeiras 1000/mês gratuitas
- **Quando usar:** Correções urgentes, não para uso regular

## 🎯 Boas Práticas

### ✅ DO (Faça)
- Configure TTLs apropriados para seu caso de uso
- Use cache policies reutilizáveis
- Monitore hit ratio do cache
- Planeje ciclo de atualização de conteúdo

### ❌ DON'T (Não Faça)
- Não use TTL = 0 (bypassa cache, desperdiça CloudFront)
- Não faça invalidations frequentes (caro e ineficiente)
- Não configure Maximum < Default TTL
- Não ignore o tempo de propagação (5-15 min)

## 🎯 Próximo Nível

Após completar esta task, considere:
- **Cache Control Headers:** Configure no S3 para controle fino
- **Versioning de Arquivos:** Use hashes no nome (ex: style.abc123.css)
- **CloudWatch Metrics:** Monitore cache hit ratio
- **Lambda@Edge:** Manipule headers de cache dinamicamente
