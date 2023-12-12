import abc
from apps.userinfo.models.person import Person

class PersonRepositoryInterface(abc.ABC):
    @abc.abstractmethod
    def create(self, person_data):
        pass

    @abc.abstractmethod
    def get_by_id(self, id: int)-> Person:
        pass