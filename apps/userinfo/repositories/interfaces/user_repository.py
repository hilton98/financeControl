import abc 

class UserRepositoryInterface(abc.ABC):
    @abc.abstractmethod
    def create(self, **kwargs):
        pass

    @abc.abstractmethod
    def get_by_email(self, email_address):
        pass

    @abc.abstractmethod
    def get_by_id(self, id):
        pass
