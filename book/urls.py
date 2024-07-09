from django.urls import path
from . import views
urlpatterns=[
    path('registration',views.registration),
    path('register', views.register),
    path('index', views.index),
    path('book',views.book),
    path('admin',views.admin),
    path('adregister',views.adregister),
    path('booking/<int:id>',views.booking),
    path('bookedroom',views.bookedroom),
    path('login',views.login),
    path('log',views.log),
    path('insert',views.insert),
    path('ins',views.ins),
]