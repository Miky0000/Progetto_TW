"""progetto_esame URL Configuration

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
from . import views

app_name = 'ordine'

urlpatterns = [
    path('list/', views.OrdineListView.as_view(), name='ordine-list'),
    path('rimborsi/', views.RimborsiListView.as_view(), name='rimborsi-list'),
    path('checkout/', views.Checkout, name='checkout'),
    path('contattacci/', views.Contatto, name='contatto-page'),
    path('recensione/', views.RecensioneView, name='recensione-page'),
    path('restituisci/<int:id>/', views.Restituisci, name='restituisci-page'),
]
