from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse

def http_test(request):
    return HttpResponse("HTTP-Test is Working")

def json_test(request):
    return JsonResponse({"title":"Ramtin is a great programmer"})

def home_view(request):
    return render(request,"index.html")

def contact_view(request):
    return render(request,"contact.html")

def about_view(request):
    return render(request, "about.html")

