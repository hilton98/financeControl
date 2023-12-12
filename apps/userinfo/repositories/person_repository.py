from django.core.exceptions import ValidationError
from apps.userinfo.models.person import Person
from apps.userinfo.repositories.interfaces.person_repository import PersonRepositoryInterface
from apps.userinfo.serializers.person_write_serializer import PersonWriteSerializer


class PersonRepository(PersonRepositoryInterface):
    def create(self, person_data):
        person_serializer_instance = PersonWriteSerializer(
            data=person_data
        )
        if not person_serializer_instance.is_valid():
            raise ValidationError(person_serializer_instance.errors)
        person_serializer_instance.save()
        person_created = person_serializer_instance.data
        return person_created
    
    def get_by_id(self, id: int)-> Person:
        return Person.objects.get(pk=id)