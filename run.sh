#!/bin/bash
while true
do
	clear
    printf '\e[3J'
    date
    python -m scrapy crawl FreeEyeOut
    sleep 15
done
