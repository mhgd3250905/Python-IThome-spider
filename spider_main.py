# -*- coding: utf-8 -*-
from IT_Home_spider import url_manager,html_downloader,html_parser,html_outputer
#解析内容为
#IT之家：

class SpiderMain(object):
    def __init__(self):
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self,root_url):
        #根据url获取对应的html信息
        html_cont = self.downloader.download(root_url)
        print '获取网页内容执行成功'
        #解析网页数据
        data=self.parser.parse(root_url, html_cont)
        # print '网页解析返回新urls返回新的data执行成功'
        # #将内容保存



if __name__ == "__main__":
    root_url = "http://it.ithome.com/"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)