# FreeEyeOut
Open Script of Slacknotes/EyeOut For macOS by @leesw98

Note: Definitely not as good as the original but it works! :)

## Requirement
 - Python==2.7.10

## Instruction
1. Get to the "FreeEyeOut" directory on Terminal. Not FreeEyeOut-master
```
cd <path-to-directory>
```
2. Install the required libraries. Use the following command.
```
pip install -r requirements.txt
```
3. Get to the "spiders" directory on Terminal.
```
cd /spiders
```
4. Edit the "FreeShittyEyeOut.py", the type of seats, and the start_urls for your use. 
5. Run the script using the following script. 
```
while true; clear && printf '\e[3J'; date; do scrapy runspider FreeShittyEyeOut.py -s LOG_ENABLED=False; sleep <seconds>; done
```
Note: If you can edit the last line into Windows/Linux equivalent, please let me know. :)



