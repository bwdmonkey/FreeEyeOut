#!/bin/bash
set -e
while true
do
	clear
    printf '\e[3J'
    date
    python -m scrapy crawl FreeEyeOut
    sleep 30
done
