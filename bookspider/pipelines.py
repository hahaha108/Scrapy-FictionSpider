# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

class BookspiderPipeline(object):

    def process_item(self, item, spider):
        dirPath = r'C:\Users\Administrator\Desktop\book' + '\\' + item['categoryName'] + '\\' + item['bookName']

        # dirpath = r"C:\Users\Administrator\Desktop\book" + "\\" + "a" + "\\" + "b"
        filepath = dirPath + "\\" + item['chapterName'] +".txt"
        if not os.path.exists(dirPath):
            os.makedirs(dirPath)
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(item['chapterContent'])
        return item

