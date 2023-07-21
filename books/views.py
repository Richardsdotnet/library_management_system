from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import users
from books.models import Author, Book
from books.serializer import BookSerializer

# Create your views here.



@api_view()
def book_list(request):
    queryset = Book.objects.all()
    serializer = BookSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view
def book_details(request, pk):
    return Response(pk)


