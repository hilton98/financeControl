import abc

class PersonRepositoryInterface(abc.ABC):
    @abc.abstractmethod
    def create(self, person_data):
        pass