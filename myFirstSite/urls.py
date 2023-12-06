from django.contrib import admin
from django.urls import path
from myFirstSite.views import http_test, json_test, home_view, contact_view, about_view

app_name = "myFirstSite"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='index'),
    path('contact', contact_view, name='contact'),
    path('about', about_view, name="about"),
    path('http-test', http_test),
    path('json-test',json_test)
]
