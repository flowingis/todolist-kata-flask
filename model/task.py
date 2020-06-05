import uuid
from dataclasses import dataclass

from command.task_add_command import TaskAddCommand


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

    @classmethod
    def from_command(cls, command: TaskAddCommand):
        return cls(
            uuid=str(uuid.uuid4()),
            description=command.description
        )
