from rest_framework import generics
from ads.models import Ad
from ads.api.serializers import AdListSerializer, AdDetailSerializer
#from rest_framework.permissions import IsAuthenticated



class AdListView(generics.ListAPIView):
    queryset = Ad.published.all()
    serializer_class = AdListSerializer

class AdDetailView(generics.RetrieveAPIView):
    queryset = Ad.published.all()
    serializer_class = AdDetailSerializer
    #permission_classes = [IsAuthenticated]