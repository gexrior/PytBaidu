# -*- coding: UTF-8 -*-
from Headwords import html_downloader
from Headwords import html_outputer
from Headwords import html_parser
from Headwords import url_manager


class SpiderMain(object):
    #爬虫的初始化，管理器、下载器、解析器、输出器
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()



    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            #有一些URL已经失效，或者无法访问，所以我们需要添加特殊情况
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s'%(count,new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                #只爬取1000个
                if count ==10:
                    break
                count = count +1
            except:
                print"craw failed"

        self.outputer.output_html()
if __name__ =="__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
