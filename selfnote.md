# Setting up PostgreSQL

1. Setup PostgreSQL service in machine.
2. Connect to PostgreSQL service.
3. Enter in psql:<br>
```CREATE DATABASE djangowebsite;
CREATE USER django WITH PASSWORD 'django';
ALTER ROLE django SET client_encoding TO 'utf8';
ALTER ROLE django SET default_transaction_isolation TO 'read committed';
ALTER ROLE django SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE myproject TO django;
```
4. Edit in settings.py for the following fields:
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
# Commands for PostgreSQL
1. sudo service postgresql stop|start|restart
2. psql
- \l <br>
list down databases available
3. sudo su - postgres
switch to postgres user. probably need to read this for testing: https://serverfault.com/questions/601140/whats-the-difference-between-sudo-su-postgres-and-sudo-u-postgres