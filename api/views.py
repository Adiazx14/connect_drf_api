from rest_framework.response import Response
from rest_framework.views import APIView, status
from .models import Package, Region, Subscriber
from .serializers import PackageSerializer, RegionSerializer, SubscriberSerializer
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

class SubscriberView(APIView):

    def get(self, request):
        subscriber = Subscriber.objects.all()
        serializer = SubscriberSerializer(subscriber, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)