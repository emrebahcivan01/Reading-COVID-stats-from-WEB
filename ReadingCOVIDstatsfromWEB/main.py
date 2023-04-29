
import requests
from bs4 import BeautifulSoup
import texttable


url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'


page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

data = []


data_iterator = iter(soup.find_all('td'))


while True:
    try:
        country = next(data_iterator).text
        confirmed = next(data_iterator).text
        deaths = next(data_iterator).text
        continent = next(data_iterator).text


        data.append((
            country,
            str(confirmed.replace(', ', '')),
            str(deaths.replace(', ', '')),
            continent
        ))


    except StopIteration:
        break


data.sort(key=lambda row: row[1], reverse=True)


import texttable as tt
table = tt.Texttable()


table.add_rows([(None, None, None, None)] + data)


table.set_cols_align(('c', 'c', 'c', 'c'))
table.header((' Country ', ' Number of cases ', ' Deaths ', ' Continent '))

print(table.draw())


