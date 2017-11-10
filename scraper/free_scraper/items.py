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

class SectionItem(scrapy.Item):
    """
    Stores a data on course section details
    course = {
        "url": *,
        "name": *,
        "subject": {
            "url": *,
            "name": *,
            "faculty": *,
        }
    }
    seats_data = {
        "total_remaining": *,
        "currently_registered": *,
        "general_remaining": *,
        "restricted_remaining": *,
    }
    """
    course = scrapy.Field()
    section = scrapy.Field()
    status = scrapy.Field()
    activity = scrapy.Field()
    url = scrapy.Field()
    seats_data = scrapy.Field()
