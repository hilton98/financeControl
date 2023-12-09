import abc

class InstitutionRepositoryInterface(abc.ABC):
    @abc.abstractmethod
    def get_all(self):
        pass

    @abc.abstractmethod
    def get_by_name(self, name:str):
        pass