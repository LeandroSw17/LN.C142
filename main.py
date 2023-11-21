import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL da página da Wikipedia
url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Faz a requisição da página
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Obtém todas as tabelas da página
all_tables = soup.find_all("table")

# Encontramos que a 7ª iteração fornece as linhas da 3ª tabela (Field brown dwarfs)
table = all_tables[6]
rows = table.find_all("tr")

# Cria uma lista vazia para armazenar as linhas da tabela
table_data = []

# Obtém todas as tags <td> e armazena na lista
for row in rows:
    cols = row.find_all("td")
    cols = [col.text.strip() for col in cols]
    table_data.append(cols)

# Cria listas vazias para armazenar os dados
nomes = []
raios = []
massas = []
distancias = []

# Loop na lista de linhas para obter os dados
for data in table_data:
    # Certifique-se de que há dados suficientes na linha
    if len(data) >= 4:
        nomes.append(data[0])
        raios.append(data[1])
        massas.append(data[2])
        distancias.append(data[3])

# Cria um DataFrame usando pandas
df = pd.DataFrame({
    "Nome da Estrela": nomes,
    "Raio": raios,
    "Massa": massas,
    "Distância": distancias
})

# Cria um arquivo CSV a partir do DataFrame
df.to_csv("brown_dwarfs_data.csv", index=False)
