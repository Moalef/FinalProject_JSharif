from rest_framework import serializers
from ads.models import Ad

class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = [ 'title']


class AdDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['id', 'title', 'description']
