from django.contrib import admin
from django.urls import path
from myFirstSite.views import http_test, json_test, home_view, contact_view, about_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('contact', contact_view),
    path('about', about_view),
    path('http-test', http_test),
    path('json-test',json_test)
]
