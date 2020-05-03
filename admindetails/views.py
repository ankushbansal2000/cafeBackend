from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,filters,generics
from .serializers import AdminDetailSerializer
from .models import admindetail
from django.http import JsonResponse

class AdminViewSet(generics.CreateAPIView):   
    #post api
    queryset = admindetail.objects.all()
    serializer_class = AdminDetailSerializer
    
class AdminDetail(generics.ListAPIView):       
    #  get api
    queryset = admindetail.objects.all()
    serializer_class = AdminDetailSerializer

#http://182.0.0.1:8000/admindetail/?email=

class AdminAuthenticateList(generics.ListAPIView):   
    # get api
    serializer_class = AdminDetailSerializer

    def get_queryset(self):
        msg=admindetail.objects.filter(id=1)
        queryset = admindetail.objects.all()
        email = self.request.query_params.get('email', None)
        password = self.request.query_params.get('password', None)
        if email is not None:
            queryset = queryset.filter(email=email,password=password)
            if queryset:
                print(queryset)
                return queryset
        return msg
    

