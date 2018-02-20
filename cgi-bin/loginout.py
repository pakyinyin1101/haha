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
<form action="createexe.py" method="post">
username: <input type="text" name="username"/><br/>
password: <input type="password" name="password"/><br/>
retype password:  <input type="password" name="repassword"/><br/>
<input type ="submit" value="register" name="submit" /><br/>
</form>'''

print'''
<form action="login.py" method="post">
Have an account already? <input type ="submit" value="login" name="submit" />
</form>'''

print '</body></html>'