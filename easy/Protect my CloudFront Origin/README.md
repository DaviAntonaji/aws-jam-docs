# Protect my CloudFront Origin

## 📋 Visão Geral

Este desafio foca em **segurança de aplicações web** usando **AWS CloudFront** e **Application Load Balancer (ALB)**. Você aprenderá a identificar e corrigir vulnerabilidades de segurança, implementando proteções em múltiplas camadas (L4 e L7) para garantir que apenas tráfego autorizado acesse sua aplicação.

## 🎯 Objetivos de Aprendizado

- ✅ Identificar vulnerabilidades de acesso direto ao ALB
- ✅ Implementar proteção na Camada 4 (Security Groups + Prefix Lists)
- ✅ Configurar proteção na Camada 7 (Headers secretos + Listener Rules)
- ✅ Validar proteções em múltiplas camadas
- ✅ Entender arquitetura de segurança em profundidade

## 🏗️ Arquitetura

```
┌─────────────────────────────────────────────────────────────────┐
│                        Internet                                │
└─────────────────┬───────────────────────────────────────────────┘
                  │
    ┌─────────────┼─────────────┐
    │             │             │
    ▼             ▼             ▼
┌─────────┐  ┌─────────┐  ┌─────────┐
│CloudFront│  │CloudFront│  │  ALB    │
│Authorized│  │Malicious│  │ Direct  │
│(com header)│  │(sem header)│  │ Access  │
└─────┬───┘  └─────┬───┘  └─────┬───┘
      │            │             │
      │            │             │
      ▼            ▼             ▼
┌─────────────────────────────────────┐
│           ALB (Jam)                 │
│                                     │
│  ✅ L4: Security Group              │
│     (apenas IPs CloudFront)         │
│                                     │
│  ✅ L7: Listener Rules              │
│     (valida header x-from-cf)       │
│                                     │
└─────────────────┬───────────────────┘
                  │
                  ▼
┌─────────────────────────────────────┐
│         Aplicação Web               │
└─────────────────────────────────────┘
```

## 📁 Estrutura do Projeto

```
Protect my CloudFront Origin/
├── README.md          # Este arquivo
├── task1.md          # Identificar vulnerabilidade
├── task2.md          # Proteção L4 (Security Groups)
├── task3.md          # Configurar header secreto (CloudFront)
├── task4.md          # Validação L7 (ALB Listener Rules)
└── task5.md          # Validação final e testes
```

## 🚀 Pré-requisitos

- **AWS Account** com permissões para CloudFront, ALB, EC2 e VPC
- **Conhecimento básico:** Security Groups, CloudFront, ALB
- **Ambiente:** Lab AWS com recursos pré-configurados

## 🎮 Como Executar

### Task 1: Identificar Vulnerabilidade
1. Leia o arquivo [`task1.md`](./task1.md)
2. Acesse URLs fornecidas no Output Properties
3. Identifique que o ALB está acessível diretamente
4. Copie o texto da página para resposta

### Task 2: Proteção L4 (Camada de Rede)
1. Leia o arquivo [`task2.md`](./task2.md)
2. Configure Security Group com Prefix List do CloudFront
3. Remova regra insegura (0.0.0.0/0)
4. Valide que acesso direto está bloqueado

### Task 3: Header Secreto (CloudFront)
1. Leia o arquivo [`task3.md`](./task3.md)
2. Configure Origin Custom Header no CloudFront
3. Defina header: `x-from-cf: MySuperSecret`
4. Aguarde deployment completar

### Task 4: Validação L7 (ALB)
1. Leia o arquivo [`task4.md`](./task4.md)
2. Configure Listener Rules no ALB
3. Valide header secreto nas requisições
4. Configure resposta padrão para requisições inválidas

### Task 5: Validação Final
1. Leia o arquivo [`task5.md`](./task5.md)
2. Teste todos os cenários de acesso
3. Valide que proteções estão funcionando
4. Confirme que apenas CloudFront autorizado funciona

## 🔧 Conceitos Técnicos

### Vulnerabilidades de Segurança
- **Acesso direto ao ALB:** Bypass das proteções do CloudFront
- **Superfície de ataque:** Exposição desnecessária de recursos
- **Bypass de controles:** Ignorar WAF, geo-restrições, autenticação

### Proteção em Camadas
- **L4 (Rede):** Security Groups + Prefix Lists
- **L7 (Aplicação):** Headers secretos + Listener Rules
- **Defesa em profundidade:** Múltiplas camadas de proteção

### AWS Prefix Lists
- **Managed Prefix Lists:** Listas gerenciadas pela AWS
- **CloudFront Origins:** IPs dos servidores de origem do CloudFront
- **Atualização automática:** AWS mantém lista atualizada

### Headers Secretos
- **Origin Custom Headers:** Headers enviados pelo CloudFront para origem
- **Validação no servidor:** ALB verifica presença e valor do header
- **Case-sensitive:** Valores são sensíveis a maiúsculas/minúsculas

## 📖 Recursos Adicionais

- [AWS CloudFront Documentation](https://docs.aws.amazon.com/cloudfront/)
- [Application Load Balancer Security](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/)
- [Security Groups Best Practices](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)
- [AWS Managed Prefix Lists](https://docs.aws.amazon.com/vpc/latest/userguide/managed-prefix-lists.html)

## 🏆 Critérios de Sucesso

- [ ] Vulnerabilidade identificada e documentada
- [ ] Proteção L4 implementada (Security Group + Prefix List)
- [ ] Header secreto configurado no CloudFront
- [ ] Validação L7 implementada no ALB
- [ ] Todos os testes de validação passaram
- [ ] Apenas CloudFront autorizado tem acesso

## 🆘 Troubleshooting

### Problemas Comuns

**ALB ainda acessível diretamente**
- Verifique se Security Group foi atualizado corretamente
- Confirme que Prefix List está configurada
- Aguarde propagação das mudanças (pode levar alguns minutos)

**CloudFront autorizado não funciona**
- Verifique se header secreto está configurado corretamente
- Confirme que Listener Rules estão aplicadas
- Verifique se deployment do CloudFront foi concluído

**CloudFront malicioso ainda funciona**
- Confirme que Listener Rules estão configuradas
- Verifique se regra padrão retorna 403
- Teste com diferentes valores de header

### 🔍 Validação de Configuração

1. **Security Group:**
   ```
   Type: HTTP
   Port: 80
   Source: Prefix List → com.amazonaws.global.cloudfront.origin-facing
   ```

2. **CloudFront Header:**
   ```
   Name: x-from-cf
   Value: MySuperSecret
   ```

3. **ALB Listener Rule:**
   ```
   IF: Header x-from-cf equals MySuperSecret
   THEN: Forward to Target Group
   ```

## 🎯 Benefícios da Implementação

- ✅ **Redução de superfície de ataque**
- ✅ **Proteção em múltiplas camadas**
- ✅ **Garantia de tráfego autorizado**
- ✅ **Manutenção de proteções CloudFront**
- ✅ **Performance otimizada**
- ✅ **Custo otimizado** (menos LCUs do ALB)

## 🏭 Aplicação em Produção

### Melhorias Adicionais
- **HTTPS:** Use certificados ACM para comunicação CloudFront ↔ ALB
- **WAF:** Implemente AWS WAF para proteção adicional
- **Monitoring:** Configure CloudWatch para monitorar tentativas de acesso
- **Logs:** Ative logs de acesso do ALB e CloudFront
- **Rotação:** Implemente rotação de headers secretos

### Considerações de Segurança
- **Headers secretos:** Trate como segredos e rotacione regularmente
- **Princípio do menor privilégio:** Use permissões mínimas necessárias
- **Monitoramento:** Implemente alertas para tentativas de acesso suspeitas
- **Backup:** Documente todas as configurações de segurança

---

**🎉 Boa sorte com o desafio!**

> **💭 Reflexão:** Este desafio ensina não apenas sobre configuração de serviços AWS, mas também sobre pensamento de segurança em camadas e defesa em profundidade - conceitos fundamentais para arquiteturas seguras em produção.
