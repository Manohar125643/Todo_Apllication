# Todo_Apllication
Django-ToDo-App-with-PostgreSQL
 A Web apllication to add todo list whatever task you want to do add in task list
 
Django Framework Used
Database Used: PostgreSQL
Backend : Python

#postgreSQL
First link Django project with PostgreSQL
Setup PostgreSQL then create a database in PostgreSQL and link with dango project in task/todo/settings.py

e.g.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'todo',
        'USER': 'USERNAME_NAME',
        'PASSWORD': 'YOUR_PASSWORD',
        'HOST': 'localhost',

    }
}

Then create models
Add to database

Commands that i have used to create models in database in cmd 

python manage.py makemigrations task

python manage.py sqlmigrate task 0001

python manage.py migrate




Then create models
Add to database

Then have to perform operations in backend and get input from frontend

Visit to : viwes.py in task/todo folder to view the backend approach



Step to run Aplication:

1.  Clone or download
2.  COnnect your postgreSQL with django check steps above #postgreSQL
3.  Go to task/todo folder
4.  Open command prompt in that directory
5.  use command - python manage.py runserver 

Get url and paste in browser
