from rest_framework import serializers
from Room.models import Room


class RoomSerializer(serializers.ModelField):

    image = serializers.ImageField(required = True)

    class Meta:
        model = Room
        fields = ['description','image','price','address']
    
    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price <= 0:
            raise serializers.ValidationError("Price must be greater than 0.")
        if price > 10000:
            raise serializers.ValidationError("Price cannot exceed 10,000.")
        return price

class GetRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ['id','description','image','price','address']

