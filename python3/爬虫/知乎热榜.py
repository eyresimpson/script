import requests
from bs4 import BeautifulSoup

# 依赖lxml解析，需要安装此库
# pip install lxml

# 设置请求头，模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'cookie': '_zap=467c06b3-9f48-43c3-9594-ab3d0a5e7b16; d_c0=AFBWaX7rhRWPTr_BAeQ340XqaoPwd28ijfA=|1662544465; q_c1=5971c5ded9984a4e977491f88d4818d3|1662605209000|1662605209000; z_c0=2|1:0|10:1674996193|4:z_c0|80:MS4xMGFFVEVBQUFBQUFtQUFBQVlBSlZUZmwtdzJSZ2JTOFJlQjdKQlpEZnB6SXZTQS1vYktNZm53PT0=|e6f9a5ff873b937171c0781dc3b152820a79d7a02c77aade043a0eb4f3032ab7; _xsrf=0e399c56-fe7b-4082-9f70-678d503f3414; arialoadData=false; tst=h; SESSIONID=VCrRaYR2Ogbi6HKwDPyHHJAb5nCESSJ5RpRmSxcMe0W; KLBRSID=d6f775bb0765885473b0cba3a5fa9c12|1675229337|1675229330'
}

# 发起请求，获取热榜页面的HTML
url = 'https://www.zhihu.com/hot'
res = requests.get(url, headers=headers)
html = res.text

# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(html, 'lxml')

# 提取所有的热榜信息
items = soup.select('.HotList-item')
for item in items:
    title = item.select_one('.HotItem-title').text.strip()
    link = item.select_one('.HotItem-title').get('href')
    print('标题：', title)
    print('链接：', link)
    print('-' * 50)
