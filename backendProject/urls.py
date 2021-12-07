"""backendProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pedidos.views import saludo,saludo_html,saludo_plantilla,get_fecha,sumar,curso

urlpatterns = [
    path('admin/', admin.site.urls),
#    path("",saludo),  #con path vacio va x default a la url saludo
    path("saludo/",saludo),
    path("saludo2/",saludo_plantilla),
    path("saludohtml/",saludo_html),
    path("fecha/",get_fecha),
    path("suma/<int:n1>/<int:n2>",sumar),
    path("curso/",curso),
]
