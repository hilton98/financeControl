from apps.userinfo.repositories.interfaces.user_repository import UserRepositoryInterface
from apps.userinfo.usecases.generate_token_access import GenerateTokenAccess 


class AuthenticateUser:
    def __init__(
        self,
        user_repository: UserRepositoryInterface,
    ):
        self.user_repository = user_repository
    
    def execute(self, post_data):
        inputted_password = post_data.get("password")
        inputted_email = post_data.get("email_address")
        user_model = self.user_repository.get_by_email(
            inputted_email
        )
        is_valid_inputted_password = user_model.check_password(
            inputted_password
        )
        if not is_valid_inputted_password:
            raise ValueError("Password is wrong")
        generate_token_access = GenerateTokenAccess(
            self.user_repository
        )
        access_token = generate_token_access.execute(user_model.pk)
        return access_token