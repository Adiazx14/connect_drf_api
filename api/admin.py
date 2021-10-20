from django.contrib import admin

from .models import Package, Region

# Register your models here.
admin.site.register(Region)
admin.site.register(Package)