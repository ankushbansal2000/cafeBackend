from django.urls import path
from .views import CartViewSet,CartGetView
urlpatterns = [
    
    path('post/',CartViewSet.as_view()),
    path('get/',CartGetView.as_view()),
    
]
