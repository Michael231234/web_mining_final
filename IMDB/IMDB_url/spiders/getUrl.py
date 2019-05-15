# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
import re
from ..items import ImdbUrlItem
import time


class GeturlSpider(scrapy.Spider):
    start = time.clock()
    name = 'getUrl'
    allowed_domains = ['imdb.com']

    def start_requests(self):
        data = pd.read_csv('/Users/konglingtong/PycharmProjects/web_mining/new.csv')
        movies = data['imdbId']
        j = 0
        for i in movies:
            while len(str(i)) < 7:
                i = '0' + str(i)
                if len(i) == 7:
                    movie_url = 'https://www.imdb.com/title/tt%s' % i
                    j += 1
                    if (j % 100) == 0:
                        time.sleep(5)
                    yield scrapy.Request(url=movie_url, callback=self.parse)

    def parse(self, response):
        items = []
        item = ImdbUrlItem()
        url = response.url
        id = re.compile(r'\d+').findall(url)[0]
        item['imdbId'] = int(id)
        item['imdbRate'] = response.css('.ratingValue strong:nth-child(1) span:nth-child(1)::text').extract()[0]
        item['storyLines'] = response.css('div.inline:nth-child(3) p:nth-child(1) span::text').extract()
        item['directors'] = response.css('div.credit_summary_item:nth-child(2) a::text').extract()
        stars = response.css('div.credit_summary_item:nth-child(4) a::text').extract()
        genres = response.css('.subtext a::text').extract()
        item['year'] = genres.pop(-1)
        item['genres'] = genres
        item['title'] = response.css('.title_wrapper h1:nth-child(1)::text').extract()[0]
        if len(stars) == 0:
            new_stars = response.css('div.credit_summary_item:nth-child(3) a::text').extract()
            if 'See full cast & crew' in new_stars:
                new_stars.remove('See full cast & crew')
            item['stars'] = new_stars
        else:
            if 'See full cast & crew' in stars:
                stars.remove('See full cast & crew')
            item['stars'] = stars
        item['time'] = response.css('.subtext time:nth-child(2)::text').extract()
        languages = response.css('#titleDetails div:nth-child(5) a::text').extract()
        if languages[0] == 'See more':
            item['languages'] = response.css('div.txt-block:nth-child(4) a::text').extract()
        else:
            item['languages'] = response.css('#titleDetails div:nth-child(5) a::text').extract()
        items.append(item)
        yield item

    stop = time.clock()
    print(stop - start)
