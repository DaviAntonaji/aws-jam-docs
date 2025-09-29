# Missing Front-End Challenge

## Visão Geral

Você trabalha para uma agência de inteligência governamental secreta chamada AnyCompany-GDI (Global Defense Initiative). Um algoritmo de computador avançado foi desenvolvido por operativos internos que encontrará e retornará as coordenadas criptografadas da localização de um grupo de atores de ameaça conhecido. 

As localizações descobertas são tipicamente geradas e retornadas por este algoritmo após um operativo navegar para uma URL web específica. No entanto, após um recente ataque de ator de ameaça ao próprio GDI, o front-end deste sistema foi destruído! 

Você foi encarregado de recriar uma solução de front-end para que o algoritmo possa ser executado novamente e a importante saída de localização possa ser acessada.

> **Nota:** Nenhum desenvolvimento web sofisticado ou programação é necessária para este desafio. Uma forma simples de invocar a função lambda via uma URL web é tudo que é necessário para o sucesso aqui.

## Contexto

Para que as localizações dos grupos de atores de ameaça sejam descobertas, a máquina de coordenadas deve ser consertada. Durante o último ataque ao GDI, a porção da URL web da máquina foi destruída. É imperativo que a URL de acesso web front-end para a invocação do algoritmo seja restaurada antes que os atores de ameaça possam atacar novamente.

## Sua Tarefa

Uma função lambda chamada `bad-guy-finder` já está configurada e pronta para ser invocada. Sua tarefa é criar o "invocador" para fazer esta função executar e retornar a string de saída necessária. 

Você não será capaz de testar a função. A única forma de fazer a função retornar a resposta será criar e utilizar a opção de invocação correta. Este "invocador" deve permitir que Alice, a analista principal do GDI, navegue para uma URL web específica para obter a saída da função.

Nenhuma alteração/adição ao código da função lambda em si é necessária para a conclusão desta tarefa. Por favor, ignore todas as outras funções lambda além de "bad-guy-finder" pois elas devem ser deixadas em paz para esta tarefa.

## Inventário

- **bad-guy-finder lambda function** - Esta é a função lambda "algoritmo de localização de ator de ameaça" fornecida.

## Primeiros Passos

1. Acesse o console AWS para verificar a função `bad-guy-finder` e ver se algo está atualmente a invocando ou não.

## Dicas

- Funções Lambda podem ser invocadas de muitas formas diferentes.
- Para esta tarefa existem muitas maneiras de obter a string de resposta, você precisará configurar um trigger frontend.
- Um trigger de função lambda pode ser criado diretamente da própria função lambda ou da seção de recursos de trigger específica dentro do console AWS.
- Você deve agora ver um item de trigger adicionado na janela do designer do console da função lambda.
- Este trigger tem uma URL de endpoint da API que pode ser acessada para obter a string de resposta.
- Invoke a Lambda usando o trigger para completar o desafio.

## Serviços que Você Deve Usar

- AWS Lambda
- Amazon API Gateway
- Application Load Balancer (ALB)

## Validação da Tarefa

Esta tarefa será automaticamente marcada como concluída quando:

- Você for capaz de acessar a string de saída da função lambda através de uma URL web que você criou.
- Esta string representa as coordenadas criptografadas para uma localização de grupo de ator de ameaça.

Além disso, você pode sempre verificar seu progresso clicando no botão "Check my progress" na tela de Detalhes do Desafio.

## Solução

### Método 1: Function URL (Mais Simples)

1. **Console → AWS Lambda → abra `bad-guy-finder`**

2. **No menu lateral clique em "Function URL"** (ou "Create function URL")

3. **Configure:**
   - **Auth type:** `NONE` (para resposta pública; se preferir, escolha `AWS_IAM` e faça chamadas autenticadas)
   - **(Opcional)** Habilite CORS se Alice for abrir no browser

4. **Clique "Create"**

5. **Ao criar, o console mostrará a Function URL** — algo como:
   ```
   https://<random-id>.lambda-url.<region>.on.aws/
   ```

6. **Acesse a URL no navegador** para obter a string de coordenadas criptografadas

### Método 2: API Gateway (Alternativo)

Se preferir usar API Gateway:

1. **Console → Amazon API Gateway → Create API**

2. **Escolha "REST API" → Build**

3. **Configure:**
   - Protocol: REST
   - Create new API: New API
   - API name: `bad-guy-finder-api`
   - Description: `API para invocar bad-guy-finder lambda`

4. **Crie um Resource e Method:**
   - Clique em "Actions" → "Create Resource"
   - Resource Name: `coordinates`
   - Clique "Create Resource"
   - Selecione o resource → "Actions" → "Create Method" → "GET"

5. **Configure a integração:**
   - Integration type: Lambda Function
   - Lambda Function: `bad-guy-finder`
   - Use Lambda Proxy integration: ✓

6. **Deploy a API:**
   - "Actions" → "Deploy API"
   - Deployment stage: `prod`
   - Deploy

7. **Use a URL de invocação** gerada

## Conceitos Importantes

### Function URL vs API Gateway

- **Function URL:** Mais simples, ideal para casos de uso simples como este
- **API Gateway:** Mais flexível, permite autenticação, rate limiting, transformações, etc.

### Autenticação

- **NONE:** Permite acesso público (ideal para este desafio)
- **AWS_IAM:** Requer credenciais AWS para acesso

### CORS

Se você planeja acessar a função de um navegador web, habilite CORS para evitar problemas de política de origem cruzada.

## Resultado Esperado

Após configurar corretamente o trigger, ao acessar a URL gerada, você deve receber uma string contendo as coordenadas criptografadas do grupo de atores de ameaça.
