from apps.userinfo.repositories.person_repository import PersonRepository
from apps.userinfo.repositories.user_repository import UserRepository
from apps.userinfo.usecases.create_account import CreateAccount
from django.db import transaction
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class User(APIView):    
    def post(self, request):
        try:
            with transaction.atomic():
                post_data = request.data.copy()
                user_repository = UserRepository()
                person_repository = PersonRepository()
                create_account = CreateAccount(
                    user_repository,
                    person_repository
                )
                user_created_data = create_account.execute(post_data)
                return Response(
                    user_created_data,
                    status=status.HTTP_201_CREATED
                )
        except ValidationError as ve:
            errors = [
                {"field": key, "error": value[0]}
                for key, value in ve
            ]
            return Response(
                errors, 
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response({
                    "message": str(e)
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )