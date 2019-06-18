#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
author:Herish
datetime:2019/3/20 14:22
software: PyCharm
description: 
'''

from scrapy import cmdline

# cmdline.execute("scrapy crawl airi_pic_spider".split(' '))
cmdline.execute("scrapy crawl jiandan_pic".split(' '))
