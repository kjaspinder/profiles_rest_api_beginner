from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """serilaizes the name field for testing out apiview"""
    """accept name of max 10 char"""
    name = serializers.CharField(max_length=10)
