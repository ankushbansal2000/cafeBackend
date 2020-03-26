from django.urls import path
from .views import OrderViewSet,CartView
urlpatterns = [
    
    path('post/',OrderViewSet.as_view()),
    path('get/',CartView.as_view())   
    
    
]
