# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import smtplib, getpass, sys, socket
from free_scraper.items import SectionItem
from free_scraper.settings import SENDER_GMAIL, SENDER_PWD

class EmailAlertPipeline(object):
    """
    Send relevant data to Email address
    """
    RECEIVER = "win981026@gmail.com"
    SMTPSERVER = smtplib.SMTP("smtp.gmail.com", 587)

    def __init__(self, server=SMTPSERVER):
        """
        Setup connection to Gmail when server opens
        """
        try:
            server.ehlo()
            server.starttls()
            server.ehlo()
            print "Connection to Gmail Successfully"
            print "Connected to Gmail"
            server.login(SENDER_GMAIL, SENDER_PWD)
            print "Login successful!"
        except Exception as e:
            print "Connection to Gmail failed"
            print e
            getpass.getpass("Press ENTER to continue")
            sys.exit(1)

    def close_spider(self, spider, server=SMTPSERVER):
        """
        Close connection when spider closes
        """
        print "Closing spider and connection."
        if server:
            server.close()

    def process_item(self, item, spider):
        """
        Process incoming items
        """
        # Change the seat types accordingly
        open_seats = bool(0 < int(item['seats_data']['general_seats']))
        if open_seats:
            try:
                title = item['course']['name'] + item['section']
                self.__send_email(title, item['url'])
            except Exception as e:
                print e

        return item

    def __send_email(self, course, url, server=SMTPSERVER):
        """
        Format and send email
        """
        print "Composing email."
        sub = course +" has free seats!"
        bodymsg = course + " has free seats! Go register in the section before some other bastards takes it.\n"+url
        header = "To: "+self.RECEIVER+"\n" + "From: "+SENDER_GMAIL+"\n" + "Subject: " + sub + "\n"
        msg = header + "\n" + bodymsg + "\n\n"
        print "Email composed."
        try:
            print "Trying to send email."
            server.sendmail(SENDER_GMAIL,self.RECEIVER,msg)
            print "Email sent successfully!"
        except smtplib.SMTPException:
            print "Email could not be sent"

class ConsoleLogPipeline(object):
    """
    Outputs CourseItem data to console
    """
    def process_item(self, item, spider):
        if isinstance(item, CourseItem):
            print "----------------FreeShittyEyeOut by /u/leesw----------------"
            print "Course: ", item['title']
            print "Total Seats Remaining: ", item['total_seats']
            print "Currently Registered: ", item['registered_seats']
            print "General Seats Remaining: ", item['general_seats']
            print "Restricted Seats Remaining: ", item['restricted_seats']
        return item
