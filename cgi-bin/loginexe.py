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

print"Content-type:text/html\n\n"
print

cgitb.enable()

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


conn=create_login_database('login_db.sqite')
form=cgi.FieldStorage()

try:
	sendusername=form.getvalue('username',None)
except IndexError:
	sendusername=None

print sendusername

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

state=check_login_data(conn,sendusername,sendpassword)

print'success'

print'</body></html>'