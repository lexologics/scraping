import scrapy
#from whiskyscraper.items import WhiskyscraperItem
from scrapy.loader import ItemLoader


class WhiskeySpider(scrapy.Spider):
    name = 'whiskey'
    start_urls = ['https://www.mitra.nl/webshop/groep/whisky/99-48-6C-B7-61-C4-31-A6']

    def parse(self, response):
        for products in response.css('div.product-info'):
            yield {
                'product_name': response.xpath('//span[@class="product-name"]/a/h2/text()').get(),
                'product_name_content': response.xpath('//span[@class="product-name"]/a/h3/text()').get(),
                'product_price_euro': response.xpath('//span[@class="vrkpr"]/text()').get().replace('.', ''),
                'product_price_cents': response.xpath('//span[@class="cents"]/text()').get(),
                'product_available': response.xpath('//div[@class="product-buttons"]/a/text()').get()
            }

# response.xpath('//span/a/text()').getall()   
# response.xpath('//span').getall()
# response.css('div.product-info').xpath('a').getall()
# 

#response.xpath('//span[@class="product-name"]/a/h2/text()').get()
#response.xpath('//span[@class="product-name"]/a/h3/text()').get()
#test = str(response.xpath('//span[@class="product-name"]/a/h2/text()').get()) + ' - ' + str(response.xpath('//span[@class="product-name"]/a/h3/text()').get())

# product_name = response.xpath('//span[@class="product-name"]/a/h2/text()').get()
# product_name_content = response.xpath('//span[@class="product-name"]/a/h3/text()').get()
# product_price_euro = response.xpath('//span[@class="vrkpr"]/text()').get().replace('.', '')
# product_price_cents = response.xpath('//span[@class="cents"]/text()').get()
# product_available = response.xpath('//div[@class="product-buttons"]/a/text()').get()