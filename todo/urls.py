from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name="main"),
    path('del/<str:item_id>', remove, name="del"),
]
