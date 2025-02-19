from django.urls import path
from .views import RoomAPIView


urlpatterns = [

    path('rooms/<int:pk>/',RoomAPIView.as_view(), name="rooms"),
    
]