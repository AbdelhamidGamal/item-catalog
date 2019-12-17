# Catalog App

application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users have the ability to post, edit and delete their own items.

## Getting Started

```
Git Clone https://github.com/3b7ameed/item-catalog.git
```


### Dependencies

* Python 3.x
* Flask
* Flask_login
* Sqlalchemy
* oauthlib
* requests
* os
* sys
* json

### Installing

```
python3 database_setup.py
```
Then
```
python3 fill_the_db_with_items.py
```
then
```
python3 app.py
```
then go to https://localhost:5000/catalog

### Json Endpoints:

View all categories within th catalog:
* https://localhost:5000/categorys/json

View all items within the catalog:
* https://localhost:5000/items/json

View all items in a certain category ( Soccer for example ) :
* https://localhost:5000/catalog/Soccer/json

view a certain item within a certain category: ( Uniform in Soccer for example)
* https://localhost:5000/catalog/Soccer/Uniform/json
