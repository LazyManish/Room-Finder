from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RoomSerializer,GetRoomSerializer,UpdateRoomSerializer
from Room.models import Room
from .permissions import IsAdminOnly


class RoomAPIView(APIView):

    permission_classes = [IsAdminOnly]

    def post(self,request):

        
        try:
            data = request.data

            serializer = RoomSerializer(data=data)

            if serializer.is_valid():
                serializer.save(admin = request.user)
                return Response({"message":"Room Created Successfully."},status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):

        try:
            admin = request.user

            if admin.role == 'buyer':

                rooms = Room.objects.all()
                serializer =GetRoomSerializer(rooms, many =True)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            else:
            
                rooms = Room.objects.filter(admin = admin)
                serializer = GetRoomSerializer(rooms, many = True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def put(self, request, pk):


        try:
            admin=request.user
            data=request.data

            room = Room.objects.get(pk=pk)  
            serializer = UpdateRoomSerializer(room, data=data, partial = True)
            if serializer.is_valid():
                serializer.save(admin=admin)
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Room.DoesNotExist:
            return Response({"message":"Room not found."}, status=status.HTTP_204_NO_CONTENT)
    

    def delete(self, request, pk):
    
        try:
            admin = request.user

            room = Room.objects.get(pk=pk, admin=admin)  
            room.delete()
            return Response({"message":"Room is deleted sucessfully."},status=status.HTTP_204_NO_CONTENT)
        
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)