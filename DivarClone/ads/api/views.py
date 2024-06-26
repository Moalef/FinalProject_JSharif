from django.forms import ValidationError
from rest_framework import generics, filters
from django.shortcuts import get_object_or_404
from ads.models import Ad, Category, Bookmark
from ads.api.serializers import AdListSerializer, AdDetailSerializer, BookmarkSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated



class AdListView(generics.ListCreateAPIView):
    queryset = Ad.published.all()

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category','status']
    search_fields = ['title']
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AdDetailSerializer
        else:
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


class AdDetailView(generics.RetrieveAPIView):
    queryset = Ad.published.all()
    serializer_class = AdDetailSerializer

    def get_object(self):
        ad = super().get_object()
        if not self.request.user.is_authenticated:
            ad.contact = 'Log in to See Contact Info.'
        return ad
    
#see his/her advertisement LIST
class AdInboxView(generics.ListAPIView):
    serializer_class = AdListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Ad.objects.filter(owner=self.request.user)

#see his/her advertisement detail and edit/delete them
class AdInboxDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AdListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Ad.objects.filter(owner=self.request.user)
    

class BookmarkListView(generics.ListAPIView):
    queryset = Bookmark.objects.all()
    print(queryset)
    serializer_class = BookmarkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    

class BookmarkCreateView(generics.CreateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

