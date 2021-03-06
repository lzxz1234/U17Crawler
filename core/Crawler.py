# -*- coding: utf-8 -*-

import urllib
import re
import base64
from pyquery import PyQuery

class Fetcher:
    '''
    1、查询主页：http://so.u17.com/all/%E9%82%A3%E5%B9%B4%E9%82%A3/m0_p1.html
    根据 #comiclist > div > div.comiclist > ul > li > div > div.info > h3 > strong > a 路径得到漫画主页链接

    2、打开漫画主页：http://www.u17.com/comic/8752.html
    根据 .chapterlist_box > .cf > li > a 路径得到章节主页

    3、打开章节主页：http://www.u17.com/chapter/155550.html
    执行 js: image_config.image_list 可以得到和图片地址
    '''
    def __init__(self):
        pass

    def queryComic(self, book_name):
        '''
        :param book_name: 查询名称
        :return: 列表，每一项为名称链接的二元组
        '''
        url = 'http://so.u17.com/all/%s/m0_p1.html'%self.urlencode(book_name)
        doc = PyQuery(url = url)
        result = []
        for comic in doc('#comiclist > div > div.comiclist > ul > li > div > div.info > h3 > strong > a'):
            result.append((re.sub(r'</?\w+[^>]*>', '', PyQuery(comic).attr("title")).strip(), PyQuery(comic).attr("href")))
        return result

    def queryChapters(self, comicUrl):
        '''
        :param comicUrl: 漫画地址
        :return: 列表，每一项为名称链接的二元组
        '''
        doc = PyQuery(url = comicUrl)
        return [(PyQuery(i).attr("title").strip(), PyQuery(i).attr("href")) for i in doc('.chapterlist_box > .cf > li > a')]

    def queryImages(self, chapterUrl):
        '''
        :param chapterUrl: 章节地址
        :return: 章节内图片地址列表
        '''
        p = re.compile(r'\"src\"\:\"([a-zA-Z0-9=]*)\"')
        doc = PyQuery(url = chapterUrl)
        for script in doc('script'):
            script_content = PyQuery(script).html()
            if script_content and script_content.find('image_config') > 0:
                return [base64.decodestring(x).strip() for x in p.findall(script_content)]

    def urlencode(self, val):
        if isinstance(val, unicode):
            return urllib.quote_plus(str(val))
        return urllib.quote_plus(val)

if __name__=='__main__':
    print Fetcher().queryImages('http://www.u17.com/chapter/334223.html')