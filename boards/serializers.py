from rest_framework import serializers
from .models import Board, Task

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
        'id',
        'name'
        )
        model = Board

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
        'id',
        'board',
        'name',
        'points'
        )
        model = Task
