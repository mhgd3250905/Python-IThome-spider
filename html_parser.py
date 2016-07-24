# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
class HtmlParser(object):
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        try:
            #解析网页
            soup = BeautifulSoup(html_cont, "html.parser", from_encoding='gbk')
            print '网页解析成功'
            #print soup

            # 获取heml之数据
            get_data=self._get_new_data(page_url, soup);

            print '获取newData成功'
        except:
            print '网页解析失败'
        return get_data

    def _get_new_data(self, page_url, soup):
        res_data = {}

        links = soup.find_all('div',class_=re.compile(r"block new-list-\d"))
        for link in links:
            #获取每一<li></li>的data
            links2=link.find_all('li')
            for link2 in links2:
                print link2
                print link2.span.text
                for link3 in link2.find_all('a'):
                    print link3.get('href')
                    print link3.text

                    res_data['date'] = link2.span.text
                    res_data['url'] = link3.get('href')
                    res_data['title'] = link3.text


        return res_data

