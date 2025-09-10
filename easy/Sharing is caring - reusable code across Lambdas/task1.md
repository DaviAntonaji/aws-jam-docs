# TASK 1 — Passo a passo (Console)

## Objetivo
Criar um Layer a partir do ZIP no S3 e anexar às duas funções.

## Pré-requisitos do seu lib (dados do enunciado)

- **Runtime:** `nodejs22.x`
- **Arquitetura:** `x86_64`
- **S3:** `s3://aws-jam-challenge-resources-{REPLACE_ME_AWS_REGION}/lambda-layers-shared-code/task-one/layer-task-one.zip`

> **Importante:** Substitua `{REPLACE_ME_AWS_REGION}` pela região onde suas Lambdas estão (ex.: `us-east-1`). Confira no topo direito do Console.

## 1) Criar o Layer

1. Abra **AWS Console** → **Lambda**
2. No menu esquerdo, clique em **Layers** → **Create layer**
3. **Name:** `tattooine-common` (ou algo nesse padrão)
4. Em **Code entry type**, escolha **Upload a file from Amazon S3**
5. Em **S3 link**, cole o URI com a região correta, por ex.:
   ```
   s3://aws-jam-challenge-resources-us-east-1/lambda-layers-shared-code/task-one/layer-task-one.zip
   ```
6. **Compatible architectures:** marque `x86_64`
7. **Compatible runtimes:** selecione **Node.js 22.x** (`nodejs22.x`)
8. Clique **Create**

> **Resultado:** Isso publica a versão 1 (ou a próxima) do layer. **Guarde o ARN exibido.**

### ⚠️ Observação importante sobre estrutura
Para Node, o ZIP do layer deve conter o lib dentro de `nodejs/node_modules/<seu-pacote>`. O ZIP fornecido pelo lab já está no formato correto.

## 2) Anexar o Layer às funções

Para cada função (faça nas duas):

### Funções alvo:
- `LabStack-prewarm-…-ChallengeFunctionOne-…`
- `LabStack-prewarm-…-ChallengeFunctionTwo-…`

### Passos:
1. Vá em **Lambda** → **Functions** e abra uma das funções acima
2. Na página da função, ache a seção **Layers** (no card "Code" ou na área "Designer") e clique **Add a layer**
3. Selecione **Custom layers** → escolha `tattooine-common`
4. Em **Version**, selecione a versão publicada agora (ex.: `1`)
5. Clique **Add** e depois **Deploy** (se aparecer)
6. Repita para a segunda função

### 💡 Dica importante
Mantenha as funções com **Runtime Node.js 22.x** e **Architecture x86_64** (em Configuration → Environment → General configuration). Se a função estiver em `arm64`, o layer não será compatível.

## 3) Testar

1. Em cada função, clique **Test** com um evento simples
2. Se tudo ok, o erro `Runtime.ImportModuleError` desaparece
3. Verifique os logs em **Monitor** → **Logs** (CloudWatch) caso precise depurar