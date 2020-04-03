# DRF-TDD-CRUD
A minimal implementation of REST API using [Django REST framework](http://www.django-rest-framework.org/).
It helps in understanding the implementation of following features
- django project configuration and admin interface.
- models, serializers, views and urls.
- Token Authentication
- Pagination
- Test Driven Development

## Requirements
- Python 3.6.9
- Django==3.0.4
- djangorestframework==3.11.0

## Installation
```
	pip install -r requirements.txt
```


## Endpoints

Endpoint | HTTP Method | CRUD Operation
-- | -- |-- 
`api/review/institute/` | POST, GET | Create, Retrieve ALL
`api/review/institute/{id}/` | GET, PUT, DELETE | Retrieve, Update, Destroy
`api/user/` | POST | Create User
`api/user/login/` | GET | Login User

## Test Cases
- Test 1
- Test 2

## Usage
We can call the API using [postman](https://www.postman.com/) or [curl](https://curl.haxx.se/) or [httpie](https://github.com/jakubroztocil/httpie#installation). 

1. Postman
content
2. httpie
- Install httpie using pip -
```
pip install httpie
```
- Start the django server
```
python manage.py runserver
```
- Access API -
```
	http http://127.0.0.1:8000/api/review/institute/1/ "Authorization: Token 39643b8bec57a7288ff4b68ce7199c9398ae7699"
```
- Response:
```
{
    "id": 2,
    "institute_name": "COEP",
    "address": "shivaji nagar pune",
    "pin_code": 411005,
    "office_mail": "coep@ceop.com",
    "phone_number": null,
    "website": null,
    "institute_type": "GO",
    "founded_in": null,
    "affiliated_to": null,
    "approved_by": null,
    "owner": 1
}
```
Note: Authorization token is required as we are using token based authentication.

3. curl
content

## Login and Tokens

To get a token first we have to login
```
	http http://127.0.0.1:8000/rest-auth/login/ username="admin" password="root1234"
```
after that, we get the token
```
{
    "key": "2d500db1e51153318e300860064e52c061e72016"
}
```
**ALL request must be authenticated with a valid token, otherwise they will be invalid**

We can create new users. (password1 and password2 must be equal)
```
http POST http://127.0.0.1:8000/rest-auth/registration/ username="USERNAME" password1="PASSWORD" password2="PASSWORD"
```
And we can logout, the token must be your actual token
```
http POST http://127.0.0.1:8000/rest-auth/logout/ "Authorization: Token <YOUR_TOKEN>" 
```

### Pagination
content