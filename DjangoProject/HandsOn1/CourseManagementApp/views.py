from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request): # we are gonna request this page hence the parameter we pass is request
    return HttpResponse("Hello, User. You're at the Course Management index.")
def register(request):
    return HttpResponse("Hello, User. You're at the Course Management register page.")