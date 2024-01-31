# Teste para a Vaga de Desenvolvedor Python com Foco em Dados na **NeoPerformance**

O repositório contém o código usado no processo e as respostas para as questões.

---

### Dia 1 - Criação da Classe do Yahoo

Meu plano era fazer um RPA usando a lib [Playwtight](https://playwright.dev/python/docs/api/class-playwright) 
(tem se comportado melhor que o selenium nos meus desenvolvimentos).

Mas ao vasculhar o site achei a url de Download que é parametrizável.

Daí foi apenas converter as datas para timestamp e o tenho o link direto para o arquivo, sem nenhuma autenticação, ou necessidade
de RPA.

Então é só enviar o arquivo diretamente ao pandas e tenho um df.

Pode se der tempo crio uma classe para fazer via RPA conforme o plano inicial.

A proxima parte é criar o "Envio para o google drive", ja fiz isso há uns anos mas usando a api do google, mas achei
uma lib que vou testar [PyDrive](https://pythonhosted.org/PyDrive/), parece reduzir bastante o desenvolvimento.

[//]: # (PS: Tive problemas com meu computador, e perdi parte do trabalho. Coisas que acontecem.)

---