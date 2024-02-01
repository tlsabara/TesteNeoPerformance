# Teste para a Vaga de Desenvolvedor Python com Foco em Dados na **NeoPerformance**

O repositório contém o código usado no processo e as respostas para as questões.

---
### 29/01/2024 Dia 1 - Criação da Classe do Yahoo
**branch: origin/dia_01**

Meu plano era fazer um RPA usando a lib [Playwtight](https://playwright.dev/python/docs/api/class-playwright) 
(tem se comportado melhor que o selenium nos meus desenvolvimentos).

Mas ao vasculhar o site achei a url de Download que é parametrizável.

Daí foi apenas converter as datas para timestamp e o tenho o link direto para o arquivo, sem nenhuma autenticação, ou necessidade
de RPA.

Então é só enviar o arquivo diretamente ao pandas e tenho um df.

Se der tempo crio uma classe para fazer via RPA conforme o plano inicial.

A proxima parte é criar o "Envio para o google drive", ja fiz isso há uns anos mas usando a api do google, mas achei
uma lib que vou testar [PyDrive](https://pythonhosted.org/PyDrive/), parece reduzir bastante o desenvolvimento.

[//]: # (PS: Tive problemas com meu computador, e perdi parte do trabalho. Coisas que acontecem.)

---
### 31/01/2024 - Dia 2 - Criação da Classe do Google
**branch: origin/dia_02**

O **PyDrive** deu certo!!! (ainda bem!)

Realizei a criação da classe do google, responsável por ler, enviar e atualizar os arquivos no
Google Drive.

O código não foi a parte mais complicada, e sim a criação da API no google, a primeira api estava
apresentando erro de validação com o google, e não to com muito tempo para debugar. Então usei uma
Api que tinha criado há 2 anos atrás e modifiquei para aplicar no projeto.

Ainda não sei como será para a execução no teste, pois a conta do google de quem for avaliar não
vai ter acesso ao arquivo que estará conectado ao Google Data Studio.

Mas o upload será realizado com certeza!

O plano de amanhã será realizar o desenvolvimento da rotina a ser executada.

---
