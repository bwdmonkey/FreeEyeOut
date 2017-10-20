# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CourseItem(scrapy.Item):
    """
    Stores a data for a course including seats, etc
    """
    title = scrapy.Field()
    total_seats = scrapy.Field()
    registered_seats = scrapy.Field()
    general_seats = scrapy.Field()
    restricted_seats = scrapy.Field()
    url = scrapy.Field()