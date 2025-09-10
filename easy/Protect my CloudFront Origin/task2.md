# TASK 2 — Proteger ALB na Camada de Rede (L4)

## Contexto
O Application Load Balancer (ALB) estava inicialmente exposto à internet através do seu Security Group.  
A regra de entrada permitia tráfego HTTP de **qualquer lugar (0.0.0.0/0)**.  
Esta configuração expunha o ALB ao acesso direto, contornando o CloudFront e ignorando todos os controles de segurança configurados (WAF, restrições geográficas, autenticação, etc.).

Para mitigar este problema, restringimos o acesso ao ALB na **Camada 4 (nível de rede)** usando uma AWS Managed Prefix List que contém os intervalos de IP dos servidores de origem do CloudFront.

## Passos Executados

### 1) Navegar para Security Group
- Abriu o **Console EC2**
- Localizou o Security Group chamado **Jam** (anexado ao ALB)

### 2) Remover regra de entrada insegura
- Deletou a regra de entrada:
  ```
  Type: HTTP
  Protocol: TCP
  Port: 80
  Source: 0.0.0.0/0
  ```

### 3) Adicionar regra de entrada segura
- Adicionou uma nova regra de entrada permitindo apenas IPs de origem do CloudFront:
  ```
  Type: HTTP
  Protocol: TCP
  Port: 80
  Source: Prefix List → com.amazonaws.global.cloudfront.origin-facing | pl-3b927c52
  ```

### 4) Salvar alterações

## Validação

### ALB URL (acesso direto)
- **Testado e confirmado** que **não está mais acessível**
- Isso significa que usuários externos não podem contornar o CloudFront para alcançar o ALB

### CloudFront URL (acesso esperado)
- **Ainda acessível** e servindo a aplicação conforme esperado
- CloudFront continua encaminhando requisições para o ALB sem problemas

## Resultado

O ALB agora está protegido no **nível de rede (L4)**.  
Apenas **servidores de origem do CloudFront** podem alcançar o ALB, impedindo tráfego direto da internet.

### Benefícios desta medida:
- ✅ **Reduz superfície de exposição**
- ✅ **Garante que todas as requisições passem pelo CloudFront**
- ✅ **Mantém performance e segurança** aplicando proteções baseadas no CloudFront (WAF, autenticação, geo-filtros)

## 🔒 Proteção Implementada

**Antes:**
```
ALB ← Qualquer IP da internet (0.0.0.0/0)
```

**Depois:**
```
ALB ← Apenas IPs de origem do CloudFront (Prefix List)
```

## ⚠️ Limitação Atual

Esta proteção L4 ainda permite que **qualquer distribuição CloudFront** acesse o ALB.  
Nas próximas tasks, implementaremos proteção adicional na **Camada 7** para garantir que apenas nossa distribuição CloudFront específica seja aceita.

