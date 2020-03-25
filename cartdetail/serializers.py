from rest_framework import serializers
from .models import cartdetail
from itemdetails.models import itemdetail
class CartDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = cartdetail
        fields = '__all__'

