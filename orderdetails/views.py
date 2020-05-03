from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,filters,generics
from .serializers import OrderDetailSerializer,OrderSerializer,OrderDetaSerializer
from .models import orderdetail
from cartdetail.models import cartdetail
from rest_framework.response import Response
import json


class OrderView(generics.ListAPIView):
    serializer_class=OrderDetailSerializer
    def get_queryset(self):
        queryset = orderdetail.objects.all()
        status = self.request.query_params.get('status', None)
        if status == "pending":
            queryset = queryset.filter(status=status)
            if queryset:
                print(queryset)
                return queryset

        if status == "PROCESSING":
            queryset = queryset.filter(status=status)
            if queryset:
                print(queryset)
                return queryset  
        
        if status == "COMPLETED":
            queryset = queryset.filter(status=status)
            if queryset:
                print(queryset)
                return queryset     

class OrderStatusUpdateList(viewsets.ModelViewSet):
    queryset = orderdetail.objects.all() 
    serializer_class = OrderDetaSerializer

class OrderViewSet(generics.CreateAPIView):
        serializer_class = OrderSerializer

        def post(self,request,*args,**kwargs):
            email = request.data['email']
            q=cartdetail.objects.filter(emailid=email)
            l=[]
            for i in q:
                d={}
                print(i.id,i.emailid,i.quantity,i.item_name)
                d["id"]=i.id
                d["email"]=i.emailid
                d["quantity"]=i.quantity
                d["name"]=i.item_name
                l.append(d)
                i.delete()
            orderdetail.objects.create(email=email,order=json.dumps(l))
            return Response({'message': "Order Created"})   