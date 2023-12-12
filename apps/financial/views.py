from apps.financial.repositories.institution_repository import InstitutionRepository
from apps.financial.usecases.get_institution import GetInstitution
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class Institution(APIView):
    @swagger_auto_schema(
        operation_summary="Rota para recuperar instituicoes/bancos registrados no sistema",
        operation_description="listagem ou busca especifica por informacoes referentes aos bancos ",
        manual_parameters=[
            openapi.Parameter(
                "?name=",
                openapi.IN_QUERY,
                description="Nome da instituicao/banco",
                type=openapi.TYPE_STRING,
            )
        ],
        responses={
            200: openapi.Response(
                "Pode retornar um array de objetos ou apenas um objeto contendo informacoes das instituicoes/bancos."
            ),
            404: openapi.Response(
                "Mensagem de erro indicando que o item nao foi encontrado"
            )
        },
    )
    def get(self, request):
        try:
            name = request.query_params.get("name", None)
            institution_repository = InstitutionRepository()
            get_institutions = GetInstitution(institution_repository)
            response = get_institutions.execute(name)
            return Response(response)
        except ValueError as ve:
            return Response(
                {
                    "message": str(ve)
                }, 
                status=status.HTTP_404_NOT_FOUND
            )