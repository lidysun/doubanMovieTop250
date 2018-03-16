# -*- coding: utf-8 -*-
import pymysql
import pymongo
import settings
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# MySQL
# class Doubanmovietop250Pipeline(object):
#     def __init__(self):
#         self.connect = pymysql.connect(
#             host = settings.MYSQL_HOST,
#             database = settings.MYSQL_DBNAME,
#             user = settings.MYSQL_USER,
#             password = settings.MYSQL_PASSWD,
#             charset = 'utf8',
#             use_unicode = True
#         )
#
#         self.cursor = self.connect.cursor()
#
#     def process_item(self, item, spider):
#         try:
#             #查看数据
#             self.cursor.execute(
#                 '''select * from blog_doubanmovie where img_url = %s''',
#                 item['img_url']
#             )
#             repetion = self.cursor.fetchone()
#             #重复
#             if repetion:
#                 pass
#             else:
#                 #插入数据
#                 self.cursor.execute("INSERT INTO blog_doubanmovie(name,info,rating,num,quote,img_url) VALUES(%s,%s,%s,%s,%s,%s)",
#                                     (item['name'],item['info'],item['rating'],item['num'],item['quote'],item['img_url'])
#                 )
#                 #提交sql
#                 self.connect.commit()
#         except Exception as error:
#             #错误
#             print error
#             self.connect.rollback()
#         return item

#MONGODB
class Doubanmovietop250Pipeline(object):
    def __init__(self):
        self.client  = pymongo.MongoClient(
            host=settings.MONGO_HOST,
            port = settings.MONGO_PORT,
            connect=True
        )
        self.client.admin.authenticate(settings.MONGO_USER,settings.MONGO_PSW)
        
        self.db = self.client[settings.MONGO_DB]
        self.coll = self.db[settings.MONGO_COLL]
        
    def process_item(self, item, spider):
        postItem = dict(item)
        try:
            self.coll.insert(postItem)
            # query_item = self.coll.find({'img_url':postItem['img_url']})
            # print query_item,'query item is not in db !'
            # if query_item:
            #     pass
            # else:
            #     self.coll.insert(postItem)
        except Exception as error:
            print error
        return item
