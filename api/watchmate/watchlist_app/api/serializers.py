from rest_framework import serializers

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    year = serializers.IntegerField()
    active = serializers.BooleanField()
    description = serializers.CharField()