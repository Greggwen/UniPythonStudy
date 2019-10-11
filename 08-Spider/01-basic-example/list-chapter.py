#!/bin/python3

from bs4 import BeautifulSoup

import requests


if __name__ == '__main__':
    server = "https://www.biqukan.com/"
    target = "https://www.biqukan.com/1_1094/"

    req = requests.get(target)
    req.encoding = "gbk"

    div_bf = BeautifulSoup(req.text, "html.parser")

    div = div_bf.find_all("div", class_="listmain")

    a_bf = BeautifulSoup(str(div[0]), "html.parser")

    a = a_bf.find_all("a")
    
    for one in a:
        print(one.string, server + one.get("href"))

