from rest_framework.response import Response
from rest_framework.views import APIView, status
from .models import Region
from .serializers import RegionSerializer
# Create your views here.

class RegionView(APIView):
    def get(self, request):
        regions = Region.objects.all()
        serializer = RegionSerializer(regions, many=True)
        return Response(serializer.data)