# flutedemo -- Ansible script to setup celesta/flute demo 

The demo is described thoroughly in this article: https://habrahabr.ru/post/335966/ 

The same demo was used in JUG.MSK presentation (https://habrahabr.ru/company/jugru/blog/339184/, video coming soon)


## Prerequisites

ansible-galaxy install ansiblebit.oracle-java
ansible-galaxy install geerlingguy.postgresql
ansible-galaxy install inponomarev.flute

## What this script does

Installs, using standard roles from ansible-galaxy: 
 - Oracle Java 
 - PostgreSQL
 - Flute
 
Then copies, using 'demo' role, 
 - a demo example,
 - flute config file

and starts flute as REST server on port 8888 (can be configured using 'restport' Ansible variable).

## How to test it?

Using SoapUI (or simply any browser) GET <yourIP>:8888/foo 

On empty database, it returns {}.

Now let's post something, say

    {
        "id": "no1",
        "date": "2017-01-02",
        "customer_id": "CUST1",
        "customer_name": "John Doe",
        "lines": [
           {"item_id": "A",
            "qty": 5
            },
            {"item_id": "B",
            "qty": 4
            }    
           ]
    }

POST <yourIP>:8888/postorder

Once again, let's get the aggregated order details: GET <yourIP>:8888/foo

The result should be:

  {"A":5,"B":4}

For further details, see https://habrahabr.ru/post/335966/
    
## Where everything is located?

To start/stop flute service, use 
  
  service flute start/stop
  
Flute service script is in /etc/init.d/flute.
 
Flute service logs are in /var/logs/flute.

Flute config file is /opt/flute/flute.xml.

Business logic scripts ("the score") is /var/opt/flute/score
