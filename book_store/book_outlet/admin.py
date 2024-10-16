from django.contrib import admin

from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # this is to autofill slug in admin while creating record
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'rating',)
    list_display = ('title', 'author', 'rating', 'is_bestselling')


admin.site.register(Book, BookAdmin)
