from rest_framework import serializers
from User.models import CustomUser



class UserRegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(write_only = True, style = {'input_type':'password'})
    password = serializers.CharField(write_only = True)

    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name','role','password','password2']

    
    def validate(self, data):

        password = data.get('password')
        password2 = data.get('password2')

        
        if password != password2:
            raise serializers.ValidationError({"Error":"Password didn't match."})
        
        if len(password) < 6:
            raise serializers.ValidationError({"Error":"Password should be more than 6 characters."})
        

        return data
        

    def create(self, validated_data):

        password = validated_data.pop('password')
        validated_data.pop('password2')

        user  = CustomUser.objects.create(**validated_data)

        user.set_password(password)
        user.save()

        return user
    
class UserLoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField(write_only = True)






        
        
        

    

        