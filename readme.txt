RUN docker-compose run web django-admin startproject app
change permission sudo chown -R $USER:$USER app/
change db in settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

RUN python manage.py migrate from container
Create user using python manage.py createsuperuser
Create new module using python manage.py startapp module_name
Then create models and run python manage.py makemigrations module_name