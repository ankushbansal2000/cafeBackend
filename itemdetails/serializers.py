from rest_framework import serializers
from .models import itemdetail,image

class ItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = itemdetail
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = image
        fields = '__all__'
