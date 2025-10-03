Task 3: Watch for pirates
Possible Points
16
Clue Penalty
0
Points Available
16
Check my progress

Task and Clues
Submit Answer
In this task, you will create a pirate user and grant all access on the table. And then query the table to validate the results.

STEP1: Log back in as awsuser or SET SESSION AUTHORIZATION 'awsuser';

STEP2: Create a user with name 'pirate' and grant all access on sailor table.

Hint: GRANT ALL ON sailors TO pirate;

STEP3: Log in as pirate or SET SESSION AUTHORIZATION 'pirate';

Qn: How many rows pirate can see from sailor table?

[Optional] You can query following system tables to monitor the security policies.

SVV_RLS_RELATION - view a list of all tables that are RLS-protected
SVV_RLS_POLICY - view a list of all row-level security policies created on the Amazon Redshift cluster.
SVV_RLS_ATTACHED_POLICY - view a list of all tables and users that have one or more row-level security policies attached.
SVV_RLS_APPLIED_POLICY - view the application of RLS policies on queries that reference RLS-protected tables.

Documentação – Challenge Secure the Sailors (Task 3)
🎯 Objetivo

Criar um usuário “pirate” e testar o impacto das políticas de Row Level Security (RLS). A intenção é mostrar que, mesmo com GRANT ALL, o usuário não consegue ver nenhuma linha porque não possui nenhuma policy de RLS anexada.

🔹 Ambiente

Workgroup: seabird-wg

Namespace: seabird-nm

Database: dev

Tabela: public.sailors (já protegida com RLS desde a Task 2)

🔹 Etapas planejadas
1. Criar o usuário pirate
CREATE USER pirate PASSWORD 'Pirate_P@ssw0rd!';

2. Garantir permissões de acesso
GRANT USAGE ON SCHEMA public TO pirate;
GRANT ALL ON TABLE public.sailors TO pirate;

3. Testar acesso
SET SESSION AUTHORIZATION 'pirate';

SELECT COUNT(*) FROM public.sailors;

🔹 Lógica de Segurança

O usuário pirate recebeu permissão total na tabela (GRANT ALL).

Contudo, a tabela sailors está protegida por RLS (habilitada na Task 2).

Em Redshift:

“Quando RLS está habilitado, qualquer usuário que não tenha uma policy anexada vê zero linhas, independentemente dos privilégios de SELECT/ALL.”

Como não anexamos nenhuma policy ao pirate, o resultado esperado para SELECT COUNT(*) é 0.

✅ Resposta da Task 3

O usuário pirate vê 0 linhas na tabela sailors.

🔹 Observação

Se fosse necessário validar tecnicamente:

SVV_RLS_RELATION mostra que sailors tem RLS habilitado.

SVV_RLS_ATTACHED_POLICY confirmaria que não há policies vinculadas ao usuário pirate.

Portanto, o comportamento de retorno 0 linhas é garantido pela configuração de RLS.