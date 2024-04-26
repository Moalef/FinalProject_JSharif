from rest_framework import generics
from ads.models import Ad
from ads.api.serializers import AdListSerializer, AdDetailSerializer
#from rest_framework.permissions import IsAuthenticated



class AdListView(generics.ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer

class AdDetailView(generics.RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer
    #permission_classes = [IsAuthenticated]

class AdCityFilterView(generics.ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer

    def get_queryset(self):
        city = self.request.query_params.get('city', None)
        return Ad.published.filter(city=city) if city else Ad.published.all()