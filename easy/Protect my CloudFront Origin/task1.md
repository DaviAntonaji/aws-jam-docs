# TASK 1 — Identificar Vulnerabilidade de Acesso Direto ao ALB

## Objetivo
Identificar que o Application Load Balancer está acessível diretamente, contornando as proteções do CloudFront.

## Passos para Identificação

### 1) Acessar Output Properties
- Vá para **Output Properties** no ambiente do challenge

### 2) Testar URLs

**URL Correta (CloudFront):**
- Copie o valor de `CloudFrontAppUserWebPageURL`
- Abra no navegador
- → Este é o caminho correto que os usuários deveriam usar

**URL Vulnerável (ALB Direto):**
- Copie o valor de `ApplicationLoadBalancerWebPageURL`
- Abra no navegador (usando HTTP)
- → Este é o caminho que **não deveria estar acessível**, mas ainda está

### 3) Identificar o Problema
Quando você abrir o ALB URL diretamente, ele vai mostrar uma página com algum texto específico.

→ **Esse texto é justamente o que você precisa copiar.**

## Resposta da Task 1

No campo de resposta da plataforma, você deve colar exatamente assim:

```
Task 1 answer: <texto que apareceu no ALB>
```

## ⚠️ Problema Identificado

Esta vulnerabilidade permite que usuários:
- **Contornem o CloudFront** completamente
- **Ignorem todas as proteções** configuradas (WAF, geo-restrições, autenticação, etc.)
- **Acessem diretamente** o Application Load Balancer
- **Bypassem** todas as políticas de segurança implementadas

## 🎯 Próximos Passos

Nas próximas tasks, você aprenderá a:
- Restringir acesso ao ALB na camada de rede (L4)
- Implementar proteção adicional na camada de aplicação (L7)
- Garantir que apenas o CloudFront autorizado possa acessar o ALB
