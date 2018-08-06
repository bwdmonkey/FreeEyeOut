# -*- coding: utf-8 -*-
import scrapy
import re
import os
import csv


class FreeeyeoutSpider(scrapy.Spider):
    name = 'FreeEyeOut'
    allowed_domains = ['courses.students.ubc.ca']
    csv_path = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'watchlist.csv')
    start_urls = []
    with open(csv_path) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            start_urls.append(row[0])

    def parse(self, response):
        title = response.css("h4::text").extract_first()
        seats = response.css('table.\\27table').extract_first()
        seats = re.split("\D",seats)
        seats = filter(None, seats)
        print "----------------FreeEyeOut by /u/leesw----------------"
        print "Course: ", title
        print "Total Seats Remaining: ",seats[2]
        print "Currently Registered: ",seats[4]
        print "General Seats Remaining: ",seats[6]
        print "Restricted Seats Remaining: ",seats[8]
        open_seats = bool(0 < int(seats[6]))
        if open_seats:
            print(title + " has free seats!")
            while open_seats:
                command = 'say "%s has free seats!"'%title
                os.system(command)
