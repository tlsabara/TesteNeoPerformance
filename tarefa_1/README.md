# Tarefa 1: 
## Automação de coleta de dados e visualização

### REQUISITOS:
 - docker e docker compose instalados. Veja mais no [Site oficial do Docker](https://docs.docker.com/engine/install/)
 - acessar [Link do arquivo de dados no google](https://docs.google.com/spreadsheets/d/1Lo2p5XalsFpbAtBUyBZEKXkQN-GmBskwIAiJutgmWeg/edit?usp=sharing)
### Passo 1:
Para executar a tarefa, adicione os arquivos (estes arquivos não foram compartilhados no repositório) `session.json`, `.env` e `settings_t.yaml`, à pasta tarefa_1.

OBS: Se você esta acessando este repositório no GitHub pode me solictar os arquivos via email (thi.sil.sab@gmail.com)

### Passo 2:
Com os arquivos na pasta basta executar com o docker:
```bash
docker compose build
docker compose up
```
OBS: execute sem o `-d`, pois o projeto executa em menos de 1 min, e você poderá ver o log.

### Passo 3:

Os dados ja estarão atualizados na minha fonte de dados e você pode acessar a vizualização [neste link](https://lookerstudio.google.com/reporting/e40e6ae6-c06e-429c-aa12-73026d94db33)
Tem um delay de 15 min para atualização

---

Se quiser que o arquivo processado vá para o seu Google Drive, basta apagar o session.json, e executar e fazer o login com sua conta.
A minha aplicação no Google precisa de algumas permissões ao seu Google Drive. 