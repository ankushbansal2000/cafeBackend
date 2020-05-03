from django.urls import path
from .views import AdminAuthenticateList,AdminViewSet,AdminDetail
urlpatterns = [
    
    path('adminlogin/',AdminAuthenticateList.as_view()),
    path('adminn/',AdminDetail.as_view()),
    path(r'admindetail/', AdminViewSet.as_view())
]




#127.0.0.1:80000/adminlogin   post request