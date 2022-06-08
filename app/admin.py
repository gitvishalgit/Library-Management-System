from django.contrib import admin

# Register your models here.
from .models import book
# Register your models here.
@admin.register(book)
class bookAdmin(admin.ModelAdmin):
    list_display=['id','title','author','isbn','category']
