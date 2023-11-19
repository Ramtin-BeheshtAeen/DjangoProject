from django.contrib import admin
from django.urls import path
from myFirstSite.views import http_test, json_test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('http-test', http_test),
    path('json-test',json_test)
]
