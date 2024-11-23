from django.contrib import admin
from .models import Book, Category, Member, Borrow

# Register your models here.
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Member)
admin.site.register(Borrow)
