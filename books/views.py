from django.http import HttpResponse
from django.shortcuts import render

import users
from books.models import Author

# Create your views here.
students = [
    {"name": "sheriff"},
    {"name": "chris"},
    {"name": "Rich"},
]


def welcome(request):
    query_set = Author.objects.filter(first_name__contains="sea")
    return render(request, "books/welcome.html", {"authors": list(query_set)})


def read(request):
    return render(request, "books/read.html")


def borrow(request):
    return render(request, 'books/borrow.html')
