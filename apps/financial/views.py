from apps.financial.repositories.institution_repository import InstitutionRepository
from apps.financial.usecases.get_institution import GetInstitution
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class Institution(APIView):
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