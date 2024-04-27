from django.forms import ValidationError
from rest_framework import generics
from django.shortcuts import get_object_or_404
from ads.models import Ad, Category
from ads.api.serializers import AdListSerializer, AdDetailSerializer
#from rest_framework.permissions import IsAuthenticated



class AdListView(generics.ListCreateAPIView):
    queryset = Ad.published.all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AdDetailSerializer
        return AdListSerializer


    def perform_create(self, serializer):
        category = get_object_or_404(Category, id=self.request.data.get('category'))
        if category.subcategories.exists():
            raise ValidationError('Ads cannot be posted in parent categories.')
        serializer.save(owner=self.request.user)

    def get_object(self):
        ad = super().get_object()
        if not self.request.user.is_authenticated:
            ad.contact = 'Log in to See Contact Info.'
        return ad


class AdDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ad.published.all()
    serializer_class = AdDetailSerializer
    #permission_classes = [IsAuthenticated]

    def get_object(self):
        ad = super().get_object()
        if not self.request.user.is_authenticated:
            ad.contact = 'Log in to See Contact Info.'
        return ad