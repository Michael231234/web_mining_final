from scrapy.cmdline import execute
execute(['scrapy', 'crawl', 'getUrl', '-o', 'IMDb1.csv', '-t', 'csv'])