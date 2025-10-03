Task 2: Secure sailors
Possible Points
40
Clue Penalty
0
Points Available
0

Task and Clues
In this task, you will lock down column level and row level access as per security requirements.

STEP1: Apply column level secruity as described below.

captain: grant select access to all columns crew: grant select access to only on s_name,s_segment and s_dietrestrictions columns finance: grant select access to only on s_name,s_address and s_acctbal columns

After completing this step, login as different users and check if only required columns are shown in result as per their role.

STEP2: Apply row level secruity as described below.

captain: See details of sailors currently onboarded and historical sailors crew: See details of only currently onboarded sailors. finance: See details of sailors currently onboarded and historical sailors

Hint:

Create two RLS polcies. One which provide access to all rows and another one which provide access to rows with s_onboard=true.
Attach all row access policy to captain and finance roles. And attach restricted rows policy to crew role.
STEP3: Turn on RLS protection on the sailors table

Qn: How many rows cuddy is seeing when he ran following query. Input the answer in text box.

select count(*) from sailors;
[optional] Are you curious to know how many rows cashking is seeing when he ran same query?



Documentação – Challenge Secure the Sailors (Task 2)
🎯 Objetivo

Aplicar Column Level Security (CLS) e Row Level Security (RLS) na tabela sailors, conforme requisitos de cada função (captain, crew, finance), e responder à pergunta:

Quantas linhas o usuário cuddy (crew) enxerga ao rodar SELECT COUNT(*) FROM sailors;?

🔹 Ambiente

Workgroup: seabird-wg

Namespace: seabird-nm

Database: dev

Tabela: public.sailors (já populada a partir do Task 1)

Roles criadas: captain, crew, finance

Usuários: cook (captain), cuddy (crew), cashking (finance)

🔹 Etapas executadas
1. Remoção de permissões herdadas
REVOKE ALL ON TABLE public.sailors FROM PUBLIC;

2. Definição de acesso por colunas
-- captain: todas as colunas
GRANT SELECT ON TABLE public.sailors TO ROLE captain;

-- crew: apenas nome, segmento e dieta
GRANT SELECT (s_name, s_segment, s_dietrestrictions)
ON TABLE public.sailors TO ROLE crew;

-- finance: apenas nome, endereço e saldo
GRANT SELECT (s_name, s_address, s_acctbal)
ON TABLE public.sailors TO ROLE finance;

3. Definição de acesso por linhas

Criadas duas políticas de RLS:

-- Todas as linhas (captain e finance)
CREATE RLS POLICY rls_all_rows
WITH (s_onboard BOOLEAN) AS s
USING (TRUE);

-- Apenas onboard (crew)
CREATE RLS POLICY rls_only_onboard
WITH (s_onboard BOOLEAN) AS s
USING (s.s_onboard = TRUE);


Vinculação às roles:

ATTACH RLS POLICY rls_all_rows     ON TABLE public.sailors TO ROLE captain;
ATTACH RLS POLICY rls_all_rows     ON TABLE public.sailors TO ROLE finance;
ATTACH RLS POLICY rls_only_onboard ON TABLE public.sailors TO ROLE crew;

ALTER TABLE public.sailors ENABLE ROW LEVEL SECURITY;

🔹 Validação

Como o ambiente não permite conexão direta com cuddy/cook/cashking, validamos com awsuser rodando a query de contagem:

SELECT
  COUNT(*) AS total_rows,
  COUNT(CASE WHEN s_onboard THEN 1 END) AS total_onboard
FROM public.sailors;


total_rows = número de sailors no banco (onboard + históricos).

total_onboard = número de sailors atualmente embarcados.

Resultado esperado por role

captain (cook): vê total_rows e todas as colunas.

crew (cuddy): vê apenas total_onboard e só 3 colunas (s_name, s_segment, s_dietrestrictions).

finance (cashking): vê total_rows e só 3 colunas (s_name, s_address, s_acctbal).

✅ Resposta da Task 2

Cuddy (crew) ao rodar SELECT COUNT(*) FROM sailors; enxerga:
total_onboard (somente os sailors embarcados).