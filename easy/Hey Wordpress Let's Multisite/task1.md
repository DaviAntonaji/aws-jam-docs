AWS Jam Lab – WordPress Multisite no Amazon Lightsail
Objetivo

Configurar um segundo site WordPress na mesma instância Lightsail existente, sem impactar o site original, utilizando o recurso WordPress Multisite.

Inventário

Instância Lightsail: PublicWebsite

IP público: 3.230.0.108

WordPress inicial já instalado (Bitnami stack)

Passos Realizados
1. Conexão à instância

Acessado o console AWS → Lightsail → PublicWebsite → SSH.

2. Recuperação de credenciais do WordPress

No terminal SSH:

sudo cat /home/bitnami/bitnami_application_password


Usuário padrão: user

Senha: (valor exibido pelo comando acima)

Essas credenciais foram usadas para login no WordPress Admin (via link PublicWebsiteWordPressAdminURL fornecido pelo lab).

3. Ativação do suporte Multisite

Editado o arquivo wp-config.php:

sudo nano /opt/bitnami/wordpress/wp-config.php


Antes da linha /* That's all, stop editing! */, adicionada:

define('WP_ALLOW_MULTISITE', true);


Salvo e reiniciado acesso ao WordPress Admin.

4. Criação da rede WordPress

Em WordPress Admin → Tools → Network Setup:

Selecionado Sub-domains.

Network Title: Marketing Site

Admin Email: user@example.com

Clicado em Install.

O WordPress exibiu blocos de configuração para aplicar manualmente.

5. Ajustes adicionais no servidor
(A) wp-config.php

Adicionadas as linhas fornecidas pelo WordPress:

define('MULTISITE', true);
define('SUBDOMAIN_INSTALL', true);
define('DOMAIN_CURRENT_SITE', '3.230.0.108.nip.io');
define('PATH_CURRENT_SITE', '/');
define('SITE_ID_CURRENT_SITE', 1);
define('BLOG_ID_CURRENT_SITE', 1);

(B) htaccess.conf

Editado o arquivo do Bitnami:

sudo nano /opt/bitnami/wordpress/htaccess.conf


Substituído o bloco de regras pelo sugerido no Network Setup, por exemplo:

RewriteEngine On
RewriteBase /
RewriteRule ^index\.php$ - [L]
RewriteRule ^wp-admin$ wp-admin/ [R=301,L]
RewriteCond %{REQUEST_FILENAME} -f [OR]
RewriteCond %{REQUEST_FILENAME} -d
RewriteRule ^ - [L]
RewriteRule . index.php [L]

(C) Reinício do Apache
sudo /opt/bitnami/ctlscript.sh restart apache

6. Criação do site secundário

No WordPress Admin → My Sites → Network Admin → Sites → Add New:

Site Address (URL): marketing-site

Site Title: Marketing Site

Admin Email: user@example.com

Clicado em Add Site.

7. Validação

Acessado no navegador:

http://marketing-site.3.230.0.108.nip.io


O site secundário carregou corretamente.

Desafio marcado como Completed no painel do Jam Lab.

Notas Importantes

O domínio nip.io converte automaticamente <subdomínio>.<IP>.nip.io para o IP informado, sem necessidade de configuração DNS extra.

Não foi necessário criar uma nova instância Lightsail; o Multisite aproveita a mesma instalação existente.

O erro de ValidatePolicy visto em tarefas anteriores não impacta aqui.