from apps.financial.models.institution import Institution
from apps.financial.repositories.interfaces.institution_repository import InstitutionRepositoryInterface
from apps.financial.utils.institution_model_to_domain import institution_model_to_domain
from django.core.exceptions import ObjectDoesNotExist

class InstitutionRepository(InstitutionRepositoryInterface):
    def get_all(self):
        institutions = Institution.objects.all()
        return [
            institution_model_to_domain(institution)
            for institution in institutions
        ]
    
    def get_by_name(self, name:str):
        try:
            institution = Institution.objects.get(name__icontains=name)
            return institution_model_to_domain(institution)
        except ObjectDoesNotExist:
            return None