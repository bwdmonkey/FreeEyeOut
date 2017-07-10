import scrapy
import re

class SSCScraper(scrapy.Spider):
    name = 'sscscrape'
    allowed_domains = ['courses.students.ubc.ca']
    start_urls = [
    # EDIT HERE USE THE SIMILAR FORMAT
        'https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=5&dept=CPSC&course=110&section=101',
    ]

    def parse(self, response):
        seats = response.css('table.\\27table').extract_first()
        seats = re.split("\D",seats)
        seats = filter(None, seats)
        print "----------------FreeShittyEyeOut by /u/leesw----------------"
        print "Seat Summary"
        print "Total Seats Remaining: ",seats[2]
        print "Currently Registered: ",seats[4]
        print "General Seats Remaining: ",seats[6]
        print "Restricted Seats Remaining: ",seats[8]
        print "----------------FreeShittyEyeOut by /u/leesw----------------"
