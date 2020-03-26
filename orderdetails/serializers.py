from rest_framework import serializers
from .models import orderdetail
from itemdetails.models import itemdetail
from cartdetail.models import cartdetail

class GetItem(serializers.ModelSerializer):
    class Meta:
        model = itemdetail
        fields = '__all__'




class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = orderdetail
        fields = '__all__'
