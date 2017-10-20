# -*- coding: utf-8 -*-
import scrapy, re, os, csv, smtplib, socket, sys, getpass
from email.mime.text import MIMEText
from FreeEyeOut.items import CourseItem

# while true; clear && printf '\e[3J'; date; do scrapy runspider FreeShittyEyeOut.py; sleep 30; done

class FreeshittyeyeoutSpider(scrapy.Spider):
    name = 'FreeShittyEyeOut'
    allowed_domains = ['courses.students.ubc.ca']

    with open('../../watchlist.csv', 'rb') as f:
        reader = csv.reader(f)
        array_list = list(reader)

    start_urls = []
    for value in array_list:
        start_urls.append(value[0])

    def parse(self, response):
        title = response.css("h4::text").extract_first()
        seats = response.css('table.\\27table').extract_first()
        seats = re.split("\D",seats)
        seats = filter(None, seats)
        total_seats = seats[2]
        registered_seats = seats[4]
        general_seats = seats[6]
        restricted_seats = seats[8]

        # TODO: more details, ie section number, time, professor
        return CourseItem(
            title=title,
            total_seats=total_seats,
            registered_seats=registered_seats,
            general_seats=general_seats,
            restricted_seats=restricted_seats,
            url=response.rule
        )
    