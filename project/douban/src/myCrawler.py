import time

import requests
import bs4
import re

from project.douban.src.dataBase import MyDB


# 链接
def open_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) "
                      "Chrome/75.0.3770.142 Safari/537.36",
    }
    res = requests.get(url, headers=headers)
    return res


def processing(string):
    return string.replace(" ", "").replace('\"', '\\"').replace("\'", "\\'")


# 解析一级网页
def find_href(res):
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    # 电影名
    links = []
    targets = soup.find_all("div", class_="hd")
    for each in targets:
        links.append(each.contents[1].get("href"))
    return links


# 解析二级网页
def find_movies(res):
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    result = {}

    target = soup.find("h1")
    # 电影名
    result['movie'] = processing(target.contents[1].text)
    # 年份
    result['years'] = processing(target.contents[3].text)[1:-1]

    target = soup.find("div", id='info')
    # 导演
    result['directors'] = processing(target.contents[1].contents[2].text)
    # 编剧
    if len(target.contents) >= 5 and len(target.contents[4].contents) >= 3:
        result['scriptwriter'] = processing(target.contents[4].contents[2].text)
    else:
        result['scriptwriter'] = ""
    # 主演
    if len(target.contents) >= 8 and len(target.contents[7].contents) >= 3:
        result['actors'] = processing(target.contents[7].contents[2].text)
    else:
        result['actors'] = ""
    # 国家
    result['country'] = processing(re.search(r'制片国家/地区: (.*?)\n', target.text).group(1))
    # 语言
    result['language'] = processing(re.search(r'语言: (.*?)\n', target.text).group(1))

    targets = soup.find_all("span", property='v:genre')
    # 类型
    result['types'] = '/'.join(list(map(lambda x: processing(x.text), targets)))

    target = soup.find("span", property='v:initialReleaseDate')
    # 上映
    result['release'] = processing(target.text)[:10]

    target = soup.find("span", property='v:runtime')
    # 时长
    result['duration'] = re.search(r'\d+', processing(target.text)).group()

    target = soup.find("strong", property='v:average')
    # 评分
    result['grade'] = processing(target.text)

    target = soup.find("span", property='v:votes')
    # 评价人数
    result['votes'] = processing(target.text)

    target = soup.find("span", class_='all hidden')
    # 详情
    if target:
        result['summary'] = processing(target.text)
    else:
        target = soup.find("span", property='v:summary')
        result['summary'] = processing(target.text)

    return result


# 一共有多少页
def find_depth(res):
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    depth = soup.find('span', class_='next').previous_sibling.previous_sibling
    return int(depth.get_text())


# 查询数据
def getDataToMysql():
    host = "https://movie.douban.com/top250"
    res = open_url(host)
    depth = find_depth(res)

    db = MyDB()
    db.link()

    for i in range(depth):
        url = host + '/?start=' + str(25 * i) + '&filter='
        hrefs = find_href(open_url(url))
        for href in hrefs:
            data = find_movies(open_url(href))
            print(f"{data.get('movie')}\n爬取成功")
            keys = ','.join(['`{}`'.format(item) for item in data.keys()])
            values = ','.join(['\'{}\''.format(item) for item in data.values()])
            sql = f"INSERT INTO douban.movie({keys})VALUES({values});"
            if db.push(sql):
                print("写入成功")
            else:
                print("写入失败")
        time.sleep(2)

    db.close()


if __name__ == '__main__':
    getDataToMysql()
