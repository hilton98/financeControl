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
    
    def get_by_email(self, email_address):
        user_model = User.objects.filter(email=email_address)
        if user_model:
            return user_model.first()
        raise ValueError(f"No user found with email address {email_address}")
    
    def get_by_id(self, id):
        user_model = User.objects.filter(pk=id)
        if user_model:
            return user_model.first()
        raise ValueError(f"No user found with id {id}")