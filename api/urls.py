from django.urls import path
from django.urls.conf import include
from .views import PackageView, RegionView

urlpatterns = [
    path('', RegionView.as_view()),
    path('packages/', PackageView.as_view())
]
