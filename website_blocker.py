#!/usr/bin/env python3
'''
Block the local machine from websites in the list during normal office
hours to increase productivity.
Requires write access to the local hosts file so needs to be instantiated
from an elevated cmd prompt.
'''


import time
from datetime import datetime as dt


hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.reddit.com",
                "www.fark.com",
                "www.cnn.com",
                "www.abcnews.go.com",
                ]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(
            dt.now().year, dt.now().month, dt.now().day, 16):
        print('working hours....')
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()

    time.sleep(5)

