from apps.userinfo.domain.entities.user import (
    User as UserEntity 
)
from django.contrib.auth.models import User


def user_model_to_domain(model: User) -> UserEntity:
    return UserEntity(
        id=model.pk, 
        last_login=model.last_login,
        date_joined=model.date_joined,
        nickname=model.username,
        name=model.first_name,
        surname=model.last_name,
        email_address=model.email,
        is_active=model.is_active
    )
