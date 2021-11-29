from authentication.models import User
from rest_framework import serializers
import datetime

class UserSerializer(serializers.ModelSerializer):

    # year = serializers.CharField(write_only = True, required = True)
    # month = serializers.CharField(write_only = True, required = True)
    # day = serializers.CharField(write_only = True, required = True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password', 'email_address', 'phone_number', 'birth_date')

    def validate(self, attrs):
        return super().validate(attrs)
    
    def create(self, validated_data):
        # birth_date = datetime.date(int(validated_data['year']), validated_data['month'], validated_data['day'])
        # return User.objects.create(**validated_data, birth_date = birth_date)
        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        # birth_date = datetime.date(validated_data['year'], validated_data['month'], validated_data['day'])
        # return super().update(instance, validated_data, birth_date = birth_date)
        return super().update(instance, validated_data)