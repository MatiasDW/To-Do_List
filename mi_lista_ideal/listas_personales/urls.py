"""mi_lista_ideal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from .views import lista_todas, lista_detail, lista_nueva, tarjeta_detail, tarjeta_nueva, tarjeta_editar, tablero_detail, tablero_nuevo, tablero_editar

urlpatterns = [
    path('listas/', lista_todas, name='lista_todas'),
    path('lista/<int:pk>/', lista_detail, name='lista_detail'),
    path('lista/nueva/', lista_nueva, name='lista_nueva'),
    path('tarjeta/<int:pk>/', tarjeta_detail, name='tarjeta_detail'),
    path('tarjeta/nueva/', tarjeta_nueva, name='tarjeta_nueva'),
    path('tarjeta/<int:pk>/editar/', tarjeta_editar, name='tarjeta_editar'),
    path('tablero/<int:pk>/', tablero_detail, name='tablero_detail'),
    path('tablero/nuevo/', tablero_nuevo, name='tablero_nuevo'),
    path('tablero/<int:pk>/editar/', tablero_editar, name='tablero_editar'),
]

