from django.contrib import admin
from .models import ToDoList

# Register your models here.


class ToDoListAdmin(admin.ModelAdmin):
    list_display=('created_date','text')


admin.site.register(ToDoList,ToDoListAdmin)