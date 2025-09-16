# 📌 Task 1: Preparar o Artefato de Deploy para o CodeDeploy

## 🎯 Objetivo

Criar um pacote `source.zip` pronto para o AWS CodeDeploy que:
- Copie todos os arquivos da aplicação para **`/opt/codedeploy/`** nas instâncias EC2
- Execute os três *lifecycle hooks* exigidos: **ApplicationStop**, **BeforeInstall**, **ApplicationStart**
- **NÃO utilize** o hook **Install** (gerenciado pelo CodeDeploy)

## 📁 Estrutura Final do ZIP

O arquivo `source.zip` final deve ter exatamente esta estrutura:

```
source.zip
├── appspec.yml          ← arquivo de especificação na raiz
└── deploy/              ← pasta com os scripts
    ├── applicationstop.sh
    ├── before.sh
    ├── applicationstart.sh
    └── index.html
```

> **⚠️ Importante:** O `appspec.yml` precisa estar **na raiz do ZIP**, no mesmo nível da pasta `deploy/`.

## 📄 Conteúdo do `appspec.yml`

### Arquivo Completo
```yaml
# AWS CodeDeploy Application Specification File
version: 0.0
os: linux
files:
  - source: /
    destination: /opt/codedeploy/
hooks:
  ApplicationStop:
    - location: deploy/applicationstop.sh
      timeout: 60
      runas: root
  BeforeInstall:
    - location: deploy/before.sh
      timeout: 300
      runas: root
  # INSTALL IS USED BY CODEDEPLOY SERVICE - DO NOT USE
  ApplicationStart:
    - location: deploy/applicationstart.sh
      timeout: 90
      runas: root
```

### Explicação das Seções

#### **version / os**
- **Obrigatórios** para deployments em EC2/On-Premises
- **version**: 0.0 (versão da especificação)
- **os**: linux (sistema operacional de destino)

#### **files**
- Instrui o CodeDeploy a copiar todo o conteúdo do pacote
- **source**: `/` (todos os arquivos do ZIP)
- **destination**: `/opt/codedeploy/` (diretório de destino nas instâncias)

#### **hooks**
Define os scripts a serem executados em cada etapa:

| Hook | Função | Script | Timeout |
|------|--------|--------|---------|
| **ApplicationStop** | Encerra o serviço/servidor antes do novo deploy | `applicationstop.sh` | 60s |
| **BeforeInstall** | Executa passos de preparação antes da instalação | `before.sh` | 300s |
| **ApplicationStart** | Inicia a aplicação após a cópia dos arquivos | `applicationstart.sh` | 90s |

> **💡 Nota:** O comentário `# INSTALL IS USED BY CODEDEPLOY SERVICE - DO NOT USE` é apenas informativo, indicando para não criar um hook chamado Install.

## 🛠️ Passo a Passo Executado

### 1. Download do Código-Fonte
- Baixar o `source.zip` fornecido na plataforma do desafio

### 2. Descompactação
- Extrair o ZIP para uma pasta local
- Verificar a estrutura de arquivos

### 3. Criação do `appspec.yml`
- Criar um novo arquivo `appspec.yml` (nome em minúsculo) na raiz da pasta
- Usar o conteúdo mostrado acima

### 4. Verificação da Estrutura
Garantir que o ZIP final contém:
- ✅ `appspec.yml` na raiz
- ✅ Pasta `deploy/` com os scripts `.sh` e `index.html`

### 5. Recompactação
- Compactar novamente (formato ZIP, nome `source.zip`)
- **Não alterar** a estrutura de diretórios

### 6. Upload para o S3
- Subir o `source.zip` final para o bucket S3 informado no desafio

## ✅ Resultado

- ✅ **Artefato criado** com estrutura correta
- ✅ **appspec.yml válido** configurado
- ✅ **Lifecycle hooks** definidos adequadamente
- ✅ **Upload para S3** realizado com sucesso
- ✅ **Pronto para deployment** na Task 2

## 🔗 Próximos Passos

Com o artefato preparado, continue para a [Task 2](./task2.md) para criar a aplicação e deployment group no CodeDeploy.

