# Tarefa 1: 
## Automação de coleta de dados e visualização

### REQUISITOS:
 - docker e docker compose instalados. Veja mais em [Instalação do Docker](https://docs.docker.com/engine/install/)

### Passo 1:
Para executar a tarefa, adicione os arquivos `session.json`, `.env` e `settings_t.yaml`, à pasta tarefa_1.

OBS: Se você esta acessando este repositório no GitHub pode me solictar os arquivos via email (thi.sil.sab@gmail.com)

### Passo 2:
Com os arquivos na pasta basta executar com o docker:
```bash
docker compose build
docker compose up
```
OBS: sim execute sem o -d, pois o projeto executa em menos de 1 min, e você poderá ver o log.

### Passo 3:

Os dados ja estarão atualizados na minha fonte de dados e você pode acessar a vizualização [neste link](https://lookerstudio.google.com/reporting/e40e6ae6-c06e-429c-aa12-73026d94db33)

---

Se quiser que o arquivo processado vá para o seu google drive, basta apagar o session.json e fazer o login com sua conta.