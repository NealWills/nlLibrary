from django.contrib import admin

# Register your models here.

from django.contrib import admin
from . import models

class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'book_id', 'book_name', 'book_user', 'book_type', 'book_ssin', 'book_content', 'is_delete', 'create_date', 'update_date', 'delete_date']
    list_filter = ['id', 'book_id', 'book_name', 'book_user', 'book_ssin']
    search_fields = ['id', 'book_id', 'book_name', 'book_user', 'book_content', 'book_ssin']


admin.site.register(models.Books, BookAdmin)

