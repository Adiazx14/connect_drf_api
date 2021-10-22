from django.urls import path
from django.urls.conf import include
from .views import PackageView, RegionView
from django.contrib import admin

urlpatterns = [
    path('', RegionView.as_view()),
    path('packages/', PackageView.as_view())
]

admin.site.site_header = 'Connect Administration'