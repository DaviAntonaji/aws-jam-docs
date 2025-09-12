# Data with the Stars – Task 2

## 🎯 Objetivo

Atender ao requisito do HIPAA 45 CFR 164.312(b): registrar e auditar atividades em sistemas que contenham ePHI (electronic Protected Health Information).

Nesta tarefa vamos:

- Fazer upload do arquivo de amostra `patient.csv` para o bucket de pacientes.
- Habilitar S3 Server Access Logging no bucket de pacientes, enviando registros para um bucket de logs separado.

## 🧭 Buckets envolvidos

- Bucket de pacientes: `jam-challenge-patientdata-us-east-1-192311737766`
- Bucket de logs (destino): `jam-challenge-accesslogs-us-east-1-192311737766`

## ✅ Passos executados

### 1) Upload do arquivo PHI

Exemplo via AWS CLI:

```bash
aws s3 cp patient.csv s3://jam-challenge-patientdata-us-east-1-192311737766/
```

### 2) Habilitar Server Access Logging

No bucket `jam-challenge-patientdata-us-east-1-192311737766`:

1. Aba "Properties" → seção "Server access logging".
2. Marcar "Enable logging".
3. Definir bucket de destino: `jam-challenge-accesslogs-us-east-1-192311737766`.
4. Configurar prefixo: `patientdata-logs/`.

## 🔎 Validação

- O arquivo `patient.csv` está visível no bucket de pacientes.
- O Server access logging aparece como "Enabled" e aponta para o bucket de logs.
- Os logs começam a ser entregues no bucket de destino em ~30–45 minutos.

Estrutura esperada dos arquivos de log:

```
patientdata-logs/2025-09-12-XX-XX-XX-XXXXX.gz
```

## 📌 Conclusão

- Além do controle de acesso (Task 1), passamos a registrar acessos (Task 2).
- Benefícios: rastreabilidade de acessos, armazenamento seguro de logs em bucket separado e conformidade com HIPAA para monitoramento de ePHI.