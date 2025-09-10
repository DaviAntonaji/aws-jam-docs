# TASK 2 — Passo a passo (Console)

## Objetivo
Publicar uma nova versão do Layer e fazer deploy canary em apenas uma função para testar a nova versão.

## 1) Publicar nova versão do Layer

1. **AWS Console** → **Lambda** → menu esquerdo **Layers**
2. Clique no seu layer `tattooine-common`
3. Botão **Create version**
4. **Code entry type:** `Upload a file from Amazon S3`
5. **S3 link** (ajuste a região):
   ```
   s3://aws-jam-challenge-resources-{REPLACE_ME_AWS_REGION}/lambda-layers-shared-code/task-two/layer-task-two.zip
   ```
6. **Compatible architectures:** marque `x86_64`
7. **Compatible runtimes:** marque **Node.js 22.x**

> **💡 Dica de compatibilidade:** Como você rodou a função em Node.js 22.x, se o console permitir, adicione também Node.js 22.x para evitar warnings de compatibilidade. (Tecnicamente o layer é só código Node e costuma funcionar igual nas duas, mas marcar 22.x deixa tudo "verde".)

8. Clique **Create**

> **Resultado:** Isso cria a versão N do mesmo layer (imutável). **Copie o ARN com o sufixo `:N`.**

## 2) Anexar essa versão apenas a uma função

### Estratégia Canary
Escolha **apenas uma** função (ex.: `LabStack-prewarm-...-ChallengeFunctionOne-...`):

### Passos:
1. **Lambda** → **Functions** → abra a função escolhida
2. Seção **Layers** → **Add a layer**
3. **Custom layers** → escolha `tattooine-common`
4. **Version** → selecione a nova versão (N) que você acabou de publicar
5. **Add** e **Deploy** (se aparecer)

> **🎯 Estratégia:** A outra função continua na versão anterior do layer, então você faz canary sem impactar tudo.

## 3) Testar e validar

1. Na função atualizada, rode **Test**
2. Se der algo estranho, veja **Monitor** → **CloudWatch Logs**
3. Se precisar voltar, repita o "Add a layer" escolhendo a versão antiga do layer (ou remova/ajuste a ordem dos layers)

### 🔄 Rollback (se necessário)
- **Opção 1:** Voltar para versão anterior do layer
- **Opção 2:** Remover/adjustar a ordem dos layers
- **Opção 3:** Verificar logs detalhados no CloudWatch