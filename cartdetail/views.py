from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,filters,generics
from .serializers import CartDetailSerializer

from .models import cartdetail
from itemdetails.models import itemdetail

class CartViewSet(generics.CreateAPIView):
    queryset = cartdetail.objects.all()
    serializer_class = CartDetailSerializer


class CartGetView(generics.ListAPIView):
    serializer_class = CartDetailSerializer
    queryset = cartdetail.objects.all()
    


    def get_queryset(self):
        id = self.request.query_params.get('email', None)
        print(id)
        queryset=cartdetail.objects.filter(emailid=id)
        return queryset
