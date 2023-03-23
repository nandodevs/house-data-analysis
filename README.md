# Análise de Preços de Imóveis Utilizando RandomForestRegression

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
[![head](imgs\img1.PNG "head")](\imgs\img1.PNG "head")

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
[![head](imgs\eda1.PNG "eda")](\imgs\eda1.PNG "eda")

### Modelagem
O modelo de machine learning utilizado foi o RandomForestRegression, um algoritmo de aprendizado de máquina que cria múltiplas árvores de decisão e as combina para obter uma melhor precisão. O modelo foi treinado com o conjunto de dados de treinamento e, em seguida, avaliado com o conjunto de dados de teste para verificar sua precisão.



### Resultados
O modelo treinado obteve uma informações fundamentais para serem utilizadas como modelo para ser aplicado para outros estados, sendo capaz de prever com certa confiabilidade o preço de venda de um imóvel com base em suas características.

### Conclusão
A técnica de RandomForestRegression pode ser utilizada com sucesso em análises de preços de imóveis, oferecendo resultados precisos e confiáveis. Este projeto pode ser utilizado como base para futuras análises e estudos na área.




