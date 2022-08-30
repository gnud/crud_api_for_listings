# coderbyte CRUD API for Listings

Let’s assume that we’re trying to build a part of the data pipeline system we designed during your technical interview.
Specifically, let’s focus on creating a SQL DB and an API that can interface with our database of recently
listed properties on the MLS.
Our goal should be to build an API to allow developers to interface with this database with simple CRUD functionality.

## Goals

- [x] Write a SQL script that can create a simple SQL table for listings (see below for schema).
- [x] Write a script to populate the DB with mock data for demo purposes.
- [x] Implement a simple REST API that has CRUD (Create, Read, Update, Delete) functionality for that database.
- [x] Write Unit Tests to ensure your API can be tested by other developers.
- [x] Document your code so another programmer can use it and expand on your code.

## Tech Stack

**Client:** REST API (JSON) compatibility

**Server:** Python, Django

## Features

- Django web app
- Rest API based on DRF
- CRUD exposure on model Listing

## Usage/Examples

Run django server

```bash
./manage runserver
```

Open this url:
http://127.0.0.1:8000/


**Note**: Setup your local environment first 

## Run Locally

**Note**: Following setup is tested for GNU/Linux, or may, or may not work on Mac, not tested on windows.

Clone the project

```bash
  git clone https://github.com/gnud/crud_api_for_listings
```

Go to the project directory

```bash
  cd crud_api_for_listings
```

### Virtual env

```bash
  virtualenv -p python3 venv
```

**Note**: you can also use pyenv/venv to generate virtualenv 

### Load environment

```bash
  . venv/bin/activate
```

### Install dependencies

```bash
  pip install -r requirements.txt
```

### Create dev user

```bash
  ./manage.py createsuperuser
```

Maybe:

user: root
email: root@example.com (example.com is working domain for examples)
password: password (Do not use this on production :) )

## Running Tests

### Initial setup

```bash
  pip install -r requirements_test.txt
```

### Load some data

```bash
  ./manage.py populate_fake_data
```

**Note**: Check the database if we have 10 records 

### Run actual tests

To run tests, run the following command

```bash
  ./manage.py test
```


# API

## Swagger

- http://127.0.0.1:8000/swagger/redoc/
- http://127.0.0.1:8000/swagger/swagger/
- http://127.0.0.1:8000/swagger/swagger.json
- http://127.0.0.1:8000/swagger/swagger.yaml

## AUTH

for demo purposes, only:
- Session cookies
- Basic authentication

work for API access using DRF.


# TODOS/IDEAS:

1. We can set authorization Token based for the API
2. We can replace the data generation with bakery and friends
3. We can install additional tools for Django like django-extensions
4. We can dockerize the web app
5. Change the database to PG or MySQL/Maria
6. Setup a linter and coverage like snowflakes
7. Setup tox for more advanced testing
8. Prepare for production
