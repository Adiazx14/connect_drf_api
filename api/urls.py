from django.urls import path
from django.urls.conf import include
from .views import PackageView, RegionDetail, RegionView, SubscriberView
from django.contrib import admin

urlpatterns = [
    path('', RegionView.as_view()),
    path('<int:id>/', view=RegionDetail.as_view()),
    path('packages/', PackageView.as_view()),
    path('subscriber/', SubscriberView.as_view())
]

admin.site.site_header = 'Connect Administration'