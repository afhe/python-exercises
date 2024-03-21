# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
import json
from ..items import SurfboardempireItem

# i. Sku_name
# ii. Product_id
# iii. Brand
# iv. Product_url

class SurfboardEmpireSpider(scrapy.Spider):
    name = 'surfboardempire'
    page_number = 1 
    start_urls = [f'https://www.surfboardempire.com.au/products.json?page=1']

    def parse(self, response):
        url = response.url
        
        json_res = json.loads(response.text)

        if len(json_res['products']) == 0:
            return

        for p in json_res['products']:
            url = f"https://surfboardempire.com.au/collections/{p['product_type']}/products/{p['handle']}"
            yield SurfboardempireItem({
                "sku_name": p['title'],
                "product_id": p['id'],
                "product_url": url,
                "brand": p['vendor'], 
            })


        self.page_number += 1 
        next_url = f'https://www.surfboardempire.com.au/products.json?page={self.page_number}'
        yield response.follow(next_url, callback=self.parse)