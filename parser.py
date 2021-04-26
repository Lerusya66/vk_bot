from bs4 import BeautifulSoup
from requests import request

# парсинг заданий
def zadan(n):
    zdaniz = {}
    html = request(
        method='GET',
        url = f'https://inf-oge.sdamgia.ru/test?filter=all&category_id={n}&print=true',

    ).content.decode('UTF-8')

    soup = BeautifulSoup(html,'html.parser')
    for post in soup.find_all("div",{'class':'prob_maindiv'}):
        text = post.find('div', {'class':'pbody'})
        t = text.find('p').text
        a = post.find('a').text
        zdaniz[a] = [str(t).replace('\xa0',' '),str(otv(a)).replace('\xa0',' ')]
    return zdaniz
#парсиннг ответоа
def otv(num):
    html = request(
        method='GET',
        url=f'https://inf-oge.sdamgia.ru/problem?id={num}',

    ).content.decode('UTF-8')
    soup = BeautifulSoup(html, 'html.parser')
    for post in soup.find_all("div", {'class': 'prob_maindiv'}):
        #print(post)
        text = post.find('div', {'class': 'pbody','id':f'sol{num}'}).text
        #t = text.find('p').text
        return text

# разделение заданий про номерам
def all_zadan(num):
    var = {'1': '21',
           '5':'24',
           '7':'17',
           '10':'23'}
    w = zadan(var[num])
    return w

print(zadan(2))