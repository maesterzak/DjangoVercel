# Django on Vercel
This is a simple project developed using Django framework and it contains the settings required for successfull deployment of Django projects on Vercel.
## Setup

Below are the steps to follow to setup this project locally on your machine;

* Clone the project locally on your machine using **git clone**
* Create and activate a new virtual enviroment.
* To install dependencies run
```
pip install -r requirements.txt
```
* Go to the projects setting.py file and remove the comments in the database section.

* In your terminal execute the following commands to makemigrations and migrate to database

```
python manage.py makemigrations
python manage.py migrate
```

## Using PostgreSQL Database

Comment the database section out completely and paste the follwing lines of code beneath it.

```
DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql_psycopg2"
        'HOST': os.environ['HOST'],
        'NAME': os.environ['NAME'],
        'USER': os.environ['USER'],
        'PASSWORD': os.environ['PASSWORD'],
        'PORT': os.environ['PORT'],

    }
}
```
