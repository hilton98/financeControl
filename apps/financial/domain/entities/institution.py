from dataclasses import dataclass
from datetime import datetime

@dataclass
class Institution:
    id: int 
    name: str
    creation_dt: datetime
    activated: bool 
