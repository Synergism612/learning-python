import requests
import bs4
import os
from urllib.request import urlretrieve
import time
# 封装成一个函数


def getList():
    # 目标url
    url = 'https://www.nipic.com/topic/show_27313_1.html'
    # 模拟浏览器
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.69 Safari/537.36'}
    # 发送请求
    response = requests.get(url, headers=headers)
    # 解析数据
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    link_list = soup.find_all("img")
    # 返回我们要的数据
    return link_list


# 定义文件名
text = '处暑海报'
if not os.path.exists(text):
    os.mkdir(text)

i = 1
for link in getList():
    # 姓名列表和链接
    # https://pic.nximg.cn/pic/20230809/22068605_214950789120_4.jpg
    name = link.attrs['alt']
    links = f"https:{link.attrs['src']}"
    urlretrieve(links, f"{text}/{i}{name}.jpg")
    # 打印成功
    print(name + '100%')
    i += 1

 # 延迟2秒
    time.sleep(2)
