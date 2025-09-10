# Task 2 – Amazon Athena Query Analysis

## 🎯 Objetivo
Utilizando o **Amazon Athena**, analisar o dataset `high_diamond_ranked_10min.csv` para descobrir **quantas vezes o time azul venceu** nas partidas ranqueadas.

## 📋 Contexto do Dataset

### Informações do Dataset:
- **Arquivo:** `high_diamond_ranked_10min.csv`
- **Localização:** `games-simple-query/ranked-games-s3`
- **Conteúdo:** Estatísticas dos **10 primeiros minutos** de partidas ranqueadas
- **Tabela:** `ranked_games_s3` (criada via query salva `CreateTableFromS3Data`)

### Estrutura dos Dados:
- **gameId:** Identificador único de cada partida
- **blueWins:** Resultado do time azul
  - `1` → **Vitória** do time azul
  - `0` → **Derrota** do time azul

## 🔧 Implementação da Solução

### 1️⃣ Preparação do Ambiente
**Localização:** Amazon Athena Console

**Ação:**
- Execute a query salva `CreateTableFromS3Data` para criar a tabela
- Verifique se a tabela `ranked_games_s3` foi criada corretamente
- Confirme acesso aos dados do S3

### 2️⃣ Query SQL para Análise
**Objetivo:** Contar vitórias do time azul

```sql
SELECT COUNT(*) AS blue_wins
FROM task2db.ranked_games
WHERE blueWins = 1;

```

### 3️⃣ Execução e Validação
**Passos:**
1. **Execute a query** no Amazon Athena Console
2. **Aguarde o resultado** (pode levar alguns segundos)
3. **Anote o número** retornado na coluna `blue_wins`
4. **Valide o resultado** verificando se faz sentido

## ✅ Critérios de Sucesso

- [ ] **Tabela criada** com sucesso via `CreateTableFromS3Data`
- [ ] **Query executada** sem erros de sintaxe
- [ ] **Resultado obtido** com número de vitórias do time azul
- [ ] **Resposta submetida** no campo correto do lab

## 📊 Análise da Query

### Explicação Técnica:
- **COUNT(*):** Conta todas as linhas que atendem à condição
- **WHERE blueWins = 1:** Filtra apenas partidas onde o time azul venceu
- **AS blue_wins:** Renomeia a coluna de resultado para clareza

### Interpretação do Resultado:
- O número retornado representa **total de vitórias** do time azul
- Cada linha do dataset = 1 partida única
- Resultado final = quantidade de partidas vencidas pelo time azul

## 🚨 Troubleshooting

### Problemas Comuns:

#### Erro: "Table not found"
- **Causa:** Tabela não foi criada ou nome incorreto
- **Solução:** Execute `CreateTableFromS3Data` primeiro

#### Erro: "Access denied"
- **Causa:** Permissões insuficientes para acessar S3
- **Solução:** Verifique IAM roles e políticas

#### Query não retorna resultado
- **Causa:** Dataset vazio ou filtro muito restritivo
- **Solução:** Teste com `SELECT COUNT(*) FROM ranked_games_s3` primeiro

### Validação de Resultado:
- **Faça sentido:** Número deve ser menor que total de partidas
- **Teste alternativo:** Execute `SELECT COUNT(*) FROM ranked_games_s3` para total
- **Verificação:** `blue_wins` deve ser ≤ total de partidas

## 📝 Instruções de Submissão

### Como Submeter a Resposta:
1. **Execute a query** no Amazon Athena
2. **Copie o número** da coluna `blue_wins`
3. **Cole no campo** "Enter answer here" do lab
4. **Clique em Submit** para finalizar

### ⚠️ Importante:
- **Use o número exato** retornado pela query
- **Não arredonde** ou modifique o resultado
- **Submeta apenas** o número, sem texto adicional

## 🎓 Conceitos Aprendidos

### 📊 Amazon Athena:
- **Query sem servidor** para análise de dados
- **Integração com S3** para datasets grandes
- **SQL padrão** para consultas familiares
- **Custo por query** executada

### 🔍 Análise de Dados:
- **COUNT()** para contagem de registros
- **WHERE** para filtragem de dados
- **Alias (AS)** para nomes de colunas claros
- **Validação** de resultados obtidos

## 🏆 Resultado Final

- ✅ **Query executada** com sucesso
- ✅ **Número de vitórias** do time azul identificado
- ✅ **Resposta submetida** no lab
- ✅ **Task 2 concluída** com sucesso

---

**💡 Reflexão:** Esta task demonstra como usar Amazon Athena para análise rápida de datasets grandes armazenados no S3, aplicando conceitos básicos de SQL para extrair insights específicos dos dados.
