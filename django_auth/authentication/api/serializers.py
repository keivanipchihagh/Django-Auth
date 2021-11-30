from authentication.models import User
from rest_framework import serializers
import datetime

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password', 'email_address', 'phone_number', 'birth_date', 'photo_dir')

    def validate(self, attrs):
        return super().validate(attrs)
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)