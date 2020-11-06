# Device Rental API

This project is build according to the requirements provided in this [requirements](api-details.txt)

### Envionment
Ubuntu 18.04
PostgreSQL v12.4


### How to Run this project
* Setup the postgreSQL server
* Make a database and set the credentials of postgres in the db.py file (dbname, host and password)
* Either enable the environment "env" provided in the source folder with the command "source bin/env/activate", or install the liberaries mentioned in the requirments.txt
* Run the server "python3 app.py"
* To study the API through swagger hit the server ip with request /apidocs (e.g "localhost/apidocs") 


### Azure

* Tested on Azure with:
    *   Azure Virtual Machine with specification:
        -   vCPUs 2
        -   RAM 8GBs
        -   Size Standard D2s v3
    *   Azure Database for PostgreSQL server for database
    *   Allow the outside connection for both postgres and Virtual Machine to access from outside

#### HTTPS endpoint will be setup when some domain is attached to this VM
