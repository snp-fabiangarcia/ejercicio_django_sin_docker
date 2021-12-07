# django_ndocker
Para inicializar el proyecto necesito:

1 - Instalar Python 3+
2 - Instalar paquetes necesarios que se encuentran en "requirements.txt" con el comando:
pip install -r requirements.txt 
3 - Instalar MySql e iniciar el servicio.
4 - Ejecutar el initial.sql para crear el schema de django.

# Creamos nuestro proyecto de Django
django-admin startproject {NOMBRE PROJECTO} .

# Configuramos nuestro proyecto con la base de datos.
Modificamos el archivo settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'userdjango',
        'PASSWORD': 'passworddjango',
        'HOST': 'localhost',
        'PORT': 3306,
    }
}

# Ahora ya podemos crear nuestra app con el siguiente comando:
python manage.py startapp {REEMPLAZAR POR NOMBRE DE APP}

# Siempre recuerden correr el comando... 
python manage.py migrate

# finalmente ejecutar la app de django con el comando:
python manage.py runserver 0.0.0.0:8000