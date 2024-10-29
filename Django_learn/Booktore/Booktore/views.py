from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello World, You are at my BOOKSTORE")
     return render(request,'index.html')
         
     
def about(request):
    # return HttpResponse("Hello World, You are at my about page of BOOKSTORE")
    return render(request,'contact.html')
def contact(request):
    # return HttpResponse("Hello World, You are at my contact page of BOOKSTORE")
     return render(request,'about.html')