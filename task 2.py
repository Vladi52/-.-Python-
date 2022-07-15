import requests
from bs4 import BeautifulSoup
import urllib.parse

url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
dict_len_word = {}
key = "start"
while key != "stop":
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    quotes = soup.find_all('div', class_='mw-category-group')
    pages = soup.find_all('a', text='Следующая страница')
    if pages:
        next_page = pages[0]['href']
        url = 'https://ru.wikipedia.org' + urllib.parse.unquote(next_page)
    else:
        key = 'stop'
    for i in range(2, len(quotes)):
        character = quotes[i].text.splitlines()[0]
        if character in dict_len_word:
            dict_len_word[character] += len(quotes[i].text.splitlines()[1:])
        else:
            dict_len_word[character] = len(quotes[i].text.splitlines()[1:])

for key, value in dict_len_word.items():
    print("{0}: {1}".format(key, value))
