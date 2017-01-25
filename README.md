Source code for a live coding session about [`unittest.mock`](https://docs.python.org/3/library/unittest.mock.html#module-unittest.mock) (using some examples common in development with [Django](https://www.djangoproject.com/)).

[![Build Status](https://travis-ci.org/cuducos/hangouts-mock.svg?branch=master)](https://travis-ci.org/cuducos/hangouts-mock)
[![Coverage Status](https://coveralls.io/repos/github/cuducos/hangouts-mock/badge.svg?branch=master)](https://coveralls.io/github/cuducos/hangouts-mock?branch=master)

### Requirements

[Python](https://python.org) — _don’t ask me the version: this is 2017 so take your best guess_ ; )

### Running

Within a _virtualenv_ just install the dependencies and run database migrations before launching the server:

```console
$ python -m pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```

### Importing data

To load `data.csv` to the database:

```console
$ python manage.py congresspeople data.csv
```

### Testing (with [`coverage`](https://coverage.readthedocs.io/) and HTML report)

Run the tests with `coverage`, generate and open a HTML report:

```
$ coverage run manage.py test
$ coverage html
$ open htmlcov/index.html
```
