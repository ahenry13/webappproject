from django.contrib import admin

# Register your models here.
from django.contrib import admin
from gamingblog.models import Games, Blog

admin.site.register(Games)
admin.site.register(Blog)

