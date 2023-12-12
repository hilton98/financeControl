from apps.userinfo.domain.entities.person import (
    Person as PersonEntity 
)
from apps.userinfo.models.person import Person
from apps.userinfo.utils.user_model_to_domain import user_model_to_domain


def person_model_to_domain(model: Person) -> PersonEntity:
    if model and model.user:
        user_data = model.user
        user_dataclass_instance = user_model_to_domain(user_data)
        return PersonEntity(
            id=model.pk, 
            full_name=model.full_name,
            name=model.name,
            surname=model.surname,
            cpf=model.cpf,
            born_dt=model.born_dt,
            creation_dt=model.creation_dt,
            status=model.status.name,
            activated=model.activated,
            user=user_dataclass_instance
        )
