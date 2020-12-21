#!/usr/bin/env python3
"""
get_google_spf.py
Occasionally you'll need to allow the Google Console access to a Compute instance. In order to do that, you need to add its SPF records to your allow list.

But how to get the SPF records? You need nslookup, which has output that is great for humans but real bad for robots.

This script will allow you to retrieve the SPF records so that you can do with them what you will - incorporate them into your IAC? Knock it out.
"""

import subprocess

process = subprocess.Popen(["nslookup", "-q=TXT", "_spf.google.com", "8.8.8.8"], stdout=subprocess.PIPE)
# output = process.communicate()[0].split('\n')
output = process.communicate()[0].decode("utf-8").split('\n')[4].split('v=spf1 ')[1].split('~all')[0].split(' ')

for o in output:
# print(output)
    print(o.replace("include:",""))
