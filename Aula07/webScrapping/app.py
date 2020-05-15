## WebScrapping

### Pipeline Machine Learning/DataScience
#### Dados não estruturados 
##### Coleta -> Processamento dos Dados 

### ETL/Análise de dados 

#### Caracterização 
### Python:
#### Entrar no site OK
#### Pegar os dados site OK
#### Filtro do que é interessante
#### Deixar essa info em um formato de interesse 
#### Destinação do dado.

## Módulos
### urllib <- requisição de páginas ## biblioteca nativa
### BeautifulSoup <- 'parsers'

# lidar com requisições
from urllib.request import urlopen as uReq 
# lidar com 'parsing' de arquivos
from bs4 import BeautifulSoup as soup 
# extra para salvar em um arquivo json
import json

# url alvo
url = "https://www.al.sp.gov.br/propositura/?id=1000252923&tipo=1&ano=2018"

# contexto
with uReq(url) as pagina:
    conteudo = pagina.read()

## Converter a string do site em um objeto manipulável
pagina_html = soup(conteudo, "html.parser")


## filtro
div_alvo = pagina_html.findAll("div", {"class": "ativo", "id": "referencias"})
    
tabela = div_alvo[0].table.tbody.find_all('td')

## formato manipulável em dicionário - ideal para inserção em banco de dados como o MongoDB

pl = {}
pl['num_legislativo'] = tabela[3].text.strip() #regex
pl['ementa'] = tabela[5].text.strip()
pl['data_publicacao'] = tabela[7].text.strip()
pl['regime'] = tabela[9].text.strip()
pl['autores'] = tabela[11].text.strip()
pl['apoiadores'] = tabela[13].text.strip()
pl['indexadores'] = tabela[15].text.strip()
pl['etapa_atual']= tabela[17].text.strip()

# montagem do arquivo csv
#registro = f'{},{},{},{},{},{},{},{}\n'

## salvar como arquivo json
with open('pls.json', 'w') as arquivo:
    json.dump(pl, arquivo, ensure_ascii=False)
    
    


