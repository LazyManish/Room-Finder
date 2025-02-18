from django.urls import path
from .views import RoomAPIView


urlpatterns = [

    path('rooms/',RoomAPIView.as_view(), name="rooms"),
    
]