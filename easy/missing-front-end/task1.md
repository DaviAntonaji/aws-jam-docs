# Missing Front-End Challenge - Task 1

## Objetivo

Criar um front-end para invocar a função Lambda `bad-guy-finder` que retorna coordenadas criptografadas de grupos de ameaça.

## Contexto

A agência AnyCompany-GDI (Global Defense Initiative) foi atacada e o front-end do sistema de localização de ameaças foi destruído. Você precisa restaurar o acesso web para invocar a função Lambda `bad-guy-finder`.

## Tarefa

- **Função Lambda:** `bad-guy-finder` (já configurada)
- **Objetivo:** Criar um "invocador" web para executar a função
- **Resultado:** String com coordenadas criptografadas

## Solução Passo a Passo

### Método 1: Function URL (Recomendado)

1. **Acesse o Console AWS Lambda**
   - Navegue até a função `bad-guy-finder`

2. **Criar Function URL**
   - No menu lateral, clique em **"Function URL"**
   - Clique em **"Create function URL"**

3. **Configuração**
   ```
   Auth type: NONE
   CORS: Habilitado (se necessário para browser)
   ```

4. **Criar e Obter URL**
   - Clique em **"Create"**
   - Copie a URL gerada (formato: `https://<random-id>.lambda-url.<region>.on.aws/`)

5. **Testar**
   - Acesse a URL no navegador
   - Deve retornar as coordenadas criptografadas

### Método 2: API Gateway (Alternativo)

1. **Criar API Gateway**
   - Console → API Gateway → Create API → REST API

2. **Configurar Endpoint**
   - Create Resource: `/coordinates`
   - Create Method: `GET`
   - Integration: Lambda Function (`bad-guy-finder`)

3. **Deploy**
   - Deploy API → Stage: `prod`

4. **Usar URL de Invocação**

## Validação

✅ **Sucesso quando:** Você consegue acessar a string de coordenadas através de uma URL web que você criou.

## Serviços Utilizados

- AWS Lambda
- Amazon API Gateway (opcional)
- Function URL (recomendado)

## Dicas Importantes

- Function URL é mais simples para casos de uso básicos
- Auth type NONE permite acesso público
- Habilite CORS se acessando via navegador
- Não modifique o código da função Lambda
- Ignore outras funções Lambda no ambiente
