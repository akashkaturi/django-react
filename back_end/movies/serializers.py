from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'




class LoginSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)
