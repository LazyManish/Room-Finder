from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RoomSerializer,GetRoomSerializer
from Room.models import Room
from .permissions import IsAdminOnly


class RoomAPIView(APIView):

    permission_classes = [IsAdminOnly]

    def post(self,request):

        data = request.data
        
        try:

            serializer = RoomSerializer(data=data)
            if serializer.is_valid():
                serializer.save(admin = request.user)
                return Response({"message":"Room Created Successfully."},status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):

        admin = request.user

        try:
            
            rooms = Room.objects.filter(admin = admin)
            serializer = GetRoomSerializer(rooms, many = True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk):

        admin=request.user
        data=request.data

        try:

            room = Room.objects.get(pk=pk, admin=admin )  
            serializer = RoomSerializer(room, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk):
        
        admin = request.user

        try:

            room = Room.objects.get(pk=pk, admin=admin)  
            room.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
        
        





    
        
