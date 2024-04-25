from rest_framework import serializers
from .models import TodoApi


class TodoSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = TodoApi
        fields = ('id', 'title', 'completed', 'user')
