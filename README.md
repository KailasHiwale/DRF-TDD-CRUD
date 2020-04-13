# DRF-TDD-CRUD
A minimal implementation of REST API using [Django REST framework](http://www.django-rest-framework.org/).
This is a demonstrative project to understand the implementation of following features in RESTFull web services:
- django project configuration for installed apps, database, authentication, testing etc.
- Creating MSV (Models, Serializers, Views) as per DRF API guidelines.
- Common customization for django admin interface and urls.  
- User request Authentication using Token Authentication and Permission policy. 
- Customizable Pagination which allow you to split large result sets into individual pages.
- Test Driven Development.

## Requirements
- Python 3.6.9
- Django==3.0.4
- djangorestframework==3.11.0
- django-nose==1.4.6

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

## Authentication

- GET Token

The simplest way we can get a token is -
```
python manage.py drf_create_token tyrian
```

### Pagination
..

## Test Driven Development

- Test Cases for -

1. Verification of user registration with invalid password.
2. Verification of user registration with valid data.
3. Verification of user registration with unique username validation.
4. User login without password authentication.
5. User logn with password authentication.
6. User login with valid credentials.
7. Endpoint validation
8. Create institute.
9. List institutes.
10. Retrieve an institutes with given id.
11. Update an institute.
12. Partial update of an institute.
13. Delete an institute with given id.

- Run Test Cases

```
python manage.py test
```

## Usage
We can call the API using [postman](https://www.postman.com/) or [curl](https://curl.haxx.se/) or [httpie](https://github.com/jakubroztocil/httpie#installation). 

1. Postman
- Install the postman
```
sudo snap install postman
```
- Start the django server
```
python manage.py runserver
```
3. Select request type, Set headers and send request
![postman screen](https://github.com/KailasHiwale/DRF-TDD-CRUD/img.png)

2. httpie
- Install httpie using pip
```
pip install httpie
```
- Start the django server
```
python manage.py runserver
```
- Access API -
```
shttp http://127.0.0.1:8000/api/review/institute/1/ "Authorization: Token 39643b8bec57a7288ff4b68ce7199c9398ae7699"
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

3. curl
..

Note: Authorization token is required as we are using token based authentication.