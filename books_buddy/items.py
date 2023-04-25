# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksBuddyItem(scrapy.Item):
    # define the fields for your item here like:
    book_title = scrapy.Field()
    book_url = scrapy.Field()
    book_price = scrapy.Field()
    rating = scrapy.Field()
    cover = scrapy.Field()


