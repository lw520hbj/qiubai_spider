# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import MySQLdb
import csv


class QiushibaikePipeline(object):
    # connect = None
    # cursor = None
    fp = None
    writer = None

    def open_spider(self, spider):
        print("爬虫开始了,写入文件")
        self.fp = open("E:\pythonfiles\qiushibaike\qiushibaike\duanzi.csv",  "w", encoding="utf-8")
        self.writer = csv.writer(self.fp)
        self.writer.writerow(["作者", "段子内容"])
        # self.connect = MySQLdb.connect(host='localhost', user='root', passwd='lw520hbj', port=3306, db='qiubai',
        #                                charset='utf8')
        # self.cursor = self.connect.cursor()

    def process_item(self, item, spider):

        self.writer.writerow([item['author'], item['content']])
        # sql = "insert into qb_duanzi(author, content) values ({0}, {1})".format(item['author'], item['content'])
        # self.cursor.execute(sql)
        # print(item['author']+":"+item['content'])

    def close_spider(self, spider):
        print("爬虫结束了，关闭文件")
        self.fp.close()
        # self.cursor.close()
