from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RoomSerializer,GetRoomSerializer,UpdateRoomSerializer
from Room.models import Room
from .permissions import IsAdminOnly
from django.db.models import Q


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
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get(self,request):

        try:
            admin = request.user
            search_query = request.query_params.get('search', None)
            min_price = request.query_params.get('min_price', None)
            max_price = request.query_params.get('max_price', None)

            if admin.role == 'buyer':

                rooms = Room.objects.all()

                if search_query:
                    rooms = rooms.filter(
                    Q(name__icontains=search_query) | Q(description__icontains=search_query)
                    )
                
                if min_price:
                 rooms = rooms.filter(price__gte=min_price)

                if max_price:
                 rooms = rooms.filter(price__lte=max_price)
                
                serializer =GetRoomSerializer(rooms, many =True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            
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