from django.contrib import admin
from .models import Book, Category, Get_Ip_Address


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','family', 'status')

admin.site.register(Category, CategoryAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title','content','author' ,'status')

admin.site.register(Book, BookAdmin)

admin.site.register(Get_Ip_Address)
