import uuid
from dataclasses import dataclass


@dataclass
class Task:
    uuid: str
    description: str

    @classmethod
    def create(cls, description: str):
        return cls(
            uuid=str(uuid.uuid4()),
            description=description
        )
