from django.shortcuts import render

# Create your views here.
def all_books(request):
    return render(request,'Books/All.books.html')
