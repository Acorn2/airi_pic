# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request


# class AiriPicPipeline(ImagesPipeline):
#     def get_media_requests(self, item, info):
#         for image_url in item['airi_image_url']:
#             yield Request(image_url)
#
#     def item_completed(self, results, item, info):
#         image_paths = [x['path'] for ok,x in results if ok]
#         if not image_paths:
#             raise DropItem('图片未下载好')
#         return item


class JiandanPicPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        item = request.meta.get('item')#注意注意注意！！！，这里有坑，不能再使用request.meta['item']
        index = request.meta.get('index')
        # print(request.url)
        # print(index)
        image_name = item['image_name'][index] + '.' + request.url.split('/')[-1].split('.')[-1]
        file_name = "{0}/{1}".format('jiandan',image_name)

        return file_name

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('图片未下载好')
        return item

    def get_media_requests(self, item, info):
        for image_url in item['image_url']:
            yield Request(image_url, meta={'item': item, 'index': item['image_url'].index(image_url)})
