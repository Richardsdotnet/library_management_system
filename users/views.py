from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def create(request):
    return render(request, 'users/create.html')
