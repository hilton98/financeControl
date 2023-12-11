import abc 

class UserRepositoryInterface(abc.ABC):
    @abc.abstractmethod
    def create(self, **kwargs):
        pass
