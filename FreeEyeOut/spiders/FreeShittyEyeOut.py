# -*- coding: utf-8 -*-
import scrapy, re, os, csv, smtplib, socket, sys, getpass
from email.mime.text import MIMEText

# while true; clear && printf '\e[3J'; date; do scrapy runspider FreeShittyEyeOut.py; sleep 30; done

class FreeshittyeyeoutSpider(scrapy.Spider):
    name = 'FreeShittyEyeOut'
    allowed_domains = ['courses.students.ubc.ca']

    with open('./watchlist.csv', 'rb') as f:
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
            try:
                sendemail(title, response.url)
            except e:
                print e
def sendemail(course, url):
    receiver = "win981026@gmail.com"
    try:
        smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        print "Connection to Gmail Successfully"
        print "Connected to Gmail"
        try:
            # Sender
            gmail_user = "freeeyeout@gmail.com"
            gmail_pwd = "freeeyeout1"
            smtpserver.login(gmail_user, gmail_pwd)
            print "Login successful!"
        except smtplib.SMTPException:
            print "Authentication failed"
            smtpserver.close()
            getpass.getpass("Press ENTER to continue")
            sys.exit(1)
    except (socket.gaierror, socket.error, socket.herror, smtplib.SMTPException), e:
        print "Connection to Gmail failed"
        print e
        getpass.getpass("Press ENTER to continue")
        sys.exit(1)
    print "Composing email."
    sub = course +" has free seats!"
    bodymsg = course + " has free seats! Go register in the section before some other bastards takes it.\n"+url
    header = "To: "+receiver+"\n" + "From: "+gmail_user+"\n" + "Subject: " + sub + "\n"
    msg = header + "\n" + bodymsg + "\n\n"
    print "Email composed."
    try:
        print "Trying to send email."
        smtpserver.sendmail(gmail_user,receiver,msg)
        smtpserver.close()
        print "Email sent successfully!"
    except smtplib.SMTPException:
        print "Email could not be sent"
        smtpserver.close()
        getpass.getpass("Press ENTER to continue")
        sys.exit(1)
