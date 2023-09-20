### MAC USERS
```
# Create virtual env
python3 -m venv env
# activate enviroment
source env/bin/activate
```

## to run the project
```
cd toma && pip install -r requirements.txt
python manage.py runserver
```



####  for django app creation for all users
```
# install django
python3 -m pip install Django djangorestframework
# check django version
django-admin --version

# create django app
django-admin startproject my_app

# run server 
cd my_app
python3 manage.py runserver
```