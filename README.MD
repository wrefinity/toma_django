### Tomatoes prediction

#### note window users are expected to use gitbash terminal
```
# Create virtual env (Window/Mac)
python -m venv env

# activate enviroment (Mac/Linux)
source env/bin/activate

# activate enviroment (Window)
. env/Scripts/activate
```

## to run the project
```
# changer directory to toma
cd toma

pip install -r requirements.txt

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


# working with the project

```
# step 1
git clone https://github.com/wrefinity/toma_django.git

# step 2
cd toma && pip install -r requirements.txt

# step 3
python manage.py runserver
```