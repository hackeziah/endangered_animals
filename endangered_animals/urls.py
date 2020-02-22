
from django.contrib import admin
from django.urls import path, reverse_lazy
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
# from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(('animals.urls','animals'), namespace="animals")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)