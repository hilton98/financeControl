from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    id: int 
    last_login: datetime
    date_joined: datetime
    nickname: str
    name: str
    surname: str 
    email_address: str
    is_active: bool 
