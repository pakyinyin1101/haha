#!/usr/bin/python

import Cookie
import datetime
import random
import os
import cgi
import cgitb
import subprocess
import sys
import sqlite3
from os import listdir, getcwd

expiration = datetime.datetime.now() + datetime.timedelta(days=-30)
try:
    cookie = Cookie.SimpleCookie(os.environ['HTTP_COOKIE'])
except KeyError:
    cookie = Cookie.SimpleCookie()

cookie["session"]["expires"] = \
  expiration.strftime("%a, %d-%b-%Y %H:%M:%S PST")
cookie["user"]["expires"] = \
  expiration.strftime("%a, %d-%b-%Y %H:%M:%S PST")

print cookie.output()
print "Content-type: text/html"

print
print '<html><body>'


print'<meta http-equiv="refresh" content="2;url=login.py">'

print '</body><html>'