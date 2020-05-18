# -*- coding: utf-8 -*-
import scrapy
from qiushibaike.items import QiushibaikeItem


class QbSpiderSpider(scrapy.Spider):
    name = 'qb_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']
    item = QiushibaikeItem()

    def parse(self, response):
        duanzidivs = response.xpath("//div[@class='col1 old-style-col1']/div")
        for duanzidiv in duanzidivs:
            author = duanzidiv.xpath(".//h2/text()").get().strip()
            self.item['author'] = author
            # 解决内容显示不完整的段子：先获取到完整段子的链接，request访问，处理交给parse_all_content函数
            if duanzidiv.xpath(".//div[@class='content']/span[2]"):
                all_link = duanzidiv.xpath("./a/@href").get()
                content_url = "https://www.qiushibaike.com"+all_link
                yield scrapy.Request(url=content_url, callback=self.parse_all_content)
            else:
                content = "".join(duanzidiv.xpath(".//div[@class='content']/span//text()").getall()).strip()
                self.item['content'] = content
            yield self.item
        # 爬取多页共二十页，也可以判断页面有没有下一页如果有则爬取
        for i in range(2, 21):
            next_url = "https://www.qiushibaike.com/text/page/"+str(i)+"/"
            yield scrapy.Request(url=next_url, callback=self.parse)


    def parse_all_content(self, response):
        all_content = response.xpath("//div[@class='content']//text()").getall()
        all_content = ''.join(all_content).strip()
        self.item['content'] = all_content
        yield self.item
