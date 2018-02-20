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

def create_session_database(db_file):
	db_not_yet_create = not os.path.exists(db_file)
	conn2 = sqlite3.connect(db_file)
	if db_not_yet_create:
		print'Create a new session table!'
		sql='''create table if not exists SESSIONDATA
		(USERNAME CHAR(20),
		SESSION INTEGER);'''
		conn2.execute(sql)
	else:
		print'login table exist'
	return conn2

print'<html><body>'

issetcookie =0
state=2

try:
    cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
    print "session = " + cookie["session"].value
    print "user =" + cookie["user"].value
    session = cookie["session"].value
    usercookie = cookie["user"].value

    conn2 = create_session_database('session_db.sqite')
    cur=conn2.cursor()
    sql="SELECT SESSION FROM SESSIONDATA WHERE USERNAME =?;"
    cur.execute(sql,[usercookie])
    checksession = cur.fetchone()
    print checksession
    if(checksession==None):
    	print 'empty checksession'
    	issetcookie=0
    elif(int(checksession[0]) == int(session)):
    	print 'active cookie'
    	issetcookie = 1



	'''dbusername=cur.fetchone()
	if(dbusername == None):
		print 'valid account'
		return 1
	idlist=set(id.lower() for id in dbusername)
	if user.lower() in idlist:
		print 'exist username'
		return 0
	else:
		print'valid account'
		return 1'''


    

except (Cookie.CookieError, KeyError):
    print "session cookie not set!"

if(issetcookie==1):
	print'''
	<form action="updateexe.py" method="post">
	current password: <input type="password" name="curpassword"/><br/>
	password: <input type="password" name="newpassword"/><br/>
	retype password: <input type="password" name="newrepassword"/>
	<input type ="submit" value="change" name="submit" /><br/>
	</form>'''

	print'''
	<form action="index.py" method="post">
	see photo<input type ="submit" value="go photo" name="submit" /><br/>
	</form>'''

print '</body></html>'