# sistema-folha-pagamento
Sistema em Python para auditoria de folha de pagamento. Realiza data cleaning (filtros de erros), cálculo automatizado de bônus variáveis e detecção de outliers financeiros. Focado em escalabilidade e lógica de engenharia de software. 

Este projeto em Python simula um sistema de folha de pagamento corporativa. 
O script processa dados brutos de funcionários, aplica bônus variáveis e gera relatórios de auditoria.

- **Cálculo de Bônus:** Algoritmo que aplica 10% para salários < 5000 e 5% para salários superiores.
- **Data Cleaning:** Identificação e separação de registros com erro (salários negativos ou zerados).
- **Outlier Detection:** Filtro automático para salários acima de R$ 10.000,00 para revisão da diretoria.
- **Relatório Estatístico:** Cálculo de gasto total e média salarial usando processamento de dicionários.
