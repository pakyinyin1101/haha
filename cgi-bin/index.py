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

def create_session_database(db_file):
	db_not_yet_create = not os.path.exists(db_file)
	conn2 = sqlite3.connect(db_file)
	if db_not_yet_create:
		sql='''create table if not exists SESSIONDATA
		(USERNAME CHAR(20),
		SESSION INTEGER);'''
		conn2.execute(sql)
	return conn2

print"Content-type:text/html\n\n"
print

cgitb.enable()

print'<html><body>'

correctcookie =0
state=2

try:
    cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
    session = cookie["session"].value
    usercookie = cookie["user"].value
    conn2 = create_session_database('session_db.sqite')
    cur=conn2.cursor()
    sql="SELECT SESSION FROM SESSIONDATA WHERE USERNAME =?;"
    cur.execute(sql,[usercookie])
    checksession = cur.fetchone()
    if(checksession==None):
    	correctcookie=0
    elif(int(checksession[0]) == int(session)):
    	correctcookie = 1

except (Cookie.CookieError, KeyError):
		print''

print'''
<form enctype="multipart/form-data" action="upload.py" method="POST">
    Choose an image (.jpg .gif .png): <br />
    <input type="file" name="pic" accept="image/gif, image/jpeg, image/png" /><br />
    <input type="submit" value="Upload" />
</form>'''

if(correctcookie==1):
	print'''<form action="clear.py" method="POST">
    <input type="submit" value="logout" />
	</form>
	'''
elif(correctcookie==0):
	print'''<form action="login.py" method="POST">
    <input type="submit" value="login" />
	</form>
	'''

print'</body></html>'