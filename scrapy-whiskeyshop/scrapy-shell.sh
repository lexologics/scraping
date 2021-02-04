scrapy shell

fetch('https://www.mitra.nl/webshop/groep/whisky/99-48-6C-B7-61-C4-31-A6')
#response

#response.css('div.product-info').get()

#products.css('span.product-name,a').get()
#products.css('span.product-name::text').get()

products = response.css('div.product-info,span.h2').getall()
product_price_euro = response.css('span.vrkpr').getall()
product_price_cents = response.css('span.cents').getall()
product_contents = response.css('span.product-content').getall()

print(response.css('span.product-name,a::text').get())
print(response.css('span.product-name,a').attrib['href'])

# out the scrapy shell, into the whiskeyscraper folder
# run the project
scrapy crawl whiskey
scrapy crawl whiskey -O whiskey.json



response.css('span.product-content,span.a::attr(href)').extract() 



