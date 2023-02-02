import requests
from bs4 import BeautifulSoup

url = 'https://news.google.com/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

news_list = soup.find_all('a', class_='DY5T1d')

for news in news_list:
    title = news.text
    link = news['href']
    print('标题：', title)
    print('链接：', link)
    print('\n')
