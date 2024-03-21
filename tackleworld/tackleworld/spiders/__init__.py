import scrapy
from ..items import TackleWorldItem

# Navigates through the top level-menu (ie Reels, Rods, etc) and loops through
# the submenu items within (ie Spinning Reels, Baitcast Reels, etc). This should be
# completed using xpaths
# b. Visits the category page and loops through each product tile on the page
# c. Yields an item for each product with the following fields:
# i. Sku_name
# ii. Image_url
# iii. Price_now
# iv. Price_was
# v. Product_url

class TackleWorldSpider(scrapy.Spider):
    name = 'tackleworld'

    start_urls = ['https://tackleworldadelaide.com.au/']

    def parse(self, response):
        top_level_links = response.xpath("//*[contains(@class, 'navPage-subMenu-button')]//a/@href").getall()

        yield from response.follow_all(top_level_links, self.parse_subpage)

    def parse_subpage(self, response):
        products = response.css('article.card')

        for p in products: 
            sku_name = p.css('div.card-body > h4 > a::text').get()
            image_url = p.css('figure.card-figure > a ::attr(src)').get()
            product_url = p.css('div.card-body > h4 > a ::attr(href)').get()
            prices = p.css('div.card-body > div.card-text > div > span::text').getall()
            price_now = prices[0]
            price_was = None if len(prices) == 1 else prices[1]
            yield TackleWorldItem({
                "sku_name": sku_name,
                "image_url": image_url,
                "product_url": product_url, 
                "price_now": price_now,
                "price_was": price_was,
            })
