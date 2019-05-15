# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbUrlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    imdbRate = scrapy.Field()
    imdbId = scrapy.Field()
    storyLines = scrapy.Field()
    directors = scrapy.Field()
    stars = scrapy.Field()
    time = scrapy.Field()
    languages = scrapy.Field()
    genres = scrapy.Field()
    title = scrapy.Field()
    year = scrapy.Field()
    pass
