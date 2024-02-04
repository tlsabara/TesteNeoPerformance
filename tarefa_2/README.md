# Tarefa 2
## Proposta de automação na Cloud

Infelizmente não tenho nehuma experiencia com GCP. 

Por outro lado, ja trabalho com AWS à anos, e Azure a menos de 1 ano (
alem de ja ter um certificado AZ-900).

Então minha abordagem vai ser usar o conhecimento das outras clouds e "converter" para a GCP.

### AWS

Seguindo a proposta, preciso comportar os arquivos do projeto, session.json e settings_t.yaml então armazenaria em um 
bucket do AWS S3, sem acesso público.

Preciso de um AWS ECR, para armazenar a imagem docker do projeto.

Usaria o AWS CodePipeline para montar a imagem Docker. No pipeline adidionaria os arquivos de configuração que estão no AWS S3.
Após o build o pipeline adiciona a imagem docker ao AWS ECR.

Usaria o AWS Lambda para tornar a imagem "executável".

Na criação da AWS Lambda:
 - Criaria uma função sem template, sem necessidade de uma URL de função (O acionamento é via agendamento).
 - E usaria a imagem do AWS ECR correspondente a tarefa nesta Lambda.

Para o trigger o proprio AWS Lambda pode ser configurado com um agendamento diretamente no serviço.
Se não for com o trigger do serviço eu utilizaria o AWS EventBridge com o agendamento.

| Serviços AWS | Serviços GCP                            |
|--------------|-----------------------------------------|
| S3           | Cloud Storage                           |
| ECR          | Container Registry ou Artifact Registry |
| CodePipeline | Cloud Build                             |
| Lambda       | Cloud Run                               |
| EventBridge  | Cloud Scheduler                         |

Não é apenas trocar dos serviços que vá fazer com que o projeto funcione completamente na outra cloud.
Há particularidades envolvidas, conforme pesquisei, o Cloud Functions que em tese é o concorrente do AWS Lambda, 
não executaria o container do projeto, para este caso é necessário usar o Cloud Run. 