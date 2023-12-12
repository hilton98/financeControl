from rest_framework import serializers

class PersonReadSerializer(serializers.Serializer):
    id=serializers.IntegerField() 
    full_name=serializers.CharField()
    name=serializers.CharField()
    surname=serializers.CharField()
    cpf=serializers.CharField()
    born_dt=serializers.DateTimeField()
    creation_dt=serializers.DateTimeField()
    status=serializers.CharField()
    activated=serializers.BooleanField()
    user=serializers.SerializerMethodField()


    def get_user(self, instance):
        user = instance.user
        if user:
            print("esses sao os dados", user)
            return {
                "id": user.id,
                "last_login": user.last_login,
                "date_joined": user.date_joined,
                "nickname": user.nickname,
                "name": user.name,
                "surname": user.surname,
                "email_address": user.email_address,
                "is_active": user.is_active
            }
