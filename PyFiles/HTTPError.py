#!/usr/bin/env python3
import urllib
import urllib.error
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import urllib.request

req = urllib.request.Request('http://www.python.org/fish.html')
try:
    urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.read())
