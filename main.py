from bs4 import BeautifulSoup 
import requests
from decor import loger

KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'it', 'accelerator', 'raspberry', 'блокчейн']
URL = 'https://habr.com/ru/all/'

@loger(path='log.txt')
def get_habr(url, words):
    res = []
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, features='html.parser')

    #Вывести в консоль список подходящих статей в формате: <дата> - <заголовок> - <ссылка>#
    articles = soup.find_all('article')
    for article in articles:
        time = article.find('time').get('title')
        h2 = article.find('h2').find('span').text
        href = article.find('h2').find('a').get('href')
        text = ''.lower()
        response_full = requests.get(f'https://habr.com{href}')
        soup_full = BeautifulSoup(response_full.text, features='html.parser')
        posts = soup_full.find('div', {'id':'post-content-body'})
        for word in words:
            if word in posts.text.lower():
                text = f'{time} - {h2} - https://habr.com{href}, слово {word}'
                res.append(text)
                print(text)
                break
    return res

get_habr(URL, words=KEYWORDS)