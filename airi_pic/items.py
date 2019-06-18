# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#仅下载百度贴吧的一个贴子中的图片，参考网址：http://aljun.me/post/6
class AiriPicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    airi_image_url = scrapy.Field()
    images = scrapy.Field()#这个是ImagesPipeline默认的

#爬取煎蛋网图片
class JiandanPicItem(scrapy.Item):
    image_url = scrapy.Field()
    image_name = scrapy.Field()
