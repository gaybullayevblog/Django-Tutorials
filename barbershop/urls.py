from django.urls import path
# from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("story/", story, name="story"),
    path('services/', services, name="services"),
    path('price/', price, name="price"),
    # path("contact/", ContactView.as_view(), name='contact'),
    path('contact/', Contact.as_view(), name='contact'),

]
