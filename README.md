# Invoicing System
## Description
This was an assignment given in my Computer Science course for a subject named Software Engineering Fundamentals. We were tasked to create an invoicing system website. This website was used multiple times throughout different subjects to be continuosly improved. This project is also made as a learning experience too, therefore information of changes made to project will also be given.

## System requirement <br>
Python 3.12.1 <br>
Pyvenv <br>

## Sidenote
File to be imported into PostgreSQL server is using dbexportfrom.pgsql

## Main modules implemented from Python:<br>
1. Django <br>
1. Whitenoise (to serve static files)
1. daphne <br>

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

After every recreation of requirements.txt via `pip freeze`, always remove `twisted-iocpsupport` from the textfile.

## Possible future changes

Instead of using the module "Whitenoise" to serve static files, use a seperate webserver (NGinx, Apache) that implements reverse-proxy to serve the static files instead.

## Setting up Daphne and PostgreSQL using docker-compose
If you're too lazy to manually setup Daphne and PostgreSQL on your machine, just run `docker compose up` after installing Docker (not going to explain Docker installation here, sorry).

## Setting up Daphne <br>
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

## Setting up PostgreSQL

Setup PostgreSQL service in machine.

Connect to PostgreSQL service.

Enter in psql then run the following commands:

```
CREATE DATABASE djangowebsite;
CREATE USER django WITH PASSWORD 'django';
ALTER ROLE django SET client_encoding TO 'utf8';
ALTER ROLE django SET default_transaction_isolation TO 'read committed';
ALTER ROLE django SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE myproject TO django;
```

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

To import the dbexportfrom.pgsql to your PostgreSQL server's database named djangowebsite, you will first have to change your current user session to postgres. For most Unix terminals this can either be done by running:
```
su postgres

or

sudo su - postgres
```


Once that is done, start importing the content of dbexportfrom.pgsql to your PostgreSQL server by running:
```
psql -U postgres djangowebsite < /docker-entrypoint-initdb.d/dbexportfrom.pgsql
```


## Differences in Production and Development

To run the server in development mode, run:

```
python manage.py runserver
```

To run the server in production mode, run:

```
daphne -e ssl:port=8000:privateKey=./certificates/key.pem:certKey=./certificates/crt.pem invoicesystem.asgi:application
```

### Settings File in Development
Key differences are that in development mode, the setting file that is used is called `settings_dev.py`. This variable is set inside `manage.py`.

```
...
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'invoicesystem.settings_dev')
...
```

Since we're running the development server using the command `python manage.py runserver`, the settings file is set inside of `manage.py`. 

### Settings File in Production
Whereas in production mode, we are running the server by executing:

```
daphne -e ssl:port=8000:privateKey=./certificates/key.pem:certKey=./certificates/crt.pem invoicesystem.asgi:application
```

Therefore, the settings file to be used is set inside `asgi.py`. This is the content of `asgi.py`.

```
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'invoicesystem.settings_prod')

application = get_asgi_application()
```

## Commits information

### 876e5dc283
The way webpages work in Django is:

User request for webpage -> Django checks in url.py -> Django calls the view for said url -> View function retrieves data or performs processing -> View function renders the template ->
Rendered HTML sent back to user's browser as HTTP Response

Typically, form-handling is done in 'View function retrieves data or performs processing'. So in forms.py, we define the fields that the view is supposed to render. 
Let's take the Salesmans' view to create Delivery Order forms `def createDeliveryOrder`. In `def createDeliveryOrder`, the form is instantiated by calling it from `forms.py`.

views.py of deliveryorder app:
```
def createDeliveryOrder(request):
    submitted = False
    deliveryorderid = DeliveryOrderForm.objects.order_by('-deliveryorderid')[:1]
    template_name = 'deliveryorder/create.html'
    form = DOForm()
...
```

In `forms.py`, we declare the metadata of DOForm, so as to tell what data should the form have. This can be seen in `class Meta`. We want to override the `def __init__` for the form because
we want to make `deliveryorderdate` field to be uneditable.

content of DOForm in deliveryorder/forms.py:
```
class DOForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(DOForm, self).__init__(*args, **kwargs)
        self.fields['deliveryorderdate'].widget.attrs['readonly'] = True

    class Meta:
        model = DeliveryOrderForm
        fields = [
    'deliveryorderid',
    'recipientname',
    'recipientphone',
    'recipientaddress',
    'deliveryorderdate',
    'itemid',
    'itemprice',
    'itemdescription',
    'itemquantity',]
```

This is also done in other forms:

content of approveDOForm in deliveryorder/forms.py
```
class approveDOForm(ModelForm):
    def __init__(self, *args, **kwargs):    
        super(approveDOForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = True

    class Meta:
        model = DeliveryOrderForm
        fields = [
    'recipientname',
    'recipientphone',
    'recipientaddress',
    'deliveryorderdate',
    'itemid',
    'itemprice',
    'itemdescription',
    'itemquantity',
    'deliveryorderstatus']
```

As shown above, we iterate through fields.values() to edit the widget.attrs['readonly'] of each field to be *True*. By assumption, `deliveryorderstatus` would be uneditable, but no. This is because `deliveryorderstatus` is of type `models.IntegerChoices`. Therefore, when displaying the form, the field `deliveryorderstatus` will be of type dropdown. This types of HTML tags cannot be set with `readonly`. This
works perfectly with our application demand, but it's behaviour should be noted in the future.