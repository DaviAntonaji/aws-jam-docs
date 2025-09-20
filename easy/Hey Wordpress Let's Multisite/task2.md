Task 2 – Erro 500 (What went wrong?)
Observação inicial

Após ativar o Multisite, acessar qualquer site retornava 500 Internal Server Error.

Erro confirmado tanto em http://<IP> quanto em http://marketing-site.<IP>.nip.io.

Investigação

Logs do Apache

sudo tail /opt/bitnami/apache/logs/error_log


Saída:

PHP Warning:  require(/opt/bitnami/wordpress/wp-includes/version.php): Failed to open stream: Permission denied
PHP Fatal error:  Uncaught Error: Failed opening required '/opt/bitnami/wordpress/wp-includes/version.php'


→ Causa: diretório wp-includes sem permissões adequadas.

Checagem de permissões

ls -l /opt/bitnami/wordpress | grep wp-includes


Saída:

d--------- 30 bitnami daemon 12288 Jun 20 07:59 wp-includes


→ Diretório estava com 000 (sem permissão alguma).

Solução indicada pela dica do lab

Ajustar permissões do diretório e reiniciar o Apache:

sudo chmod 775 /opt/bitnami/wordpress/wp-includes
sudo /opt/bitnami/ctlscript.sh restart apache

Passos adicionais aplicados por nós (para ficar 100% correto)

Resetar donos e permissões de forma consistente:

sudo chown -R bitnami:daemon /opt/bitnami/wordpress
sudo find /opt/bitnami/wordpress -type d -exec chmod 775 {} \;
sudo find /opt/bitnami/wordpress -type f -exec chmod 664 {} \;
sudo chmod 640 /opt/bitnami/wordpress/wp-config.php


Garantir travessia nos diretórios-pai (importante em Bitnami):

sudo chmod 775 /opt /opt/bitnami /opt/bitnami/wordpress
sudo test -d /bitnami && sudo chmod 775 /bitnami
sudo test -d /bitnami/wordpress && sudo chmod 775 /bitnami/wordpress

Validação

Acessado novamente:

http://<PUBLIC-IP>

http://marketing-site.<PUBLIC-IP>.nip.io

Sites carregaram corretamente.

Task 2 marcada como Completed.
 investigado erro 500 → diretório wp-includes com permissão 000.

Aplicada a solução do lab (chmod 775 wp-includes).

Aplicados ajustes adicionais de donos e permissões para corrigir tudo de forma consistente.

Resultado: ambos os sites ativos e validador do Jam concluído. ✅