from django.core.exceptions import ValidationError
from apps.userinfo.repositories.interfaces.person_repository import PersonRepositoryInterface
from apps.userinfo.repositories.interfaces.user_repository import UserRepositoryInterface
from apps.userinfo.serializers.person_read_serializer import PersonReadSerializer
from apps.userinfo.usecases.generate_token_access import GenerateTokenAccess
from apps.userinfo.utils.person_model_to_domain import person_model_to_domain

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
                user_id = user_created.pk
                status_is_activated = 9
                post_data["status"] = status_is_activated
                post_data["user"] = user_id
                person_created = self.person_repository.create(post_data)
                data = self.generate_data_to_response(
                    person_created.get("id"),
                    user_id
                )
                return data
        except ValidationError as ve:
            raise ValidationError(ve)
        
    def generate_data_to_response(self, person_id, user_id):
        data_to_response = {}
        person_model_instance = self.person_repository.get_by_id(person_id)
        person_dataclass_instance = person_model_to_domain(person_model_instance)
        generate_token_access = GenerateTokenAccess(
            self.user_repository
        )
        data_to_response["user"] = PersonReadSerializer(person_dataclass_instance).data
        data_to_response["access_token"] = generate_token_access.execute(user_id)
        return data_to_response