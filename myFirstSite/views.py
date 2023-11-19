from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

def http_test(request):
    return HttpResponse("HTTP-Test is Working")

def json_test(request):
    return JsonResponse({"title":"Ramtin is a great programmer"})
