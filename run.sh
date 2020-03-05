#!/bin/bash
set -e
source venv/bin/activate
while true
do
	clear
    printf '\e[3J'
    date
    python -m scrapy crawl FreeEyeOut
    sleep 60
done
