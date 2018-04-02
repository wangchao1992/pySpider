#coding=utf-8
#Python-version 2.7
# 使用 lxml 的 etree 库
"""
运行程序后，输入主题和起始页，就可以爬取相关图片
"""
from lxml import etree
import urllib
import urllib2
class Spider():
    def __init__(self):
        kw = raw_input("请输入要爬的贴吧主题：")
        self.begin = int(raw_input("请输入起始页"))
        self.end = int(raw_input("请输入终止页："))
        self.url = 'http://tieba.baidu.com/f'

        param = urllib.urlencode({'kw': kw,
                                  'ie': 'utf-8'
                                  })
        self.url = self.url + '?' + param
        self.tiebaSpider()
    def tiebaSpider(self):
        for page in range(self.begin,self.end + 1, 1):
            page = (page - 1) * 50
            url = self.url + "&pn=" + str(page)
            html = self.loadPage(url)
            html_etree = etree.HTML(html)
            links = html_etree.xpath("//div[@class='threadlist_lz clearfix']//div/a/@href")
            for link in links:
                self.getImgLink(link)

    def loadPage(self,url):
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read()
    def getImgLink(self,link):
        url = "https://tieba.baidu.com"+link
        html_etree = etree.HTML(self.loadPage(url))
        srclist = html_etree.xpath('//img[@class="BDE_Image"]/@src')
        print srclist
        for src in srclist:
            self.saveImg(src)
    def saveImg(self,url):
        res = self.loadPage(url)
        imgName = url[-10:]
        with open("./img/"+imgName,'wb') as f:
            f.write(res)





if __name__=="__main__":
    myspider = Spider()
    #myspider.tiebaSpider()

