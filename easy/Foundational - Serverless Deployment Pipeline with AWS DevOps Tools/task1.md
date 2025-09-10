# AWS Challenge – Task 3: CodeCommit + CodePipeline + Lambda

## Descrição
Pipeline Pioneers deseja automatizar o deploy de sua aplicação serverless escrita em **Node.js**, utilizando:
- **AWS CodeCommit** para versionamento do código.  
- **AWS CodePipeline** para CI/CD.  
- **AWS Lambda** como ambiente de execução.  

O repositório e o pipeline já foram criados previamente. A tarefa era subir os arquivos e garantir que o pipeline funcionasse corretamente.

---

## Passos Realizados

1. Acessar o **AWS CodeCommit** e localizar o repositório:
   - Nome: `ServerlessApplicationRepo`.  

2. Fazer upload dos arquivos obrigatórios no **branch main**:
   - `index.js`  
   - `buildspec.yml`  

3. Acessar o **AWS CodePipeline** e verificar o pipeline:
   - Nome: `ServerlessDeploymentPipeline`.  

4. Problema identificado:  
   - O pipeline estava configurado para buscar código no branch `develop`.  
   - O repositório possuía apenas o branch `main`.  
   - Resultado: falha na execução com erro *“no branch named develop was found”*.  

5. Correção aplicada:  
   - Alterado o branch de origem no **Source stage** do pipeline de `develop` para `main`.  
   - Salvas as alterações.  
   - Executado **Release change** para disparar o pipeline novamente.  

6. Resultado:  
   - O pipeline rodou com sucesso.  
   - Os arquivos do repositório foram processados.  
   - O deploy no **AWS Lambda** foi concluído.  

---

## Critérios de Validação
- Arquivos `index.js` e `buildspec.yml` no CodeCommit (`main`). ✅  
- Pipeline `ServerlessDeploymentPipeline` em execução bem-sucedida. ✅  
- Deploy no AWS
