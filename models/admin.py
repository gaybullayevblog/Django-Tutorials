from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Musician)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Author)
admin.site.register(Book)