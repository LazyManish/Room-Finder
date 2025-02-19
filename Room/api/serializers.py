from rest_framework import serializers
from Room.models import Room


class RoomSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(required = True)

    class Meta:
        model = Room
        fields = ['description','image','price','address']
    
    def clean_price(self,validated_data):
        price = validated_data.get('price')

        if price <= 0:
            raise serializers.ValidationError("Price must be greater than 0.")
        if price > 10000:
            raise serializers.ValidationError("Price cannot exceed 10,000.")
        return price

class GetRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ['id','admin','description','image','price','address']

