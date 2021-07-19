from rest_framework import serializers
from authentication.models import User
import re


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=4, write_only=True,
                                     style={'input_type': 'password'}, trim_whitespace=True)
    fullname = serializers.CharField(max_length=255, min_length=3, allow_blank=False, trim_whitespace=True)
    mobile_number = serializers.CharField(min_length=10)
    age = serializers.IntegerField(max_value=500,allow_null=True)

    class Meta:
        model = User
        fields = ['email', 'fullname', 'mobile_number', 'password', 'age']

    def validate_fullname(self, fullname):
        regex = re.compile(r'^[a-zA-Z\s]+$')
        if regex.match(fullname):
            return fullname
        raise serializers.ValidationError("Enter a valid fullname")

    def validate_mobile_number(self, mobile_number):
        regex = re.compile(r'^\+?[0-9]+$')
        if regex.match(mobile_number):
            return mobile_number
        raise serializers.ValidationError("Enter a valid phone number")


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=4, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password')