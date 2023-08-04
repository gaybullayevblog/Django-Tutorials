from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("portfolio/", portfolio, name="portfolio"),
    path("blog/", BlogPageView.as_view(), name="blog"),
    path("blog/<pk>", DetailBlogView.as_view(), name="blog_single"),
    path("contact/", contact, name="contact"),

]