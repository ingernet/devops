#!/usr/bin/env python3
"""
fail2ban_report.py
I parse fail2ban logs looking for instances of IPs that were banned.
I tally them up and display only those that have attacked us more than 100 times.
(Otherwise, the output would just be toooooo much.)
"""

import subprocess
import glob

# change ban_log_path if your fail2ban log files live somewhere else for some reason
ban_log_path = '/var/log/fail2ban.log*'



banned_ips = {
}

def inc_count(ip):
    """If IP already exists in banned_ips dict, increment its frequency by one. """
    Otherwise, just add it.
    if ip in banned_ips.keys():
        banned_ips[ip] = int(banned_ips[ip]) + 1
    else:
        banned_ips[str(ip)] = int(1)


# Assemble your command.
args = ['zgrep', ' Ban ']
args.extend(glob.glob(ban_log_path))

# Run your zgrep - this will search both gzipped files and uncompressed files
banresult = subprocess.check_output(args).split(b'\n')
while('' in banresult):
    banresult.remove('')

for x in banresult:
    if len(x.decode().split("Ban ")) > 1:
        inc_count(x.decode().split("Ban ")[1])

# sort your list of banned IPs from highest to lowest.
q = sorted(banned_ips.items(), key=lambda item: item[1], reverse=True)
print("{} IPs have hit us in the last month; the ones listed below hit us more than 100 times:".format(len(q)))
for key, value in q:
    if value > 100:
        print(key, ":", value)


