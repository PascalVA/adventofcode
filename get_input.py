#!/usr/bin/env python3

import requests
import sys

from os.path import dirname, isdir, realpath
from pathlib import Path

if len(sys.argv) != 2:
    print("Usage: %s DAY" % (sys.argv[0],))
    sys.exit(1)

y, d = 2020, int(sys.argv[1])

with open('cookie.txt', 'r') as f:
    cookie = f.read().rstrip()

res = requests.get(
    f"https://adventofcode.com/{y}/day/{d}/input",
    headers={"Cookie": cookie}
).text

filepath = f'{y}/{d:02d}/input.txt'
dirpath = realpath(dirname(filepath))
if not isdir(dirpath):
    Path(dirpath).mkdir(parents=True, exist_ok=True)

with open(filepath, 'w+') as f:
    f.write(res.rstrip())
