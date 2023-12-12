from apps.financial.repositories.interfaces.institution_repository import InstitutionRepositoryInterface
from apps.financial.serializers.institutions_read_serializer import InstitutionReadSerializer


class GetInstitution:
    def __init__(self, institutionRepositoryInterface: InstitutionRepositoryInterface):
        self.institutionRepositoryInterface = institutionRepositoryInterface
    
    def execute(self, name:str):
        if name:
            return self.get_by_name(name)
        return self.get_all_institutions()

    def get_by_name(self, name):
        institution = self.institutionRepositoryInterface.get_by_name(name)
        if institution:
            institution_serialized = InstitutionReadSerializer(
                institution
            ).data
            return institution_serialized
        raise ValueError(f"Institution with name '{name}' not find.")

    def get_all_institutions(self):
        institutions = self.institutionRepositoryInterface.get_all()
        institutions_serialized = InstitutionReadSerializer(
            institutions, many=True
        ).data
        return institutions_serialized