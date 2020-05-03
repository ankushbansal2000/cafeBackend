from .serializer import UserSerializer
from .models import UserDetails
from rest_framework import generics,status,serializers
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from itemdetails.models import itemdetail
from itemdetails.serializers import ItemDetailSerializer
# Create your views here.
 
class RegUser(generics.CreateAPIView):
    querset = UserDetails.objects.all()
    serializer_class = UserSerializer



class UserAuthentication(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        message2="please provide details"
        email = self.request.query_params.get('email', None)
        password = self.request.query_params.get('password', None)
        if email and password is not None:
            queryset = UserDetails.objects.filter(user_email=email,user_pass=password)
            if queryset:
                return queryset
            else:
                raise NotFound('not found')
        else:
            raise NotFound('please provide the details')
