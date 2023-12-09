from apps.financial.domain.entities.institution import (
    Institution as InstitutionEntity 
)
from apps.financial.models.institution import Institution


def institution_model_to_domain(model: Institution) -> InstitutionEntity:
    return InstitutionEntity(
        id=model.pk, 
        name=model.name,
        creation_dt=model.creation_dt,
        activated=model.activated
    )
