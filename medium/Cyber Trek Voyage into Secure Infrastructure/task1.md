# Task 1: Access Control Lockdown Quest

**Pontos Possíveis:** 45  
**Penalidade por Dica:** 0  
**Pontos Disponíveis:** 45

## 🎯 Background

Sua organização está usando o Amazon CloudFront Distribution para servir conteúdo estático de um bucket Amazon S3. A equipe tentou restringir o acesso ao bucket Amazon S3 usando bucket policy, mas isso resultou em um erro "Access Denied" quando tentaram acessar o website usando o Domain name do Amazon CloudFront Distribution. Você precisa atualizar a política do bucket S3 para resolver o problema.

## 📋 Your Task

Como Cyber Adventurer, sua responsabilidade é resolver o problema e fortificar a fortaleza digital implementando controles de acesso rigorosos para o bucket S3 que abriga dados críticos. Seu objetivo é criar uma barreira impenetrável, permitindo que apenas a distribuição CloudFront especificada e autorizada acesse o valioso conteúdo do bucket Amazon S3, mantendo os intrusos afastados.

## 🚀 Getting Started

Use o botão **Open AWS Console** no topo da tela do desafio para abrir seu console AWS e obter acesso ao Amazon CloudFront Distribution e Amazon S3 Bucket.

## 📦 Inventory

- **Amazon CloudFront Distribution:** Consulte o Amazon CloudFront Distribution ID na seção Output Properties
- **Amazon S3 bucket:** O nome do Amazon S3 Bucket começa com `static-website-jam`

## 🛠️ Services You Should Use

- Amazon CloudFront
- Amazon S3 Bucket

## ✅ Task Validation

A tarefa será concluída automaticamente assim que você configurar a política correta de bucket Amazon S3 com least privilege. Além disso, você sempre pode verificar seu progresso pressionando o botão "Check my progress" na tela de detalhes do desafio.

---

## 🔍 Resolução Detalhada

### 🧩 Contexto do Problema

O site estático "Cyber Trek Voyage" é hospedado em um bucket Amazon S3 e distribuído globalmente através do Amazon CloudFront. Durante os testes, o site apresentava o erro `AccessDenied` ao ser acessado pelo domínio da distribuição CloudFront.

### ⚙️ Causa Raiz

- A política existente do bucket concedia `s3:GetObject` para o serviço `s3.amazonaws.com`, o que é incorreto
- Não havia nenhuma condição associando a permissão à ARN da distribuição CloudFront específica
- Como resultado, o CloudFront não conseguia recuperar os arquivos, retornando o erro Access Denied

### 🧠 Etapas da Solução

#### 1. Identificação dos Recursos

De acordo com os **Outputs da Challenge**:
- **CloudFront Distribution ID:** (exemplo: E2TUXQI3IFLTF6)
- **Nome do Bucket S3:** static-website-jam-XXXXXX

#### 2. Confirmação do Método de Acesso

No painel **CloudFront** → **Origins**, confirme que a distribuição utiliza **Origin Access Control (OAC)**, e não o modelo antigo OAI (Origin Access Identity).

#### 3. Criação de Política Segura para o Bucket

Aplique uma nova política de acesso mínima (least privilege), permitindo somente que a distribuição CloudFront (via OAC) realize a leitura dos objetos do bucket.

### 📝 Política Final Aplicada

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowCloudFrontOACOnly",
      "Effect": "Allow",
      "Principal": {
        "Service": "cloudfront.amazonaws.com"
      },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::static-website-jam-XXXXXX/*",
      "Condition": {
        "StringEquals": {
          "AWS:SourceArn": "arn:aws:cloudfront::<ACCOUNT_ID>:distribution/<DISTRIBUTION_ID>"
        }
      }
    },
    {
      "Sid": "DenyInsecureTransport",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::static-website-jam-XXXXXX/*",
      "Condition": {
        "Bool": {
          "aws:SecureTransport": "false"
        }
      }
    }
  ]
}
```

**⚠️ Lembre-se de substituir:**
- `static-website-jam-XXXXXX` pelo nome real do seu bucket
- `<ACCOUNT_ID>` pelo número da sua conta AWS (12 dígitos)
- `<DISTRIBUTION_ID>` pelo ID da sua distribuição CloudFront

### 🔧 Passo a Passo no Console

1. Vá para **S3** → selecione seu bucket `static-website-jam-*`
2. Aba **Permissions**
3. Role até **Bucket Policy** → clique em **Edit**
4. Cole a política acima (com as substituições corretas)
5. Clique em **Save changes**

### 🔐 Ajustes e Validações

| Etapa | Descrição | Status |
|-------|-----------|--------|
| Bloquear acesso público | "Block all public access" ativado | ✅ |
| Política pública | Nenhum acesso com "Principal": "*" | ✅ |
| Teste via domínio S3 | Retorna "Access Denied" | ✅ |
| Teste via CloudFront | Site carregando normalmente | ✅ |
| HTTPS obrigatório | Enforced via aws:SecureTransport | ✅ |
| Verificação na Challenge | "Check my progress" bem-sucedido | ✅ |

### 🔐 Resultado de Segurança

A nova configuração garante que:
- ✅ O bucket S3 permaneça totalmente privado
- ✅ Somente a distribuição CloudFront autorizada possa acessar os objetos
- ✅ Requisições públicas diretas ou sem HTTPS sejam negadas
- ✅ A infraestrutura siga as boas práticas de least privilege e segurança em trânsito (TLS) recomendadas pela AWS

### 🧾 Resumo Técnico

| Componente | Configuração | Status |
|------------|--------------|--------|
| S3 Bucket | static-website-jam-XXXXXX | Seguro |
| CloudFront Distribution | E2TUXQI3IFLTF6 | Autorizada |
| Método de Acesso | Origin Access Control (OAC) | Ativo |
| Acesso Público | Bloqueado | ✅ |
| HTTPS Obrigatório | Sim | ✅ |
| Validação do Desafio | Concluído com sucesso (45 pts) | ✅ |

## 🏁 Conclusão

✅ **Access Control Lockdown Quest concluída com sucesso.**

O site agora é entregue com segurança através do CloudFront, enquanto o bucket S3 permanece protegido contra acessos diretos ou não autorizados.

---

## 🔧 Troubleshooting

### Problema: Ainda recebo Access Denied via CloudFront
- Verifique se o ARN da distribuição está correto na bucket policy
- Confirme que o account ID está correto (12 dígitos)
- Verifique se OAC está configurado na origem do CloudFront

### Problema: Não sei meu Account ID
```bash
# Via AWS CLI
aws sts get-caller-identity --query Account --output text
```

### Problema: Bucket policy dá erro ao salvar
- Valide o JSON (use um validador online se necessário)
- Verifique se todas as aspas e vírgulas estão corretas
- Confirme que não há espaços ou caracteres extras
