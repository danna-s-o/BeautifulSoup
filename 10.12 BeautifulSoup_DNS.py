from bs4 import BeautifulSoup
import requests

url_dns = 'https://www.dns-shop.ru/catalog/17a892f816404e77/noutbuki/'


def get_info_laptop(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        print(response.text)

        products = soup.find_all('a', class_='catalog-product__name ui-link ui-link_black')

        for product in products:

            product_name = product.find('span').get_text(strip=True)

            price_block = product.find_parent('div', class_='catalog-product') \
                .find('div', class_='product-buy__price-wrap product-buy__price-wrap_interactive')

            if price_block:

                price = price_block.find('div', class_='product-buy__price').get_text(strip=True)

                subscription_price = price_block.find('div', class_='product-buy__sub').get_text(strip=True)


                print(f'Ноутбук: {product_name}')
                print(f'Основная цена: {price} руб.')
                print(f'Цена по подписке: {subscription_price}')
                print('_' * 20)


get_info_laptop(url_dns)
