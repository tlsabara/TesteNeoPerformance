# Tarefa: Proposta de automação na Cloud

Infelizmente não tenho nehuma experiencia com GCP. 

Por outro lado, ja trabalho com AWS à anos, e Azure a menos de 1 ano (
alem de ja ter um certificado AZ-900).

Então minha abordagem vai ser usar o conhecimento das outras clouds e "converter" para a GCP.

### AWS



Seguindo a proposta, preciso comportar os arquivos do projeto, session.json e settings_t.yaml então armazenaria em um S3, sem acesso público.

Preciso também de uma Role no IAM, para ler e atualizar dados nestes arquivos, esta Role será usada para acessar os arquivos.

Usaria o AWS Lambda para comportar o script e torná-lo executável.
Criação da AWS Lambda:
 - Criaria uma função sem template, sem necessidade de uma URL de função (O acionamento é via agendamento).
 - Importaria o código do S3. 