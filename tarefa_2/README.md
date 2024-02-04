# Tarefa 2
## Proposta de automação na Cloud

Seguindo a proposta, preciso comportar os arquivos do projeto, session.json e settings_t.yaml então armazenaria em um 
storage do Cloud Storage, sem acesso público.

Preciso de um serviço como Container Registry ou Artifact Registry, para armazenar a imagem docker do projeto.

Usaria o Cloud Build  para montar a imagem Docker. No pipeline adidionaria os arquivos de configuração que estão no Cloud Storage.
Após o build o pipeline adiciona a imagem docker ao AWS ECR.

Usaria o Cloud Run para tornar a imagem  que "executável".

Para o acionamento usaria o Cloud Scheduler com um agendamento diário.
