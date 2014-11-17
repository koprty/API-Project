API-Project
===========

##Lise Ho, Christina Ko, Ivy Wong

**Getting the Amazon API part to work**

`pip install python-amazon-product-api`

`sudo apt-get install libxml2-dev libxslt-dev python-dev`

`pip install lxml`

**Getting the Ebay API to work**

`pip install ebaysdk`

**Run app.py to run the application.**

**Note you need an Amazon access key, secret key, and associate tag.**

**We cannot post any of these elements because of security issues.**

Place these elements in amazon.py for a working version of the app.

config ={
    'access_key': your-access-key,
    'secret_key': your-secret-key,
    'associate_tag': your-associate-tag,
    'locale': 'us',
    }
