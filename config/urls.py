from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('hello_worl  d.urls')),
    # path('', include('my_blog.urls'))
    # path('', include('barbershop.urls'))
    # path('', include('models.urls'))
    # path('', include('forms.urls'))
    # path('', include('todo.urls'))
    # path('', include('paginator.urls'))
    # path('', include('user.urls'))
    path('', include('file.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)