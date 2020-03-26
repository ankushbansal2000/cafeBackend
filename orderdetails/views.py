from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,filters,generics
from .serializers import OrderDetailSerializer
from .models import orderdetail
from cartdetail.models import cartdetail
from itemdetails.models import itemdetail
from rest_framework.response import Response



class CartView(generics.ListAPIView):
    serializer_class=OrderDetailSerializer
    queryset = orderdetail.objects.all()


class OrderViewSet(generics.CreateAPIView):
        # queryset = itemdetail.objects.all()
        serializer_class = OrderDetailSerializer

        def post(self,request,*args,**kwargs):
            email = request.data['email']
            json = request.data['order']
            print(email)
            q=cartdetail.objects.filter(emailid=email)
            
            for i in q:
                i.delete()
            orderdetail.objects.create(email=email,order=json)
            return Response({'message': "Order Created"})
    #         print(i.id,i.emailid,i.quantity,i.item_name)
    #     # 
    #     