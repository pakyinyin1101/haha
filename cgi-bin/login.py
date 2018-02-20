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

print 'Content-Type: text/html'
print

cgitb.enable()

print'<html><body>'

print'''
<form action="loginexe.py" method="post">
username: <input type="text" name="username"/><br/>
password: <input type="password" name="password"/><br/>
<input type ="submit" value="login" name="submit" /><br/>
</form>'''

print'''
<form action="create.py" method="post">
No account? <input type ="submit" value="sign up" name="submit" />
</form>'''

print '</body></html>'