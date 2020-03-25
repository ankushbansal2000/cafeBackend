from rest_framework import serializers
from .models import itemdetail

class ItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = itemdetail
        fields = '__all__'
