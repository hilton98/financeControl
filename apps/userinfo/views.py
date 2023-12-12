from apps.userinfo.repositories.person_repository import PersonRepository
from apps.userinfo.repositories.user_repository import UserRepository
from apps.userinfo.usecases.authenticate_user import AuthenticateUser
from apps.userinfo.usecases.create_account import CreateAccount
from django.db import transaction
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class User(APIView):
    @swagger_auto_schema(
        operation_summary="Criacao de conta no sistema",
        operation_description="Cadastrar um usuário inicia uma conta no sistema.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={                
                "email": openapi.Schema(type=openapi.TYPE_STRING),
                "password": openapi.Schema(type=openapi.TYPE_STRING),
                "full_name": openapi.Schema(type=openapi.TYPE_STRING),
                "name": openapi.Schema(type=openapi.TYPE_STRING),
                "surname": openapi.Schema(type=openapi.TYPE_STRING),
                "username": openapi.Schema(type=openapi.TYPE_STRING),
                "born_dt": openapi.Schema(type=openapi.TYPE_STRING),
                "cpf": openapi.Schema(type=openapi.TYPE_STRING),
            },
            example={
                "email": "Fulano98@gmail.com",
                "password": "Senha123@",
                "full_name": "Fulano de tal",
                "name": "Fulano",
                "surname": "Tal",
                "username": "FTAL998",
                "born_dt": "1998-12-14 09:10:55.313 -0300",
                "cpf": "10332815277"
            },
        ),
        responses={
            201: openapi.Response(
                "Retorna um objeto contendo os dados registrados e o token de acesso.",
            ),
            400: openapi.Response(
                "Pode retornar um objeto contendo um campo e o seu respectivo erro ou apenas uma mensagem de erro.",
            ),
        },
    )
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
                response = create_account.execute(post_data)
                return Response(
                    response,
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

class Login(APIView):
    @swagger_auto_schema(
        operation_summary="Acesso do usuário na plataforma através de suas credenciais.",
        operation_description="Apenas o email e senha cadastrados previamente no sistema sao utilizados como credenciais de acesso.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "email_address": openapi.Schema(type=openapi.TYPE_STRING),
                "password": openapi.Schema(type=openapi.TYPE_STRING),
            },
            example={
                "email_address": "fulanodetal@gmail.com",
                "password": "SenhaFulano123",
            },
        ),
        responses={
            200: openapi.Response(
                "Retorna um token de acesso.",
            )
        },
    )
    def post(self, request):
        try:
            post_data = request.data.copy()
            user_repository = UserRepository()
            authenticate_user = AuthenticateUser(user_repository)
            access_token = authenticate_user.execute(post_data)
            return Response(
                {"access_token": access_token},
                status=status.HTTP_200_OK
            )
        except ValueError as ve:
            return Response({
                    "message": str(ve)
                }, 
                status=status.HTTP_401_UNAUTHORIZED
            )