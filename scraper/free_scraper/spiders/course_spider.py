# -*- coding: utf-8 -*-
import scrapy, re, os, csv, smtplib, socket, sys, getpass
import os
from email.mime.text import MIMEText
from free_scraper.spiders.parsers.course_parser import parse_subjects

class course_spider(scrapy.Spider):
    """
    Scrape for defined list of courses and gets their seat status
    """
    name = 'course_spider'

    urls = [
        "https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=0"
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=parse_subjects)
