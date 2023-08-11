from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import users
from books.models import Author, Book
from books.serializer import BookSerializer, AuthorSerializer


# Create your views here.


@api_view()
def book_list(request):
    queryset = Book.objects.all()
    serializer = BookSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view()
def book_details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    serializer = BookSerializer(book)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view()
def author_list(request):
    queryset = Author.objects.all()
    serializer = AuthorSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view()
def author_details(request, pk):
    author = get_object_or_404(Author, pk=pk)
    serializer = AuthorSerializer(author)
    return Response(serializer.data, status=status.HTTP_200_OK)
