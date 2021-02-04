scrapy shell

fetch('<URL>')
response


#For Mitra Wiskey:
product_name = response.xpath('//span[@class="product-name"]/a/h2/text()').get()
product_name_content = response.xpath('//span[@class="product-name"]/a/h3/text()').get()
product_price_euro = response.xpath('//span[@class="vrkpr"]/text()').get().replace('.', '')
product_price_cents = response.xpath('//span[@class="cents"]/text()').get()
product_available = response.xpath('//div[@class="product-buttons"]/a/text()').get()


# out the scrapy shell, into the whiskeyscraper folder
# RUN THE PROJECT
scrapy crawl whiskey
scrapy crawl whiskey -O whiskey.json

