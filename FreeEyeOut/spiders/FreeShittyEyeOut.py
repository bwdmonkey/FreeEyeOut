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
        'https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=5&dept=CHEM&course=121&section=102',
        'https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=5&dept=CHEM&course=121&section=110',
        'https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=5&dept=CHEM&course=121&section=111',
        'https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=5&dept=CHEM&course=121&section=122',
        'https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=5&dept=CHEM&course=121&section=133',
        'https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=5&dept=CHEM&course=121&section=188',
    ]
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
