from django.core.exceptions import ValidationError
from apps.userinfo.repositories.interfaces.person_repository import PersonRepositoryInterface
from apps.userinfo.repositories.interfaces.user_repository import UserRepositoryInterface


class CreateAccount:
    def __init__(
        self,
        user_repository: UserRepositoryInterface,
        person_repository: PersonRepositoryInterface
    ):
        self.person_repository = person_repository
        self.user_repository = user_repository
    
    def execute(self, post_data):
        try:
            user_created = self.user_repository.create(
                email=post_data.get("email"),
                password=post_data.get("password"),
                first_name=post_data.get("name"),
                last_name=post_data.get("surname"),
                username=post_data.get("username"),
                is_active=True
            )
            if user_created:
                status_is_concluded = 3
                post_data["status"] = status_is_concluded
                post_data["user"] = user_created.pk
                person_created = self.person_repository.create(post_data)
            return person_created
        except ValidationError as ve:
            raise ValidationError(ve)