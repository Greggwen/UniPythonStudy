#!/bin/python3

from bs4 import BeautifulSoup
import requests
import sys

"""
说明：下载小说《一念永恒》

Datetime: 2019-10-11
"""

class DownloadNovel(object):
    
    def __init__(self):
        self.server = "https://www.biqukan.com/"
        self.target = "https://www.biqukan.com/1_1094/"
        self.chapters = [] # 存放章节名称
        self.chapters_url = [] # 存放章节URL
        self.nums = 0 # 章节数

    """
    获取下载链接
    """
    def get_target_url(self):
        req = requests.get(self.target)
        req.encoding = "gbk"

        div_bf = BeautifulSoup(req.text, "html.parser")
        div = div_bf.find_all("div", class_="listmain")

        a_bf = BeautifulSoup(str(div[0]), "html.parser")
        a = a_bf.find_all("a")
        self.nums = len(a[15:])

        for one in a[15:]:
            self.chapters.append(one.string)
            self.chapters_url.append(self.server + one.get("href"))


    """
    获取章节内容
    """
    def get_contents(self, target):
        req = requests.get(url = target)
        req.encoding = "gbk"
        bf = BeautifulSoup(req.text, "html.parser")
        texts = bf.find_all('div', class_ = 'showtxt')
        texts = texts[0].text.replace('\xa0'*8,'\n\n')
        return texts

    """
    将爬取的文章内容写入文件
    """
    def write_to_text(self, name, path, content):
        # write_flag = True
        
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(content)
            f.write('\n\n')


if __name__ == '__main__':
    dl = DownloadNovel()

    dl.get_target_url()
    print('《一年永恒》开始下载：')

    for i in range(dl.nums):
        dl.write_to_text(dl.chapters[i], '一念永恒.txt', dl.get_contents(dl.chapters_url[i]))
        sys.stdout.write("  已下载:%.3f%%" %  float(i/dl.nums) + '\r')
        sys.stdout.flush()
    print('《一年永恒》下载完成')