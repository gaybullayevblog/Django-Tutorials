from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("service/", views.service, name="service"),
    path("menu/", views.menu, name="menu"),
    path("pages/", views.pages, name="pages"),
    path("booking/", views.booking, name="booking"),
    path("our_team/", views.our_team, name="our_team"),
    path("testimonial/", views.testimonial, name="testimonial"),
    path("contact/", views.contact, name="contact"),

]