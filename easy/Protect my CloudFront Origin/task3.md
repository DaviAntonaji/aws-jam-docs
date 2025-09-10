# TASK 3 — Preparar Proteção L7 com Header Secreto (lado CloudFront)

## Contexto
Após restringir o acesso ao ALB na Camada 4 (SG permitindo apenas IPs de origem do CloudFront), qualquer distribuição CloudFront ainda pode alcançar o ALB.  
Para garantir que apenas **nossa** distribuição CloudFront seja aceita, iniciamos um controle da Camada 7 usando um **header secreto**. Nesta tarefa, configuramos o header no lado CloudFront (cliente).

## Resumo das Alterações
Configurado um Origin Custom Header fixo na distribuição CloudFront **Application User**:

- **Nome do header:** `x-from-cf`  
- **Valor do header:** `MySuperSecret`  
- (Sensível a maiúsculas/minúsculas)

## Passos
1. Abra **CloudFront** → **Distributions**
2. Selecione a distribuição **Application User**
3. Vá para **Origins**, selecione a origem que aponta para **ALB (Jam)**, clique **Edit**
4. Em **Origin custom headers**, clique **Add header** e configure:
   - **Name:** `x-from-cf`
   - **Value:** `MySuperSecret`
5. **Salve** e aguarde a conclusão do deployment

## Validação
- **ALB URL (HTTP direto)** permanece bloqueado (devido à regra SG L4)
- **Application User CloudFront URL** ainda funciona
- **Malicious User CloudFront URL** ainda pode funcionar **até** o ALB aplicar o header na Task 4

## Notas / Boas Práticas
- Em produção, a comunicação de origem deve ser **HTTPS** com certificados ACM e políticas rigorosas
- Valores de header secreto devem ser tratados como segredos (rotacionar se expostos)
