from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,filters,generics
from .serializers import CartDetailSerializer
from rest_framework.response import Response
from .models import cartdetail
from itemdetails.models import itemdetail

class CartViewSet(generics.CreateAPIView):
    serializer_class = CartDetailSerializer
    def post(self,request,*args,**kwargs):
        emailid = request.data['emailid']
        item_name=request.data['item_name']
        item_price=request.data['item_price']
        quantity=request.data['quantity']
        price_per_item=str(int(item_price)*int(quantity))
        a=cartdetail.objects.create(emailid=emailid,item_name=item_name,item_price=item_price,quantity=quantity,price_per_item=price_per_item)
        return Response({'price': price_per_item})

class CartGetView(generics.ListAPIView):
    serializer_class = CartDetailSerializer
    queryset = cartdetail.objects.all()
    


    def get_queryset(self):
        id = self.request.query_params.get('email', None)
        print(id)
        queryset=cartdetail.objects.filter(emailid=id)
        return queryset
