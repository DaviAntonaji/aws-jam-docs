# Prepare to Fail (over) – Task 1

## 🎯 Objetivo

Configurar um **Application Load Balancer (ALB)** para prover **alta disponibilidade** distribuindo tráfego entre **duas instâncias EC2**.

---

## 📝 Contexto

Executar um site em uma única EC2 cria um **ponto único de falha**. Registrando duas EC2 no **Target Group** do ALB, se uma ficar indisponível, o tráfego é roteado automaticamente para a outra.

---

## ⚙️ Passos executados

### 1) Verificar o DNS do ALB
- Acessar o **DNS Name** do ALB no navegador.
- Erro observado: **503 Service Temporarily Unavailable** → sem targets saudáveis no Target Group.

---

### 2) Configurar Security Groups
- **ALB SG**: permitir entrada em **HTTP 80** (e HTTPS 443, se necessário) de `0.0.0.0/0`.
- **EC2 SG**: permitir entrada em **HTTP 80** a partir do SG do ALB (no lab, `0.0.0.0/0` também funciona).

---

### 3) Registrar Targets
- Ir em **EC2 > Target Groups > Targets**.
- Inicialmente não há instâncias registradas.
- Registrar as duas EC2:
  - `i-056a1e084874ac26a`
  - `i-0f419fc23fc51b03b`
- Porta: **80 (Traffic port)**.

---

### 4) Health Check
- Path: `/`
- Protocolo: `HTTP`
- Porta: `Traffic port (80)`
- Códigos de sucesso: `200`
- Healthy threshold: `5`
- Unhealthy threshold: `2`
- Intervalo: `30s`
- Timeout: `5s`

---

### 5) Validação
- Aguardar ~1–2 minutos.
- As duas EC2 ficam **healthy** no Target Group.
- Acessar novamente o DNS do ALB → site carrega com sucesso.

---

## ✅ Resultado
- O ALB distribui tráfego entre **duas EC2 saudáveis**.
- **Alta disponibilidade** alcançada: se uma cai, o tráfego faz failover para a outra.

---

## 🔎 Notas
- Produção:
  - Restringir o SG da EC2 para aceitar apenas do SG do ALB (evitar `0.0.0.0/0`).
  - Manter **Cross-Zone Load Balancing** habilitado (padrão no ALB).
  - Usar Auto Scaling Group para substituição automática de instâncias.