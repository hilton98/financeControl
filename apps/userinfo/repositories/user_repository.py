from django.core.exceptions import ValidationError
from apps.userinfo.repositories.interfaces.user_repository import UserRepositoryInterface
from apps.userinfo.serializers.user_write_serializer import UserWriteSerializer
from django.contrib.auth.models import User

class UserRepository(UserRepositoryInterface):
    def create(self, **kwargs):
        user_data = {}
        for field, value in kwargs.items():
            user_data[field] = value
        user_serializer_instance = UserWriteSerializer(
            data=user_data
        )
        if not user_serializer_instance.is_valid():
            raise ValidationError(user_serializer_instance.errors)
        user_created = User.objects.create_user(**kwargs)
        return user_created
