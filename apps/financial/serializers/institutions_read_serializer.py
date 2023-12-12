from rest_framework import serializers

class InstitutionReadSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField()
    creation_dt=serializers.DateTimeField()
