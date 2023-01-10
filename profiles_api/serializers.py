from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializers a name fiedl for testiong our APIView"""
    name = serializers.CharField(max_length = 10)
    
