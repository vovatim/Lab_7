from django.contrib import admin
from .models import Book_User
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'number')
    list_filter = ('user',)
    search_fields = ['book']

admin.site.register(Book_User, PostAdmin)