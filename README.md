# Enriquecedor-de-CNPJs - Resumo
Código que a partir de um arquivo CSV com CNPJs usa a API da receita para enriquecer os CNPJs

# Objetivo do código
Enriquecer uma base de até 700 CNPJs com pontos, barras e traços, enviados por meio de um arquivo CSV para adicionar informações de data de abertura, natureza jurídica, capital social, faturamento estimado, porte, código da atividade primária, código da atividade secundária 1, código da atividade secundária 2, código da atividade secundária 3, ..., código da atividade secundária 99.

# Como o código funciona
Usaremos a base de informações de CNPJ da API da receita federal pelo link https://www.receitaws.com.br/v1/cnpj/{cnpj}. A API é gratúita mas tem limitação de 720 solicitações por dia e até 3 consultas por segundo por IP. Portanto, usaremos a biblioteca Time para não realizar todas as solicitações de uma só vez

**Para utilizar o código deve alterar o Token de acesso para o seu Token**

# Resultado do código
Uma planilha CSV com a informação de CNPJ, data de abertura, natureza jurídica, capital social, faturamento estimado, porte, código da atividade primária, código da atividade secundária 1, código da atividade secundária 2, código da atividade secundária 3, ..., código da atividade secundária 99.
