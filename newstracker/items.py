# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewstrackerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    desc = scrapy.Field()
    url = scrapy.Field()
    time = scrapy.Field()
    source = scrapy.Field()
    t_label = scrapy.Field()
    d_label = scrapy.Field()

    pass

#For DBCS
class BusinessItem(scrapy.Item):
    title = scrapy.Field()
    id = scrapy.Field()
    owner = scrapy.Field()
    deadline = scrapy.Field()
    pass

