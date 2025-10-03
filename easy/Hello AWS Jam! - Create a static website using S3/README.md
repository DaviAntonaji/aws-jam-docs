# 🌐 Hello AWS Jam! - Create a static website using S3

## 📋 Visão Geral

Sua empresa recentemente patenteou o **Jam Fuel** - uma forma revolucionária de usar bananas para abastecer automóveis! Porém, vocês não têm presença na web e precisam urgentemente de um site estático como página inicial até que o conteúdo web completo seja desenvolvido.

Este desafio ensina os conceitos fundamentais de hospedagem de sites estáticos usando Amazon S3, incluindo configuração de acesso público, políticas de bucket e hospedagem de websites.

## 🎯 Objetivos de Aprendizado

- ✅ Criar e configurar um bucket S3 para hospedagem de website estático
- ✅ Entender conceitos de Block Public Access e políticas de bucket
- ✅ Configurar hospedagem de website estático no S3
- ✅ Implementar políticas de acesso público para conteúdo web
- ✅ Criar e fazer upload de arquivos HTML básicos
- ✅ Testar e validar o website funcionando

## 🏗️ Arquitetura

```
Internet
    ↓
S3 Bucket (aws-jam-*)
├── index.html (página principal)
├── error.html (página de erro)
└── Bucket Policy (acesso público)
```

## 🛠️ Serviços Utilizados

- **Amazon S3** - Armazenamento e hospedagem de website estático
- **IAM** - Políticas de bucket para controle de acesso

## 📚 Conceitos Principais

### 1. **Hospedagem de Website Estático no S3**
- Configuração de Static Website Hosting
- Definição de documentos de índice e erro
- Endpoint público do website

### 2. **Controle de Acesso Público**
- Block Public Access settings
- Bucket policies para acesso público
- Princípio de least privilege

### 3. **Estrutura de Arquivos Web**
- Documento de índice (index.html)
- Documento de erro (error.html)
- Upload e organização de arquivos

## 🚀 Passo a Passo Detalhado

### 1. **Criar o Bucket S3**

```bash
# Nome do bucket deve começar com "aws-jam-"
# Exemplo: aws-jam-meusite-123
```

**Via Console AWS:**
1. Navegue para **S3** → **Create bucket**
2. **Bucket name:** `aws-jam-[seu-nome]-[número]`
3. **Region:** Escolha sua região preferida
4. Mantenha configurações padrão e clique **Create bucket**

### 2. **Habilitar Static Website Hosting**

1. Abra o bucket criado
2. Vá para a aba **Properties**
3. Role até **Static website hosting** → **Edit**
4. Marque **Enable**
5. **Hosting type:** `Host a static website`
6. **Index document:** `index.html`
7. **Error document:** `error.html`
8. **Save changes**

### 3. **Permitir Acesso Público**

1. Aba **Permissions** → **Block public access (bucket settings)** → **Edit**
2. **Desmarque todas as 4 opções:**
   - Block all public access
   - Block public access to buckets and objects granted through new access control lists (ACLs)
   - Block public access to buckets and objects granted through any access control lists (ACLs)
   - Block public access to buckets and objects granted through new public bucket or access point policies
3. Digite `confirm` para confirmar
4. **Save changes**

### 4. **Configurar Bucket Policy**

1. Ainda em **Permissions** → **Bucket policy** → **Edit**
2. Cole a política abaixo, **substituindo `Bucket-Name` pelo nome do seu bucket:**

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": ["s3:GetObject"],
      "Resource": ["arn:aws:s3:::Bucket-Name/*"]
    }
  ]
}
```

3. **Save changes**

### 5. **Criar e Fazer Upload do index.html**

Crie um arquivo `index.html` com o seguinte conteúdo:

```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Hello</title>
  </head>
  <body>
    <h1>Hello AWS Jam!</h1>
    <p>Now hosted on Amazon S3!</p>
  </body>
</html>
```

**Upload:**
1. Aba **Objects** → **Upload**
2. Selecione o arquivo `index.html`
3. **Upload**

### 6. **Criar e Fazer Upload do error.html**

Crie um arquivo `error.html` com o seguinte conteúdo:

```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Error</title>
  </head>
  <body>
    <h1>You have an Error :(</h1>
    <p>UGH!</p>
  </body>
</html>
```

**Upload:**
1. Aba **Objects** → **Upload**
2. Selecione o arquivo `error.html`
3. **Upload**

### 7. **Testar o Website**

1. Aba **Properties** → seção **Static website hosting**
2. Copie o **Bucket website endpoint** (formato: `http://aws-jam-meusite-123.s3-website-<região>.amazonaws.com`)
3. Abra a URL no navegador
4. Você deve ver a página "Hello AWS Jam!"

## 🔍 Validação

### Critérios de Sucesso
- [ ] Bucket criado com nome começando em "aws-jam-"
- [ ] Static website hosting habilitado
- [ ] Block public access desabilitado
- [ ] Bucket policy configurada corretamente
- [ ] Arquivos index.html e error.html carregados
- [ ] Website acessível via endpoint público
- [ ] Página principal exibe "Hello AWS Jam!"

### Teste de Validação
1. Use o **Bucket website endpoint** na seção de validação do challenge builder
2. O script automatizado verificará se todos os requisitos foram atendidos

## 🎓 Conceitos Aprendidos

### **Amazon S3 Static Website Hosting**
- Hospedagem de sites estáticos sem servidor
- Configuração de documentos de índice e erro
- Endpoints públicos automáticos

### **Segurança e Acesso Público**
- Block Public Access como mecanismo de segurança
- Bucket policies para controle granular de acesso
- Princípio de least privilege aplicado

### **Estrutura Web Básica**
- HTML5 semântico
- Documentos de índice e erro
- Organização de arquivos em buckets

## ⚠️ Pontos de Atenção

### **Nomenclatura do Bucket**
- **Obrigatório:** Nome deve começar com "aws-jam-"
- **Único:** Nomes de bucket devem ser globalmente únicos
- **Convenção:** Use formato `aws-jam-[seu-nome]-[número]`

### **Configuração de Segurança**
- **Cuidado:** Desabilitar Block Public Access expõe o bucket
- **Aplicação:** Use apenas para conteúdo público (websites)
- **Produção:** Considere CloudFront para melhor segurança

### **Propagação de Mudanças**
- **Tempo:** Mudanças podem levar alguns minutos para propagar
- **Cache:** Navegadores podem cachear páginas antigas
- **Teste:** Use modo incógnito para testes limpos

## 🔧 Troubleshooting Comum

### **Website não carrega**
- Verifique se Block Public Access está desabilitado
- Confirme se a bucket policy está correta
- Teste o endpoint diretamente

### **Erro 403 Forbidden**
- Verifique a bucket policy
- Confirme se o nome do bucket na policy está correto
- Verifique se Block Public Access está desabilitado

### **Página em branco**
- Confirme se index.html foi carregado corretamente
- Verifique se o nome do arquivo está exato (index.html)
- Teste acessando o arquivo diretamente

## 📖 Recursos Adicionais

### **Documentação AWS**
- [S3 Static Website Hosting](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html)
- [S3 Bucket Policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-policies.html)
- [Block Public Access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html)

### **Próximos Passos**
- **CloudFront:** Adicionar CDN para melhor performance
- **HTTPS:** Configurar certificados SSL/TLS
- **Custom Domain:** Usar domínio próprio
- **CI/CD:** Automatizar deploy de conteúdo

## 🏆 Critérios de Sucesso

- [ ] **Compreensão:** Entender conceitos de hospedagem estática
- [ ] **Implementação:** Configurar S3 corretamente
- [ ] **Segurança:** Aplicar políticas de acesso adequadas
- [ ] **Validação:** Website funcionando e acessível
- [ ] **Troubleshooting:** Resolver problemas comuns

---

**🎉 Parabéns!** Você criou seu primeiro website estático na AWS usando S3. Este é um dos conceitos mais fundamentais para hospedagem de conteúdo web na nuvem.

> **💡 Dica:** Este padrão é amplamente usado para hospedagem de SPAs (Single Page Applications), documentação, e sites de marketing. É a base para muitas arquiteturas serverless modernas.
