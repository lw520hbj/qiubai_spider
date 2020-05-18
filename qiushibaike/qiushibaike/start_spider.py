from scrapy import cmdline


if __name__ == "__main__":
    # print("请输入爬虫的名称：")
    # spider_name = input()
    spider_name = 'qb_spider'
    cmdline.execute(['scrapy', 'crawl', spider_name])
