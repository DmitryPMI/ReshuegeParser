import requests
from bs4 import BeautifulSoup

link = input('Введите ссылку: ')
page = requests.get(link).text

soup = BeautifulSoup(page, 'html.parser')

for num in soup.find_all('span', {'class': 'prob_nums'}):
    num.find('a').decompose()

soup.find('div', {'class': 'new_header'}).decompose()

html_content = soup.prettify()

filename = input('Введите название файла: ')
with open(filename + '.html', 'w') as f:
    f.write(html_content)
