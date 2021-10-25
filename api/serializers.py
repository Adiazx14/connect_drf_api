from rest_framework import fields, serializers
from .models import Package, Region, Subscriber

class RegionSerializer(serializers.ModelSerializer):
    packages = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Region
        fields = "__all__"
    
    def get_packages(self, obj):
        packages = obj.package_set.all()
        serializer = PackageSerializer(packages, many=True)
        return serializer.data


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = "__all__"

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'