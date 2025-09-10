# Task 4 – Proteção em L7 com Header Secreto no ALB (Regras do Listener)

## Contexto
Depois de restringir o acesso em L4 usando a prefix list do CloudFront (Task 2) e configurar o header secreto no CloudFront (Task 3), o último passo foi aplicar essa validação no nível do **listener do ALB (L7)**.  
Isso garante que apenas requisições vindas da **nossa distribuição CloudFront** (com o header correto) sejam aceitas.  
Qualquer outra distribuição CloudFront ou tentativa de acesso direto será negada.

---

## Alterações Realizadas

**ALB:** Jam  
**Listener:** HTTP:80  

### Regra – Prioridade 1
- **Condição (If):**
  - Header HTTP `x-from-cf` **igual a** `MySuperSecret`  
- **Ação (Then):**
  - Retornar resposta fixa  
    - **Response code:** `200`  
    - **Content-Type:** `text/html`  
    - **Response body:** HTML padrão do lab (Hello there from CloudFront!)  

### Regra – Default (Last)
- **Condição (If):**
  - Nenhuma condição (executada quando nenhuma outra regra é atendida).  
- **Ação (Then):**
  - Retornar resposta fixa  
    - **Response code:** `403`  
    - **Content-Type:** `text/plain`  
    - **Response body:** `Access denied`  

---

## Validação

- **URL do CloudFront Application User:**  
  ✅ Funcionando corretamente, pois envia o header secreto `x-from-cf: MySuperSecret`.

- **URL do CloudFront Malicious User:**  
  ❌ Bloqueado com **403 Access denied**, já que não envia o header secreto.

- **URL direto do ALB:**  
  ❌ Continua bloqueado em L4 pela regra de Security Group (prefix list do CloudFront).

---

## Resultado
O ALB agora está totalmente protegido:

- **Camada 4 (Security Group):** Apenas IPs de CloudFront podem se conectar.  
- **Camada 7 (Listener Rule):** Apenas requisições com o header secreto correto (`x-from-cf: MySuperSecret`) são aceitas.  

Com isso, fechamos a brecha de segurança: somente a **nossa distribuição CloudFront** consegue se comunicar com o ALB, bloqueando distribuições maliciosas e tentativas de bypass direto.
