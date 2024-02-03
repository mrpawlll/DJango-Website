# TCS3651 Assignment 1
## System requirement <br>
Python 3.12.1 <br>
Pyvenv <br>

## Main modules implemented from Python:<br>
1. Django <br>
1. Whitenoise (to serve static files)
1. daphne <br>

## Instructions <br>
First, you should install Python for your own system first. Then, install pyvenv for that installation of Python. After that, initialize a virtual environment. This can be done by running: <br>
python -m venv env <br>

Once virtual environment is setup, enter the python virtual environment by running the ```activate``` script file inside ```./env``` </br>

To execute the `activate` script file, user probably needs to set execution policy. This can be done by running: <br>
```
Set-ExecutionPolicy -scope Process Unrestricted
```

Then, install the libraries required by running: <br>
pip install -r pip-requirements.txt <br>

Then you can run the server by navigating into invoicesystem, then typing:
```
daphne -e ssl:port=8000:privateKey=./certificates/key.pem:certKey=./certificates/crt.pem invoicesystem.asgi:application
```

## Users in the system are :<br>
- salesman <br>
- manager <br>
- courier <br>
- financeoffice <br>

Their passwords are the same as their username. To get to admin page, you will need to type directly into the url.
Example:localhost:8000/admin

## Caveats

If using 'pip' to update library requirements in the website, type :

```
pip freeze > pip-requirements.txt
```

If using pipreqs to update, just run it as usual.

## Possible future changes

Instead of using the module "Whitenoise" to serve static files, use a seperate webserver (NGinx, Apache) that implements reverse-proxy to serve the static files instead.


## Setting up POSTGRES

Setup PostgreSQL service in machine.

Connect to PostgreSQL service.

Enter in psql.

CREATE DATABASE djangowebsite;
CREATE USER django WITH PASSWORD 'django';
ALTER ROLE django SET client_encoding TO 'utf8';
ALTER ROLE django SET default_transaction_isolation TO 'read committed';
ALTER ROLE django SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE myproject TO django;

Edit in settings.py for the following fields:
```
...

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "djangowebsite",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "<your machine's IP>",
        "PORT": "5432", #could be a different port if you set it up differently
    }
}

...
```