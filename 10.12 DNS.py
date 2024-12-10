from pprint import pprint

from bs4 import BeautifulSoup
import requests
import lxml

# url = 'https://tataev-market.ru/catalog/mebel/?all'
# response = requests.get(url)
#
# soup_tataev = BeautifulSoup(response.content, 'html.parser')
#
# product_names = list(soup_tataev.find_all('a', class_="product__name-text"))
# prices = list(soup_tataev.find_all('span', class_="product__price-current"))
#
# row_data = {}
#
# for i in range(len(product_names)):
#     row_data[product_names[i].text] = prices[i].text
#
# for i in range(len(product_names)):
#     # print(f'Товар: {product_names[i].text}\nЦена: {prices[i].text}')
#     # print('_'*30)
#     pass
#
# pprint(row_data)

# url_quotes = 'https://quotes.toscrape.com/'
#
# response = requests.get(url_quotes)
# soup_quotes = BeautifulSoup(response.content, 'lxml')
#
# quotes = list(soup_quotes.find_all('span', class_='text'))
# authors = list(soup_quotes.find_all('small', class_='author'))
# row_data = {}
#
# for i in range(len(quotes)):
#     row_data[quotes[i].text] = authors[i].text
#
# for key, value in row_data.items():
#     print(f'{key} \n(c){value}')
#     print('_'*60)


url_clock = 'https://www.alltime.ru/watch/'

response = requests.get(url_clock)
soup_all_times = BeautifulSoup(response.content, 'lxml')

clocks = list(soup_all_times.find_all('span', itemprop='name'))
prices = list(soup_all_times.find_all('span', class_="catalog-item-price text-h5"))
row_data = {}

for i in range(len(clocks)):
    row_data[clocks[i].text] = prices[i].get_text(strip=True)

for key, value in row_data.items():
    print(f'Модель часов: {key} \nЦена:{value}')
    print('_'*60)