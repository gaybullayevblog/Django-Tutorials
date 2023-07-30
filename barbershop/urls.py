from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("story/", views.story, name="story"),
    path('services/', views.services, name="services"),
    path('price/', views.price, name="price"),
    path('contact/', views.contact, name="contact"),
]
