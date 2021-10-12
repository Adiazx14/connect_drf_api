from rest_framework import fields, serializers
from .models import Region

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"