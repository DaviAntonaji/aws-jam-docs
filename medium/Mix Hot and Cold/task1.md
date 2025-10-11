# Task 1: Turn on the Game 🎮

**Pontos Possíveis:** 15  
**Penalidade de Dica:** 0  
**Pontos Disponíveis:** 15  
**Check my progress:** Disponível

---

## 📖 Background

Nesta tarefa, você irá gerar dados de sessão de jogos usando o **Kinesis Data Generator** e transmiti-los para o **Kinesis Data Streams**.

O Kinesis Data Generator é uma ferramenta web que facilita a geração de dados de teste para streams do Kinesis, permitindo simular fluxos de dados em tempo real.

## 🎯 Sua Tarefa

Configurar o Kinesis Data Generator para enviar dados de sessões de jogos para um Kinesis Data Stream pré-criado.

## 📚 Passo a Passo

### 1️⃣ Acessar o Data Generator

**Ação:**
1. Vá para a seção **Output Properties** do desafio
2. Encontre a propriedade **DataGeneratorURL**
3. Clique no link ou copie e cole no navegador

### 2️⃣ Fazer Login

**Credenciais:**
```
Username: awsuser
Password: Awsuser123
```

**Ação:**
1. Insira as credenciais
2. Clique em **Sign In**

### 3️⃣ Configurar Região e Stream

**Região:**
- Selecione **us-east-1** no dropdown de região

**Stream Name:**
- Um Kinesis Data Stream pré-criado deve aparecer automaticamente no dropdown
- **Anote este nome** - é a resposta da Task 1! 📝

**Exemplo de nome:**
```
GameSessionStream-XXXXXXXXXX
```

### 4️⃣ Configurar Template de Dados

**Na seção Output Properties, encontre:**
- Propriedade: **Template**
- Valor: JSON template para dados de sessão de jogos

**Template de exemplo:**
```json
{
  "gameId": {{random.number(1000000)}},
  "creationTime": {{date.now}},
  "gameDuration": {{random.number({"min":1800,"max":3600})}},
  "seasonId": "9",
  "winner": {{random.number({"min":1,"max":2})}},
  "firstBlood": {{random.number({"min":1,"max":2})}},
  "firstTower": {{random.number({"min":1,"max":2})}},
  "firstInhibitor": {{random.number({"min":1,"max":2})}},
  "firstBaron": {{random.number({"min":1,"max":2})}},
  "firstDragon": {{random.number({"min":1,"max":2})}},
  "firstRiftHerald": {{random.number({"min":1,"max":2})}},
  "t1_champ1id": {{random.number({"min":1,"max":134})}},
  "t1_champ1_sum1": {{random.number({"min":1,"max":13})}},
  "t1_champ1_sum2": {{random.number({"min":1,"max":13})}},
  "t1_champ2id": {{random.number({"min":1,"max":134})}},
  "t1_champ2_sum1": {{random.number({"min":1,"max":13})}},
  "t1_champ2_sum2": {{random.number({"min":1,"max":13})}},
  "t1_champ3id": {{random.number({"min":1,"max":134})}},
  "t1_champ3_sum1": {{random.number({"min":1,"max":13})}},
  "t1_champ3_sum2": {{random.number({"min":1,"max":13})}},
  "t1_champ4id": {{random.number({"min":1,"max":134})}},
  "t1_champ4_sum1": {{random.number({"min":1,"max":13})}},
  "t1_champ4_sum2": {{random.number({"min":1,"max":13})}},
  "t1_champ5id": {{random.number({"min":1,"max":134})}},
  "t1_champ5_sum1": {{random.number({"min":1,"max":13})}},
  "t1_champ5_sum2": {{random.number({"min":1,"max":13})}},
  "t1_towerKills": {{random.number({"min":0,"max":11})}},
  "t1_inhibitorKills": {{random.number({"min":0,"max":3})}},
  "t1_baronKills": {{random.number({"min":0,"max":2})}},
  "t1_dragonKills": {{random.number({"min":0,"max":5})}},
  "t1_riftHeraldKills": {{random.number({"min":0,"max":2})}},
  "t1_ban1": {{random.number({"min":1,"max":134})}},
  "t1_ban2": {{random.number({"min":1,"max":134})}},
  "t1_ban3": {{random.number({"min":1,"max":134})}},
  "t1_ban4": {{random.number({"min":1,"max":134})}},
  "t1_ban5": {{random.number({"min":1,"max":134})}},
  "t2_champ1id": {{random.number({"min":1,"max":134})}},
  "t2_champ1_sum1": {{random.number({"min":1,"max":13})}},
  "t2_champ1_sum2": {{random.number({"min":1,"max":13})}},
  "t2_champ2id": {{random.number({"min":1,"max":134})}},
  "t2_champ2_sum1": {{random.number({"min":1,"max":13})}},
  "t2_champ2_sum2": {{random.number({"min":1,"max":13})}},
  "t2_champ3id": {{random.number({"min":1,"max":134})}},
  "t2_champ3_sum1": {{random.number({"min":1,"max":13})}},
  "t2_champ3_sum2": {{random.number({"min":1,"max":13})}},
  "t2_champ4id": {{random.number({"min":1,"max":134})}},
  "t2_champ4_sum1": {{random.number({"min":1,"max":13})}},
  "t2_champ4_sum2": {{random.number({"min":1,"max":13})}},
  "t2_champ5id": {{random.number({"min":1,"max":134})}},
  "t2_champ5_sum1": {{random.number({"min":1,"max":13})}},
  "t2_champ5_sum2": {{random.number({"min":1,"max":13})}},
  "t2_towerKills": {{random.number({"min":0,"max":11})}},
  "t2_inhibitorKills": {{random.number({"min":0,"max":3})}},
  "t2_baronKills": {{random.number({"min":0,"max":2})}},
  "t2_dragonKills": {{random.number({"min":0,"max":5})}},
  "t2_riftHeraldKills": {{random.number({"min":0,"max":13})}},
  "t2_ban1": {{random.number({"min":1,"max":134})}},
  "t2_ban2": {{random.number({"min":1,"max":134})}},
  "t2_ban3": {{random.number({"min":1,"max":134})}},
  "t2_ban4": {{random.number({"min":1,"max":134})}},
  "t2_ban5": {{random.number({"min":1,"max":134})}}
}
```

**Ação:**
1. Copie o valor do template das Output Properties
2. Cole no campo **Template 1** no Data Generator

### 5️⃣ Configurar Parâmetros de Envio

**Records per second:**
```
5-50 (recomendado para início)
```
- Comece com 5-10 para evitar sobrecarga
- Pode aumentar gradualmente se necessário

**Partition key:**
```
gameId
```
ou
```
{{random.number()}}
```

> 💡 **Partition key** determina em qual shard do Kinesis o registro será enviado

### 6️⃣ Iniciar Streaming

**Ação:**
1. Clique no botão **Send Data**
2. Aguarde a confirmação de que dados estão sendo enviados
3. Você verá contador de registros aumentando

**Indicadores de sucesso:**
```
✅ Records sent: 150
✅ Records/second: 5.0
✅ KB/second: 2.5
```

### 7️⃣ (Opcional) Verificar no Console AWS

**Para confirmar o nome do stream:**

**Console:**
1. AWS Console → **Kinesis**
2. **Data streams** (região us-east-1)
3. Veja o stream name na lista

**AWS CLI (se disponível):**
```bash
aws kinesis list-streams --region us-east-1
```

**Saída esperada:**
```json
{
  "StreamNames": [
    "GameSessionStream-XXXXXXXXXX"
  ]
}
```

---

## ✅ Validação da Tarefa

**Pergunta do desafio:**
```
What is the kinesis data stream name to which you are sending the data?
```

**Resposta:**
Insira o **nome exato** do Kinesis Data Stream que apareceu no dropdown do Data Generator.

**Formato:**
```
GameSessionStream-XXXXXXXXXX
```

> ⚠️ **Importante:** Envie apenas o **nome** do stream, não o ARN completo

---

## 🔍 Troubleshooting

### Problema: Stream name não aparece no dropdown

**Causas possíveis:**
- Região incorreta selecionada
- Problema de permissões no Data Generator

**Solução:**
1. Verifique se selecionou **us-east-1**
2. Faça logout e login novamente
3. Limpe cache do navegador
4. Tente em janela anônima

### Problema: Erro ao enviar dados

**Mensagens comuns:**
```
Error putting records: User is not authorized
```

**Solução:**
- Verifique credenciais (awsuser / Awsuser123)
- Confirme que está na região correta
- Aguarde alguns segundos e tente novamente

### Problema: Template inválido

**Erro:**
```
Invalid JSON in template
```

**Solução:**
1. Verifique se copiou o template completo
2. Certifique-se de que não há caracteres extras
3. Use validador JSON online se necessário

### Problema: Records not sending

**Checklist:**
- [ ] Region = us-east-1
- [ ] Stream name selecionado
- [ ] Template colado corretamente
- [ ] Records per second > 0
- [ ] Clicou em "Send Data"

---

## 📊 Entendendo os Dados

### Estrutura do Template

**Campos principais:**

| Campo | Tipo | Descrição |
|-------|------|-----------|
| gameId | Number | ID único do jogo |
| creationTime | Timestamp | Quando o jogo foi criado |
| gameDuration | Number | Duração em segundos (1800-3600) |
| seasonId | String | ID da temporada |
| winner | Number | Time vencedor (1 ou 2) |
| t1_champ1id | Number | ID do campeão 1 do time 1 |
| t1_towerKills | Number | Torres destruídas pelo time 1 |
| t2_dragonKills | Number | Dragões eliminados pelo time 2 |

**Nota:** Este é um subset simplificado de dados de jogos MOBA (League of Legends style)

### Função {{random.number()}}

**Sintaxe:**
```json
{{random.number(1000000)}}           // Número aleatório até 1000000
{{random.number({"min":1,"max":2})}} // Entre 1 e 2
```

**Outros helpers disponíveis:**
```json
{{date.now}}                    // Timestamp atual
{{random.uuid}}                 // UUID aleatório
{{random.alphanumeric(10)}}    // String alfanumérica
```

---

## 💡 Dicas Importantes

### 1. Mantenha Streaming Ativo
- Deixe o streaming rodando para as próximas tasks
- Não feche a aba do Data Generator ainda
- Task 2 precisará desses dados

### 2. Ajuste Records/Second
- Comece com 5-10 para testes
- Aumente para 20-50 se quiser mais dados rapidamente
- Muito alto pode causar throttling

### 3. Monitore Recursos
- Verifique métricas do Kinesis no console
- Observe incoming records rate
- PutRecords.Success deve estar em 100%

### 4. Pause se Necessário
- Clique em "Stop Sending Data" para pausar
- Útil se precisar fazer ajustes
- Clique "Send Data" novamente para retomar

---

## 🎓 Conceitos Aprendidos

### 1. Kinesis Data Streams

**O que é:**
Serviço de streaming de dados em tempo real da AWS que pode capturar, processar e armazenar grandes volumes de dados.

**Componentes:**
- **Stream:** Conjunto de shards
- **Shard:** Unidade de capacidade (1 MB/s in, 2 MB/s out)
- **Record:** Unidade de dado (max 1 MB)
- **Partition Key:** Determina em qual shard vai

### 2. Kinesis Data Generator

**Benefícios:**
- Geração rápida de dados de teste
- Templates personalizáveis
- Helpers para dados realistas
- Controle de taxa de envio

**Casos de uso:**
- Teste de aplicações de streaming
- Simulação de IoT devices
- Prototipagem de pipelines

### 3. Partition Keys

**Importância:**
- Distribui dados entre shards
- Garante ordem dentro de uma partition key
- Afeta throughput e distribuição

**Estratégias:**
- Random: Distribuição uniforme
- Entity ID: Agrupa dados relacionados
- Timestamp: Pode causar hot shards

---

## 🎯 Checklist de Conclusão

- [ ] Data Generator acessado com sucesso
- [ ] Login realizado (awsuser / Awsuser123)
- [ ] Região us-east-1 selecionada
- [ ] Stream name identificado e anotado
- [ ] Template colado em Template 1
- [ ] Records per second configurado (5-50)
- [ ] Partition key definido
- [ ] Streaming iniciado (Send Data)
- [ ] Registros sendo enviados (contador ativo)
- [ ] Nome do stream submetido como resposta
- [ ] Task 1 validada com sucesso

---

**✅ Próxima etapa:** Task 2 - Ingestão dos dados de streaming para o Redshift!

> **💡 Mantenha o streaming ativo** - você precisará desses dados para as próximas tasks.
