# -*- coding: utf-8 -*-
import scrapy
import re
import os


class FreeshittyeyeoutSpider(scrapy.Spider):
    name = 'FreeShittyEyeOut'
    allowed_domains = ['courses.students.ubc.ca']
    start_urls = [
    # EDIT HERE USE THE SIMILAR FORMAT
        'https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=5&dept=CPSC&course=110&section=101',
        'https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=5&dept=CPSC&course=110&section=103',
        'https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=5&dept=CPSC&course=110&section=104',
        'https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=5&dept=CPSC&course=121&section=201',
        'https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=5&dept=CPSC&course=121&section=202',
        'https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=5&dept=CPSC&course=121&section=203',
        'https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=5&dept=CPSC&course=210&section=201',
        'https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=5&dept=CPSC&course=210&section=202',
        'https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=5&dept=CPSC&course=210&section=203',
    ]
    def parse(self, response):
        title = response.css("h4::text").extract_first()
        seats = response.css('table.\\27table').extract_first()
        seats = re.split("\D",seats)
        seats = filter(None, seats)
        print "----------------FreeShittyEyeOut by /u/leesw----------------"
        print "Course: ", title
        print "Total Seats Remaining: ",seats[2]
        print "Currently Registered: ",seats[4]
        print "General Seats Remaining: ",seats[6]
        print "Restricted Seats Remaining: ",seats[8]
        open_seats = bool(0 < int(seats[6]))
        if open_seats:
            while open_seats:
                command = 'say "%s has free seats!"'%title
                os.system(command)
                print seats[6]
                print open_seats
                print('\a\a\a')
