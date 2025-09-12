# Data with the Stars!

## 📋 Visão Geral

Desafio focado em segurança e conformidade no S3 para dados sensíveis (ePHI). Você irá aplicar controles de acesso por Bucket Policy e habilitar auditoria via Server Access Logging para atender requisitos HIPAA.

## 🗂️ Estrutura

- `task1.md`: Controle de acesso no S3 via Bucket Policy (USER-A vs USER-B)
- `task2.md`: Auditoria de acessos com S3 Server Access Logging

## 🔗 Tarefas

- [Task 1 – Controle de Acesso no S3](./task1.md)
- [Task 2 – Auditoria de Acessos no S3](./task2.md)

## ✅ Objetivos de Aprendizado

- Entender limitações de permissões em ambientes de lab e alternativas seguras
- Aplicar Bucket Policies para controle de acesso a dados sensíveis
- Habilitar e validar S3 Server Access Logging para auditoria
- Compreender alinhamento com requisitos de conformidade (HIPAA)

## 🏁 Critérios de Conclusão

- [ ] USER-A consegue acesso total ao bucket de pacientes
- [ ] USER-B recebe AccessDenied em qualquer operação no bucket
- [ ] Server Access Logging habilitado e escrevendo em bucket de logs dedicado

---

Boa prática: documente as decisões tomadas e valide cada alteração incrementalmente.
