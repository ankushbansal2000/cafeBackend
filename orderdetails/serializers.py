from rest_framework import serializers
from .models import orderdetail
from itemdetails.models import itemdetail
from cartdetail.models import cartdetail


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = orderdetail
        fields = ['email']


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = orderdetail
        fields = '__all__'
