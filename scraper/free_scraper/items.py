# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# class SectionItem(scrapy.Item):
#     """
#     Stores a data for a course including seats, etc
#     """
#     title = scrapy.Field()
#     total_seats = scrapy.Field()
#     registered_seats = scrapy.Field()
#     general_seats = scrapy.Field()
#     restricted_seats = scrapy.Field()
#     url = scrapy.Field()

class CourseItem(scrapy.Item):
    """
    Stores data about a course and associated subject
    SubItems: ScrapySectionItem, ScrapySubjectItem
    """
    subject = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    # section = scrapy.SectionItem() How do I link the two?

class SectionItem(scrapy.Item):
    """
    Stores a data on course section details
    """
    status = scrapy.Field()
    section = scrapy.Field()
    url = scrapy.Field()
    activity = scrapy.Field()
