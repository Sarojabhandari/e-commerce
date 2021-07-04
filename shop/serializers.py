from rest_framework import serializers
from shop.models import Category

    


class CategorySerializer(serializers.Serializer):
 id = serializers.IntegerField(read_only=True)
 name = serializers.CharField()
 image = serializers.ImageField()
 parent = serializers.PrimaryKeyRelatedField(read_only=True)
