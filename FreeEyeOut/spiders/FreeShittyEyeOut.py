# -*- coding: utf-8 -*-
import scrapy
import re
import os
import csv

# while true; clear && printf '\e[3J'; date; do scrapy runspider FreeShittyEyeOut.py; sleep 30; done

class FreeshittyeyeoutSpider(scrapy.Spider):
    name = 'FreeShittyEyeOut'
    allowed_domains = ['courses.students.ubc.ca']

    with open('watchlist.csv', 'rb') as f:
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
        print "----------------FreeShittyEyeOut by /u/leesw----------------"
        print "Course: ", title
        print "Total Seats Remaining: ",total_seats
        print "Currently Registered: ",registered_seats
        print "General Seats Remaining: ",general_seats
        print "Restricted Seats Remaining: ",restricted_seats
        # Change the seat types accordingly
        open_seats = bool(0 < int(general_seats))
        if open_seats:
            while open_seats:
                command = 'say "%s has free seats!"'%title
                os.system(command)
                print('%s has free seats!')%title
