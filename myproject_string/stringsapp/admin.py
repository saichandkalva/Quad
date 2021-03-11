from django.contrib import admin

# Register your models here.
from django.contrib import admin
from stringsapp.models import phonenum, inputstring

admin.site.register(phonenum)
admin.site.register(inputstring)
