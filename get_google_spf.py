#!/usr/bin/env python3
"""
get_google_spf.py
Occasionally you'll need to allow the Google Console access to a Compute instance. In order to do that, you need to add its SPF records to your allow list.

But how to get the SPF records? You need nslookup, which has output that is great for humans but real bad for robots.

This script will allow you to retrieve the SPF records so that you can do with them what you will - incorporate them into your IAC? Knock it out.

This version filters out the IPv6 records, but can be easily modified to do something else with them if you're into that whole thing.

Reference: https://support.google.com/a/answer/60764
"""

import subprocess

process = subprocess.Popen(['nslookup', '-q=TXT', '_spf.google.com', '8.8.8.8'], stdout=subprocess.PIPE)
output = process.communicate()[0].decode('utf-8').split('\n')[4].split('v=spf1 ')[1].split('~all')[0].split(' ')

google_ranges_final =[]
for o in output:
    spf_host = o.replace('include:','')
    if len(spf_host) > 0:
        spf_query = subprocess.Popen(['nslookup', '-q=TXT', spf_host, '8.8.8.8'], stdout=subprocess.PIPE)
        spf_host_ranges = spf_query.communicate()[0].decode('utf-8').split('\n')[4].split('v=spf1 ')[1].split('~all')[0].split(' ')
        for s in spf_host_ranges:
            if s.startswith('ip4'):
                google_ranges_final.append(s.replace('ip4:',''))
print("")
print(', '.join(google_ranges_final))
