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

form=cgi.FieldStorage()



try:
	sendusername=form.getvalue('username',None)
except IndexError:
	sendusername=None




expiration = datetime.datetime.now() + datetime.timedelta(days=30)
cookie = Cookie.SimpleCookie()
cookie["session"] = random.randint(0,1000)
cookie["session"]["path"] = "/"
cookie["user"] = sendusername
cookie["user"]["path"] = "/"
cookie["session"]["expires"] = \
  expiration.strftime("%a, %d-%b-%Y %H:%M:%S PST")
cookie["user"]["expires"] = \
  expiration.strftime("%a, %d-%b-%Y %H:%M:%S PST")

print cookie.output()
print"Content-type:text/html\n\n"

print

cgitb.enable()

session=cookie["session"].value
print session

try:
    checksession = cookie["session"].value
    print'haha'
except (Cookie.CookieError, KeyError):
    print "session cookie not set!"

print'<html><body>'

def create_login_database(db_file):
	db_not_yet_create = not os.path.exists(db_file)
	conn = sqlite3.connect(db_file)
	if db_not_yet_create:
		print'Create a new login table!'
		sql='''create table if not exists LOGINDATA
		(USERID INTEGER PRIMARY KEY AUTOINCREMENT,
		USERNAME CHAR(20),
		PASSWORD CHAR(20));'''
		conn.execute(sql)
	else:
		print'login table exist'
	return conn

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


def check_login_data(conn,user,word):
	cur=conn.cursor()
	sql='''SELECT PASSWORD FROM LOGINDATA WHERE USERNAME=:user1;'''
	cur.execute(sql,{'user1':user})
	dbpassword=cur.fetchone()
	if(dbpassword == None):
		print 'no username exist'
		return 0
	tmp=dbpassword[0]
	if (word == tmp):
		print 'correct account!'
		return 1
	else:
		print'incorrect password'
		return 0

def delete_cookie():
	 print'<meta http-equiv="refresh" content="2;url=redirect.py">'

conn=create_login_database('login_db.sqite')

try:
	sendpassword=form.getvalue('password',None)
except IndexError:
	sendpassword=None

print sendpassword

if(sendusername == None):
	print'Empty username!<br/>' 
	
if(sendpassword == None):
	print'Empty password!<br/>'
	
if(sendusername ==None or sendpassword== None ):
	print'''<form action="login.py" method="post">
	 	Please fill in again!
	 	Go to<input type ="submit" value="login" name="submit" />
		</form>'''
	delete_cookie()

state=check_login_data(conn,sendusername,sendpassword)
if(state==0):
	print'no correct account data'
	delete_cookie()
if(state==1):
	conn2=create_session_database('session_db.sqite')
	sql='''UPDATE SESSIONDATA SET SESSION = ? WHERE USERNAME=?;'''
	conn2.cursor().execute(sql,[session,sendusername])
	conn2.commit()
	print'insert success!'
	print'''
	<form action="update.py" method="post">
	change password? <input type ="submit" value="change password" name="submit" />
	</form>'''

print'success'

print'</body></html>'

