Secure the Sailors
Select a challenge below to get started.

Solve using:

Open AWS Console
>_AWS_CLI
Restart Challenge

Your challenge is ready!
All the best, and remember to have fun!


Overview
You are hired as game developer for "Sail to the Unknown" game. One of the functions is to secure sailor's data. You need to ensure the access is provided on a need to know basis, i.e users should only have access to the information that their job function requires.

Following is the metadata of the "sailors" table.

s_id: Unique ID; s_name: Name; s_address: Address (PII); s_phone: Phone (PII); s_acctbal: outstant account balance; s_segment: Sailor category - Platinum/Diamond/Emerald/Gold; s_dietrestrictions: Diet detail - Vegan/Kosher/non-vegeterian etc.; s_onboard: Onboard status. true - sailing on the ship, false - sailor offboarded or yet to onboard.

The game has the following roles with the data they need to access.

captain: access to all the data. crew: access to only sailor name, segment and diet restrictions. Only onboarded sailor information should be accessible. billing: access to only sailor's name, address and account balances for both onboard and historical sailors. anyone else: none

Task 1: All aboard
Possible Points
24
Clue Penalty
0
Points Available
24
Check my progress

Task and Clues
Submit Answer
In this task, you will create sailors table and load the data. Also you will create different roles and users as described in the challenge summary.

A Redshift Serverelss (seabird-wg) data warehouse was pre-created for you in the account.

Step1: Go to Redshift console. Expand left navigation pane and click on Query Editor V2.

Connect to Redshift Serverelss data store (seabird-wg) using "Database user name and password" option.

username: awsuser
password: Retrieve the password from RedshiftServerlessSecret-* secret in AWS Secrets Manager.
database: dev
Step2: Create sailors table and load it from s3://redshift-demos/data/gamejam/sailors/ using COPY command.

Refer CREATE TABLE for syntax. Following are the column names and data types to use.

s_id bigint,
s_name varchar(25),
s_address varchar(40),
s_phone varchar(15),
s_acctbal numeric(12,2),
s_segment varchar(10),
s_dietrestrictions varchar(20),
s_onboard boolean 
Step3: Create below users and roles.

User names: cook, cuddy, cashking Role names: captain, crew, finanace

Step4: Grant roles to users.

captain role to cook user
crew role to cuddy user
finance role to cashking user
Qn: How many sailors onboarded with diamond status on current voyage?

🎯 Objetivo

Configurar o ambiente Redshift Serverless para armazenar os dados dos marinheiros (sailors), criar usuários e roles de acordo com as funções definidas no enunciado e responder à primeira pergunta de negócio:

Quantos sailors Diamond estão onboard na viagem atual?

🔹 Ambiente

Workgroup: seabird-wg

Namespace: seabird-nm

Database: dev

User admin: awsuser (senha obtida via RedshiftServerlessSecret-* no Secrets Manager)

Redshift IAM Role: arn:aws:iam::370381165256:role/Redshiftgamesrole

🔹 Etapas executadas
1. Conexão ao Redshift

Acesso via Query Editor v2 no Console AWS.

Autenticação com user awsuser + senha recuperada no Secrets Manager.

2. Criação da tabela sailors
CREATE TABLE IF NOT EXISTS public.sailors (
  s_id               BIGINT,
  s_name             VARCHAR(25),
  s_address          VARCHAR(40),
  s_phone            VARCHAR(15),
  s_acctbal          NUMERIC(12,2),
  s_segment          VARCHAR(10),
  s_dietrestrictions VARCHAR(20),
  s_onboard          BOOLEAN
);

3. Carga dos dados do S3

Após alguns erros iniciais (ARN e formato), foi identificado que o dataset podia ser lido diretamente do bucket redshift-demos sem especificar formato.

TRUNCATE TABLE public.sailors;

COPY public.sailors (
  s_id,
  s_name,
  s_address,
  s_phone,
  s_acctbal,
  s_segment,
  s_dietrestrictions,
  s_onboard
)
FROM 's3://redshift-demos/data/gamejam/sailors'
IAM_ROLE 'arn:aws:iam::370381165256:role/Redshiftgamesrole';


✅ Resultado: dados carregados com sucesso.

4. Criação de usuários e roles
-- Roles
CREATE ROLE captain;
CREATE ROLE crew;
CREATE ROLE finance;

-- Users
CREATE USER cook     PASSWORD 'Cook_P@ssw0rd!';
CREATE USER cuddy    PASSWORD 'Cuddy_P@ssw0rd!';
CREATE USER cashking PASSWORD 'Cash_P@ssw0rd!';

-- Grants
GRANT ROLE captain TO USER cook;
GRANT ROLE crew    TO USER cuddy;
GRANT ROLE finance TO USER cashking;


(Nesta task só foi exigido criar usuários e roles; a aplicação de políticas de acesso por coluna/linha virá nas próximas tasks.)

5. Consulta para responder a pergunta
SELECT COUNT(*) AS diamond_onboard
FROM public.sailors
WHERE s_onboard = TRUE
  AND LOWER(TRIM(s_segment)) = 'diamond';

🔹 Próximos passos (Task 2 em diante)

Implementar Row-Level Security (RLS) e Column-Level Security de acordo com as necessidades:

captain: acesso total.

crew: apenas s_name, s_segment, s_dietrestrictions de quem está onboard.

finance: apenas s_name, s_address, s_acctbal (todos os sailors, inclusive offboard).

others: sem acesso.