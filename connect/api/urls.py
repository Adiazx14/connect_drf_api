from django.urls import path
from django.urls.conf import include
from .views import RegionView

urlpatterns = [
    path('', RegionView.as_view())
]
