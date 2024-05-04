from rest_framework import serializers
from ads.models import Ad, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'parent']


class AdListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    
    class Meta:
        model = Ad
        fields = [ 'title' , 'city', 'publish', 'category'] 


class AdDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        # fields = ['title' , 'city', 'owner' , 'category' ,'description' , 'contact' , 'publish' , 'status']
        fields = ['title' , 'city' , 'category' ,'description' , 'contact' , 'publish' , 'status']
