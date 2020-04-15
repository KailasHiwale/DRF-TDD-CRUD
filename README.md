# DRF-TDD-CRUD
A minimal implementation of REST API using [Django REST framework](http://www.django-rest-framework.org/).
This is a demonstrative project to understand the implementation of following features in RESTFull web services:
- Django project configuration for installed apps, database, authentication, testing etc.
- Creating MSV (Models, Serializers, Views) as per DRF API guidelines.
- Common customization for django admin interface and urls.  
- User request Authentication using Token Authentication and Permission Policy. 
- Customizable Pagination which allows you to split large result sets into individual pages.
- Test Driven Development.

## Requirements
- Python==3.6.9
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
We need to do following changes in `reviewapp/settings.py` in order to enable token authentication.
***First*** add `restframework.authtoken` to your `INSTALLED_APPS`. ***Second*** add the `TokenAuthentication` to `REST_FRAMEWORK`
```
INSTALLED_APPS = [
    # Django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party Apps
    'rest_framework',
    'rest_framework.authtoken',  # here
    'django_nose',

    # Local Apps
    'review',
    'user',
]

REST_FRAMEWORK = {
    ...
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    ...
}
```

### GET Token
The simplest way we can get a token is -
```
python manage.py drf_create_token tyrian
```

## Pagination
Pagination allows you to control how many objects per page to be returned. To enable it add the following lines to REST_FRAMEWORK dictionary in `reviewapp/settings.py`
```
REST_FRAMEWORK = {
    ...
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
    ...
}
```

## Testing

### Test Cases for

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

### Setting the default format
You can set the test request default format by adding a `TEST_REQUEST_DEFAULT_FORMAT` key in `REST_FRAMEWORK` cofig. dictionary in your `reviewapp/settings.py`
```
REST_FRAMEWORK = {
    ...
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
    ...
}
```

### Run Test Cases

```
python manage.py test
```

## Usage
There are multiple ways to call the API, such as [postman](https://www.postman.com/), [curl](https://curl.haxx.se/), [httpie](https://github.com/jakubroztocil/httpie#installation). 

### Postman
- Install the postman
```
sudo snap install postman
```
- Start the django server
```
python manage.py runserver
```
- Select request type, Set headers and send request

![postman screen](https://github.com/KailasHiwale/DRF-TDD-CRUD/blob/master/img.png)

### httpie
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
shttp http://127.0.0.1:8000/api/review/institute/2/ "Authorization: Token 39643b8bec57a7288ff4b68ce7199c9398ae7699"
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

### curl
- Install curl
```
sudo apt install curl
```
- Start the django server
```
python manage.py runserver
```
- Access API using curl
```
curl http://127.0.0.1:8000/api/review/institute/ -H 'Authorization: Token 39643b8bec57a7288ff4b68ce7199c9398ae7699'
```
- Response
```
{"count":2,"next":null,"previous":null,"results":[{"id":2,"institute_name":"AISSMSIOIT","address":"shivaji nagar pune","pin_code":411005,"office_mail":"coep@ceop.com","phone_number":null,"website":null,"institute_type":"GO","founded_in":null,"affiliated_to":null,"approved_by":null,"owner":1},{"id":4,"institute_name":"PICT","address":"pune","pin_code":null,"office_mail":null,"phone_number":null,"website":null,"institute_type":"GO","founded_in":null,"affiliated_to":null,"approved_by":null,"owner":1}]}
```
***Note -*** Authorization token is required as we are using token based authentication.