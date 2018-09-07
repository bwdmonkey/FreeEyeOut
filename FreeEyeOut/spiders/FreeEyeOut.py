# -*- coding: utf-8 -*-
from os import path, system
from services.mailer import Mailer
import scrapy
import re
import csv


class FreeeyeoutSpider(scrapy.Spider):
    name = 'FreeEyeOut'
    allowed_domains = ['courses.students.ubc.ca']

    def __init__(self, *args, **kwargs):
        self.csv_path = path.join(path.abspath(path.dirname(path.dirname(__file__))), 'watchlist.csv')
        self.mailing_list = {}
        self.start_urls = []
        with open(self.csv_path) as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                self.start_urls.append(row[0])
                self.mailing_list[row[0]] = row[1:]
        super(FreeeyeoutSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        url = response.request.url
        title = response.css("h4::text").extract_first()
        seats = response.css('table.\\27table').extract_first()
        seats = re.split("\D",seats)
        seats = filter(None, seats)
        print "----------------FreeEyeOut by /u/leesw----------------"
        print "Course: ", title
        print "Total Seats Remaining: ", seats[2]
        print "Currently Registered: ", seats[4]
        print "General Seats Remaining: ", seats[6]
        print "Restricted Seats Remaining: ", seats[8]
        open_seats = bool(0 < int(seats[6]))
        if open_seats:
            print(title + " has free seats!")
            target_emails = self.mailing_list[url]
            Mailer(title, url, target_emails).alert()
            while open_seats:
                command = 'say "%s has free seats!"' % title
                system(command)
