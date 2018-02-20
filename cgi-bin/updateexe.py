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

issetcookie =0
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
    	issetcookie=0
    elif(int(checksession[0]) == int(session)):
    	issetcookie = 1

except (Cookie.CookieError, KeyError):
    print''

def create_login_database(db_file):
	db_not_yet_create = not os.path.exists(db_file)
	conn = sqlite3.connect(db_file)
	if db_not_yet_create:
		sql='''create table if not exists LOGINDATA
		(USERID INTEGER PRIMARY KEY AUTOINCREMENT,
		USERNAME CHAR(20),
		PASSWORD CHAR(20));'''
		conn.execute(sql)
	return conn

def check_login_password(conn,user,word):
	cur=conn.cursor()
	sql='''SELECT PASSWORD FROM LOGINDATA WHERE USERNAME=?;'''
	cur.execute(sql,[user])
	dbpassword=cur.fetchone()
	if(dbpassword == None):
		return 0
	tmp=dbpassword[0]
	if(tmp == word):
		return 1
	else:
		return 0

def change_login_password(conn,user,word):
	sql='''UPDATE LOGINDATA SET PASSWORD = ? WHERE USERNAME=?;'''
	conn.cursor().execute(sql,[word,user])
	conn.commit()

if(issetcookie==1):
	conn=create_login_database('login_db.sqite')
	form=cgi.FieldStorage()

	try:
		sendcurpassword=form.getvalue('curpassword',None)
	except IndexError:
		sendcurpassword=None


	try:
		sendnewpassword=form.getvalue('newpassword',None)
	except IndexError:
		sendnewpassword=None

	try:
		sendnewrepassword=form.getvalue('newrepassword',None)
	except IndexError:
		sendnewrepassword=None


	if(sendnewpassword!= sendnewrepassword):
		print'password is not equal to sendrepassword!<br/>'
	if(sendcurpassword == None):
		print'Empty current password!<br/>' 
	
	if(sendnewpassword == None):
		print'Empty new password!<br/>'
	
	if(sendnewrepassword == None):
		print'Empty retype password!<br/>'

	if(sendcurpassword ==None or sendnewpassword==None or sendnewrepassword== None or sendnewpassword!= sendnewrepassword):
		print'''<form action="update.py" method="post">
	 	Please fill in again!
	 	Go to<input type ="submit" value="change password" name="submit" />
		</form>'''
	else:
		state=check_login_password(conn,usercookie,sendcurpassword)

	if(state==0):
		print'worngdata!<br/>'
		print'''<form action="update.py" method="post">
	 	Please fill in again!
	 	Go to<input type ="submit" value="change password" name="submit" />
		</form>'''
	elif(state==1):
		change_login_password(conn,usercookie,sendnewpassword)
		print'account success create!<br/>'
		print'''<form action="login.py" method="post">
	 	Go to<input type ="submit" value="login" name="submit" />
		</form>
		<form action="create.py" method="post">
	 	Create another account?<input type ="submit" value="register" name="submit" />
		</form>
		'''

print'</body></html>'