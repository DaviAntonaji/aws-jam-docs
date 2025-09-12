# Prepare to Fail (over) – Task 2

## 🎯 Objetivo

Garantir que o **ALB** distribua as requisições entre as duas instâncias **EC2** e validar o funcionamento recuperando as duas metades da Challenge Key.

---

## ✅ Configurações aplicadas

No **Target Group → Attributes**:
- **Load balancing algorithm**: `Round robin`.
- **Stickiness (session affinity)**: `Off`.
- **Cross-zone load balancing**: `Enabled` (padrão).

---

## 🧭 Passos
1. Acessar **EC2 > Target Groups**.
2. Editar os **Attributes** do Target Group.
3. Ajustar o algoritmo para `Round robin` e desabilitar `Stickiness`.
4. Salvar.

---

## 🧪 Validação

Personalizar ou verificar a resposta de cada EC2. Exemplo de customização:

```bash
echo "EC2 Instance ID: $(curl -s http://169.254.169.254/latest/meta-data/instance-id)" | sudo tee /var/www/html/index.html
```

Realizar múltiplas requisições ao DNS do ALB:

```bash
for i in {1..10}; do curl -s http://<ALB-DNS>; done
```

Esperado: respostas alternando entre as duas instâncias, por exemplo:

```
Instância A → EC2 Instance ID: i-056a1e084874ac26a
JAM Challenge Key 1: GnK2e

Instância B → EC2 Instance ID: i-0f419fc23fc51b03b
JAM Challenge Key 2: looPS
```

Importante: concatene as duas partes da chave (Key 1 + Key 2) para concluir o desafio.

---

## ✅ Resultado

- O ALB distribui tráfego entre as duas EC2.
- Foi possível recuperar as duas metades da Challenge Key via ALB, comprovando o balanceamento.
