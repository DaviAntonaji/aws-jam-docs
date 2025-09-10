# Desafio AWS Game Development – Task 1

## Pergunta
Para armazenar e recuperar de forma eficiente grandes ativos binários de jogos, qual solução de armazenamento da AWS é conhecida por sua escalabilidade e capacidades de armazenamento de objetos?

### Contexto
- **Amazon S3 (Simple Storage Service):** Serviço de armazenamento de objetos, ideal para ativos de jogos (imagens, áudios, vídeos, modelos 3D, CSVs, etc.). Altamente escalável e durável.
- **Amazon DynamoDB:** Banco de dados NoSQL para acesso em tempo real e baixa latência. Indicado para dados dinâmicos de jogadores e gerenciamento de estado.
- **Amazon RDS (Relational Database Service):** Banco de dados relacional gerenciado para dados estruturados, como perfis de jogadores, progresso no jogo e rankings.

## Resposta
**Amazon S3**

## Explicação
O Amazon S3 é a escolha correta porque foi projetado especificamente para **armazenamento de objetos** e oferece a escalabilidade necessária para lidar com **grandes ativos binários** usados em jogos multiplayer online. Isso o torna a melhor solução para armazenar e recuperar ativos de jogos como texturas, imagens, áudios e vídeos.
