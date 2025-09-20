# 🌐 Hey WordPress Let's Multisite

## 📋 Visão Geral

Este desafio ensina como configurar **WordPress Multisite** em uma instância Amazon Lightsail existente, permitindo hospedar múltiplos sites WordPress em uma única instalação. O foco está em configurar um segundo site sem impactar o site original e resolver problemas comuns de permissões.

## 🎯 Objetivo

Configurar um segundo site WordPress na mesma instância Lightsail existente, sem impactar o site original, utilizando o recurso **WordPress Multisite** e resolver problemas de permissões que surgem após a configuração.

## 🔧 Conceitos Principais

- **Amazon Lightsail** - Hospedagem simplificada de aplicações
- **WordPress Multisite** - Rede de sites em uma única instalação
- **Bitnami Stack** - Stack LAMP pré-configurada
- **Subdomínios** - Configuração de sites secundários
- **Permissões de Sistema** - Troubleshooting de permissões de arquivos
- **Apache Configuration** - Configuração de rewrite rules
- **DNS Dinâmico** - Uso de nip.io para resolução de domínios

## 🏗️ Arquitetura

```
┌─────────────────────────────────────────────────────────────┐
│                Amazon Lightsail Instance                   │
│                     (PublicWebsite)                        │
│                                                             │
│  ┌─────────────────┐    ┌─────────────────┐                │
│  │   WordPress     │    │  WordPress      │                │
│  │   Site Principal│    │  Multisite      │                │
│  │   3.230.0.108   │    │  marketing-site │                │
│  │                 │    │  3.230.0.108    │                │
│  └─────────────────┘    └─────────────────┘                │
│           │                        │                       │
│           └────────┬─────────────────┘                       │
│                    │                                         │
│  ┌─────────────────▼─────────────────┐                     │
│  │        Apache + PHP               │                     │
│  │     (Bitnami Stack)               │                     │
│  └───────────────────────────────────┘                     │
└─────────────────────────────────────────────────────────────┘
```

## 📚 Tarefas

### [Task 1: Configuração WordPress Multisite](./task1.md)

**Objetivo:** Configurar WordPress Multisite e criar site secundário

**Conceitos abordados:**
- Conexão SSH com instância Lightsail
- Recuperação de credenciais WordPress
- Ativação do suporte Multisite no wp-config.php
- Criação da rede WordPress com subdomínios
- Configuração de rewrite rules no Apache
- Criação de site secundário na rede
- Uso de nip.io para resolução de domínios

### [Task 2: Resolução de Erro 500](./task2.md)

**Objetivo:** Diagnosticar e corrigir erro 500 após configuração Multisite

**Conceitos abordados:**
- Troubleshooting de erros HTTP 500
- Análise de logs do Apache
- Diagnóstico de problemas de permissões
- Correção de permissões de diretórios WordPress
- Configuração adequada de ownership de arquivos
- Validação de funcionamento de sites

## 🚀 Passo a Passo Resumido

### Task 1 - Configuração Multisite
1. **Conectar via SSH** à instância Lightsail
2. **Recuperar credenciais** WordPress do arquivo de senha
3. **Ativar Multisite** no wp-config.php
4. **Configurar rede** WordPress via admin
5. **Aplicar configurações** no servidor (wp-config.php e .htaccess)
6. **Reiniciar Apache** para aplicar mudanças
7. **Criar site secundário** na rede
8. **Validar funcionamento** dos sites

### Task 2 - Correção de Permissões
1. **Identificar erro 500** em todos os sites
2. **Analisar logs** do Apache para diagnóstico
3. **Verificar permissões** dos diretórios WordPress
4. **Corrigir permissões** do diretório wp-includes
5. **Ajustar ownership** completo dos arquivos
6. **Reiniciar Apache** para aplicar correções
7. **Validar funcionamento** de ambos os sites

## ⚠️ Pontos Importantes

### Configuração Multisite
- **Subdomínios vs Subdiretórios:** Este lab usa subdomínios
- **Domínio nip.io:** Converte automaticamente `<subdomínio>.<IP>.nip.io` para o IP
- **Rewrite Rules:** Configuração específica do Bitnami em `htaccess.conf`
- **wp-config.php:** Adição de constantes específicas do Multisite

### Troubleshooting de Permissões
- **Diretório wp-includes:** Frequentemente afetado por permissões incorretas
- **Ownership:** Arquivos devem pertencer a `bitnami:daemon`
- **Permissões de diretórios:** 775 para diretórios, 664 para arquivos
- **wp-config.php:** Deve ter permissão 640 por segurança

### Comandos Críticos
```bash
# Verificar logs de erro
sudo tail /opt/bitnami/apache/logs/error_log

# Corrigir permissões específicas
sudo chmod 775 /opt/bitnami/wordpress/wp-includes

# Corrigir ownership completo
sudo chown -R bitnami:daemon /opt/bitnami/wordpress

# Reiniciar Apache
sudo /opt/bitnami/ctlscript.sh restart apache
```

## 🔍 Exemplo de Configuração

### wp-config.php - Constantes Multisite
```php
define('WP_ALLOW_MULTISITE', true);
define('MULTISITE', true);
define('SUBDOMAIN_INSTALL', true);
define('DOMAIN_CURRENT_SITE', '3.230.0.108.nip.io');
define('PATH_CURRENT_SITE', '/');
define('SITE_ID_CURRENT_SITE', 1);
define('BLOG_ID_CURRENT_SITE', 1);
```

### .htaccess - Rewrite Rules
```apache
RewriteEngine On
RewriteBase /
RewriteRule ^index\.php$ - [L]
RewriteRule ^wp-admin$ wp-admin/ [R=301,L]
RewriteCond %{REQUEST_FILENAME} -f [OR]
RewriteCond %{REQUEST_FILENAME} -d
RewriteRule ^ - [L]
RewriteRule . index.php [L]
```

## 📊 Dificuldade e Tempo

**Dificuldade:** ⭐⭐⭐☆☆  
**Tempo estimado:** 45-60 minutos

## 🎓 Lições Aprendidas

### WordPress Multisite
- **Economia de recursos:** Múltiplos sites em uma instalação
- **Gerenciamento centralizado:** Admin único para toda a rede
- **Configuração complexa:** Requer modificações em múltiplos arquivos
- **DNS dinâmico:** nip.io facilita testes sem configuração DNS

### Troubleshooting Linux
- **Logs são fundamentais:** Sempre verificar logs de erro primeiro
- **Permissões críticas:** WordPress é sensível a permissões incorretas
- **Ownership matters:** Propriedade de arquivos deve ser consistente
- **Reinício de serviços:** Apache precisa ser reiniciado após mudanças

### Boas Práticas
- **Backup antes de mudanças:** Sempre fazer backup antes de modificar arquivos
- **Teste incremental:** Validar após cada mudança significativa
- **Documentação:** Registrar configurações que funcionam
- **Segurança:** Manter permissões adequadas (640 para wp-config.php)

## 🔗 Recursos Adicionais

### Documentação WordPress
- [WordPress Multisite Network](https://wordpress.org/support/article/create-a-network/)
- [WordPress File Permissions](https://wordpress.org/support/article/changing-file-permissions/)
- [WordPress Debugging](https://wordpress.org/support/article/debugging-in-wordpress/)

### Amazon Lightsail
- [Lightsail WordPress](https://aws.amazon.com/lightsail/features/wordpress/)
- [Bitnami WordPress](https://bitnami.com/stack/wordpress)
- [Lightsail SSH Access](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/amazon-lightsail-connect-to-your-instance-virtual-private-server)

### Ferramentas Úteis
- [nip.io](https://nip.io/) - DNS dinâmico para testes
- [Apache Rewrite Rules](https://httpd.apache.org/docs/current/rewrite/intro.html)
- [Linux File Permissions](https://www.guru99.com/file-permissions.html)

## ✅ Critérios de Sucesso

### Task 1 - Configuração Multisite
- [ ] Multisite ativado no wp-config.php
- [ ] Rede WordPress configurada com subdomínios
- [ ] Site secundário criado na rede
- [ ] Ambos os sites acessíveis via navegador
- [ ] Validação no Jam marcada como "Completed"

### Task 2 - Correção de Permissões
- [ ] Erro 500 identificado e diagnosticado
- [ ] Logs do Apache analisados
- [ ] Permissões do wp-includes corrigidas
- [ ] Ownership completo dos arquivos ajustado
- [ ] Ambos os sites funcionando corretamente
- [ ] Validação no Jam marcada como "Completed"

## 🚨 Troubleshooting Comum

### Erro 500 Persistent
- Verificar se Apache foi reiniciado após mudanças
- Confirmar que todas as permissões estão corretas
- Verificar se wp-config.php não tem erros de sintaxe
- Analisar logs do Apache para erros específicos

### Site Secundário Não Carrega
- Confirmar que subdomínio está configurado corretamente
- Verificar se nip.io está resolvendo o domínio
- Testar acesso direto ao IP da instância
- Verificar se rewrite rules estão aplicadas

### Problemas de Permissões
- Executar comandos de correção de ownership
- Verificar se usuário bitnami tem acesso aos arquivos
- Confirmar permissões de diretórios pai (775)
- Reiniciar Apache após correções

---

**🎉 Boa sorte com o desafio!**

> **💭 Reflexão:** Este desafio combina conhecimento de WordPress, administração Linux e troubleshooting - habilidades essenciais para qualquer profissional que trabalha com hospedagem web e aplicações PHP. A capacidade de diagnosticar e resolver problemas de permissões é fundamental em ambientes de produção.
