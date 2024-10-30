from django.contrib import admin 
from .models import MyModel
admin.site.register(MyModel)

class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name','createdd_at')
    search_fields = ('name')
admin.site.register(MyModel, MyModelAdmin)