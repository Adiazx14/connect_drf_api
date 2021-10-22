from django.contrib import admin
from django.db import models

from .models import Package, Region

class PackageInline(admin.TabularInline):
    model = Package

class RegionAdmin(admin.ModelAdmin):
    model = Region
    inlines = [PackageInline]

# Register your models here.
admin.site.register(Region, RegionAdmin)
admin.site.register(Package)