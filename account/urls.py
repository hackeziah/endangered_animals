from django.conf.urls import url
from django.urls import path
from .views import registration_view, login_view, logout_view, account_view

urlpatterns = [

    # url(r'^$', index, name='index'),
    url(r'^registration-form$', registration_view, name='registration-view'),
    url(r'^login-view$', login_view, name='login-view'),
    url(r'^logout$', logout_view, name='logout'),
    url(r'^account$', account_view, name='account'),








]
