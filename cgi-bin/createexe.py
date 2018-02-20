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

def check_login_name(conn,user):
	cur=conn.cursor()
	sql='''SELECT USERNAME FROM LOGINDATA;'''
	cur.execute(sql)
	dbusername=cur.fetchone()
	if(dbusername == None):
		print 'valid account'
		return 1
	idlist=set(id.lower() for id in dbusername)
	if user.lower() in idlist:
		print 'exist username'
		return 0
	else:
		print'valid account'
		return 1

def insert_login_data(conn,user,word):
	sql='''INSERT INTO LOGINDATA(USERNAME,PASSWORD) VALUES(?,?);'''
	conn.cursor().execute(sql,[user,word])
	conn.commit()
	print'insert success!'

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

try:
	sendrepassword=form.getvalue('repassword',None)
except IndexError:
	sendrepassword=None

print sendrepassword
state=2
if(sendpassword!= sendrepassword):
	print'password is not equal to sendrepassword!<br/>'
if(sendusername == None):
	print'Empty username!<br/>' 
	
if(sendpassword == None):
	print'Empty password!<br/>'
	
if(sendrepassword == None):
	print'Empty retype password!<br/>'

if(sendusername ==None or sendrepassword==None or sendpassword== None or sendpassword!= sendrepassword):
	print'''<form action="create.py" method="post">
	 	Please fill in again!
	 	Go to<input type ="submit" value="register" name="submit" />
		</form>'''
else:
	state=check_login_name(conn,sendusername)

if(state==0):
	print'exist username!<br/>'
	print'''<form action="create.py" method="post">
	 	Please fill in again!
	 	Go to<input type ="submit" value="register" name="submit" />
		</form>'''
if(state==1):
	insert_login_data(conn,sendusername,sendpassword)
	conn2=create_session_database('session_db.sqite')
	sql='''INSERT INTO SESSIONDATA(USERNAME,SESSION) VALUES(?,-1);'''
	conn2.cursor().execute(sql,[sendusername])
	conn2.commit()
	print'account success create!<br/>'
	print'''<form action="login.py" method="post">
	 	Go to<input type ="submit" value="login" name="submit" />
		</form>
		<form action="create.py" method="post">
	 	Create another account?<input type ="submit" value="register" name="submit" />
		</form>
		'''

print'success'

print'</body></html>'
