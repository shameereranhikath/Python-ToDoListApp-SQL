# Python-ToDoListApp-SQL
To Do List App using SQL Server

ToDoList web application using Python django administration link is http://127.0.0.1:8000/admin Username is admin password is admin django 

Website Link is http://127.0.0.1:8000/ToDoList/

About the App Sql Server 2012 Database is used Django is the framework used in this App

After loading the Application in Visual studio code,
First change the HOSTNAME,USERID,PASSWORD of the sql server in database section of the settings files of the project
Then run database migrations using the command

python manage.py  makemigrations

python manage.py migrate

The Database will be automatically generated in SQL Server 2012 by Django

