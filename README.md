# Análise de Preços de Imóveis

Este projeto tem como objetivo demonstrar o uso da técnica de RandomForestRegression para análise de preços de imóveis. Através de um modelo de machine learning, podemos analisar diversas variáveis de imóveis e prever com maior precisão o preço de venda.

#### Tecnologias Utilizadas
* Python 3
* Scikit-learn
* Pandas
* Numpy
* Yellowbrick
* Flask

####  Instalação
1. Faça o clone deste repositório:

```
git clone https://github.com/nandodevs/house-data-analysis.git
```
Instale as dependências necessárias:

```
pip install -r requirements.txt
```
--------------------------------------------------
### Dataset
O dataset utilizado neste projeto foi obtido no Kaggle. Trata-se de um conjunto de dados com informações sobre imóveis em São Paulo, Rio de Janeiro, BH, Porto Alegre e Campinas, incluindo diversas características como número de quartos, banheiros, tamanho do lote, localização, dentre outros.

###### Head do dataset

[![Head](https://github.com/nandodevs/house-data-analysis/blob/master/imgs/img1.PNG?raw=true "Head")](https://github.com/nandodevs/house-data-analysis/blob/master/imgs/img1.PNG?raw=true "Head")

### Análise Exploratória dos Dados
Nesse processo iremos fazer a limpeza dos dados, removendo colunas e valores desnecessários que possam interferir na modelagem dos dados.

```python
# Ajustando Andar
base_dados.loc[base_dados['floor'] == '301']
base_dados.iloc[2562, 5] = 30

# Ajustado o " - "
base_dados['floor'] = base_dados['floor'].apply(lambda Registro : 0 if Registro == '-' else Registro) # Se tiver - substitui por 0
base_dados['floor'] = pd.to_numeric(base_dados['floor'])

# Verificar
base_dados.head()

```
O resultado fica assim:
[![eda](https://github.com/nandodevs/house-data-analysis/blob/master/imgs/eda1.PNG?raw=true "eda")](https://github.com/nandodevs/house-data-analysis/blob/master/imgs/eda1.PNG?raw=true "eda")

### Modelagem
O modelo de machine learning utilizado foi o RandomForestRegression, um algoritmo de aprendizado de máquina que cria múltiplas árvores de decisão e as combina para obter uma melhor precisão. O modelo foi treinado com o conjunto de dados de treinamento e, em seguida, avaliado com o conjunto de dados de teste para verificar sua precisão.

OBS: O modelo foi filtrado pela cidade de São Paulo, sendo ela utilizada como base para todo o processo.

###### Checando a correlação
Verificamos qual a correlação entre os valores do dataset, primeiro no modelo mais simples:

[![](https://github.com/nandodevs/house-data-analysis/blob/master/imgs/corr1.PNG?raw=true)](https://github.com/nandodevs/house-data-analysis/blob/master/imgs/corr1.PNG?raw=true)

Depois utilzamos a lib YellowBrick para exibir de forma mais sofisticada essa correlação.
[![](https://github.com/nandodevs/house-data-analysis/blob/master/imgs/corr2.png?raw=true)](https://github.com/nandodevs/house-data-analysis/blob/master/imgs/corr2.png?raw=true)

###### Podemos perceber que rooms, bathroom e parking spaces tem a maior correlação.

Utilizamos também o YellowBrick para avaliar a performance do modelo e seu nível de erro durante a análise de dados.

[![]https://github.com/nandodevs/house-data-analysis/blob/master/imgs/corr2.png?raw=true)](https://github.com/nandodevs/house-data-analysis/blob/master/imgs/corr2.png?raw=true)

### Desenvolvimento de API
Foi utilizado a biblioteca Flask para criar uma API para consulta do resultado do modelo obtido através dos testes.

Por meio dessa API, fica mais simples a consulta das informações e tornar mais viável sua utilização para um público diversificado.

Além disso, as informações foram salvas em banco SQL, para agilizar e ter controle de acessos a API.

Aqui temos o resultado do retorno da consulta ao banco de dados, mostrando o valor a ser cobrado pelo aluguel, a data e hora da consulta (início e fim) e o tempo gasto na consulta.

[![](https://github.com/nandodevs/house-data-analysis/blob/master/imgs/api1.PNG?raw=true)](https://github.com/nandodevs/house-data-analysis/blob/master/imgs/api1.PNG?raw=true)

### Resultados
O modelo treinado obteve uma informações fundamentais para serem utilizadas como modelo para ser aplicado para outros estados, sendo capaz de prever com certa confiabilidade o preço de venda de um imóvel com base em suas características.

### Conclusão
A técnica de RandomForestRegression pode ser utilizada com sucesso em análises de preços de imóveis, oferecendo resultados precisos e confiáveis. Este projeto pode ser utilizado como base para futuras análises e estudos na área.
