from django.contrib import admin
from . import models


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'isbn', 'author']


admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Author)
