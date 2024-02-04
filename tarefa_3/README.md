# Tarefa 3
## Limpeza de Dados (ETL)

Realizei a atividade solicitada e o código pode ser acessado no notebook [Explorer.ipynb](./explorer.ipynb)

## Perguntas e Respostas:

1. Quais os 5 melhores produtos em termos de faturamento (Receita) - por mês

| Ano  | Mês | objeto   | receita     |
|------|-----|----------|-------------|
| 2022 | 1   | CELULAR  | 22618391.67 |
|      |     | DISCO    | 7933086.75  |
|      |     | XADREZ   | 4765995.22  |
|      |     | BOTA     | 3985218.32  |
|      |     | DADO     | 2461920.37  |
|      | 2   | CELULAR  | 2446880.84  |
|      |     | DISCO    | 2072043.61  |
|      |     | XADREZ   | 689151.36   |
|      |     | DADO     | 453290.12   |
|      |     | LANTERNA | 410740.12   |
|      | 3   | CELULAR  | 2178334.00  |
|      |     | DISCO    | 1553005.19  |
|      |     | XADREZ   | 995815.66   |
|      |     | DADO     | 454631.46   |
|      |     | LANTERNA | 441417.40   |
|      | 4   | CELULAR  | 2842073.10  |
|      |     | DISCO    | 1159961.20  |
|      |     | XADREZ   | 912481.70   |
|      |     | DADO     | 560910.92   |
|      |     | BOTA     | 489441.16   |
|      | 5   | CELULAR  | 2788723.40  |
|      |     | DISCO    | 1326968.70  |
|      |     | XADREZ   | 818529.49   |
|      |     | BOTA     | 678558.93   |
|      |     | MOCHILA  | 442018.05   |
| 2022 | 6   | CELULAR  | 3870205.30  |
|      |     | DISCO    | 1526536.63  |
|      |     | XADREZ   | 909253.40   |
|      |     | MOCHILA  | 517413.24   |
|      |     | DADO     | 494354.85   |
|      | 7   | CELULAR  | 5174363.20  |
|      |     | DISCO    | 1633145.20  |
|      |     | BOTA     | 1202437.63  |
|      |     | XADREZ   | 975118.94   |
|      |     | AGULHA   | 901037.74   |
|      | 8   | CELULAR  | 5702284.80  |
|      |     | DISCO    | 1562737.05  |
|      |     | XADREZ   | 1180695.56  |
|      |     | DADO     | 521424.70   |
|      |     | BOTA     | 513917.02   |
|      | 9   | CELULAR  | 3152946.00  |
|      |     | DISCO    | 1799034.04  |
|      |     | XADREZ   | 1062514.11  |
|      |     | BOTA     | 680806.95   |
|      |     | MOCHILA  | 418542.92   |
|      | 10  | CELULAR  | 3227134.80  |
|      |     | DISCO    | 2282723.35  |
|      |     | XADREZ   | 850161.43   |
|      |     | BOTA     | 528004.27   |
|      |     | LANTERNA | 279778.62   |
| 2022 | 11  | CELULAR  | 11266816.70 |
|      |     | DISCO    | 3208325.70  |
|      |     | XADREZ   | 2031048.40  |
|      |     | BOTA     | 1061364.18  |
|      |     | MOCHILA  | 599807.37   |
|      | 12  | CELULAR  | 4321265.60  |
|      |     | DISCO    | 1644924.26  |
|      |     | BOTA     | 803448.79   |
|      |     | XADREZ   | 541300.35   |
|      |     | MOCHILA  | 465451.65   |



2. Quais os top 5 produtos que menos trazem cliques para o site, por mês?

| Ano  | Mês | objeto    | cliques |
|:-----|:----|:----------|:--------|
| 2022 | 1   | CANETA    | 994     |
|      |     | BOLSA     | 1615    |
|      |     | MOUSE     | 2556    |
|      |     | TELEVISÃO | 3573    |
|      |     | APITO     | 11378   |
|      | 2   | BICICLETA | 4       |
|      |     | CANETA    | 35      |
|      |     | TELEVISÃO | 70      |
|      |     | ÓCULOS    | 553     |
|      |     | MOUSE     | 1333    |
|      | 3   | TECLADO   | 78      |
|      |     | TELEVISÃO | 236     |
|      |     | MOUSE     | 921     |
|      |     | CACHIMBO  | 2714    |
|      |     | APITO     | 2834    |
|      | 4   | TELEVISÃO | 103     |
|      |     | BICICLETA | 301     |
|      |     | MOUSE     | 418     |
|      |     | CACHIMBO  | 984     |
|      |     | APITO     | 1707    |
|      | 5   | MOUSE     | 206     |
|      |     | TELEVISÃO | 527     |
|      |     | CANETA    | 1202    |
|      |     | ÓCULOS    | 1602    |
|      |     | APITO     | 2163    |
| 2022 | 6   | TECLADO   | 82      |
|      |     | MOUSE     | 199     |
|      |     | BICICLETA | 232     |
|      |     | TELEVISÃO | 395     |
|      |     | ÓCULOS    | 1030    |
|      | 7   | MOUSE     | 46      |
|      |     | TELEVISÃO | 579     |
|      |     | XÍCARA    | 2358    |
|      |     | APITO     | 2696    |
|      |     | BICICLETA | 4957    |
|      | 8   | MOUSE     | 74      |
|      |     | CANETA    | 220     |
|      |     | TELEVISÃO | 1511    |
|      |     | XÍCARA    | 1638    |
|      |     | APITO     | 1929    |
|      | 9   | MOUSE     | 197     |
|      |     | AGULHA    | 1298    |
|      |     | TELEVISÃO | 1349    |
|      |     | ÓCULOS    | 1696    |
|      |     | APITO     | 2322    |
|      | 10  | CANETA    | 103     |
|      |     | BOLSA     | 110     |
|      |     | MOUSE     | 130     |
|      |     | TELEVISÃO | 1567    |
|      |     | XÍCARA    | 2011    |
| 2022 | 11  | CANETA    | 150     |
|      |     | TELEVISÃO | 813     |
|      |     | BOLSA     | 1336    |
|      |     | XÍCARA    | 1583    |
|      |     | APITO     | 3431    |
|      | 12  | MOUSE     | 71      |
|      |     | TECLADO   | 71      |
|      |     | BOLSA     | 672     |
|      |     | TELEVISÃO | 1108    |
|      |     | XÍCARA    | 1845    |


Mas também tivemos produtos que não trouxeram nenhum cliquee

| Ano  | Mês | objeto         | cliques |
|:-----|:----|:---------------|:--------|
| 2022 | 1   | CACHIMBO       | 0       |
|      |     | CANETA         | 0       |
|      |     | CARRO          | 0       |
|      |     | FONE DE OUVIDO | 0       |
|      |     | MOEDA          | 0       |
|      |     | RÁDIO          | 0       |
|      |     | RÉGUA          | 0       |
|      |     | TÊNIS          | 0       |
|      |     | ÓCULOS         | 0       |
|      | 2   | BICICLETA      | 0       |
|      |     | CANETA         | 0       |
|      |     | CARRO          | 0       |
|      |     | DISCO          | 0       |
|      |     | MOEDA          | 0       |
|      |     | TÊNIS          | 0       |
|      |     | ÓCULOS         | 0       |
|      | 3   | CACHIMBO       | 0       |
|      |     | CANETA         | 0       |
|      |     | CARRO          | 0       |
|      |     | DISCO          | 0       |
|      |     | MOEDA          | 0       |
|      |     | RÁDIO          | 0       |
|      |     | RÉGUA          | 0       |
|      |     | TÊNIS          | 0       |
|      |     | ÓCULOS         | 0       |
| 2022 | 4   | CACHIMBO       | 0       |
|      |     | CANETA         | 0       |
|      |     | CARRO          | 0       |
|      |     | MOEDA          | 0       |
|      |     | TÊNIS          | 0       |
|      |     | ÓCULOS         | 0       |
|      | 5   | CACHIMBO       | 0       |
|      |     | CANETA         | 0       |
|      |     | CARRO          | 0       |
|      |     | MOEDA          | 0       |
|      |     | RÉGUA          | 0       |
|      |     | TÊNIS          | 0       |
|      |     | ÓCULOS         | 0       |
|      | 6   | CACHIMBO       | 0       |
|      |     | CANETA         | 0       |
|      |     | CARRO          | 0       |
|      |     | MOEDA          | 0       |
|      |     | TÊNIS          | 0       |
|      |     | ÓCULOS         | 0       |
|      | 7   | CACHIMBO       | 0       |
|      |     | CANETA         | 0       |
|      |     | CARRO          | 0       |
|      |     | MOEDA          | 0       |
|      |     | TÊNIS          | 0       |
|      |     | ÓCULOS         | 0       |
| 2022 | 8   | CACHIMBO       | 0       |
|      |     | CANETA         | 0       |
|      |     | CARRO          | 0       |
|      |     | MOEDA          | 0       |
|      | 9   | CANETA         | 0       |
|      |     | CARRO          | 0       |
|      |     | MOEDA          | 0       |
|      |     | TÊNIS          | 0       |
|      |     | ÓCULOS         | 0       |
|      | 10  | CACHIMBO       | 0       |
|      |     | CANETA         | 0       |
|      |     | CARRO          | 0       |
|      |     | MOEDA          | 0       |
|      |     | RÁDIO          | 0       |
|      |     | TÊNIS          | 0       |
|      |     | ÓCULOS         | 0       |
|      | 11  | CACHIMBO       | 0       |
|      |     | CANETA         | 0       |
|      |     | CARRO          | 0       |
|      |     | MOEDA          | 0       |
|      |     | RÁDIO          | 0       |
|      |     | TÊNIS          | 0       |
|      |     | ÓCULOS         | 0       |
|      | 12  | CANETA         | 0       |
|      |     | CARRO          | 0       |
| 2022 | 12  | FONE DE OUVIDO | 0       |
|      |     | MOEDA          | 0       |
|      |     | RÁDIO          | 0       |
|      |     | ÓCULOS         | 0       |


3. Quais 5 produtos tem o melhor valor médio (Receita) por transação - no ano;

| Ano  | objeto   | receita    | conversao | ticket_medio_anual |
|:-----|:---------|:-----------|:----------|:-------------------|
| 2022 | APITO    | 168371.05  | 449       | 374.991203         |
|      | CANETA   | 18375.76   | 60        | 306.262667         |
|      | LIVRO    | 1709006.92 | 5925      | 288.439986         |
|      | MOEDA    | 1162106.76 | 4850      | 239.609641         |
|      | CACHIMBO | 1127055.44 | 5034      | 223.888645         |


4. Existe algum outro insight, positivo ou negativo, que vale ser destacado?