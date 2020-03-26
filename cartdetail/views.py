from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,filters,generics
from .serializers import CartDetailSerializer,CartUpdate
from rest_framework.response import Response
from .models import cartdetail
from itemdetails.models import itemdetail

class CartUpate(viewsets.ModelViewSet):
    
    queryset = cartdetail.objects.all()
    serializer_class = CartUpdate

    
class CartViewSet(generics.CreateAPIView):
    serializer_class = CartDetailSerializer
    

class CartGetView(generics.ListAPIView):
    serializer_class = CartDetailSerializer
    queryset = cartdetail.objects.all()


    # lookup_field='id'
    # print("rahul")
    # def update(self, request,*args, **kwargs):
    #     id=1
    #     queryset = cartdetail.objects.filter(id=id)
    #     return queryset


    def get_queryset(self):
        id = self.request.query_params.get('email', None)
        print(id)
        queryset=cartdetail.objects.filter(emailid=id)
        print (queryset)
        return queryset
