# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json


# class NowcoderscrapyPipeline(object):
#     def __init__(self):
#         self.filename = open("test.json", "w", encoding="utf-8")
#
#     def process_item(self, item, spider):
#         text = json.dumps(dict(item), ensure_ascii=False) + "\n"
#         self.filename.write(text)
#         return item
#


class NowcoderscrapyPipeline(object):
    def __init__(self):
        # 连接MySQL数据库
        self.connect = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='nowcoder', port=3306)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        # 往数据库里面写入数据
        sql = "insert into javabycompany(tag, title, content, date) values (%s, %s, %s, %s)"
        self.cursor.execute(sql, (item['tag'], item['title'], item['content'], item['date']))
        self.connect.commit()
        return item

    # 关闭数据库
    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
