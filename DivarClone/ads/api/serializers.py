from rest_framework import serializers
from ads.models import Ad, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'parent']


class AdListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
                                                    queryset=Category.objects.filter(parent__isnull=False),
                                                    source='category', write_only=True)
    class Meta:
        model = Ad
        fields = [ 'title' , 'city', 'owner' , 'category' ,'description' , 'contact' , 'publish']


class AdDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['title' , 'city', 'owner' , 'category' ,'description' , 'contact' , 'publish']
