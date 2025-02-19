from django.urls import path
from .views import RoomAPIView


urlpatterns = [

    path('rooms/',RoomAPIView.as_view(), name="rooms"),
    path('rooms/<int:pk>/',RoomAPIView.as_view(), name="rooms-detail"),
    
]