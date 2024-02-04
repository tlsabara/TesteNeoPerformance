# Automação de coleta de dados e visualização:

#### Tarefa 1

P: Crie um script em Python para coletar dados históricos do Yahoo Finance. A solução deve extrair dados diários dos últimos 365 dias das empresas Meta, Amazon, Apple, Netflix e Google toda vez que for acionada. Persista os dados no Google Sheets e crie uma visualização para usuários no Sheets ou no Looker Studio. O fluxo deve ser o mais automatizado possível. Disponibilize o código da solução.

---
# Proposta de automação na Cloud:

#### Tarefa 2

P: Suponha que você precise acionar esse script244 todos os dias, de hora em hora. Como você estruturaria o script para implementá-lo na Google Cloud? Explique o fluxo, os serviços utilizados e quais suas funções. (Não é necessário implementar devido aos custos)


### Elementos que considero cruciais:
- Conta de serviço para utilizar serviços da cloud e google sheets.
- Google Secrets para garantir segurança de senhas e outros dados sensíveis.
- Orquestrador. Pode ser tanto o Composer como o Cloud Scheduler para acionar rotinas na frequência estipulada.
- Hospedagem do Script, podendo ser no Cloud Functions, Cloud Run Storage ou Outro.

---
# Limpeza de Dados (ETL)

#### Tarefa 3

A ObjetosTeca é uma empresa que comercializa uma ampla variedade de produtos, os quais necessitam de uma organização cuidadosa para a elaboração de relatórios mensais. Com o intuito de atender a essa demanda, foi repassada ao setor de dados uma planilha base de vendas desses produtos. No entanto, é importante mencionar que ocorreu um problema no arquivo, resultando em dados corrompidos. Apesar desse contratempo, visando assegurar a elaboração dos relatórios, o diretor solicitou uma limpeza na base de dados para extrair algumas informações relevantes. Disponibilize o código da solução.

Dica: A listagem de produtos únicos vendidos pela ObjetosTeca está na aba SKUS da planilha.

1. Quais os 5 melhores produtos em termos de faturamento (Receita) - por mês;
2. Quais os top 5 produtos que menos trazem cliques para o site, por mês?
3. Quais 5 produtos tem o melhor valor médio (Receita) por transação - no ano;
4. Existe algum outro insight, positivo ou negativo, que vale ser destacado?
