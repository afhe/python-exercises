# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SurfboardempireItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    sku_name = scrapy.Field()
    product_id = scrapy.Field()
    product_url = scrapy.Field()
    brand = scrapy.Field()

