# Classy Django REST Framework. [![Build Status](https://travis-ci.org/vintasoftware/classy-django-rest-framework.svg?branch=develop)](https://travis-ci.org/vintasoftware/classy-django-rest-framework) [![Coverage Status](https://coveralls.io/repos/github/vintasoftware/classy-django-rest-framework/badge.svg?branch=develop)](https://coveralls.io/github/vintasoftware/classy-django-rest-framework?branch=develop)

## What is this?

[Django REST framework](https://www.django-rest-framework.org) is a powerful and flexible toolkit that makes it easy to build Web APIs. It provides class based generic API views and serializers. We've taken all the attributes and methods that every view/serializer defines or inherits, and flattened all that information onto one comprehensive page per class. This project is heavily based on [Classy Class-Based Views](https://ccbv.co.uk) and was developed by [Vinta Software Studio](https://www.vinta.com.br).

## Dependencies
* Python 3.8+
* s3cmd (For deploy)

## Building

On the project root, create a virtual envinroment using `python -m venv env` (it's important to use `env` as the name) and activate it.

`pip install -r requirements.txt`

`fab build`

The first build will take a while.

To run locally:

`fab runserver`

## Deployment

create a .env file with the content:

```
AWS_BUCKET_NAME=''
AWS_ACCESS_KEY_ID=''
AWS_SECRET_ACCESS_KEY=''
```

Make sure you have built it as instructed above and deploy via

`fab deploy`

## Tests

Install test dependencies:
`pip install -r requirements-test.txt`

Run the tests with:
`fab test`

## Commercial Support

[![alt text](https://avatars2.githubusercontent.com/u/5529080?s=80&v=4 "Vinta Logo")](https://www.vinta.com.br/)

This project is maintained by [Vinta Software](https://www.vinta.com.br/) and is used in products of Vinta's clients. We are always looking for exciting work, so if you need any commercial support, feel free to get in touch: contact@vinta.com.br

