#!/usr/bin/env python3
import requests, sys

if len(sys.argv) != 3:
    print("Usage: %s YEAR DAY" % (sys.argv[0],))
    sys.exit(1)

y, d = sys.argv[1], sys.argv[2]
filename = '%s/dec%s/input.txt' % (y, d)
url = "https://adventofcode.com/%s/day/%s/input" % (y, d)

with open('cookie.txt', 'r') as f:
    cookie = f.read().rstrip()

res = requests.get(url, headers={"Cookie": cookie}).text

with open(filename, 'w+') as f:
    f.write(res.rstrip())
