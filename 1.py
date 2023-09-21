import requests
import bs4
import os
from urllib.request import urlretrieve
import time
#封装成一个函数
def dobantop(id):
    #目标url
    url = 'https://movie.douban.com/top250?start={}&filter='.format(id)
    #模拟浏览器
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.69 Safari/537.36'}
    #发送请求
    response = requests.get(url, headers=headers)
    #解析数据
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    link_list = soup.find_all("div", class_="pic")
    #返回我们要的数据
    return link_list

#定义文件名
text='豆瓣top250排行榜'
# if not os.path.exists(text):
#     os.mkdir(text)
i=0
#250张图片
for i in range(0,275,25):
    link_list = dobantop(i)
    for link in link_list:
            #姓名列表和链接
            name=link.a.img['alt']
            links=link.a.img['src']
            i+=1
            # urlretrieve(links, text + '/' + (str(i)+name) + '.jpg')
            # 打印成功
            print(name + '100%')

     # 延迟2秒
    time.sleep(2)
