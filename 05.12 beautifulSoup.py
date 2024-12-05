from urllib.parse import urljoin

from bs4 import BeautifulSoup
import requests
import random

url_books = 'https://litlife.club/genres/72-trillery'

def get_rand_book(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        cards = soup.select('div.card.mb-3')
        books = []

        for card in cards:
            title_tag = card.select_one('h3.break-word.h5 a')
            author_tag = card.select_one('span.font-weight-normal a')

            if title_tag and author_tag:
                book_title = title_tag.get_text(strip=True)
                author_name = author_tag.get_text(strip=True)
                books.append((book_title, author_name))

        random_book = random.choice(books)
        print(f'Случайная книга: {random_book[0]} \nАвтор: {random_book[1]}')


get_rand_book(url_books)

print('_'*50)

url_cartoons = 'https://www.film.ru/compilation/luchshie-multfilmy-disney'

def get_rand_cartoon(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        afisha = soup.select('div.redesign_afisha_movie_main')
        cartoons = []

        for afisha in afisha:
            title_tag = afisha.select_one('a')


            title_link = title_tag.get('href')
            full_url = urljoin(url, title_link)
            response_title = requests.get(full_url)

            if response_title.status_code == 200:
                soup_title = BeautifulSoup(response_title.content, 'html.parser')

                abstract = soup_title.select('div.wrapper_movies_text p')


                if title_tag and abstract:
                    title_name = title_tag.get_text(strip=True)
                    abstract_text = abstract[0].get_text(strip=True)

                    cartoons.append((title_name, abstract_text))

        random_cartoon = random.choice(cartoons)
        print(f'Случайный мультфильм: {random_cartoon[0]} \nОписание: {random_cartoon[1]}')


get_rand_cartoon(url_cartoons)

