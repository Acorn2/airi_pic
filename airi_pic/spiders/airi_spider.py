#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
author:Herish
datetime:2019/3/20 14:23
software: PyCharm
description: 
'''
import scrapy
from airi_pic.items import AiriPicItem

class AiriPicSpider(scrapy.Spider):
    name = 'airi_pic_spider'

    start_urls = ['http://tieba.baidu.com/p/4023230951']

    def parse(self,response):
        sel = scrapy.Selector(response)

        image_url = sel.xpath('//div[@id="post_content_75283192143"]/img[@class="BDE_Image"]/@src').extract()

        item = AiriPicItem()
        item['airi_image_url'] = image_url

        yield item