# serializers.py
from rest_framework import serializers
from .models import Tasks

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id', 'title', 'description', 'is_completed', 'created_at', 'category', 'priority', 'progress_percentage']
        read_only_fields = ['id', 'created_at']

    def update(self, instance, validated_data):
        if 'progress_percentage' in validated_data and validated_data['progress_percentage'] ==100:
            validated_data['is_completed'] = True
        return super().update(instance, validated_data) 