from apps.userinfo.repositories.interfaces.user_repository import UserRepositoryInterface
from rest_framework_simplejwt.tokens import RefreshToken


class GenerateTokenAccess:
    def __init__(
        self,
        user_repository: UserRepositoryInterface,
    ):
        self.user_repository = user_repository

    def execute(self, user_id):
        user_model = self.user_repository.get_by_id(user_id)
        refresh = RefreshToken.for_user(user_model)
        access_token = str(refresh.access_token)
        return access_token