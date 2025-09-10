# Task 5 – Validação Final da Proteção do ALB

## Contexto
Após configurar a proteção em L4 (Security Group com prefix list do CloudFront) e em L7 (header secreto validado no listener do ALB), o último passo foi validar que apenas a distribuição correta do CloudFront consegue acessar o ALB.  

Este teste garante que:  
- O acesso direto ao ALB está bloqueado.  
- Distribuições CloudFront não autorizadas são negadas.  
- Somente a distribuição CloudFront correta (Application User) tem acesso à aplicação.

---

## Testes Realizados

1. **Acesso direto ao ALB (ApplicationLoadBalancerWebPageURL via HTTP):**  
   - Resultado: **Timeout**.  
   - Motivo: tráfego da internet não está na prefix list → bloqueado no Security Group (L4).  

2. **Acesso via CloudFront Malicious User (CloudFrontMaliciousUserWebPageURL via HTTPS):**  
   - Resultado: **Access denied**.  
   - Texto exibido incluía o código de validação para submissão do desafio.  
   - Esse código confirma que requisições de outras distribuições CloudFront não são aceitas (L7).  

3. **Acesso via CloudFront Application User (CloudFrontAppUserWebPageURL via HTTPS):**  
   - Resultado: aplicação carregada normalmente.  
   - Confirma que apenas a distribuição correta, com o header secreto configurado, consegue acessar o ALB.  

---

## Observações Importantes
- O bloqueio em **L4 (Security Group)** é fundamental para reduzir custos, pois evita que requisições negadas cheguem a ser processadas pelo ALB e contem no consumo de **LCUs**.  
- A proteção em **L7 (Listener Rule)** garante que apenas a distribuição CloudFront esperada, com o header secreto, é aceita.  
- Combinando
