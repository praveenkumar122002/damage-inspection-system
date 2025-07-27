from rest_framework import serializers
from .models import User, Inspection
from django.contrib.auth.hashers import make_password

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

class InspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inspection
        fields = '__all__'
        read_only_fields = ['inspected_by', 'created_at']

    def validate_image_url(self, value):
        if not value.endswith(('.jpg', '.jpeg', '.png')):
            raise serializers.ValidationError("Invalid image URL format.")
        return value
