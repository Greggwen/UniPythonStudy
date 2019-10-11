#!/bin/python3

from bs4 import BeautifulSoup
import requests


if __name__ == "__main__":
    target = "https://www.biqukan.com/1_1094/5403177.html"

    req = requests.get(target)
    req.encoding = "gbk"  # 根据目标页面的字符集设定
    
    bf = BeautifulSoup(req.text, 'html.parser')

    texts = bf.find_all("div", "showtxt")

    print(texts[0].text.replace('\xa0'*8,'\n\n'))