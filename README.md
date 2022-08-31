# Store cellular accessories.
## About project:
The order is executed without payment, but it can be added using django-robokassa (https://github.com/kmike/django-robokassa). In the future I will add a payment system and will improve the site getting rid of bugs. The design and template were invented and made by me. The layout is not adaptive.
## Website Link
https://bektur.pythonanywhere.com/
## In order to run a project locally, run the following commands:
* pip install -r requirements.txt
* python manage.py makemigrations
* python manage.py migrate
* python manage.py runserver (run the project)
## In order to login to the admin panel you need to create a user:
* python manage.py createsuperuser
* Then enter "/admin" in the address bar
