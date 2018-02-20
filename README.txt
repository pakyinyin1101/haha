
Sorry, I can't generate it in Openshift but it works in localhost.

app.py:It starts the program to open the server.It links the /cgi-bin/index.py.

/cgi-bin/index.py:It generates the Index page. It have function to upload photo,create account

/cgi-bin/login.py:It shows the website interface that prints the account.It asks for users to type their username and password.There are a submit button after they have finished typing the data.It sends usersname and password information to  
/cgi-bin/loginexe.py

/cgi-bin/loginexe.py:It reads the usersname and password from /cgi-bin/login.py.It checks the user input type is valid or not .If not,print error message and redirect to /cgi-bin/login.py.Then it visits the database "login.db.sqite" to check there are usersname match the input of users and the password is correct or not.If not,it prints error message and redirects to /cgi-bin/login.py.If username and password are correct, it generates cookie, the 'logout' button , 'change password' button(direct to /cgi-bin/update.py) and 'index page' button(direct to /cgi-bin/index.py).

/cgi-bin/create.py:It shows the website interface that is about register new account.It asks for users to type their username ,password and retype password.It sends those information to /cgi-bin/createexe.py.

/cgi-bin/createexe.py:It reads the usersname and password from /cgi-bin/create.py.It checks the user input type is valid or not.If not,print error message and redirect to /cgi-bin/login.py.Then it visits the database "login.db.sqite" to check there are usersname that is registered by others.If there exists username used,it prints error message and redirects to /cgi-bin/create.py.If not, it inserts the username and password to database "login.db.sqite". It also inserts username and default session var = -1 into databse"session.db.sqite".It generates the 'login' button (direct to /cgi-bin/login.py).

/cgi-bin/update.py:It reads the cookies to check which user visits this webpage.It prints current password,new password and retype password.It directs to /cgi-bin/updateexe.py to change password.

/cgi-bin/updateexe.py:It reads the current password, new password and new repassword from /cgi-bin/create.py.It updates username and password.

/cgi-bin/redirect.py:It deletes the cookies.

login.db.sqite:It stores usersname and password.

session.db.sqite:It stores username and their session.
-----------------------------------------------------------------------------------------------------------------------------
I spend many time to set up and cant uplaod the photoes.Therefore I only do milestones one.
