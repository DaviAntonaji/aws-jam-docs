# Prepare to Fail (over)

## 📋 Visão Geral

Desafio focado em **alta disponibilidade** e **balanceamento de carga** com **Application Load Balancer (ALB)** em frente a múltiplas instâncias **EC2**. O objetivo é eliminar ponto único de falha e comprovar distribuição de requisições entre instâncias.

## 🗂️ Estrutura

- `task1.md`: Criar alta disponibilidade com ALB e duas EC2
- `task2.md`: Ajustar algoritmo e validar distribuição entre as instâncias

## 🔗 Tarefas

- [Task 1 – High Availability com ALB](./task1.md)
- [Task 2 – Round robin e validação de chave](./task2.md)

## ✅ Objetivos de Aprendizado

- Configurar Target Groups, Health Checks e Security Groups para ALB
- Registrar múltiplas EC2 e entender estados de saúde
- Ajustar atributos do Target Group (algoritmo e stickiness)
- Validar distribuição de tráfego e coletar evidências

## 🏁 Critérios de Conclusão

- [ ] ALB frente a duas EC2 com status healthy
- [ ] Site acessível via DNS do ALB
- [ ] Algoritmo `Round robin` ativo e `Stickiness` desativada
- [ ] Duas metades da Challenge Key obtidas via ALB

---

Boa prática: use Auto Scaling Group em produção para reposição automática de instâncias.

