from django.urls import path
from .views import OrderViewSet,OrderView
urlpatterns = [
    
    path('post/',OrderViewSet.as_view()),
    path('get/',OrderView.as_view()),
    
]
