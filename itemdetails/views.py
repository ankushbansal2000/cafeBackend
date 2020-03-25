from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,filters,generics
from .serializers import ItemDetailSerializer
from .models import itemdetail
from django.http import HttpResponse
class ItemViewSet(viewsets.ModelViewSet):
    queryset = itemdetail.objects.all()
    serializer_class = ItemDetailSerializer

    # def post(self,request,*args,**kwargs):
    #     image = request.data['image']
    #     name=request.data['name']
    #     price=request.data['price']
    #     quantity=request.data['quantity']
    #     desc=request.data['desc']
    #     itemdetail.objects.create(name=name,image=image,price=price,quantity=quantity,desc=desc)
    #     return HttpResponse({'message': "Item Created"},status=200)