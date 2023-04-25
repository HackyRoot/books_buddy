import scrapy
from books_buddy.items import BooksBuddyItem


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        for product in response.css(".product_pod"):
            item = BooksBuddyItem()
            item["book_title"] = product.css('h3 a::attr(title)').get()
            item["book_url"] = product.css('h3 a::attr(href)').get()
            item["book_price"] = product.css('.price_color::text').get()
            item["rating"] = product.css('p::attr(class)').get().split()[-1]
            item["cover"] = product.css('img::attr(src)').get()
            yield item

        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(url=next_page, callback=self.parse)