from dataclasses import dataclass
from datetime import datetime
from apps.userinfo.domain.entities.user import User as UserEntity

@dataclass
class Person:
    id: int 
    full_name: str
    name: str
    surname: str
    cpf: str
    born_dt: datetime
    creation_dt: datetime
    status: str
    activated: bool
    user: UserEntity