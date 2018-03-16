# -*- coding: utf-8 -*-
import scrapy
from doubanMovieTop250.items import Doubanmovietop250Item


class DoubanMovieSpider(scrapy.Spider):
    name = 'douban_movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250?start=0']

    def parse(self, response):
        movies = response.xpath('//ol[@class="grid_view"]/li/div[@class="item"]')
        for movie in movies:
            item = Doubanmovietop250Item()
            item['name'] = movie.xpath('./div[@class="info"]/div[@class="hd"]/a/span[@class="title"]/text()').extract_first()
            item['info'] = (movie.xpath('./div[@class="info"]/div[@class="bd"]/p/text()').extract_first()).strip()
            item['rating'] = movie.xpath('./div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract_first()
            item['num'] = movie.xpath('./div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[last()]/text()').extract_first()
            quote = movie.xpath('./div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span[@class="inq"]/text()')
            if quote is not None:
                item['quote'] = quote.extract_first()
            else:
                item['quote'] = ' '
            item['img_url'] = movie.xpath('./div[@class="pic"]/a/img/@src').extract_first()
            yield item
            
        pages = ['https://movie.douban.com/top250?start={}'.format(str(n)) for n in range(25,226) if n%25==0]
        for url in pages:
            yield scrapy.Request(url, callback=self.parse)