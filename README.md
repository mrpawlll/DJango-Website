# TCS3651 Assignment 1
## System requirement <br>
Python 3.12.1 <br>
Pyvenv <br>

## Sidenote
db.sqlite3 is just a backup in-case dbexportfrom.pgsql's content is screwed up.

File to be imported into PostgreSQL server is using dbexportfrom.pgsql

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

### Using docker-compose
Just run `docker compose up` in the `docker` directory.

## Deploying to AWS Beanstalk

Modules used : 

1. VPC 
1. Elastic Beanstalk 
1. RDS

Process flow :
Setup VPC -> Setup Elastic Beanstalk -> Setup RDS -> Initialize RDS Instance -> Upload pgsql file to S3 -> Populate RDS Instance with pgsql file -> Done

### Setup VPC
Checklists during initializing VPC:
1. One Availibility Zone (AZ)
1. At least 1 Public Subnet ( used to host the webserver)
1. At least 1 Private Subnet( used to host the database server)

After initializing as such, create another subnet for the VPC in a different AZ than the initialized VPC. This is to make more than one AZ connected to the VPC. This'll be important to allow our database to be added in the VPC.

### Setup Elastic Beanstalk
1. Caveats are mostly regarding the content in zipfile.
2. **DO NOT MAKE CONTENT OF ZIPFILE AS SUCH:**
```
|_ invoicesystem
    |
    |_command
    |_extracfg.conf
    |_manage.py
    |_query.py
    |_requirements.txt
    |_.ebextensions
    |   |_
    |   ```
    |_certificates
    |   |_
    |   ```
    |_deliveryorder
    |   |_
    |   ```
    |_invoice
    |   |_
    |   ```
    |_invoicesystem
    |   |_
    |   ```
    |_login
    |   |_
    |   ```
    |_static
        |_
        ```
```
3. **MAKE CONTENT IN ZIPFILE AS SUCH (Sample is in invoicesystem_1231.zip):**
```
command
extracfg.conf
manage.py
query.py
requirements.txt
.ebextensions
  |_etc
certificates
  |_etc
deliveryorder
  |_etc
invoice
  |_etc
invoicesystem
  |_etc
login
  |_etc
static
  |_etc
```

4. requirements.txt needs to contain the libraries needed to run the Django Webserver, so it's safest to first run `pip freeze > requirements.txt` to list the required libraries. Though doing this in Windows might list `twisted-iocpsupport` as a part of the needed libraries to run the Django Webserver, but this isn't a library for Unix systems so delete that out.

5. Then, continue setting up the default configurations for the EB's environment following the limitations set by AWS Academy.

6. Once you reach the 'Networking & Database' part of the configuration, set the VPC of the EB environment to be the VPC you created earlier.

7. Select the **PUBLIC SUBNET** that you've created earlier. DO NOT SELECT THE **PRIVATE SUBNET** for your webpage, since you need to serve it to the Internet.

8. Check the box indicating that you want to allocate public IPs to the EC2 instances you'll be creating.

9. Skip to review and finish setting it up.

### Setup RDS

1. First, create a `Database Subnet Group`. Choose the VPC you created earlier.

2. Next, choose the Availability Zones you've selected during the creation of VPC earlier for the **PRIVATE SUBNETS**.

3. Choose the **PRIVATE SUBNETS** to create your RDS instances for this DB subnet group. Although you'll mainly be using single instance RDS, it is required for you to have multiple AZs to host your RDS instances.

4. Once your `Database Subnet Group` is created, create a new Database.

5. Just configure for a PostgreSQL server. For the templates, select `Free tier`. This'll automatically make the database a Single DB Instance.

6. Make your master password whatever, but **REMEMBER IT** since you'll need it to populate the database with important data

7. Off Storage Autoscaling

8. Connect to the EC2 instance created during the EB initialization earlier.

9. Select the VPC you've created earlier.

10. Usually, this'll select the Database Subnet Group you've created earlier but in case not, select it.

11. Review the configurations you've made to see whether or not it complies with the limitations set by AWS Academy.

12. Done.

### Initialize RDS Instance

1. To populate the RDS Instance, we need to first enter the CLI of our EC2 instance created through Elastic Beanstalk. This is because we made the Database to only connect to the EC2 instance created through EB.

2. Once in the CLI of our EC2 instance run the following command to install `PostgreSQL client`:
```
dnf install postgresql15
```

3. Then, once `PostgreSQL client` is installed, run the following command to connect to the RDS instance:
```
psql --host=<your RDS instance endpoint> --port=5432 --username=postgres --password

*you'll have to navigate back to RDS to get your RDS instance endpoint URL*
```

4. Once you've connected to the RDS instance, run the following commands to create the djangowebsite database:
```
CREATE DATABASE djangowebsite;
CREATE USER django WITH PASSWORD 'django';
ALTER ROLE django SET client_encoding TO 'utf8';
ALTER ROLE django SET default_transaction_isolation TO 'read committed';
ALTER ROLE django SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE myproject TO django;
```

5. Then, exit out of the PostgreSQL server

### Upload pgsql file to S3
1. We want to upload the pgsql file to S3 to allow it to be copied into the EC2 instance. So navigate to the S3 module, then upload the `dbexportfrom.pgsql` file into your general bucket
1. We're done here lol

### Populate RDS Instance with pgsql file
1. Connect back to your EC2 instance
2. Run the following command to copy the `dbexportfrom.pgsql` file into your EC2 instance's machine:
```
aws s3 cp <S3 URI of your dbexportfrom.pgsql> ./
*you'll have to go back to S3 module, click the dbexportfrom.pgsql and retrieve the copy the uri into your clipboard
```

3. After copying the `dbexportfrom.pgsql` file, run the following command to connect to your PostgreSQL server's database and run the SQL queries in `dbexportfrom.pgsql`:
```
psql --host=invoice-database-1.c3us44qg8m8n.us-east-1.rds.amazonaws.com --port=5432 --username=postgres --password --dbname=djangowebsite < dbexportfrom.pgsql # import data from dbexportfrom.pgsql to postgres server
```

4. You can reconnect to the PostgreSQL server and run `\dt` to confirm if the database is populated. Command to reconnect to the PostgreSQL server's database:
```
psql --host=invoice-database-1.c3us44qg8m8n.us-east-1.rds.amazonaws.com --port=5432 --username=postgres --password --dbname=djangowebsite
```

### DONE!
Now, you can go back to your Elastic Beanstalk environment and copy the Domain's URL into your clipboard and paste it in your browser's address bar. If everything is configured correctly, you should be greeted with the login page. If not, good luck bro.