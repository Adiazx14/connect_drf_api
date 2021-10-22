from rest_framework.response import Response
from rest_framework.views import APIView, status
from .models import Package, Region
from .serializers import PackageSerializer, RegionSerializer
# Create your views here.

class RegionView(APIView):
    def get(self, request):
        regions = Region.objects.all()
        serializer = RegionSerializer(regions, many=True)
        return Response(serializer.data)

class RegionDetail(APIView):

    def get(self, request, id):
        try:
            region = Region.objects.get(id=id)
        except: return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RegionSerializer(region)
        
        return Response(serializer.data)

class PackageView(APIView):
    def get(self, request):
        regions = Package.objects.all()
        serializer = PackageSerializer(regions, many=True)
        return Response(serializer.data)

