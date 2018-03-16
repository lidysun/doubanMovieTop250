# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Doubanmovietop250Item(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()#名字
    info = scrapy.Field() #信息
    rating = scrapy.Field() #评分
    num = scrapy.Field() #评论人数
    quote = scrapy.Field() #经典语句
    img_url = scrapy.Field() #电影图片
    pass
